from flask import Flask, jsonify
api = Flask(__name__)

@api.route("/")
def msg():
     return jsonify(msg_="Hello World!")

if __name__=="__main__":
     api.run("0.0.0.0",debug=True)