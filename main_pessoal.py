from funcoes import *

api_key = '13a45376e8770f8efe9450e0974de27d'
auth_token = 'ATTAef2ff1e1acbc3e69e1128b6cc6179afec94c7a2c5d49abb165a277602f335574CFF83B61'
board_id = '63d91c958c44c45d8c4d9191'
to_do_id = '63d91c98a794ecbf9d148031'
id_plugin = '5ec6c1c179ade984555a12eb'
id_card = "63d91cbc7e1256979fe314b8"

api = Trello(api_key, auth_token)
# api.get_boards()

# api.get_lists(board_id)

list_of_cards = api.get_cards(to_do_id)
list_checkItems = get_checkItems(list_of_cards)
cards_without_badges = remove_bagdes(list_of_cards)
print(list_checkItems)
for card in list_of_cards:
    print(card)

# print(remove_bagdes(list_of_cards))
# api.get_plugins(board_id)

# print(api.get_pluginData(id_card))

# print(get_checkItems(api.get_cards(to_do_id)))
