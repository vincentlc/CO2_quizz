import requests
from config import API_TOKEN_READ

model_1 = "Mistral-7B-Instruct-v0.2"
model_2 = "Mixtral-8x7B-Instruct-v0.1"

API_URL = "https://api-inference.huggingface.co/models/mistralai/" + model_1
headers = {"Authorization": f"Bearer {API_TOKEN_READ}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# give the code to get date in python
output = query({
    "inputs": "<s>[INST] Tell me about you[/INST]",
})
print(output[0]['generated_text'])