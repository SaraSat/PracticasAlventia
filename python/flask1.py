from flask import Flask, escape, request

app =Flask(__name__)

""" Si no pones nada en el navegador,
te saldrá el saludo: Hola Mundo,
A través del método get podrá cambiar el
nombre del saludo--> 127.0.0.1:5000/?nombre=Sara"""

@app.route('/') 
def hello():
    nombre=request.args.get("nombre","Mundo")
    return 'Hola, {nombre}'.format(nombre=escape(nombre))


"""Aquí la ruta cambia, si añadimos a la ruta despedida,
ahora nos saldrá Hasta pronto Mundo, igualmente
mediante el método get, podremos cambiar el nombre
"""
@app.route('/despedida')
def despedida():
    nombre=request.args.get("nombre","Mundo")
    return 'Hasta pronto, {nombre}'.format(nombre=escape(nombre))

def main():
    app.run(host='0.0.0.0',debug=True)

if __name__=='__main__':
    main()