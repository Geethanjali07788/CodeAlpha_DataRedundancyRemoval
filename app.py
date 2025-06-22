from flask import Flask, request, jsonify
from handler import insert_data

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    result = insert_data(data)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)