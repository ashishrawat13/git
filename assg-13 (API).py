import requests
import json
parameters={'method':'getQuote','format':'json','lang':"en",'key':''}
response=requests.get("https://api.forismatic.com/api/1.0/getQuote.json",params=parameters)
res=response.json()
print("Random Quote: {} \n                    - {}".format(res['quoteText'],res['quoteAuthor']))
#

