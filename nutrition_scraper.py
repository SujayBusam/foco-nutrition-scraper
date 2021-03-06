#1/usr/bin/python
import urllib2, urllib2, json, httplib
import json

# Nutrient Label Items from website
url = 'http://nutrition.dartmouth.edu:8088/cwp'


# mm_id is available from the daily menu parse...
# recipe_id is negative
# mm_rank is provided too

# able to change menu dates and access food listing for each date. 
parameters = {"service":"","method":"get_recipes_for_menumealdate","id":11,"params":[{"sid":"DDS.03cb6fca95f4cbea2245365827038394"},"{\"menu_id\":\"27\",\"meal_id\":\"3\",\"remoteProcedure\":\"get_recipes_for_menumealdate\",\"day\":27,\"month\":3,\"year\":2013,\"use_menu_query\":true,\"order_by\":\"pubgroup-alpha\",\"cache\":true}"]}

# Beef Casserole code
parameters = {"service":"","method":"get_nutrient_label_items","id":17,"params":[{"sid":"DDS.03cb6fca95f4cbea2245365827038394"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9786,\"recipe_id\":-473,\"mmr_rank\":165,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}

# Constructed code for Chicken Tamale given the daily menu item -- successful
parameters = {"service":"","method":"get_nutrient_label_items","id":17,"params":[{"sid":"DDS.03cb6fca95f4cbea2245365827038394"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9786,\"recipe_id\":-5202,\"mmr_rank\":169,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}


data = json.dumps(parameters)

headers = {"Content-Type": "application/json",
    'Content-Length' : len(data),
    "Referer":"http://nutrition.dartmouth.edu:8088/",
    #"Cookie":'JSESSIONID=2C6BBA00328C1C2F67794E50337D6E3A.N1TS002',
    "User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
    "method":"get_nutrient_label_items",
    "params": "",
    "id":25 # why static?
}

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

read =  response.read()
print read


response.close()
