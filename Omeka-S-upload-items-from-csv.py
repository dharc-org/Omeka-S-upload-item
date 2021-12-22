# -*- coding: utf-8 -*-

# Omeka-S-upload-items-from-csv.py
# v0.1

import requests
import json
import os
import sys

# check arguments
if len(sys.argv) < 2:
    print("No parameter has been include")
    print(" 1) config.json file")
    print(" 2) csv data file - i.e. data.csv")
    print("i.e. $ python3 Omeka-S-upload-items-from-csv.py config.json data.csv")
    sys.exit()

# get var from arguments
paramsPath = sys.argv[1]
pathCsv = sys.argv[2]

# set params and headers
paramsJson = json.loads(open(paramsPath, 'rb').read())
apiLink = paramsJson['apiLink']
params = {
    'key_identity': paramsJson['key_identity'],
    'key_credential': paramsJson['key_credential']
}
headers = {
    'Content-type': 'application/json'
}

# set data
item_class = 1
title = "Opera nuova da script"
creator = "Autore Opera"
item_set = 956
data = {"dcterms:title":
            [{"property_id": 1, "property_label": "dcterms:title", "@value": title, "type": "literal"},
             {"property_id": 2, "property_label": "dcterms:creator", "@value": creator, "type": "literal"}
             ],
        "@type": "o:Item",
        "o:item_set": [{"o:id": item_set}],
        "o:media": []
        }

print(apiLink)
print(params)
print(data)
print(headers)

response = requests.post(apiLink, params=params, data=json.dumps(data), headers=headers)
print(response)
