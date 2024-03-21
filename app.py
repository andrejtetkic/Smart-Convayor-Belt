from flask import *
from distutils.log import debug 
from fileinput import filename 

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "abc"
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/success', methods = ['POST'])
def success():   
    if request.method == 'POST':
        f = request.files['file']
        session['filen'] = f.filename
        f.save(f.filename)
        #render_template('index.html', name = f.filename)
        return "file uploaded successfully"

if __name__=='__main__':
    app.run(host = '0.0.0.0', port=80, debug = True)