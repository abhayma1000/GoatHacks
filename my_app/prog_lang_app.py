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








# Buyers post this information that they want to buy a certain ID's service
# Main operations are POST by the buyer and then GET (only ones with their name) for the seller
buy_confirmations_datastore = {
    "1" : {"id": "1", "Name": "Abhay", "Email": "amathur3@wpi.edu", "Price": 10, "Day": "Monday", "Buyer Name": "Jimmy", "Buyer Email": "jimmy@wpi.edu"},
}

@app.route('/buy_confirmations', methods=['GET', 'POST'])
def buy_confirmations_route():
   if request.method == 'GET':
       return list_buy_confirmations()
   elif request.method == "POST":
       return create_buy_confirmation(request.get_json(force=True))

def list_buy_confirmations():
   return {"buy_confirmations":list(buy_confirmations_datastore.values())}

def create_buy_confirmation(new_lang):
    language_name = new_lang['id']
    
    for i in range(len(sell_offers_datastore)):
        
        if list(sell_offers_datastore.keys())[i] == new_lang['id']:
            delete_sell_offer(new_lang['id'])

            buy_confirmations_datastore[language_name] = new_lang
            return new_lang

@app.route('/buy_confirmations/<buy_confirmation_name>', methods=['GET', 'PUT', 'DELETE'])
def buy_confirmation_route(buy_confirmation_name):
   if request.method == 'GET':
       return get_buy_confirmation(buy_confirmation_name)
   elif request.method == "PUT":
       return update_buy_confirmation(buy_confirmation_name, request.get_json(force=True))
   elif request.method == "DELETE":
       return delete_buy_confirmation(buy_confirmation_name)

def get_buy_confirmation(buy_confirmation_name):
    # Get buy confirmation based on the name you pass in
    new_datastore = []

    for i in buy_confirmations_datastore.values():
        if i['Name'] == buy_confirmation_name:
            new_datastore.append(i)
    
    return new_datastore
#    return buy_confirmations_datastore[buy_confirmation_name]

def update_buy_confirmation(lang_name, new_lang_attributes):
   lang_getting_update = buy_confirmations_datastore[lang_name]
   lang_getting_update.update(new_lang_attributes)
   return lang_getting_update

def delete_buy_confirmation(lang_name):
   deleting_lang = buy_confirmations_datastore[lang_name]
   del buy_confirmations_datastore[lang_name]
   return deleting_lang


