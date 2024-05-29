from app import db
from sqlalchemy.sql import func
from utils import methods


class Proveedor(db.Model):
    __tablename__ = "proveedor"
    __table_args__ = {"extend_existing": True}

    idproveedor = db.Column(db.Integer, primary_key=True)

    idtipoproveedor = db.Column(db.Integer)
    idtipodocumentoidentidad = db.Column(db.Integer)
    idusuario = db.Column(db.Integer)
    razon_social_pr = db.Column(db.String(200))
    nombre_comercial_pr = db.Column(db.String(200))
    numero_documento_pr = db.Column(db.String(20))
    direccion_pr = db.Column(db.String(200))
    referencia_pr = db.Column(db.String(250))
    cod_distrito_pr = db.Column(db.String(2))
    cod_provincia_pr = db.Column(db.String(2))
    cod_departamento_pr = db.Column(db.String(2))
    cod_sunasa_pr = db.Column(db.String(50))
    estado_pr = db.Column(db.Integer)
    createdat = db.Column(db.DateTime, server_default=func.now())
    updatedat = db.Column(db.DateTime, server_default=func.now())
    latitud = db.Column(db.String(40))
    longitud = db.Column(db.String(40))
    forma_pago = db.Column(db.Integer)
    medio_pago = db.Column(db.Integer)
    cta_corriente = db.Column(db.String(255))
    cta_detracciones = db.Column(db.String(255))
    param_igv = db.Column(db.Numeric(10, 2))
    cmp = db.Column(db.String(20))
    rne = db.Column(db.String(20))
    tiempo_pago = db.Column(db.Integer)


class ContactoProveedor(db.Model):
    __tablename__ = "contacto_proveedor"
    __table_args__ = {"extend_existing": True}

    idcontactoproveedor = db.Column(db.Integer, primary_key=True)

    idproveedor = db.Column(db.Integer)
    nombres_cp = db.Column(db.String(20))
    apellidos_cp = db.Column(db.String(20))
    cargo_cp = db.Column(db.String(150))
    telefono_fijo_cp = db.Column(db.String(20))
    anexo_cp = db.Column(db.String(10))
    telefono_movil_cp = db.Column(db.String(20))
    email_cp = db.Column(db.String(50))
    estado_cp = db.Column(db.Integer)
    createdat = db.Column(db.DateTime)
    updatedat = db.Column(db.DateTime)
    idcargocontacto = db.Column(db.Integer)
    envio_correo_cita = db.Column(db.Integer)


class Documents(db.Model):
    __tablename__ = "documentos"
    __table_args__ = {"extend_existing": True}

    iddocumento = db.Column(db.Integer, primary_key=True)

    fecha_emision = db.Column(db.Date)
    tipo_documento = db.Column(db.String(3))
    serie = db.Column(db.String(10))
    numero = db.Column(db.String(20))
    importe = db.Column(db.Numeric(10, 2))
    idsiniestro = db.Column(db.Integer)
    createdat = db.Column(db.DateTime)
    idproveedor_int = db.Column(db.Integer)
    idproveedor = db.Column(db.Integer)
    estado = db.Column(db.Integer)
    descripcion = db.Column(db.String(255))
    remitente = db.Column(db.String(255))
    updatedat = db.Column(db.DateTime)
    doc_referencia = db.Column(db.Integer)
    tipo_pago = db.Column(db.Integer)
    estado_concar = db.Column(db.Integer)
    estado_dev = db.Column(db.Integer)
    fecha_vencimiento = db.Column(db.Date)
    documento_cc = db.Column(db.Integer)
    nro_cuenta = db.Column(db.Integer)
    flg_dcto = db.Column(db.String(1))
    idusuario_deriva = db.Column(db.Integer)
    fecha_recepcion = db.Column(db.Date)
    asunto = db.Column(db.String(255))
    idusuario_recepcion = db.Column(db.Integer)
    link_factura = db.Column(db.Text)
    link_expediente = db.Column(db.Text)
    fecha_concar = db.Column(db.Date)
    motivo_nc = db.Column(db.String(500))
    tipo_nc = db.Column(db.Integer)
    link_xml = db.Column(db.Text)

class DocumentoSiniestro(db.Model):
    __tablename__ = "documento_siniestro"
    __table_args__ = {"extend_existing": True}

    id_documento_siniestro = db.Column(db.Integer, primary_key=True)

    idsiniestro = db.Column(db.Integer)
    createdat = db.Column(db.DateTime)
    iddocumento = db.Column(db.Integer)
    importe_siniestro = db.Column(db.Numeric(10,2))
    link_expediente = db.Column(db.Text)

