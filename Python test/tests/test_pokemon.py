import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '41a77e0b7904d3bcd0fd54df99e9cb34'

def test_status_code():
  response = requests.get(f'{host}/trainers', params={'trainer_id':1522})
  assert response.status_code == 200

def test_part_of_body  ():
  response = requests.get(f'{host}/trainers', 
                          params={'trainer_id':1522}, 
                          headers={'trainer_token': token},)
                        
  assert response.json()["trainer_name"] == "СHECK"
