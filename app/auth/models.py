from app import db


users_views = db.Table(
    'usuario_vista',
    db.Column('idusuario', db.Integer, db.ForeignKey('usuario.idusuario')),
    db.Column('idvista', db.Integer, db.ForeignKey('vista.idvista')),
    info={'bind_key': 'base'}
)


class Module(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'modulo'

    idmodulo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    idplataforma = db.Column(db.Integer)
    views = db.relationship('View', back_populates='module')


class User(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'usuario'
    __table_args__ = {"extend_existing": True}

    idusuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    correo = db.Column(db.String(60))
    tipo = db.Column(db.Integer)
    estado = db.Column(db.Integer)
    idcolaborador = db.Column(db.Integer, db.ForeignKey('colaborador.idcolaborador'))
    collaborator = db.relationship('Collaborator', back_populates='user')
    views = db.relationship('View', secondary=users_views, backref='user')


class Collaborator(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'colaborador'

    idcolaborador = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.String(16))
    ap_paterno = db.Column(db.String(30))
    ap_materno = db.Column(db.String(30))
    nombre1 = db.Column(db.String(30))
    nombre2 = db.Column(db.String(30))
    correo = db.Column(db.String(50))
    user = db.relationship('User', back_populates='collaborator', uselist=False)

    def full_name(self):
        names = [self.ap_paterno, self.ap_materno, self.nombre1, self.nombre2]
        full_name = ''
        for name in names:
            if name:
                full_name += f'{name} '
        return full_name.strip().title()


class View(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'vista'

    idvista = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    idmodulo = db.Column(db.Integer, db.ForeignKey('modulo.idmodulo'))
    module = db.relationship('Module', back_populates='views')


class Record(db.Model):
    __bind_key__ = 'base'
    __tablename__ = 'bitacora'

    idbitacora = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text)
    idusuario = db.Column(db.Integer)
    flg_tipo = db.Column(db.Integer) # 1: inicio de sesión, 2: cambio de contraseña
    estado = db.Column(db.Integer) # 1: activo, 2: inactivo


class Session(db.Model):
    __tablename__ = 'sesion_usuario'

    idsesion = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text)
    idusuario = db.Column(db.Integer)
    estado = db.Column(db.Integer) # 1: activo, 0: inactivo

class Company(db.Model):
    __tablename__ = 'empresa'

    idempresa = db.Column(db.Integer, primary_key=True)
    razon_social = db.Column(db.Text)
    nombre_comercial = db.Column(db.Integer)

class Area(db.Model):
    __tablename__ = 'area'

    idarea = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text)
    descripcion = db.Column(db.Integer)
    idempresa = db.Column(db.Integer, db.ForeignKey('empresa.idempresa'))


class Plataform(db.Model):
    __tablename__ = 'plataforma'

    idplataforma = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text)
    idempresa = db.Column(db.Integer, db.ForeignKey('empresa.idempresa'))
    tipo_plataforma = db.Column(db.Integer)


class Cargo(db.Model):
    __tablename__ = 'cargo'

    idcargo = db.Column(db.Integer, primary_key=True)
    nombre_cargo = db.Column(db.Text)
    idarea = db.Column(db.Integer, db.ForeignKey('area.idarea'))