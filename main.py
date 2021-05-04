from flask import Flask, flash, redirect, render_template, request, url_for
import sqlite3 as sql
conexion = sql.connect("database.db", check_same_thread=False)

app = Flask(__name__)
app.secret_key = 'clave'


@app.route('/')
def index():
     return render_template('index.html')

@app.route('/crear-cliente/', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
         nombre = request.form['nombre']
         apellido = request.form['apellido']
         codigo = request.form['codigo']
         telefono = request.form['telefono']
         inmueble = request.form['inmueble']
         operacion = request.form['operacion']
         precio = request.form['precio']
         ciudad = request.form['ciudad']

         cursor = conexion.cursor()
         cursor.execute("""
               INSERT INTO clientes VALUES 
               (null, ?, ?, ?, ?, ?, ?, ?, ?)""", 
               (nombre, apellido, codigo, 
               telefono, inmueble, operacion, 
               precio, ciudad))
         conexion.commit()

         flash('Nuevo cliente agregado')

         return redirect(url_for('index'))


    return render_template('crear-cliente.html')

@app.route('/apartamento/')
def apartamento():
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM clientes WHERE inmueble = 'apartamento'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('apartamento.html', clientes = clientes)


@app.route('/casa/')
def casa():
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM clientes WHERE inmueble = 'casa'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('casa.html', clientes = clientes)

@app.route('/galpon')
def galpon():
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM clientes WHERE inmueble = 'galpon'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('galpon.html', clientes = clientes)

@app.route('/local/')
def local():
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM clientes WHERE inmueble = 'local'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('local.html', clientes = clientes)

@app.route('/oficina/')
def oficina():
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM clientes WHERE inmueble = 'oficina'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('oficina.html', clientes = clientes)

@app.route('/terreno/')
def terreno():
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM clientes WHERE inmueble = 'terreno'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('terreno.html', clientes = clientes)

@app.route('/alquiler/<inmueble>')
def alquiler(inmueble):
     cursor = conexion.cursor()
     cursor.execute(f"SELECT * FROM clientes WHERE inmueble = '{inmueble}' AND  operacion = 'alquiler'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('alquiler.html', clientes = clientes)

@app.route('/compra/<inmueble>')
def compra(inmueble):
     cursor = conexion.cursor()
     cursor.execute(f"SELECT * FROM clientes WHERE inmueble = '{inmueble}' AND  operacion = 'compra'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('compra.html', clientes = clientes)

@app.route('/venta/<inmueble>')
def venta(inmueble):
     cursor = conexion.cursor()
     cursor.execute(f"SELECT * FROM clientes WHERE inmueble = '{inmueble}' AND  operacion = 'venta'")
     clientes = cursor.fetchall()
     cursor.close()
     return render_template('venta.html', clientes = clientes)


@app.route('/editar/<cliente_id>', methods = ['GET', 'POST'])
def editar(cliente_id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        codigo = request.form['codigo']
        telefono = request.form['telefono']
        inmueble = request.form['inmueble']
        operacion = request.form['operacion']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        #return f"{marca} {modelo} {precio} {ciudad}"
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE clientes
            SET nombre = ?,
                apellido = ?,
                codigo = ?,
                telefono = ?,
                inmueble  = ?, 
                operacion = ?,
                precio = ?,
                ciudad = ?
            WHERE id = ?
        """, (nombre, apellido, codigo, telefono, inmueble, operacion,
        precio, ciudad, cliente_id))
        cursor.connection.commit()

        flash('Has editado el coche correctamente')
        

        return redirect(url_for('index'))
    
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM clientes WHERE id = {cliente_id}")
    cliente = cursor.fetchall()
    cursor.close()

    return render_template('crear-cliente.html', cliente = cliente[0])


     

@app.route('/borrar/<cliente_id>')
def borrar(cliente_id): 
     cursor =conexion.cursor()
     cursor.execute(f'DELETE FROM clientes WHERE id = {cliente_id}')
     conexion.commit()

     return redirect(url_for('apartamento'))

if __name__ == '__main__':
    app.run(debug=True)