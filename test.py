from flask import Flask

app = Flask(__name__)

@app.route('/helloesp')
def hello():
    return "Hello ESP2866, from Flask"
app.run(host='0.0.0.0',port=8090)