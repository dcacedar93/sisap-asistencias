from sqlalchemy import text
from app import db
from flask import request
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from app.config import FLASK_ENV
from app.facturas.models.FacturasModel import Documents, Proveedor, EstadoDocumento, DocumentoSiniestro
from app.config import AWS_ACCOUNT_ID, AWS_BUCKET_NAME_RECURSOS
from utils.s3_service import S3Client

def estadosDoc(estado):
    if estado == 1:
        estado_nombre = "Recibido"
    elif estado == 2:
        estado_nombre = "Aceptado"
    elif estado == 3:
        estado_nombre = "Observado"
    elif estado == 5:
        estado_nombre = "Devuelto"
    elif estado == 6:
        estado_nombre = "Pagado"
    elif estado == 18:
        estado_nombre = "Pendiente"
    elif estado == 19:
        estado_nombre = "Sustentado"
    else:
        estado_nombre = "En revisión"

    return estado_nombre

#-- Carga de facturas y expedientes
def mostrarCargaFacturasPorProveedor(fecha_min, fecha_max, id_proveedor):
    respuesta = []
    query=text(f"""SELECT
        s.fecha_atencion,
        s.num_orden_atencion,
        a.aseg_numDoc,
        UPPER(CONCAT(a.aseg_nom1, ' ', a.aseg_nom2, ' ', a.aseg_ape1, ' ', a.aseg_ape2)) AS afiliado,
        p.nombre_plan,
		s.idsiniestro
    FROM
        (
            SELECT * FROM siniestro
            WHERE
                idproveedor = '{id_proveedor}'
                AND fecha_atencion >= '{fecha_min}'
                AND fecha_atencion < '{fecha_max}'
        ) AS s
        INNER JOIN asegurado AS a ON s.idasegurado = a.aseg_id
        INNER JOIN plan AS p ON a.aseg_tipo = p.idplan
    ORDER BY
        s.fecha_atencion DESC;""")

    result=db.engine.execute(query).all()

    for i in result:
        respuesta.append({
            "fecha_atencion": i.fecha_atencion,
            "num_orden_atencion": i.num_orden_atencion,
            "aseg_numDoc": i.aseg_numDoc,
            "afiliado": i.afiliado,
            "nombre_plan": i.nombre_plan,
            "idsiniestro": i.idsiniestro
        })

    if result:
        return respuesta
    else:
        return False

def cutUrlBase(url) :
    if url is None or url == "":
        return ""
    #https://recursosglobal.s3.amazonaws.com
    return url.replace("https://red-salud.s3.us-east-2.amazonaws.com","")

def uploadFilePdf(request):
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

        hoursec = datetime.today().strftime('%d%m%Y%H%M%S')
        file.filename = f"{hoursec}_" + "FACTURA.pdf"

        if file:
            s3_client = S3Client(AWS_ACCOUNT_ID, AWS_BUCKET_NAME_RECURSOS)
            output = s3_client.upload_fileobj(file, pathExtra="sisap/pdf/")
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

def uploadFileXml(request):
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

        hoursec = datetime.today().strftime('%d%m%Y%H%M%S')
        file.filename = f"{hoursec}_" + "FACTURA.xml"

        if file:
            s3_client = S3Client(AWS_ACCOUNT_ID, AWS_BUCKET_NAME_RECURSOS)
            output = s3_client.upload_fileobj(file, pathExtra="sisap/xml/")
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

def uploadFileXmlExp(request):
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

        hoursec = datetime.today().strftime('%d%m%Y%H%M%S')
        file.filename = f"{hoursec}_" + "EXPEDIENTE.pdf"

        if file:
            s3_client = S3Client(AWS_ACCOUNT_ID, AWS_BUCKET_NAME_RECURSOS)
            output = s3_client.upload_fileobj(file, pathExtra="sisap/expedientes/")
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

def registrarFactura(tipo_comprobante, serie, correlativo, idproveedor, fecha_emision, importe, idsiniestro, link_factura, link_xml, link_expediente, iddocumento):
    proveedor = Proveedor.query.filter(Proveedor.idproveedor == idproveedor).first()

    if tipo_comprobante == "F":
        documento = Documents(
            fecha_emision = fecha_emision,
            tipo_documento = tipo_comprobante,
            serie = serie,
            numero = correlativo,
            importe = importe,
            idsiniestro = idsiniestro,
            idproveedor = proveedor.idproveedor,
            estado = 18,
            link_factura = link_factura,
            link_xml = link_xml,
            link_expediente = link_expediente
        )
        db.session.add(documento)
        db.session.commit()
        db.session.flush()
        iddocumento = documento.iddocumento
    elif tipo_comprobante == "NC":
        documento = Documents(
            fecha_emision = fecha_emision,
            tipo_documento = tipo_comprobante,
            serie = serie,
            numero = correlativo,
            importe = importe,
            idsiniestro = idsiniestro,
            idproveedor = proveedor.idproveedor,
            estado = 18,
            doc_referencia = iddocumento,
            link_factura = link_factura,
            link_xml = link_xml,
            link_expediente = link_expediente
        )
        db.session.add(documento)
        db.session.commit()
        db.session.flush()
        iddocumento = documento.iddocumento

    fecha_actual = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    add_doc_siniestros = DocumentoSiniestro(
            idsiniestro = idsiniestro,
            iddocumento = iddocumento,
            createdat = fecha_actual
    )
    db.session.add(add_doc_siniestros)
    db.session.commit()
    db.session.flush()
    id_doc_sin = add_doc_siniestros.id_documento_siniestro

    estado_doc =EstadoDocumento(
        iddocumento = iddocumento,
        estado = 18,
        serie = serie,
        fecha_registro = fecha_actual,
        idusuario_gestiona = idproveedor,
        observacion = "Se registró el documento en SISAP",
        tipo_usuario = 2
    )
    db.session.add(estado_doc)
    db.session.commit()
    db.session.flush()
    idestado = estado_doc.idestado

    return "ok"

