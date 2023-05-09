from flask import Flask, request, jsonify
import openai
import requests

app = Flask(__name__)
secret_key_path = 'secret_key.txt'

with open('secret_key.txt', 'r') as file:
    secret_key = file.read()

openai.api_key = secret_key


def code_converter(data):
    instruction = f"Act as a code convertor, convert given {data['input_language']} code into {data['target_language']}, perform same functionality with proper syntax, proper main function and import or include statement if it is required, variable name, do not give any explanation, do not give any extra information\n```"
    prompt = instruction + data['code'] + '```'
    openai_model = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.0,
    )
    target_code = openai_model.choices[0].text.strip()
    print(target_code)
    return target_code
@app.route("/converted_code", methods=["POST"])
def converter():
    data = request.get_json()
    response = code_converter(data)
    response = {"result": response}
    return jsonify(response)

@app.route("/upload", methods=['POST'])
def upload_file():
    file = request.files['file']
    content = file.read().decode('utf-8').strip('\n')
    form_data = request.form.to_dict()
    all_data = {
        "input_language":form_data['input_language'],
        "target_language":form_data['target_language'],
        "code":content
    }
    
    response = code_converter(all_data)
    return {'result':response}


# def code_chacker():
#     url = "https://api.compilers.sphere-engine.com/api/v4/compile"
#     params = {
#         "access_token": "YOUR_ACCESS_TOKEN",
#         "language": "python",
#         "source": "print('Hello, world!')",
#     }
#     response = requests.post(url, data=params)
#     if response.ok:
#         result = response.json()
#         if result["success"]:
#             return True
#         else:
#             return result["errors"]
#     else:
#         print("Something went wrong:", response.reason)



