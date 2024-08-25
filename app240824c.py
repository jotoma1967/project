

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
 
fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("linea 46 ",fecha_actualizacion,"****************************")
@app.route('/')
def index():
    with app.app_context():
        # Puedes acceder a `current_app` y otras funcionalidades aquí
        print("Nombre de la aplicación:", current_app.name)
    # Obtén la fecha y hora actual
    #fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Renderiza la plantilla con la fecha actual
        print("linea 49 ", fecha_actualizacion,"**************************************")
def prueba():    
    return render_template('index.html', fecha_actualizacion=fecha_actualizacion)
'''
if __name__ == '__app240824b__':
    
    print ("linea 54    *****************************")
    index()
    print("linea 59 ",fecha_actualizacion)
    ##app.run(debug=True)
    app.run()
'''
if True: #__name__ == '__main__':
    
    print ("linea 84   *****************************")
    index()
    print("linea 86 ",fecha_actualizacion)
    prueba()
    ##app.run(debug=True)
    ##from waitress import serve
    ##serve(app, host="0.0.0.0", port = 10000)#0.0.0.0", port=10000)

    print("linea 90 **********************")
    app.run()
    #from waitress import serve
    ##serve(app, host="0.0.0.0", port=10000)
