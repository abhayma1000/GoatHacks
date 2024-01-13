from flask import Flask, request

app = Flask(__name__)


# Sellers POST their information on the server and then the buyers GET this information on their local machine
# The main operations are POST by the seller and GET by the buyers
sell_offers_datastore = {
    "1" : {"id": "1", "name": "Abhay", "Time of day": "Lunch", "Price": 10, "#MealSwipes": 1, "Location": "Morgan"},
    "2" : {"id": "2", "name": "Stephen", "Time of day": "Dinner", "Price": 1, "#MealSwipes": 2, "Location": "Halal"},
    "3" : {"id": "3", "name": "Khoi", "Time of day": "Breakfast", "Price": 2, "#MealSwipes": 5, "Location": "Morgan"},
    "4" : {"id": "4", "name": "Huy", "Time of day": "Lunch", "Price": 3, "#MealSwipes": 3, "Location": "Halal"},
    "5" : {"id": "5", "name": "Phong", "Time of day": "Dinner", "Price": 4, "#MealSwipes": 0, "Location": "CC"},
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
    "1" : {"id": "1", "name": "Abhay", "Time of day": "Lunch", "Price": 10, 
    "#MealSwipes": 1, "Location": "Morgan", "Buyer Name": "Jimmy", "Exact Time": "11:00", "Exact Location": "Near Trash Can"},
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
        if i['name'] == buy_confirmation_name:
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


