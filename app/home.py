from flask import Blueprint, jsonify


bp = Blueprint('home', __name__)

@bp.route('/')
@bp.route('/home')
def index():
    return jsonify({'response': 'SISAP - Asistencias Red Salud API'})
