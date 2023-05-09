from fastapi import FastAPI
import json
import requests

 
def read_json_file(file_path):
    response = requests.get(file_path)
    json_data = json.loads(response.text)
    # json_data = (response.text)
    print(json_data)
    return json_data


app = FastAPI()
@app.get("/json-data") 
def get_json_data():
    file_path = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"  
    data = read_json_file(file_path)    
    return data
