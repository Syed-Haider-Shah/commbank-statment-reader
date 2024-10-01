from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__) #instance of an app
cors = CORS(app, origins='*') #change this later

@app.route("/api/users", methods=['GET'])
def users():
  return jsonify(
    {
      "users": [
        'haider',
        'shah',
        'syed'
      ]
    }
  )

if __name__ == "__main__":
  app.run(debug=True, port=8080)