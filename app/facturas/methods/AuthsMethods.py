from sqlalchemy import text
from app import db
import json
from datetime import datetime
from app.auth.header import get_auth_token
from app.auth.models import  Session

def busquedaIduser(request):
    token = get_auth_token(request)
    user = Session.query.filter(Session.token == token).first()
    if user:
        iduser = user.idusuario
    else:
        iduser = 0
    return iduser