def registrarLinks(iddocumento, link_factura, link_xml, link_expediente, idproveedor):
    up_documentos = Documents.query.filter(Documents.iddocumento == iddocumento).first()
    if link_factura != None or link_factura != "":
        up_documentos.link_factura = link_factura
    if link_expediente != None or link_expediente != "":
        up_documentos.link_expediente = link_expediente
    if link_xml != None or link_xml != "":
        up_documentos.link_xml = link_xml
    up_documentos.estado = 19
    db.session.add(up_documentos)
    db.session.commit()

    fecha_actual = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    estado_doc =EstadoDocumento(
        iddocumento = iddocumento,
        estado = 19,
        fecha_registro = fecha_actual,
        idusuario_gestiona = idproveedor,
        observacion = "Se sustentó el documento en SISAP",
        tipo_usuario = 2
    )
    db.session.add(estado_doc)
    db.session.commit()
    db.session.flush()
    idestado = estado_doc.idestado

    return "ok"

def actualizarEstadoDoc(iddocumento, idproveedor, estado):
    fecha_actual = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    for id in iddocumento:
        up_documentos = Documents.query.filter(Documents.iddocumento == id.iddocumento).first()
        up_documentos.estado = 1
        db.session.add(up_documentos)
        db.session.commit()

        estado_doc =EstadoDocumento(
            iddocumento = id.iddocumento,
            estado = estado,
            fecha_registro = fecha_actual,
            idusuario_gestiona = idproveedor,
            observacion = "Se recibió documento",
            tipo_usuario = 2
        )
        db.session.add(estado_doc)
        db.session.commit()
        db.session.flush()
        idestado = estado_doc.idestado

#-- Seguimiento de documentos
def consultarComprobantesSeguimiento(fecha_min, fecha_max, idproveedor):
    respuesta = []
    query=text(f"""SELECT
        d.iddocumento,
        d.serie,
        d.numero,
        d.estado,
        d.idproveedor,
        d.link_factura,
        d.link_expediente,
        d.createdat,
        s.num_orden_atencion,
        s.idsiniestro,
        (select max(ed.fecha_registro) from estado_documento ed where iddocumento=d.iddocumento group by ed.iddocumento) as fecha_act
    FROM documentos d
    WHERE d.createdat>='{fecha_min}' AND d.createdat>='{fecha_max}' AND idproveedor={idproveedor};""")

    result=db.engine.execute(query).all()

    estado_nombre = estadosDoc(i.estado)

    for i in result:
        respuesta.append({
            "iddocumento": i.iddocumento,
            "comprobante": i.serie+"-"+i.numero,
            "nro_orden": i.num_orden_atencion,
            "estado": estado_nombre,
            "fecha_act": i.fecha_act,
            "link_factura": i.link_factura,
            "link_expediente": i.link_expediente,
            "idsiniestro": i.idsiniestro
        })

    if result:
        return respuesta
    else:
        return False

def actualizarFactura(iddocumento, tipo_comprobante, serie, correlativo, fecha_emision, importe, idusuario):
    up_documento = Documents.query.filter(Documents.iddocumento == iddocumento).first()
    up_documento.fecha_emision = fecha_emision
    up_documento.tipo_documento = tipo_comprobante
    up_documento.serie = serie
    up_documento.numero = correlativo
    up_documento.importe = importe
    up_documento.estado = 1
    db.session.add(up_documento)
    db.session.commit()

    fecha_actual = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    estado_doc = EstadoDocumento(
        iddocumento = iddocumento,
        estado = 1,
        serie = serie,
        fecha_registro = fecha_actual,
        idusuario_gestiona = idusuario,
        observacion = "Se actualizó documento",
        tipo_usuario = 2
    )
    db.session.add(estado_doc)
    db.session.commit()
    db.session.flush()
    idestado = estado_doc.idestado

    return "ok"

#-- Consulta de historial
def consultarHistorial(iddocumento):
    respuesta = []
    estado_doc = EstadoDocumento.query.filter(EstadoDocumento.iddocumento == iddocumento).all()
    for ed in estado_doc:

        estado_nombre = estadosDoc(ed.estado)

        respuesta.append({
            "estado": estado_nombre,
            "fecha_act": ed.fecha_registro,
            "observacion": ed.fecha_registro
        })

    if estado_doc:
        return respuesta
    else:
        return False