class EstadoDocumento(db.Model):
    __tablename__ = "estado_documento"
    __table_args__ = {"extend_existing": True}

    idestado = db.Column(db.Integer, primary_key=True)
    iddocumento = db.Column(db.Integer)
    estado = db.Column(db.String(255))
    fecha_registro = db.Column(db.DateTime, server_default=func.now())
    idusuario_gestiona = db.Column(db.Integer)
    observacion = db.Column(db.String(255))


class MotivoObs(db.Model):
    __tablename__ = "motivo_obs"
    __table_args__ = {"extend_existing": True}

    idmotivo_obs = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text)
    modulo = db.Column(db.Integer)


class MotivoDevolucion(db.Model):
    __tablename__ = "motivo_devolucion"
    __table_args__ = {"extend_existing": True}

    idmotivo_devolucion = db.Column(db.Integer, primary_key=True)
    idestado_documento = db.Column(db.Integer)
    idmotivo = db.Column(db.Integer)
    descripcion = db.Column(db.Text)


class ProveedorInt(db.Model):
    __tablename__ = "proveedor_int"
    __table_args__ = {"extend_existing": True}

    idproveedor_int = db.Column(db.Integer, primary_key=True)
    idtipodocumentoidentidad = db.Column(db.Integer)
    razon_social_pr = db.Column(db.String(200))
    nombre_comercial_pr = db.Column(db.String(200))
    numero_documento_pr = db.Column(db.String(20))
    direccion_pr = db.Column(db.String(200))
    referencia_pr = db.Column(db.String(250))
    cod_distrito_pr = db.Column(db.String(2))
    cod_provincia_pr = db.Column(db.String(2))
    cod_departamento_pr = db.Column(db.String(2))
    createdat = db.Column(db.DateTime, server_default=func.now())
    updatedat = db.Column(db.DateTime, server_default=func.now())
    idusuario = db.Column(db.Integer)
    nro_cta = db.Column(db.String(255))
    idbanco = db.Column(db.Integer)


class Siniestro(db.Model):
    __tablename__ = "siniestro"
    __table_args__ = {"extend_existing": True}

    idsiniestro = db.Column(db.Integer, primary_key=True)

    idasegurado = db.Column(db.Integer)
    idcertificado = db.Column(db.Integer)
    idareahospitalaria = db.Column(db.Integer)
    idhistoria = db.Column(db.Integer)
    idmedico = db.Column(db.Integer)
    idproveedor = db.Column(db.Integer)
    idespecialidad = db.Column(db.Integer)
    idproducto = db.Column(db.Integer)
    fecha_atencion = db.Column(db.Date)
    fase_atencion = db.Column(db.Integer)
    est_tr = db.Column(db.Integer)
    est_md = db.Column(db.Integer)
    est_lab = db.Column(db.Integer)
    createdat = db.Column(db.DateTime)
    updatedat = db.Column(db.DateTime)
    es_reconsulta = db.Column(db.Integer)
    num_orden_atencion = db.Column(db.String(20))
    estado_siniestro = db.Column(db.Integer)
    idcita = db.Column(db.Integer)
    sin_labFlag = db.Column(db.Integer)
    estado_atencion = db.Column(db.String(1))
    usuario_crea = db.Column(db.Integer)
    usuario_anula = db.Column(db.Integer)
    fecha_atencion_act = db.Column(db.Date)
    usuario_activa = db.Column(db.Integer)
    tipo_desapcho = db.Column(db.Integer)
    tipo_siniestro = db.Column(db.Integer)
    motivo_anula = db.Column(db.String(500))
    comentario = db.Column(db.String(255))


class Asegurado(db.Model):
    __tablename__ = "asegurado"
    __table_args__ = {"extend_existing": True}

    aseg_id = db.Column(db.Integer, primary_key=True)

    tipoDoc_id = db.Column(db.Integer)
    aseg_numDoc = db.Column(db.String(20))
    aseg_nom1 = db.Column(db.String(50))
    aseg_nom2 = db.Column(db.String(50))
    aseg_ape1 = db.Column(db.String(50))
    aseg_ape2 = db.Column(db.String(50))
    aseg_direcc = db.Column(db.String(250))
    aseg_telf = db.Column(db.String(20))
    aseg_ubg = db.Column(db.String(10))
    aseg_fechNac = db.Column(db.String(20))
    aseg_estCiv = db.Column(db.String(6))
    aseg_sexo = db.Column(db.String(2))
    aseg_nac = db.Column(db.String(50))
    aseg_email = db.Column(db.String(100))
    aseg_ocupa = db.Column(db.String(100))
    aseg_tarjAseg = db.Column(db.String(20))
    aseg_freg = db.Column(db.DateTime, server_default=func.now())
    idusuario = db.Column(db.Integer)
    aseg_tipo = db.Column(db.Integer)
    asex_id = db.Column(db.Integer)
    idusuario_actualiza = db.Column(db.Integer)
    fecha_actualiza = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )

    def get_full_name_aseg(self, document_type="DNI", name_format=""):
        if document_type == "DNI":
            name_list = [self.aseg_ape1, self.aseg_ape2, self.aseg_nom1, self.aseg_nom2]
            return methods.concatenate_list(name_list, name_format)
        elif document_type == "RUC":
            name_list = [self.aseg_ape1]
            return methods.concatenate_list(name_list, name_format)
        else:
            name_list = [self.aseg_ape1, self.aseg_ape2, self.aseg_nom1, self.aseg_nom2]
            return methods.concatenate_list(name_list)


