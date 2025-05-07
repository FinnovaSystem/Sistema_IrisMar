from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy.sql import text
from . import db
from flask import current_app


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return filtrar_propiedades()

@main.route('/filtrar_propiedades', methods=['GET'])
def filtrar_propiedades():
    filtro = request.args.get('filtro')  # Puede ser 'ciudad' o 'departamento'
    departamento_id = request.args.get('departamento')
    ciudad_id = request.args.get('ciudad')
    tipo_operacion = request.args.get('tipo_operacion', 'indistinto')  # Valor predeterminado
    tipo_propiedad = request.args.get('tipo_propiedad', 'indistinto')  # Valor predeterminado

    # Obtener todos los departamentos
    departamentos = db.session.execute(text('SELECT * FROM Departamento')).fetchall()

    # Obtener las ciudades del departamento seleccionado o todas las ciudades si no hay departamento seleccionado
    ciudades = []
    if filtro == 'departamento' and departamento_id:
        ciudades = db.session.execute(
            text('SELECT * FROM Ciudad WHERE departamento_id = :departamento_id'),
            {'departamento_id': departamento_id}
        ).fetchall()
    elif filtro == 'ciudad':
        ciudades = db.session.execute(text('SELECT * FROM Ciudad')).fetchall()

    # Construir la consulta de propiedades dinámicamente
    consulta = '''
        SELECT id, titulo, descripcion, precio, tipo, imagen_cabecera
        FROM Propiedad
        WHERE 1=1
    '''
    parametros = {}

    if ciudad_id:
        # Si se selecciona una ciudad, filtrar por esa ciudad
        consulta += ' AND ciudad_id = :ciudad_id'
        parametros['ciudad_id'] = ciudad_id
    elif departamento_id:
        # Si se selecciona un departamento, filtrar por todas las ciudades de ese departamento
        consulta += ' AND ciudad_id IN (SELECT id FROM Ciudad WHERE departamento_id = :departamento_id)'
        parametros['departamento_id'] = departamento_id

    if tipo_operacion and tipo_operacion != 'indistinto':
        consulta += ' AND tipo_operacion = :tipo_operacion'
        parametros['tipo_operacion'] = tipo_operacion

    if tipo_propiedad and tipo_propiedad != 'indistinto':
        consulta += ' AND tipo_propiedad = :tipo_propiedad'
        parametros['tipo_propiedad'] = tipo_propiedad

    propiedades = db.session.execute(text(consulta), parametros).fetchall()

    return render_template(
        'index.html',
        filtro=filtro,
        departamentos=departamentos,
        ciudades=ciudades,
        propiedades=propiedades,
        departamento_id=departamento_id,
        ciudad_id=ciudad_id,
        tipo_operacion=tipo_operacion,
        tipo_propiedad=tipo_propiedad
    )



@main.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre_usuario')
        contrasena = request.form.get('contrasena')
        try:
            usuario = db.session.execute(
                text('SELECT * FROM Usuario WHERE nombre_usuario = :nombre_usuario AND contrasena = :contrasena'),
                {'nombre_usuario': nombre_usuario, 'contrasena': contrasena}
            ).fetchone()
            if usuario:
                flash('Inicio de sesión exitoso!', 'success')
            else:
                flash('Usuario o contraseña inválidos.', 'danger')
        except Exception as e:
            print(f"Error durante el inicio de sesión: {e}")
            flash('Ocurrió un error. Por favor, inténtalo de nuevo.', 'danger')
    return render_template('login.html')

from flask import flash


