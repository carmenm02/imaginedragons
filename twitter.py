#Ejercicio 1.A

class UserAccount:
    def __init__(self,nombre: str, email: str):
        self.nombre = nombre
        self._email = email
        self.tweets = []
        self.followers = []
        self.timeline = []
#He elegido para nombre y email cadenas de texto, mientras que para el resto he creado listas. Además he decidido que el nombre sea publico mientras que el email sea privado.


