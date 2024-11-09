from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def home():
    return "Hello World!"

@app.route('/greeting', methods=['POST'])
def greeting():
    
    data = request.json

    name = data.get('name')

    response = {
        'message': f'Hello, {name}!',
        'success': True
    }

    # Return a JSON response
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)