from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    spirit = requests.get("http://localhost:5001/spirit")
    volume = requests.get("http://localhost:5002/volume")
    mixer = requests.post("http://localhost:5003/mixer", data = spirit)

    return render_template('base.html', spirit=spirit.text, volume = volume.text, mixer=mixer.text)

if __name__=="__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')