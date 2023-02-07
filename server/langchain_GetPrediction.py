from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_API_KEY")

print(os.environ["OPENAI_API_KEY"])

app = Flask(__name__)
CORS(app)
#context = ""

llm = OpenAI(temperature=0.9)

@app.route("/", methods=['GET', 'POST'])
def index():
  global context
  if request.method == 'GET':
    return "Hello from AI!"
  else:
    content = request.json
    prompt = content['prompt']

    print('prompt:' + prompt)
    response = llm(prompt)
    print('response:' + response)
  
    return jsonify(bot = response)

if __name__ == "__main__":
  app.run()
