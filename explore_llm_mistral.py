import requests
from config import API_TOKEN_READ
from transformers import AutoModelForCausalLM, AutoTokenizer

model_1 = "Mistral-7B-Instruct-v0.2"
model_2 = "Mixtral-8x7B-Instruct-v0.1"

API_URL = "https://api-inference.huggingface.co/models/mistralai/" + model_2
headers = {"Authorization": f"Bearer {API_TOKEN_READ}"}

# tokenizer = AutoTokenizer.from_pretrained("mistralai/"+model_2)


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def generate_instruction(instruction):
    return "<s>[INST]" + instruction + "[/INST]</s>"


def easy_query(text):
    reply = query({"inputs": generate_instruction(text), })
    assert len(reply) > 0
    generated_text = reply[0].get("generated_text", text)
    return generated_text.split("[/INST]</s>")[1].strip()




instruction_quizz = """You are a quizz bot.
Your task is to write questions about the carbon footprint of object.
In each question, you will ask to compare two objects.
You will not pick the same object in different questions.
You will respond with 1 questions.
Each question will be less than 10 words long.
###
Here are the objects and their carbon footprint:
Smartphone: 37
Computer: 188
Banana: 3
Apple: 2
Car: 101
Bus: 203
Pen: 44
Ball: 55
Steak: 144
Orange: 9
Mango: 11
###
Here are examples:
Which has the lowest carbon footprint, a banana or an apple?
###
You will respond a random 1 questions.
"""
#everytime you will accumulate the previous one in order to generate a new question

##Which has a higher carbon footprint between a smartphone and a computer?
return_first_response = easy_query(instruction_quizz)
print(return_first_response)

user_answer = "I think it's the bus"

question_2 = instruction_quizz+return_first_response+"""[INST]
The user gave you the following answer:
""" + user_answer + """
Your task is to check the user's answer based only on the carbon footprints. If it's false, give the correct answer. If it's correct congratulate the user
You will respond in less than 10 words.
[/INST]
"""
response_2 = easy_query(question_2)
print(response_2)

simple_question = """Class the following element carbon footprint from lower to higher
Here are the objects and their carbon footprint that are integer value:
Banana: 3
Apple: 2
Orange: 9
Mango: 11
"""

#Bref ca marche pas
# print(easy_query(simple_question))


