import requests
from config import CHAVE_API, TOP_HEADLINES, EVERYTHING 

def top_noticias(pais, fonte=None, pesquisa=None, categoria=None ):
  """
  Retorna as Top Noticias do dia
  """

  if fonte:
    url=f"{TOP_HEADLINES}sources={fonte}&apiKey={CHAVE_API}"
  elif categoria:
    url=f"{TOP_HEADLINES}country={pais}&category={categoria}&apiKey={CHAVE_API}"
  elif pesquisa:
    url=f"{TOP_HEADLINES}country={pais}&q={pesquisa}&apiKey={CHAVE_API}"
  else:
    url=f"{TOP_HEADLINES}country={pais}&apiKey={CHAVE_API}"
  
  #Pegando a resposta da API
  resposta = requests.get(url).json()

  #Pegando todos os artigos
  artigos = resposta['articles']

  #Lista vazia para preencher com as informações
  lista_top_noticias = []
  for artigo in artigos:
    lista_top_noticias.append(
      f"{artigo['title']}, "
      f"{artigo['source']['id']}, "
      f"{artigo['author']}, "
      f"{artigo['publishedAt']} "
    )

  return lista_top_noticias


def todas_noticias(pesquisa, lingua=None):
  """
  Retorna todas as noticias do site newsapi.org
  """

  lista_todas_noticias = []

  if pesquisa:
    if lingua:
      url=f"{EVERYTHING}q={pesquisa}&language={lingua}&apiKey={CHAVE_API}"
  
  #Pegando a resposta da API
  resposta = requests.get(url).json()

  #Pegando todos os artigos
  artigos = resposta['articles']

  #Lista vazia para preencher com as informações
  for artigo in artigos:
    lista_todas_noticias.append(
      f"{artigo['title']}, "
      f"{artigo['source']['id']}, "
      f"{artigo['author']}, "
      f"{artigo['publishedAt']} "
    )

  return lista_todas_noticias