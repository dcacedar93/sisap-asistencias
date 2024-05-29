from app import db
from flask import make_response, jsonify
from app.auth.models import Session


def get_auth_token(request):
    """
    * Obtener el valor del token, que tiene el key Authorization en el header
    """
    try:
        AUTH_PREFIX = "Bearer"
        auth_token = request.headers.get("Authorization", False)
        print(auth_token)
        if AUTH_PREFIX in auth_token:
            token = split_auth_header(auth_token)
            return token
        else:
            return False
    except Exception as err:
        print("Error:", err)
        return False


def split_auth_header(auth_token):
    array_auth = auth_token.split(" ")
    return array_auth[1]


def validate_session(request):
    """
    * Validar que el token del campo Authorization sea el de una sesión activa
    """
    token = get_auth_token(request)
    if not token:
        return False

    session = (
        Session.query.filter(Session.token == token).filter(Session.estado == 1).first()
    )
    if not session:
        return False

    return True if session.estado == 1 else False


def update_session(request, session_state=0):
    """
    * Actualizar el estado de la sesión (1: activo, 0: inactivo)
    """
    token = get_auth_token(request)
    if not token:
        return False

    session = (
        Session.query.filter(Session.token == token).filter(Session.estado == 1).first()
    )

    if not session:
        return False

    session.estado = session_state
    db.session.add(session)
    db.session.commit()

    return True if session.estado == 0 else False


def response_token_unauthorized():
    """
    * Retorna un error de servidor en caso el token no sea válido
    """
    response = jsonify({"success": False, "message": "Token no autorizado"})
    return make_response(response, 500)
