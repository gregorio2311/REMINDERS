
#Conectar la base de datos con Python
''' METODO 1 para conecectarse a la base de datos de firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Cargo el proyecto del proyecto firebase
firebase_sdk = credentials.Certificate('pia-apmov-firebase-adminsdk-89b6c-709551a0af.json')

#Hacer referencia a la base de datos en tiempo real de firebase
firebase_admin.initialize_app(firebase_sdk,{'databaseURL' : 'https://pia-apmov-default-rtdb.firebaseio.com/'})

#Crear una coleccion (entidad) con funcion push 
ref = db.reference('/Pendientes')
ref.push({'Tipo' : 'Tareas', 'Hora' : '13:00', 'Recordar' : '13:00'}) '''


                                        #CREAR UN API
from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/ruta', methods=['POST'])
def procesar_solicitud():
    d = {}
    d['datos'] = str(request.args['datos'])
    # Realiza las operaciones necesarias con Firebase
    return jsonify(d)

if __name__ == '__main__':
    app.run()




                                    #METODO 2 para conectarse a la base de datos de firebase
from firebase import firebase

firebase = firebase.FirebaseApplication("https://pia-apmov-default-rtdb.firebaseio.com/",None)

# Solicitar al usuario que ingrese un nombre
hobbie = input("Ingresa el hobbie: ")

# Solicitar al usuario que ingrese una edad
hora = input("Ingresa la hora: ")

# Imprimir los datos ingresados
print("Tu hobbie es:", hobbie)
print("Tu hora es:", hora)


Pendientes = {
    'Tipo' : hobbie,
    'Hora' : hora,
}


#Metodo para llenar la base de datos con POST
resultado=firebase.post('/Carpeta_firebase/subcarpeta_firebase',Pendientes)
print(resultado)


#Metodo para eliminar Delete
#firebase.delete('/Carpeta_firebase/subcarpeta_firebase', '')
