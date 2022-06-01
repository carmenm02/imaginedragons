
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
        timeline = self.timeline
        for follower in self.followers:
            follower(tweet2)
            timeline.append(follower)
            