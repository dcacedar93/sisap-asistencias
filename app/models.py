from app import db

class Ubigeo(db.Model):
    __tablename__ = "ubigeo"
    __table_args__ = {"extend_existing": True}
    idubigeo = db.Column(db.Integer, primary_key = True)
    cod_reniec = db.Column(db.String)
    dpto_reniec = db.Column(db.String)
    prov_reniec = db.Column(db.String)
    dist_reniec = db.Column(db.String)
    cod_inei = db.Column(db.String)
    dpto_inei = db.Column(db.String)
    prov_inei = db.Column(db.String)
    dist_inei = db.Column(db.String)
    nombre_dep = db.Column(db.String)
    nombre_prov = db.Column(db.String)
    nombre_dist = db.Column(db.String)