#1/usr/bin/python
import urllib2, urllib2, json, httplib
from bs4 import BeautifulSoup
import json

from pprint import pprint

# Nutrient Label Items from website

 # ids is wrong. .. the ids is merely a counter so that it doesn't clobber other data. An id increments for all the elements in the recipe.


#soup = BeautifulSoup(urllib2.urlopen('http://nutrition.dartmouth.edu:8088/cwp?nocache=1359761631598').read())


url = 'http://nutrition.dartmouth.edu:8088/cwp'
#parameters = {'id':8, 'method':'get_nutrient_label_items', 'param':'[{"0":"sid"},{"1":}

#parameters = {"service":"","method":"get_nutrient_label_items","id":8,"params":[{"sid":"DDS.8a220b5994c384ca0d2935ac172c668e"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9328,\"recipe_id\":-5272,\"mmr_rank\":13,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}
parameters = {"service":"","method":"get_recipes_for_menumealdate","id":18,"params":[{"sid":"DDS.8a220b5994c384ca0d2935ac172c668e"},"{\"menu_id\":\"27\",\"meal_id\":\"5\",\"remoteProcedure\":\"get_recipes_for_menumealdate\",\"day\":31,\"month\":1,\"year\":2013,\"use_menu_query\":true,\"order_by\":\"pubgroup-alpha\",\"cache\":true}"]}
data = json.dumps(parameters)

headers = {"Content-Type": "application/json",
'Content-Length' : len(data),
"Referer":"http://nutrition.dartmouth.edu:8088/",
#"Cookie":'JSESSIONID=2C6BBA00328C1C2F67794E50337D6E3A.N1TS002',
"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
"method":"get_nutrient_label_items",
"params": "",
"id":25
}

#conn=httplib.HTTPConnection(url,80)
#conn.request("POST","/cwp?nocache=1359761631598",data,headers)
#conn.request("POST","/cwp?",data,headers)

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

result = response.read()

decoded_result = json.loads(result)
#pprint(decoded_result)

response.close()

#print decoded_result["id"]


print '*******   DAILY FOOD AT FOCO LIST *******'
#print response.read()
#print response.read()

#soup = BeautifulSoup(response)

#print soup.prettify()

print '*******   CONSOLIDATED LIST OF ALL THE FOOD ITEMS *******'

# Parse the original list for the id of each food item 
#input = response.read()





#print '*******'
#print '*******   SPECIFIC NUTRIENT INFORMATION FOR A FOOD *******'

url = 'http://nutrition.dartmouth.edu:8088/cwp'

#parameters = {"service":"","method":"get_nutrient_label_items","id":8,"params":[{"sid":"DDS.8a220b5994c384ca0d2935ac172c668e"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9328,\"recipe_id\":-5272,\"mmr_rank\":13,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}
#parameters = {"service":"","method":"get_recipes_for_menumealdate","id":18,"params":[{"sid":"DDS.8a220b5994c384ca0d2935ac172c668e"},"{\"menu_id\":\"27\",\"meal_id\":\"5\",\"remoteProcedure\":\"get_recipes_for_menumealdate\",\"day\":31,\"month\":1,\"year\":2013,\"use_menu_query\":true,\"order_by\":\"pubgroup-alpha\",\"cache\":true}"]}

# parameteres that work and show a different item
#parameters = {"service":"","method":"get_nutrient_label_items","id":8,"params":[{"sid":"DDS.8a220b5994c384ca0d2935ac172c668e"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9328,\"recipe_id\":-5279,\"mmr_rank\":13,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}
parameters = {"service":"","method":"get_nutrient_label_items","id":2,"params":[{"sid":"DDS.8a220b5994c384ca0d2935ac172c668e"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9328,\"recipe_id\":-5279,\"mmr_rank\":22,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}


#### the food item parameteres depend on three things: mm_id, mm_id, mmr_rank. 
##  the id in the parameters doesn't matter! merely to prevent clobbering 
## each item seems to share the same mm_id which is 9328...
## the mm_rank does not go linearly down the menu: 
## 


data = json.dumps(parameters)

headers = {"Content-Type": "application/json",
'Content-Length' : len(data),
"Referer":"http://nutrition.dartmouth.edu:8088/",
#"Cookie":'JSESSIONID=2C6BBA00328C1C2F67794E50337D6E3A.N1TS002',
"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
"method":"get_nutrient_label_items",
"params": "",
"id":25
}

#conn=httplib.HTTPConnection(url,80)
#conn.request("POST","/cwp?nocache=1359761631598",data,headers)
#conn.request("POST","/cwp?",data,headers)

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

print response.read()

print '*******'


# grab each individual food item name and then insert that into 

