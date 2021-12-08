import tweepy
import datetime
consumer_key = ''
consumer_secret = ''

acess_token = ''
acess_secret_token = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acess_secret_token)
api = tweepy.API(auth)

carnaval = datetime.date(2022,2,25)
hoje = datetime.date.today()

diferenca = carnaval - hoje

api.update_status(f'Faltam {diferenca.days} para o carnaval 2022')
