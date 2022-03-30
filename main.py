import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def is_bitlink(token, url):
  headers = {
    "Authorization": 'Bearer {}'.format(token)
  }

  tmp_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
  parsed_url = urlparse(url)

  url = tmp_url.format(parsed_url.netloc + parsed_url.path)
  response = requests.get(url, headers=headers)
  
  return response.ok


def count_clicks(token, link):
  headers = {
    "Authorization": 'Bearer {}'.format(token)
  }

  params = {
    "units" : -1
  }
  
  tmp_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
  parsed_url = urlparse(link)
  bitlink = parsed_url.netloc + parsed_url.path

  url = tmp_url.format(bitlink)
  response = requests.get(url, headers=headers, params=params)
  response.raise_for_status()

  return response.json()['total_clicks']


def shorten_link(token, url, domain):
  headers = {
    "Authorization": 'Bearer {}'.format(token),   
  }

  payload = {
    "long_url": url
  }
  
  if domain:
    payload += { "domain": domain }
  
  url = 'https://api-ssl.bitly.com/v4/shorten'
  
  response = requests.post(url, headers=headers, json=payload)
  
  response.raise_for_status()

  return response.json()['link']


def check_link(url):
  response = requests.get(url)
  response.raise_for_status()


def main():
  load_dotenv()

  token = os.getenv('BITLY_TOKEN')
  domain = os.getenv('BYTLI_DOMAIN')
  
  parser = argparse.ArgumentParser(
        description="""Программа позволяет сократить ссылку или получить количество кликов по уже сокращенной
                    для этого при вызове скрипта нужно передать аргументом --url ссылку, с которой нужно произвести операцию.""")
  parser.add_argument('--url', help='Введите ссылку')
  args = parser.parse_args()
  try:
    check_link(args.url)    
    if is_bitlink(token, args.url):
      total_clicks = count_clicks(token, args.url)
      print('Всего переходов по ссылке:', total_clicks)
    else:
      bitlink = shorten_link(token, args.url, domain)
      print('Битлинк', bitlink)
  except requests.exceptions.HTTPError:
      print("Вы ввели неправильную ссылку или неверный токен.")


if __name__ == "__main__":
  main()
