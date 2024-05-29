from app import db
from utils import methods
from app.auth import header
from app.auth.models import User, Session
from app.auth.schemas import ModuleSchema


def get_auth_data(request):
    """
        * Obtener el token del header y el ID de la plataforma del body
    """
    auth_token = header.get_auth_token(request)
    platform_id = request.json.get('plataforma_id', False)
    if auth_token and platform_id:
        return {
            'token': auth_token,
            'platform_id': platform_id,
        }
    else:
        return False

def get_user(user_id):
    """
        * Obtener la información del usuario y del colaborador
    """
    user = User.query.filter(User.idusuario == user_id).first()
    collaborator = user.collaborator
    return {
        'id': user.idusuario,
        'name': collaborator.full_name(),
        'username': user.username,
        'email': user.correo
    }

def get_views_modules(user_id, platform_id):
    """
        * Realizar las consultas de los módulos y vistas a las que el usuario tiene acceso
    """
    user = User.query.filter(User.idusuario == user_id).first()
    module_list = []
    data = []

    for view in user.views:
        if view.module.idplataforma == platform_id:
            module = {
                'id': view.module.idmodulo,
                'name': view.module.nombre
            }
            module_list.append(module)

    module_list = methods.remove_duplicates(module_list)
    for module in module_list:
        views_module = list(filter(lambda view: view.idmodulo == module['id'], user.views))
        module_serialize = ModuleSchema(module, views_module).dump()
        data.append(module_serialize)
    return data

def generate_session(user_id):
    """
        * Crear sesion en la base de datos para validar el acceso del usuario
    """
    try:
        token = methods.generate_token()
        new_session = Session(
            token=token,
            idusuario=user_id,
            estado=1
        )
        db.session.add(new_session)
        db.session.commit()
        return new_session.token
    except Exception as err:
        print(err)
        return False
