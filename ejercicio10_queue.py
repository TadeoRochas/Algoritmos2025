from queue_ import Queue
from stack_ import Stack
from datetime import time #apunte: Sirve para darle el tipo de dato hora a una variable.

class Notificacion:
    def __init__(self, hora:time , app:str, mensaje:str):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje
        
    def __str__(self):
        return f"Hora: {self.hora} - {self.app}: {self.mensaje}"
    
cola = Queue()

cola.arrive(Notificacion(time(3,33), "WhatsApp", "Dean Winchester te ha enviado un mensaje"))
cola.arrive(Notificacion(time(11,25), "Instagram", "Castiel ha publicado una historia"))
cola.arrive(Notificacion(time(12,44), "Facebook", "Tu publicacion ha sido compartida"))
cola.arrive(Notificacion(time(13,12), "Facebook", "Tienes recuerdos..."))
cola.arrive(Notificacion(time(13,49), "Twitter", "Python se actualizó..."))
cola.arrive(Notificacion(time(14,2), "Twitter", "Precio dolar hoy:..."))
cola.arrive(Notificacion(time(15,15), "Telegram", "Actualizacion disponible"))
cola.arrive(Notificacion(time(16,30), "Snapchat", "Hey!"))
cola.arrive(Notificacion(time(19,33), "TikTok", "Sam Winchester ha publicado un video"))

#Punto a
#Esta funcion sirve para eliminar las notificaciones de una app en particular.
def eliminarNoti(app):
    colaTemporal = Queue()
    while not cola.qEmpty():
        notificacion = cola.attention()
        if notificacion.app != app:
            colaTemporal.arrive(notificacion)
    
    while not colaTemporal.qEmpty():
        cola.arrive(colaTemporal.attention())

#Punto b
#Esta funcion sirve para mostrar las notificaciones de Twitter que contienen la palabra "Python" en su mensaje.
def mostrarNoti():
    copiaCola = cola.qCopy()
    while not copiaCola.qEmpty():
        notif = copiaCola.attention()
        if notif.app == "Twitter" and notif.mensaje.startswith("Python"): #apunte: startswith() sirve para buscar si la cadena de texto comienza con lo que le pasamos como argumento.
            print(notif)

#Punto c
#Esta funcion sirve para mostrar las notificaciones que se encuentran en un rango horario determinado.
#La funcion se podría adaptar a ingresar el rango horario desde la entrada de la misma, pero elegí hacerlo con los valores que solicita el punto del ejercicio para faciliarlo un poco.
def notifSegunHorario():
    copiaCola = cola.qCopy()
    stackNotificaciones = Stack()
    contador = 0
    while not copiaCola.qEmpty():
        notificacion = copiaCola.attention()
        if (notificacion.hora >= time(11,43) and notificacion.hora <= time(15,57)): #apunt: time(hora,minuto) se usa para buscar la hora de la notificacion en los intervalos pedidos en el ejercicio. 
            stackNotificaciones.push(notificacion)
            contador += 1
        
    if contador == 0:
        print("No hay notificaciones en el rango horario solicitado.")
    else:
        print(f"Se encontraron {contador} notificaciones en el rango horario solicitado:")
        
    while not stackNotificaciones.sEmpty():
        notificacion = stackNotificaciones.pop()
        print(notificacion)
    


print("Notificaciones originales:")
cola.show()
print("------------")
eliminarNoti("Facebook")
print("Notificaciones sin Facebook:")
cola.show()
print("------------")
print("Notificaciones de Twitter que contienen 'Python':")
mostrarNoti()
print("------------")
print("Notificaciones entre las 11:43 y 15:57:")
notifSegunHorario()
print("------------")
print("Notificaciones finales:")
cola.show()