from flask import Flask, request, jsonify, render_template
import os

from utils import get_response, predict_class

app = Flask(__name__, template_folder='templates')
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_message', methods=['POST'])
def handle_message():
    data = request.get_json()
    message = data.get('message', '')

    if not message:
        return jsonify({'response': "Desculpe, não entendi sua mensagem."})

    intents_list = predict_class(message)
    response = get_response(message)
    return jsonify({'response': response})

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, port = port)