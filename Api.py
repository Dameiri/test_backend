import requests
import json

#l'endpoint en dict
url='https://api.github.com/some/endpoint'
payload={"id":"id",
         "trame":"trame",
         "colors":"colors_names",
         "mass_surf":"mass_surf",
         "is_compainterwall":"is_compat_interior_wall",
         "height": "mesh_height",
         "width": "mesh_width",
         "roll_pallet":"roll_pallet",
         "comb":"comb"}
#post en json  
r=requests.post(url,data=json.dumps(payload))
print(json.dumps(payload))

url2='https.//httpbin.org/get'
#get request
getting=requests.get(url2,params=payload)     
#print(getting.status_code)    


#