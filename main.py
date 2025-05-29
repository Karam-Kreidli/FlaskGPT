from flask import Flask,  jsonify, request
import openai
import threading
import socket

class NewThreadedTask(threading.Thread):
     def __init__(self):
         super(NewThreadedTask, self).__init__()

     def run(self):
        return

app = Flask(__name__)
hostName = socket.gethostname()

openai.api_key = ''
messages = [ {"role": "system", "content":
              "You are an intelligent system"} ]

@app.route('/api/v1/chat', methods=['GET'])
def get_prompt():
    return hostName

@app.route('/api/v1/chat', methods=['POST'])
def give_prompt():
    message = request.json
    prompt = message['prompt']
    messages.append(
        {"role": "user", "content": prompt},
    )
    chat = openai.chat.completions.create(
    model="gpt-4o", messages=messages
    )
    reply = chat.choices[0].message.content
    return jsonify(reply), 202

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")