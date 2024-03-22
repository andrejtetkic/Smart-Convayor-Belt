import os
from flask import *
from distutils.log import debug 
from fileinput import filename 
from logging import FileHandler,WARNING

app = Flask(__name__, static_folder='static', template_folder='templates')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
app.secret_key = "abc"

@app.route("/")
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "logcount.json")
    data = json.load(open(json_url))
    return render_template('index.html', data1=data["0"], data2=data["1"], data3=data["2"], dataAll=data["0"]+data["1"]+data["2"])

@app.route('/success', methods = ['POST'])
def success():   
    if request.method == 'POST':
        f = request.files['file']
        session['filen'] = f.filename
        f.save(f.filename)
        #render_template('index.html', name = f.filename)
        return "file uploaded successfully"

    
""" 
@app.route('/ObjectClassification/Logger/logcount.json', methods = ['GET'])
def logcount():
    with open('/ObjectClassification/Logger/logcount.json') as f:
        data = json.load(f)
    return jsonify(data) """

if __name__=='__main__':
    app.run(host = '0.0.0.0', port=80, debug = True)