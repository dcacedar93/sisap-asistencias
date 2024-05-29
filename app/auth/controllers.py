from flask import request, make_response, jsonify
from app.auth import methods
from app.auth import header
from app.auth.models import Record


def get_access():
    """
    * @url '/api/auth/login'
    * Obtener la autorización de los módulos y vistas a las que el usuario tiene acceso
    """
    try:
        auth_data = methods.get_auth_data(request)
        if auth_data:
            token = auth_data["token"]
            platform_id = auth_data["platform_id"]

            active_record = (
                Record.query.filter(Record.token == token)
                .filter(Record.estado == 1)
                .first()
            )
            print("active_record: ", active_record)
            user = methods.get_user(active_record.idusuario)
            session_token = methods.generate_session(user.get("id"))
            module_list = methods.get_views_modules(user.get("id"), platform_id)

            if session_token and module_list:
                response = jsonify(
                    {
                        "success": True,
                        "data": {
                            "user": user,
                            "token": session_token,
                            "modules": module_list,
                        },
                    }
                )
                return make_response(response, 200)
            else:
                raise Exception("No se obtuvo ninguna acceso a la plataforma")
        else:
            raise Exception("Error al obtener el token y el ID de la plataforma")
    except Exception as err:
        print("Error:", err)
        response = jsonify({"success": False, "message": "Error al iniciar sesión"})
        return make_response(response, 500)


def remove_session():
    """
    * @url '/api/auth/logout'
    * Actualizar el estado de la sesión en la base de datos
    """
    try:
        session = header.update_session(request)

        if session:
            response = jsonify({"succes": True})
            return make_response(response, 200)
        else:
            raise Exception("Hubo problemas para inhabilitar la sesión")
    except Exception as err:
        print("Error: ", err)
        response = jsonify({"success": False, "message": "Error al cerrar sesión"})
        return make_response(response, 500)
