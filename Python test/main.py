import requests

host = 'https://api.pokemonbattle.me:9104'
token = '41a77e0b7904d3bcd0fd54df99e9cb34'

response_craete = requests.post(f'{host}/pokemons',
                          json={
    "name": "JOPKA",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},
                        headers={"Content-Type":"application/json" ,
                                  "trainer_token": token})
print(response_craete.text)

response_change = requests.put(f'{host}/pokemons',
                          json={

    "pokemon_id": "11146",
    "name": "POPKA",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
},
                        headers={"Content-Type":"application/json" ,
                                  "trainer_token": token})
print(response_change.text)


response_poc = requests.post(f'{host}/trainers/add_pokeball',
                          json={

    "pokemon_id": "11146",
},
                        headers={"Content-Type":"application/json" ,
                                  "trainer_token": token})
print(response_poc.text)

