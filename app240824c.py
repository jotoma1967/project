

import pip 

try:
    import flask
except ImportError:
     
    pip.main(["install","flask"])

    import  flask  

try:
    from flask import  render_template
except ImportError:
     
    pip.main(["install","render_template"])

    from flask import  render_template  


try:
    from flask import  Flask
except ImportError:
     
    pip.main(["install","Flask"])

    from flask import  Flask

try:
    from flask import  current_app
except ImportError:
     
    pip.main(["install","current_app"])

    from flask import  current_app

try:
    from  flask import g
except ImportError:
     
    pip.main(["install","g"])

    import  g

try:
    from  flask import url_for
except ImportError:
     
    pip.main(["install","url_for"])

    import  url_for

try:
    from  flask import jsonify
except ImportError:
     
    pip.main(["install","jsonify"])

    import  jsonify

try:
    import  waitress
except ImportError:
     
    pip.main(["install","waitress"])

    import  waitress

try:
    from  waitress import serve
except ImportError:
     
    pip.main(["install","serve"])

    import  serve


#from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
#app = Flask(__name__, template_folder='templates')
app.config['SERVER_NAME'] = 'https://project-jpuo.onrender.com'
app.config['APPLICATION_ROOT'] = '/'
app.config['PREFERRED_URL_SCHEME'] = 'https'

# Simulate URL building outside of request context
with app.app_context():
    #print(url_for('index.html'))
    print("linea 75 ********************")

fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

'''
@app.before_request
def before_request():
    g.user = 'Usuario'

'''

print("linea 46 ",fecha_actualizacion,"****************************")

@app.route('/data')
def data():
    with app.app_context():
        return jsonify({
            'nombre': 'Juan',
            'edad': 30,
            'uno':fecha_actualizacion
        })
data()
##
# app.run()
'''
@app.route('/')
def index():
    with app.app_context():
        ##g.user = "exito"
        # Puedes acceder a `current_app` y otras funcionalidades aquí
        print("Nombre de la aplicación:", current_app.name)

        ##print("variable g ", g.user)
    # Obtén la fecha y hora actual
    #fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Renderiza la plantilla con la fecha actual
        print("linea 49 ", fecha_actualizacion,"**************************************")
        return render_template('index.html', ufecha_actualizacion="suerte")
'''
##serve(app, host="0.0.0.0", port = 10000)
#index()
##app.run()

'''

if __name__ == '__main__':
    #before_request()
    print ("linea 84   *****************************")
    index()
    print("linea 86 ",fecha_actualizacion)
    
    ##app.run(debug=True)
    ##from waitress import serve
    ##serve(app, host="123.45.67.89", port = 10000)#0.0.0.0", port=10000)

    print("linea 90 **********************")
    app.run(debug=True)
    #from waitress import serve
    ##serve(app, host="0.0.0.0", port=10000)
'''