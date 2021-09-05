from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run(): 
    return "{\"message\":\"Hello World Python Nuvepro from Jenkins now\"}"
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)