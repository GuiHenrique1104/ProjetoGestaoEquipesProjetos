import funcoes
import json

key_trabalho = '2f341d4faeae59b2cf6a8337793ff7f8'
token_trabalho = 'ATTA3089c5b323ff2f0dd9555bbcd0e1441c4af9f14f10cd22cafde2089d4b432e0349C12889'

board_id = "6391f25a8b734c0134dee1a4"
doing_id = "6391f25a8b734c0134dee1ad"
id_card = "63eb7c3ff872726e75b9918f"
id_plugin_time = "5ec6c1c179ade984555a12eb"
id_plugin_x = "5eda444d3be9d07a01eb82a4"
id_guilherme = "63cfcc7947f8f1c60efa7f25"

api = funcoes.Trello(key_trabalho, token_trabalho)
# api.get_boards()
# api.get_lists(board_id)
# api.get_cards(doing_id)
# api.get_plugins(board_id)
# api.get_members(id_guilherme)
api.get_pluginData(id_card)
