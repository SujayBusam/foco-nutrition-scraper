#1/usr/bin/python
import urllib2, urllib2, json, httplib
from bs4 import BeautifulSoup
import json

#soup = BeautifulSoup(urllib2.urlopen('http://nutrition.dartmouth.edu:8088/cwp?nocache=1359761631598').read())

url = 'http://nutrition.dartmouth.edu:8088/cwp'
#parameters = {'id':8, 'method':'get_nutrient_label_items', 'param':'[{"0":"sid"},{"1":}

#parameteres = s
parameters = {"service":"","method":"get_nutrient_label_items","id":8,"params":[{"sid":"DDS.8a220b5994c384ca0d2935ac172c668e"},"{\"remoteProcedure\":\"get_nutrient_label_items\",\"mm_id\":9328,\"recipe_id\":-5272,\"mmr_rank\":13,\"rule\":\"fda|raw\",\"output\":\"dictionary\",\"options\":\"facts\",\"cache\":true,\"recdata\":null}"]}
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