@main.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre_usuario')
        correo_electronico = request.form.get('correo_electronico')
        celular = request.form.get('celular')
        contrasena = request.form.get('contrasena')
        confirmar_contrasena = request.form.get('confirmar_contrasena')

        # Validar que las contraseñas coincidan
        if contrasena != confirmar_contrasena:
            flash('Las contraseñas no coinciden.', 'danger')
            return render_template('register.html')

        # Validar que el nombre de usuario no exista
        usuario_existente = db.session.execute(
            text('SELECT * FROM Usuario WHERE nombre_usuario = :nombre_usuario'),
            {'nombre_usuario': nombre_usuario}
        ).fetchone()

        if usuario_existente:
            flash('Este usuario ya se encuentra registrado.', 'danger')
            return render_template('register.html')

        try:
            rol = "Comercial"
            db.session.execute(
                text('INSERT INTO Usuario (nombre_usuario, correo_electronico, celular, contrasena, rol) VALUES (:nombre_usuario, :correo_electronico, :celular, :contrasena, :rol)'),
                {'nombre_usuario': nombre_usuario, 'correo_electronico': correo_electronico, 'celular': celular, 'contrasena': contrasena, 'rol': rol}
            )
            db.session.commit()
            flash('Registro exitoso! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('main.iniciar_sesion'))
        except Exception as e:
            print(f"Error durante el registro: {e}")
            flash('El registro falló. Por favor, inténtalo de nuevo.', 'danger')

    return render_template('register.html')

@main.route('/contacto', methods=['GET'])
def contacto():
    return render_template('contact.html')





import os
from flask import request, redirect, url_for, flash
from werkzeug.utils import secure_filename

# Configuración para subir imágenes
UPLOAD_FOLDER = 'static/Img-prop'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/cargar_propiedad', methods=['POST'])
def cargar_propiedad():
    upload_folder = current_app.config['UPLOAD_FOLDER']  # Obtén la carpeta de subidas

    # Datos del formulario
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    tipo = request.form['tipo']
    imagenes = request.files.getlist('imagenes')  # Obtiene todas las imágenes

    # Simula el ID de la propiedad (en un caso real, este ID vendría de la base de datos)
    propiedad_id = 2  # Cambia esto por el ID real de la propiedad después de guardarla en la base de datos

    if len(imagenes) > 6:
        flash('Solo puedes subir hasta 6 imágenes', 'error')
        return redirect(url_for('main.index'))

    imagenes_guardadas = []
    for idx, imagen in enumerate(imagenes, start=1):  # Comienza el índice en 1
        if imagen and allowed_file(imagen.filename):
            # Genera el nombre del archivo con la nomenclatura Prop<ID>-Img<ID>.ext
            extension = imagen.filename.rsplit('.', 1)[1].lower()
            filename = f"Prop{propiedad_id}-Img{idx}.{extension}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagen.save(filepath)
            imagenes_guardadas.append(filename)

    if not imagenes_guardadas:
        flash('No se subieron imágenes válidas', 'error')
        return redirect(url_for('main.index'))

    # Define la primera imagen como cabecera
    imagen_cabecera = imagenes_guardadas[0]

    # Aquí puedes guardar los datos en la base de datos
    # Ejemplo:
    # nueva_propiedad = Propiedad(
    #     titulo=titulo,
    #     descripcion=descripcion,
    #     precio=precio,
    #     tipo=tipo,
    #     imagen_cabecera=imagen_cabecera,
    #     imagenes=','.join(imagenes_guardadas)
    # )
    # db.session.add(nueva_propiedad)
    # db.session.commit()

    flash('Propiedad cargada exitosamente', 'success')
    return redirect(url_for('main.index'))



@main.route('/detalle_propiedad/<int:id>', methods=['GET'])
def detalle_propiedad(id):
    # Consulta para obtener los detalles de la propiedad
    propiedad = db.session.execute(
        text('SELECT * FROM Propiedad WHERE id = :id'),
        {'id': id}
    ).fetchone()

    # Manejar la excepción si no se encuentra la propiedad
    if not propiedad:
        flash('La propiedad no existe o no está disponible.', 'error')
        return redirect(url_for('main.index'))

    return render_template('detalle_propiedad.html', propiedad=propiedad)