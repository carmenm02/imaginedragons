import time
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
        if not isinstance(user,UserAccount):
            raise Exception("El usuario no es válido")
        if user not in self.following:
            self.following.append(user)
            user.followers.append(self)
        else:
            print("Ya sigues a :" + user.nombre)
        #En este caso el metodo follow va a recibir datos de tipo UserAccount

        #Ejercicio 1C
    def tweet(self, tweet1: str):
        if len(tweet1)>140:
            raise Exception("Mensaje demasiado largo")
        self.tweets.append(tweet1)
        self.actualizar_tweets_timeline(tweet1)
    def actualizar_tweets_timeline(self,tweet2):
        for follower in self.followers:
            follower
            self.timeline.append(tweet2)
    
#Ejercicio 2
class Tweet:
    def __init__(self, message:str, sender: UserAccount):
        if len(message)>140:
            raise Exception("Mensaje demasiado largo")
        if not isinstance(sender,UserAccount):
            raise Exception("El usuario no es válido")
        
        self.message = message
        self.sender = sender
        self.tiempo = time.time()
    def __str__(self) -> str:
        return f"Tweet de {self.sender.nombre}. Tweet:{self.message}.Publicado{time.time(int(self.tiempo))}"