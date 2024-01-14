from flask import Flask, request

app = Flask(__name__)

from flask_cors import CORS

cors = CORS(app)


# Sellers POST their information on the server and then the buyers GET this information on their local machine
# The main operations are POST by the seller and GET by the buyers
sell_offers_datastore = {
    # "1" : {"id": "1", "Email": "huy3@wpi.edu", "Price": 10, "Date": "2024-01-23"},
    # "2" : {"id": "2", "Email": "amathur3@wpi.edu", "Price": 1220, "Date": "2024-05-23"},
    # "3" : {"id": "3", "Email": "phong@wpi.edu", "Price": 333, "Date": "2024-02-23"},
    # "4" : {"id": "4", "Email": "epstein@wpi.edu", "Price": 69, "Date": "2024-04-23"},
    # "5" : {"id": "5", "Email": "khoiisfat@wpi.edu", "Price": 23323, "Date": "2024-03-23"},
}

@app.route('/sell_offers', methods=['GET', 'POST'])
def sell_offers_route():
   if request.method == 'GET':
       return list_sell_offers()
   elif request.method == "POST":
       return create_sell_offer(request.get_json(force=True))

def list_sell_offers():
   return {"sell_offers":list(sell_offers_datastore.values())}

def create_sell_offer(new_lang):
   language_name = new_lang['id']
   sell_offers_datastore[language_name] = new_lang
   return new_lang

@app.route('/sell_offers/<sell_offer_name>', methods=['GET', 'PUT', 'DELETE'])
def sell_offer_route(sell_offer_name):
   if request.method == 'GET':
       return get_sell_offer(sell_offer_name)
   elif request.method == "PUT":
       return update_sell_offer(sell_offer_name, request.get_json(force=True))
   elif request.method == "DELETE":
       return delete_sell_offer(sell_offer_name)

def get_sell_offer(sell_offer_name):
   return sell_offers_datastore[sell_offer_name]

def update_sell_offer(lang_name, new_lang_attributes):
   lang_getting_update = sell_offers_datastore[lang_name]
   lang_getting_update.update(new_lang_attributes)
   return lang_getting_update

def delete_sell_offer(lang_name):
   deleting_lang = sell_offers_datastore[lang_name]
   del sell_offers_datastore[lang_name]
   return deleting_lang



