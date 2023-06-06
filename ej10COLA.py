"""10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra Python, si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son."""

from datetime import datetime
from cola import Cola
from pila import Pila

class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

def eliminar_notificaciones_facebook(cola):
    total_notificaciones = cola.size()
    cont = 0
    while cont < total_notificaciones:
        notificacion = cola.atention()
        if notificacion.aplicacion != 'Facebook':
            cola.arrive(notificacion)
        cont += 1

def mostrar_notificaciones_twitter_con_python(cola):
    total_notificaciones = cola.size()
    cont = 0
    while cont < total_notificaciones:
        notificacion = cola.atention()
        if notificacion.aplicacion == 'Twitter' and 'Python' in notificacion.mensaje:
            print ("*-----------------------------------------------------------------------------------------------------*")
            print(f"Notificacion de Twitter: Hora: {notificacion.hora}, Mensaje: {notificacion.mensaje}")
            print ("*-----------------------------------------------------------------------------------------------------*")
        cola.arrive(notificacion)
        cont += 1

def contar_notificaciones_entre_horas(cola, hora_inicio, hora_fin):
    pila_temporal = Pila()
    total_notificaciones = cola.size()
    cont = 0
    while cont < total_notificaciones:
        notificacion = cola.atention()
        if hora_inicio <= notificacion.hora <= hora_fin:
            pila_temporal.push(notificacion)
        cola.arrive(notificacion)
        cont += 1
    return pila_temporal.size()

notificaciones_smartphone = Cola()
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 11, 35), 'Facebook', 'Hola, como te va'))
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 12, 10), 'Twitter', 'hice un trabajo en Python de cola'))
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 13, 45), 'Facebook', 'Hoy jugue al futbol'))
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 14, 20), 'Twitter', 'tengo un archivo de Python para pasarte'))
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 15, 10), 'Facebook', 'recien salgo del trabajo'))
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 16, 30), 'Twitter', 'programe una aplicacion en Python'))
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 17, 0), 'Twitter', 'vas a jugar a la pelota?'))
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 18, 15), 'Facebook', 'tenemos que hablar'))
notificaciones_smartphone.arrive(Notificacion(datetime(2023, 5, 21, 19, 30), 'Twitter', 'vayamos a tomar una cerveza al bar'))


eliminar_notificaciones_facebook(notificaciones_smartphone)
mostrar_notificaciones_twitter_con_python(notificaciones_smartphone)
hora_inicio = datetime(2023, 5, 21, 11, 43)
hora_fin = datetime(2023, 5, 21, 15, 57)
cantidad_notificaciones = contar_notificaciones_entre_horas(notificaciones_smartphone, hora_inicio, hora_fin)


print(".")
print(".")


print ("*-----------------------------------------------------------------------------------------------------*")
print(f"Total de notificaciones entre las horas {hora_inicio} y {hora_fin}: {cantidad_notificaciones}")
print ("*-----------------------------------------------------------------------------------------------------*")
