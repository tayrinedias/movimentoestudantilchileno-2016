import tweepy
import datetime

# Metodo que coleta todos os tweets da timeline
# de um usuario especifico.
def collect_user_timeline(user):

  # Registre sua aplicacao em https://apps.twitter.com
  consumer_key="sua consumer_key"
  consumer_secret="sua consumer_secret"
  access_token="seu access_token"
  access_token_secret="seu access_token_secret"

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)

  # Busca toda a timeline de um usuario especifico, 
  # conforme documentacao em:
  # http://tweepy.readthedocs.org/en/v3.5.0/api.html#API.user_timeline
  timeline = api.user_timeline(user,max_id=999999999999999999)

  # Recupera o instante atual na forma AnoMesDiaHoraMinuto
  agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')

  # Vamos salvar os tweets de cada usuario em um arquivo diferente.
  tweets_file = open(user+"_tweets_"+agora+".txt", 'w')

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

      # Na tela, imprime o resumo do tweet...
      print(user,i,status.id,status.created_at,status.text)
      # ... no arquivo, imprime o tweet (status) inteiro.
      tweets_file.write(str(status._json)+"\n")

      # Salva o ID do ultimo tweet coletado para ser usado 
      # na busca da proxima pagina de tweets.
      last_status_id = status.id

    timeline = api.user_timeline(user,max_id=last_status_id-1)

  # Fecha o arquivo para que todas as informacoes enviadas
  # para ele sejam salvas com seguranca.
  tweets_file.close()

# Metodo principal do programa.
# Manda buscr os tweets de cada uma das contas de tweet 
# especificadas no array(?!) accounts.
def main():
  accounts=['giselecraveiro', 'true_software', 'MarizaPorto2']
  for account in accounts:
    collect_user_timeline(account)


# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()
