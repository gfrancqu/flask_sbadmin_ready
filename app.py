####################################################
 # 
 # File Name 		:app.py
 # Created by		:Guillaume Francqueville
 # Creation date	:novembre 10th, 2016
 # Last changed by 	:Guillaume Francqueville
 # Last change 		:novembre 13th, 2016 18:11
 # Description		:basic bootstrap templates for flask using SB Admin theme, just fork and dev
 #
####################################################

from flask import *
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html',title='index page')

@app.route('/vendor/<path:filename>')
def serve_vendor(filename):
    return send_from_directory('vendor',filename)

if __name__ == "__main__":
    app.run()