class LiquidacionGrupo(db.Model):
    __tablename__ = "liquidacion_grupo"
    __table_args__ = {"extend_existing": True}

    liqgrupo_id = db.Column(db.Integer, primary_key=True)

    fecha_genera = db.Column(db.DateTime, server_default=func.now())
    usuario_genera = db.Column(db.Integer)
    forma_pago = db.Column(db.Integer)
    medio_pago = db.Column(db.Integer)
    num_operacion = db.Column(db.String(15))
    fecha_liquida = db.Column(db.DateTime)
    usuario_liquida = db.Column(db.Integer)
    liqgrupo_estado = db.Column(db.Integer)
    email_notifica = db.Column(db.String(50))
    cta_corriente = db.Column(db.String(255))
    cta_detracciones = db.Column(db.String(255))
    detraccion = db.Column(db.Numeric(10, 2))
    total = db.Column(db.Numeric(10, 2))
    estado = db.Column(db.Integer)
    motivo = db.Column(db.String(255))


class LiquidacionGrupoDetalle(db.Model):
    __tablename__ = "liquidacion_grupodetalle"
    __table_args__ = {"extend_existing": True}

    liqdetallegrupo_id = db.Column(db.Integer, primary_key=True)

    liqgrupo_id = db.Column(db.Integer)
    liqdetalleid = db.Column(db.Integer)
    liqgrupodetalle_estado = db.Column(db.Integer)
    estado = db.Column(db.Integer)


class Liquidacion(db.Model):
    __tablename__ = "liquidacion"
    __table_args__ = {"extend_existing": True}

    liquidacionId = db.Column(db.Integer, primary_key=True)

    idsiniestro = db.Column(db.Integer)
    liquidacionTotal = db.Column(db.Numeric(10, 2))
    liquidacionFech_reg = db.Column(db.DateTime, server_default=func.now())
    liquidacion_estado = db.Column(db.Integer)
    liquidacionTotal_neto = db.Column(db.Numeric(10, 2))


class LiquidacionDetalle(db.Model):
    __tablename__ = "liquidacion_detalle"
    __table_args__ = {"extend_existing": True}

    liqdetalleid = db.Column(db.Integer, primary_key=True)

    liquidacionId = db.Column(db.Integer)
    idplandetalle = db.Column(db.Integer)
    liqdetalle_monto = db.Column(db.Numeric(10, 2))
    idproveedor = db.Column(db.Integer)
    liqdetalle_numfact = db.Column(db.String(80))
    liqdetalle_aprovpago = db.Column(db.Integer)
    liqdetalle_neto = db.Column(db.Numeric(10, 2))
    idusuario_aprueba = db.Column(db.Integer)
    iddocumento = db.Column(db.Integer)
    flg_proveedor = db.Column(db.Integer)
    tipo_pago = db.Column(db.Integer)
    idproducto_auth = db.Column(db.Integer)
    producto_desc_auth = db.Column(db.String(255))
    idusuario_auth = db.Column(db.Integer)
    fecha_hora_auth = db.Column(db.DateTime, server_default=func.now())
    idproveedor_auth = db.Column(db.Integer)
    idproveedor_int_auth = db.Column(db.String(255))


class Pago(db.Model):
    __tablename__ = "pago"
    __table_args__ = {"extend_existing": True}

    idpago = db.Column(db.Integer, primary_key=True)

    fecha_pago = db.Column(db.DateTime, server_default=func.now())
    usuario_paga = db.Column(db.String(255))
    numero_operacion = db.Column(db.String(255))
    idproveedor = db.Column(db.Integer)
    importe = db.Column(db.Numeric(10, 2))
    usuario_agrupa = db.Column(db.Integer)
    fecha_agrupa = db.Column(db.DateTime, server_default=func.now())
    importe_detraccion = db.Column(db.Numeric(10, 2))
    email_notifica = db.Column(db.String(255))
    flg_proveedor = db.Column(db.Integer)
    dni = db.Column(db.String(12))
    nombres_apellidos = db.Column(db.String(100))
    idbanco_salida = db.Column(db.Integer)
    nro_cuenta = db.Column(db.String(40))
    url_constancia = db.Column(db.Text)
    idbanco_destino = db.Column(db.Integer)
    fecha_operacion = db.Column(db.DateTime, server_default=func.now())


