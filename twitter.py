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
    def __repr__(self):
        return f"Usuario - {self.nombre}"
    
#Ejercicio 2a y b
class Tweet:
    def __init__(self, message:str, sender: UserAccount):
        if len(message)>140:
            raise Exception("Mensaje demasiado largo")
        if not isinstance(sender,UserAccount):
            raise Exception("El usuario no es válido")
        
        self.message = message
        self.sender = sender
        self.tiempo = time.time()
    #2c
    def __str__(self):
        return f"Tweet de {self.sender.nombre}. Tweet:{self.message}.Publicado{time.time(int(self.tiempo))}"

class DirectMessage(Tweet):
    def __init__(self,args,kwargs):
        if "receiver" not in kwargs:
            raise Exception("No se especifica el usuario que recibe el tweet")
        receiver = kwargs.pop('receiver')
        if not isinstance(receiver,UserAccount):
            raise Exception("Usuario no valido")
        self.receiver = receiver
        super().__init__(*args,**kwargs)
    #2c
    def __str__(self):
        return f"Mensaje directo de {self.sender.nombre}a{self.receiver.nombre}. Tweet: {self.message}.Publicado: {time.time(int(self.tiempo))}"

class Retweet(Tweet):
    def __init__(self,*args,**kwargs):
        if "tweet_to_retweet" not in kwargs:
            raise Exception("No se ha especificado ningun tweet")
        tweet_to_retweet = kwargs.pop('tweet_to_retweet')
        if not isinstance(tweet_to_retweet,Tweet):
            raise Exception("No es un tweet")
        self.tweet_original = tweet_to_retweet
        super().__init__(*args,**kwargs)
    #2c
    def __str__(self):
        return f"Retweet de {self.sender.nombre}. Tweet: {self.message}. Tweet original: {self.tweet_original.message} Publicado: {time.time(int(self.tiempo))}"
#El ejercicio 2D lo he creado en otra pagina, aqui procedo a aplicar los cambios que he comentado en ella