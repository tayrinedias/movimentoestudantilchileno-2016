import tweepy

# Registre sua aplicacao em https://apps.twitter.com
consumer_key="sua consumer_key"
consumer_secret="sua consumer_secret"
access_token="seu access_token"
access_token_secret="seu access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#user = api.get_user('alegomes')

# Busca toda a timeline de um usuario especifico, 
# conforme documentacao em:
# http://tweepy.readthedocs.org/en/v3.5.0/api.html#API.user_timeline
timeline = api.user_timeline('alegomes',max_id=999999999999999999)

# Vamos contar a quantidade de tweets obtidos.
i = 0

# Enquanto houver elementos na timeline...
while timeline:

  # Imprime a quantidade de elementos obtidos.
  print(len(timeline),"tweets recuperados")

  # A timeline eh composta por tweets.
  # O Twitter chama cada tweet de Status.
  # No tweepy, Status eh a classe (?!) definida em 
  # https://github.com/tweepy/tweepy/blob/master/tweepy/models.py#L73
  for status in timeline:

    i = i + 1

    print(i,status.id,status.created_at,status.text)
    last_status_id = status.id

  timeline = api.user_timeline('alegomes',max_id=last_status_id-1)
