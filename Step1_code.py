from flask import Flask, request

app = Flask(__name__)

seed = 0

@app.route('/', methods=['POST'])
def update_seed():
    global seed
    data = request.get_json()
    if 'num' in data:
        seed = data['num']
        return "Seed updated successfully to: " + str(seed)
    else:
        return "Error: Please provide 'num' parameter in JSON body", 400

@app.route('/', methods=['GET'])
def get_seed():
    global seed
    return str(seed)

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(debug=True, host='0.0.0.0')
