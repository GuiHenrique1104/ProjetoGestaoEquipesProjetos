import requests
import json
from datetime import datetime

# api_url = f"https://api.trello.com"

class Trello:

    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token

    def get_boards(self):
        api_url = f"https://api.trello.com/1/members/me/boards?fields=id,name,desc,closed,dateClosed,dateLastActivity,shortUrl"

        params = {
            'key': self.api_key,
            'token': self.api_token
        }

        headers = {
            'Accept': 'application/json'
        }

        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
            # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ":")))
        return "Não foi possível fazer a requisição dos Quadros do Trello"

    def get_lists(self, board_id):
        api_url = f"https://api.trello.com/1/boards/{board_id}/lists?fields=id,name,closed,pos"

        params = {
            'key': self.api_key,
            'token': self.api_token
        }

        headers = {
            'Accept': 'application/json'
        }

        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
            # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ":")))
        return "Não foi possível fazer a requisição das Listas do Trello"

    def get_cards(self, list_id):
        api_url = f'https://api.trello.com/1/lists/{list_id}/cards?fields=id,name,desc,closed,start,due,dateLastActivity,dueComplete,shortUrl,badges'

        params = {
            'key': self.api_key,
            'token': self.api_token
        }

        headers = {
            'Accept': 'application/json'
        }

        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:

            # check_items = get_checkItems(response.json())
            # response = remove_bagdes(response.json())
            # return response, check_items

            return response.json()
            # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ":")))
        return "Não foi possível fazer a requisição dos Cartões do Trello"

    def get_members(self, member_id):
        api_url = f"https://api.trello.com/1/members/{member_id}"

        params = {
            'key': self.api_key,
            'token': self.api_token
        }

        headers = {
            'Accept': 'application/json'
        }

        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
            # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ":")))
        return "Não foi possível fazer a requisição do Membro do Trello"

    def get_plugins(self, board_id):
        url = f"https://api.trello.com/1/boards/{board_id}/plugins"

        headers = {
            "Accept": "application/json"
        }

        params = {
            'key': self.api_key,
            'token': self.api_token
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
            # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ":")))
        return "Não foi possível fazer a requisição de Plugins do Trello"

    def get_pluginData(self, id_card):
        url = f"https://api.trello.com/1/cards/{id_card}/pluginData?fields=all"

        headers = {
            "Accept": "application/json"
        }

        params = {
            'key': self.api_key,
            'token': self.api_token
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
            # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ":")))
        return "Não foi possível fazer a requisição de PluginData do Trello"


def timestamp_to_iso8601(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    iso8601 = dt.isoformat() + 'Z'
    return iso8601


def get_checkItems(list_of_cards):
    list_of_checks = []
    for card in list_of_cards:
        for key, value in card.items():
            if key == 'badges':
                list_of_checks.append((value['checkItems'], value['checkItemsChecked']))
    return list_of_checks


def remove_bagdes(list_of_cards):
    for card in list_of_cards:
        del card['badges']
    return list_of_cards

# api_key = '13a45376e8770f8efe9450e0974de27d'
# auth_token = 'ATTAef2ff1e1acbc3e69e1128b6cc6179afec94c7a2c5d49abb165a277602f335574CFF83B61'
# board_id = '63d91c958c44c45d8c4d9191'
# list_id = '63d91c98a794ecbf9d148031'
# member_id = '63dc0cc1bc89d5a492ab1559'
#
# api = Trello(api_key, auth_token)
# print(api.get_boards())
# # print(api.get_lists(board_id))
# # print(api.get_cards(list_id))
# print(api.get_members(member_id))
