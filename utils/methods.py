import uuid
import pytz
import os
import qrcode
from datetime import datetime, timedelta
from num2words import num2words
from itertools import groupby
from operator import itemgetter
from app.config import AWS_ACCOUNT_ID, AWS_BUCKET_NAME_RECURSOS
from utils.s3_service import S3Client
from dateutil.relativedelta import relativedelta
from urllib.request import urlopen

def generate_token():
    """
        * Retorna el string del token que se genero usando el paquete de uuid
    """
    token = uuid.uuid4()
    return str(token)

def convert_str_to_datetime(str_date, format_date='%d/%m/%Y'):
    """
        * Convierte de un tipo de dato string a un tipo de dato datetime
        * @param format_date es el formato que tiene str_date para que el método strptime pueda crear el datetime
    """
    return datetime.strptime(str_date, format_date)

def remove_duplicates(elements):
    """
        * Elimina los elementos duplicados de una lista
        * @param elements es de tipo list
        * Retorna una nueva lista de elementos únicos
    """
    res_list = []
    for index in range(len(elements)):
        if elements[index] not in elements[(index+1):]:
            res_list.append(elements[index])
    return res_list

def concatenate_list(values, style=''):
    """
        * Concatena un conjunto de strings de una lista en un string
        * @param values es una lista de strings
        * @param style puede tomar los valores de lower, upper o title
        * Retorna un string concatenado de los elementos del parámetro values
    """
    concatenate = ''
    for value in values:
        if value:
            concatenate += f'{value.strip()} '
    result = concatenate.strip()

    if style == 'lower':
        return result.lower()
    elif style == 'upper':
        return result.upper()
    elif style == 'title':
        return result.title()
    else:
        return result

def get_local_datetime(datetime_value, timezone='America/Lima'):
    """
        * Convierte un datetime en formato UTC a la zona horaria indicada en el parámetro, por defecto es 'America/Lima'
        * @param datetime_value es la fecha de tipo datetime
        * @param timezone indica la zona horaria a la que se va convertir y es de tipo string
        * Retorna un fecha de tipo datetime según la zona horaria indicada en el parámetro timezone
    """
    local_timezone = pytz.timezone(timezone)
    current_time = datetime_value.replace(tzinfo=pytz.utc)
    return current_time.astimezone(tz=local_timezone)

def get_max_min_values(values, min_value=1000000, max_value=0):
    """
        * @param values es una lista de números
        * @param min_value es un entero con un valor por defecto de 1000000
        * @param max_value es un entero con un valor por defecto de 0
        * Devuelve un diccionario ({'min_value': X, 'max_value': Y}) indicando el valor máximo y el valor mínimo de la lista
    """
    for value in values:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return {
        'min_value': min_value,
        'max_value': max_value
    }

def calculate_tax(amount: float):
    total_amount = amount or 0
    taxable_amount = total_amount / 1.18 or 0
    tax_amount = (total_amount - taxable_amount) or 0
    return {
        'tax_amount': format(tax_amount, '.2f'),
        'taxable_amount': format(taxable_amount, '.2f'),
        'total_amount': format(total_amount, '.2f')
    }

def calculate_currency_tax(amount: float):
    total_amount = amount or 0
    taxable_amount = total_amount / 1.18 or 0
    tax_amount = (total_amount - taxable_amount) or 0
    return {
        'tax_amount': '{:,.2f}'.format(tax_amount),
        'taxable_amount': '{:,.2f}'.format(taxable_amount),
        'total_amount': '{:,.2f}'.format(total_amount)
    }

def transform_amount_to_word(amount: str):
    [int_value, decimal_value] = amount.split('.')
    amount_word = num2words(int_value, lang='es')
    amount_word = f'{amount_word} CON {decimal_value}/100'.upper()
    return amount_word

def remove_files(files, parent_dir=''):
    for removed_file in files:
        file_deleted = f'{parent_dir}/{removed_file}' if parent_dir else removed_file
        if os.path.isfile(file_deleted):
            os.remove(file_deleted)

def get_range_dates(initial_date='', final_date=''):
    initial_date = convert_str_to_datetime(initial_date, '%Y-%m-%d').date()
    final_date = convert_str_to_datetime(final_date, '%Y-%m-%d').date()
    delta = final_date - initial_date
    date_list = []

    for index in range(delta.days + 1):
        new_date = initial_date + timedelta(days=index)
        date_list.append(new_date.strftime('%Y-%m-%d'))
    return date_list

def generate_qr_code(qr_filename, qr_message):
    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(qr_message)
        qr.make(fit=True)
        image_qr = qr.make_image(back_color='white', fill_color='black').convert('RGB')
        image_qr.save(qr_filename)
        qr_filename = os.path.abspath(qr_filename)
        if os.path.isfile(qr_filename):
            return qr_filename
        return False
    except Exception:
        return False


def group_by_list(list_values, key_value):
    list_values = sorted(list_values, key=itemgetter(key_value))
    list_values = groupby(list_values, key=itemgetter(key_value))

    sorted_list = []
    for key, value in list_values:
        sorted_list.append({"date": key, "charges": list(value)})
    return sorted_list

#  subir un archivo adjunto a una ruta en aws buscket
def uploadFile(request,pathExtra):
    try:
        urlS3 = ""
        if "file_obj" not in request.files:
            return {
                "success": False,
                "message": "No file key in request.files"
            }, 502
        file = request.files["file_obj"]
        print(file.content_type)
        if file.filename == "":
            return {
                "success": False,
                "message": "Seleccione un archivo"
            }, 200
        if file:
            s3_client = S3Client(AWS_ACCOUNT_ID, AWS_BUCKET_NAME_RECURSOS)
            output = s3_client.upload_fileobj(file, pathExtra)
            urlS3 = output

        if urlS3 == '':
            return {
                "success": False,
                "message": "Error al subir el archivo"
            }, 502
        return {
            "success": True,
            "data": {
                "name": file.filename,
                "url": urlS3,
                "url_save": cutUrlBase(urlS3)
            }
        }, 200

    except Exception as err:
        return {"success": False, "message": str(err)}, 502
def cutUrlBase(url) :
    if url is None or url == "":
        return ""
    #https://recursosglobal.s3.amazonaws.com
    return url.replace("https://red-salud.s3.us-east-2.amazonaws.com","")

def edadActual(fecha_nacimiento):
    try:
        if type(fecha_nacimiento) is str:
            fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            print(fecha_nac)
            print(datetime.now())
            edad = relativedelta(datetime.now(), fecha_nac)
        else:
            edad = relativedelta(datetime.now(), fecha_nacimiento)
        return edad.years
    except:
        return 0

def download_constancia(filename, download_filename):
    url =f'{filename}'
    response = urlopen(url)
    general_pdf = f'{download_filename}.pdf'
    with open(general_pdf, 'wb') as pdf_file:
        pdf_file.write(response.read())
    return general_pdf

def delete_files(file_list):
    for item in file_list:
        if os.path.isfile(item):
            os.remove(item)