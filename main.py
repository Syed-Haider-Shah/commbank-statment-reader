from flask import Flask, jsonify

app = Flask(__name__) #instance of an app

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