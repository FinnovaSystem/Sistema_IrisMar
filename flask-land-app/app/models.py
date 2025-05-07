from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(80), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(120), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)
    propiedades = db.relationship('Propiedad', backref='propietario', lazy=True)

class Ciudad(db.Model):
    __tablename__ = 'Ciudad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)

class Propiedad(db.Model):
    __tablename__ = 'Propiedad'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.Enum('casa', 'apartamento', 'terreno'), nullable=False)
    dormitorios = db.Column(db.Integer, nullable=True)
    ciudad_id = db.Column(db.Integer, db.ForeignKey('Ciudad.id', ondelete='CASCADE'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id', ondelete='CASCADE'), nullable=False)