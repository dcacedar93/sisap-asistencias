from flask import Blueprint,jsonify
from app.facturas.controller import facturasController

bp = Blueprint('facturas', __name__,template_folder="templates")

#-- Carga de facturas y expedientes
@bp.route('/carga', methods=['POST'])
def mostrarCargaFacturasPorProveedor():
    v = facturasController.mostrarCargaFacturasPorProveedor()
    return v

@bp.route('/cargarPdf', methods=['POST'])
def uploadFilePdf():
    v = facturasController.cargarPdf()
    return v

@bp.route('/cargarXml', methods=['POST'])
def uploadFileXml():
    v = facturasController.cargarXml()
    return v

@bp.route('/cargarPdfExpedientes', methods=['POST'])
def uploadFileXmlExp():
    v = facturasController.cargarPdfExpedientes()
    return v

@bp.route('/registrarFactura', methods=['POST'])
def registrarDoc():
    v = facturasController.registrarFactura()
    return v

@bp.route('/registrarLinks', methods=['POST'])
def registrarUrl():
    v = facturasController.registrarLinks()
    return v

@bp.route('/actualizarEstadoDoc', methods=['POST'])
def actualizarEstadoDoc():
    v = facturasController.actualizarEstadoDoc()
    return v

#-- Seguimiento de documentos
@bp.route('/consultarComprobantes', methods=['POST'])
def consultarComprobantesSeguimiento():
    v = facturasController.consultarComprobantesSeguimiento()
    return v

@bp.route('/actualizarFactura', methods=['POST'])
def actualizarFactura():
    v = facturasController.actualizarFactura()
    return v

@bp.route('/consultarHistorial', methods=['POST'])
def consultarHistorial():
    v = facturasController.consultarHistorial()
    return v
