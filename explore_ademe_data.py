import requests
import json
# Code Vincent

base_url = "https://impactco2.fr/api/v1/"
thematics = "thematiques"
ecv = "ecv"
# Get the thematics
response = requests.get(base_url + thematics)
assert response.status_code == 200
json_response = response.json()

# Printing the categories and values
# for category in response.json().get("data", []):
#     print(" ".join([category.get("emoji",""),category.get("name")]))

# Get the slug of all thematics
category_list = []
for category in response.json().get("data", []):
    category_list.append(category.get("slug"))
print(category_list)

# Get ecv of the first category
for category in category_list:
    response_category = requests.get("/".join([base_url, thematics, ecv, category]))
    assert response_category.status_code == 200
    print(json.dumps(response_category.json(), indent=4))  # print the result