class PagoDetalle(db.Model):
    __tablename__ = "pago_detalle"
    __table_args__ = {"extend_existing": True}

    idpago_detalle = db.Column(db.Integer, primary_key=True)

    idpago = db.Column(db.Integer)
    liqgrupo_id = db.Column(db.Integer)


class Bancos(db.Model):
    __tablename__ = "banco"
    __table_args__ = {"extend_existing": True}

    idbanco = db.Column(db.Integer, primary_key=True)

    descripcion = db.Column(db.String(60))
    nombre_corto = db.Column(db.String(30))
    estado = db.Column(db.Integer)
    estado_salida = db.Column(db.Integer)

class BancoContabilidad(db.Model):
    __tablename__ = "banco_contabilidad"
    __table_args__ = {"extend_existing": True}

    idbanco_contabilidad = db.Column(db.Integer, primary_key=True)

    idbanco = db.Column(db.Integer)
    cuenta_contable = db.Column(db.String(30))
    anexo_contable = db.Column(db.String(30))
    estado = db.Column(db.Integer)


class ProveedorBanco(db.Model):
    __tablename__ = "proveedor_banco"
    __table_args__ = {"extend_existing": True}

    idproveedor_banco = db.Column(db.Integer, primary_key=True)

    idproveedor = db.Column(db.Integer)
    idbanco = db.Column(db.Integer)
    cta_corriente = db.Column(db.String(255))
    cta_interbancaria = db.Column(db.String(255))
    cta_detracciones = db.Column(db.String(255))


class ClienteEmpresa(db.Model):
    __tablename__ = "cliente_empresa"
    __table_args__ = {"extend_existing": True}

    idclienteempresa = db.Column(db.Integer, primary_key=True)

    idcategoriacliente = db.Column(db.Integer)
    idtipodocumentocliente = db.Column(db.Integer)
    nombre_comercial_cli = db.Column(db.String(150))
    nombre_corto_cli = db.Column(db.String(100))
    razon_social_cli = db.Column(db.String(150))
    numero_documento_cli = db.Column(db.String(20))
    representante_legal = db.Column(db.String(200))
    telefono_cli = db.Column(db.String(50))
    dni_representante_legal = db.Column(db.String(20))
    direccion_legal = db.Column(db.String(20))
    pagina_web_cli = db.Column(db.String(90))
    fecha_alta_cli = db.Column(db.DateTime)
    createdat = db.Column(db.DateTime, server_default=func.now())
    updatedat = db.Column(db.DateTime, server_default=func.now())
    estado_cli = db.Column(db.Integer)
    id_serie = db.Column(db.Integer)
    ubigeo = db.Column(db.String(6))
    idbroker = db.Column(db.Integer)
    tipo_dev = db.Column(db.Integer)

#class Plan(db.Model):
#    __tablename__ = "plan"
#    __table_args__ = {"extend_existing": True}
#
#    idplan = db.Column(db.Integer, primary_key=True)
#
#    idprograma = db.Column(db.Integer)
#    idclienteempresa = db.Column(db.Integer)
#    nombre_plan = db.Column(db.String(100))
#    codigo_plan = db.Column(db.String(50))
#    idred = db.Column(db.Integer)
#    createdat = db.Column(db.DateTime, server_default=func.now())
#    updatedat = db.Column(db.DateTime, server_default=func.now())
#    estado_plan = db.Column(db.Integer)
#    dias_carencia = db.Column(db.Integer)
#    dias_mora = db.Column(db.Integer)
#    dias_atencion = db.Column(db.Integer)
#    prima_monto = db.Column(db.Numeric(10,2))
#    num_afiliados = db.Column(db.Integer)
#    flg_cancelar = db.Column(db.String(1))
#    flg_dependientes = db.Column(db.String(1))
#    flg_activar = db.Column(db.String(1))
#    prima_adicional = db.Column(db.Numeric(10,2))
#    cuerpo_mail = db.Column(db.String(5000))
#    centro_costo = db.Column(db.Integer)
#    flg_tipo = db.Column(db.Integer)
#    cob_inkafarma = db.Column(db.Numeric(10,2))
#    id_serie = db.Column(db.Integer)
#    tipo_plan = db.Column(db.Integer)
#    periodo_cobro = db.Column(db.String(50))
#    flg_mostrarprecio = db.Column(db.Integer)
#    recurrencia = db.Column(db.String(30))
#    fecha_act_event = db.Column(db.Date)
#    idperiodo = db.Column(db.Integer)