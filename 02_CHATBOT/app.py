from flask import Flask, render_template, request, jsonify
from chatbot import get_answer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json['question']
    answer = get_answer(user_question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
