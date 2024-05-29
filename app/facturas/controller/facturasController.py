from flask import jsonify, request, make_response
from app.auth.header import response_token_unauthorized, validate_session
from app.facturas.methods import facturasMethods, AuthsMethods

#-- Carga de facturas y expedientes
def mostrarCargaFacturasPorProveedor():
    try:
        data = request.json
        print(data)
        fecha_min = data.get("fecha_min", False)
        fecha_max = data.get("fecha_max", False)
        id_proveedor = data.get("id_proveedor", False)
        respuesta = []
        respuesta = facturasMethods.mostrarCargaFacturasPorProveedor(fecha_min, fecha_max, id_proveedor)

        if respuesta:
            return jsonify({"status": 200, "data": respuesta})
        else:
            return jsonify({"status": 400, "data": "No hay datos"})

    except Exception as err:
        response_data = {
            "message": str(err)
        }
        return make_response(jsonify(response_data), 500)

def cargarPdf():
    try:
        respuesta=facturasMethods.uploadFilePdf(request)
        return respuesta
    except Exception as err:
        response_data = {
            "message": "Error al cargar pdf"
        }
        return make_response(jsonify(response_data), 500)

def cargarXml():
    try:
        respuesta=facturasMethods.uploadFileXml(request)
        return respuesta
    except Exception as err:
        response_data = {
            "message": "Error al cargar xml"
        }
        return make_response(jsonify(response_data), 500)

def cargarPdfExpedientes():
    try:
        respuesta=facturasMethods.uploadFileXmlExp(request)
        return respuesta
    except Exception as err:
        response_data = {
            "message": "Error al cargar expediente"
        }
        return make_response(jsonify(response_data), 500)

def registrarFactura():
    try:
        session = validate_session(request)
        if session:
            idusuario = AuthsMethods.busquedaIduser(request)
            data = request.json
            tipo_comprobante = data.get("tipo_comprobante", False)
            serie = data.get("serie", False)
            correlativo = data.get("correlativo", False)
            idproveedor = data.get("idproveedor", False)
            fecha_emision = data.get("fecha_emision", False)
            importe = data.get("importe", False)
            idsiniestro = data.get("idsiniestro", False)
            link_factura = data.get("link_factura", False)
            link_xml = data.get("link_xml", False)
            link_expediente = data.get("link_expediente", False)
            iddocumento = data.get("iddocumento", False)
            respuesta=facturasMethods.registrarFactura(tipo_comprobante, serie, correlativo, idproveedor, fecha_emision, importe, idsiniestro, link_factura, link_xml, link_expediente, iddocumento)
            if respuesta:
                return jsonify({"status": 200})
            else:
                return jsonify({"status": 400, "data": "No hay datos"})
        else:
            return response_token_unauthorized()
    except Exception as err:
        response_data = {
            "message": "Error al registrar factura"
        }
        return make_response(jsonify(response_data), 500)

def registrarLinks():
    try:
        data = request.json
        iddocumento = data.get("iddocumento", False)
        link_factura = data.get("link_factura", False)
        link_xml = data.get("link_xml", False)
        link_expediente = data.get("link_expediente", False)
        respuesta = []
        respuesta = facturasMethods.registrarLinks(iddocumento, link_factura, link_xml, link_expediente)

        if respuesta:
            return jsonify({"status": 200, "data": respuesta})
        else:
            return jsonify({"status": 400, "data": "No hay datos"})

    except Exception as err:
        response_data = {
            "message": str(err)
        }
        return make_response(jsonify(response_data), 500)

def actualizarEstadoDoc():
    try:
        data = request.json
        iddocumento = data.get("iddocumento", False)
        idproveedor = data.get("idproveedor", False)
        estado = data.get("estado", False)
        respuesta = []
        respuesta = facturasMethods.actualizarEstadoDoc(iddocumento, idproveedor, estado)

        if respuesta:
            return jsonify({"status": 200, "data": respuesta})
        else:
            return jsonify({"status": 400, "data": "No hay datos"})

    except Exception as err:
        response_data = {
            "message": str(err)
        }
        return make_response(jsonify(response_data), 500)

#-- Seguimiento de documentos
def consultarComprobantesSeguimiento():
    try:
        data = request.json
        print(data)
        fecha_min = data.get("fecha_min", False)
        fecha_max = data.get("fecha_max", False)
        idproveedor = data.get("idproveedor", False)
        respuesta = []
        respuesta = facturasMethods.consultarComprobantesSeguimiento(fecha_min, fecha_max, idproveedor)

        if respuesta:
            return jsonify({"status": 200, "data": respuesta})
        else:
            return jsonify({"status": 400, "data": "No hay datos"})

    except Exception as err:
        response_data = {
            "message": str(err)
        }
        return make_response(jsonify(response_data), 500)

def actualizarFactura():
    try:
        session = validate_session(request)
        if session:
            idusuario = AuthsMethods.busquedaIduser(request)
            data = request.json
            iddocumento = data.get("iddocumento", False)
            tipo_comprobante = data.get("tipo_comprobante", False)
            serie = data.get("serie", False)
            correlativo = data.get("correlativo", False)
            fecha_emision = data.get("fecha_emision", False)
            importe = data.get("importe", False)
            respuesta=facturasMethods.actualizarFactura(iddocumento, tipo_comprobante, serie, correlativo, fecha_emision, importe, idusuario)
            if respuesta:
                return jsonify({"status": 200})
            else:
                return jsonify({"status": 400, "data": "No hay datos"})
        else:
            return response_token_unauthorized()
    except Exception as err:
        response_data = {
            "message": "Error al registrar factura"
        }
        return make_response(jsonify(response_data), 500)

#-- Consulta de historial
def consultarHistorial(iddocumento):
    try:
        data = request.json
        print(data)
        iddocumento = data.get("iddocumento", False)
        respuesta = []
        respuesta = facturasMethods.consultarHistorial(iddocumento)

        if respuesta:
            return jsonify({"status": 200, "data": respuesta})
        else:
            return jsonify({"status": 400, "data": "No hay datos"})

    except Exception as err:
        response_data = {
            "message": str(err)
        }
        return make_response(jsonify(response_data), 500)