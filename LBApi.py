import requests 
import letterboxd

#the ltbx api is close and is only in beta. 
#the only way to use their api is to apply for it.
#sad.

#Going to apply, hoping for a response soon, will be using RSS feed
#instead

#https://api-docs.letterboxd.com/#paths

#https://api.letterboxd.com/api/v0/ENDPOINT_PATH

#langEndpoint = 'https://api.letterboxd.com/api/v0//films/languages'

'''
response = requests.get(langEndpoint)
langsSupported = response.json()

print(langsSupported)
'''

lbxd = letterboxd.new()



#GET\u0000'https://api.letterboxd.com/api/v0//films/languages'\u0000