
#Ejercicio 1A

class UserAccount:
    def __init__(self,nombre: str, email: str):
        self.nombre = nombre
        self._email = email
        self.tweets = []
        self.followers = []
        self.timeline = []
        self.following = []
#He elegido para nombre y email cadenas de texto, mientras que para el resto he creado listas. Además he decidido que el nombre sea publico mientras que el email sea privado.

#Ejercicio 1B
    def follow(self,user):
        if user not in self.following:
            self.following.append(user)
            user.followers.append(self)
        else:
            print("Ya sigues a :" + user.nombre)