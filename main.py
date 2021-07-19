from flask import Flask
import sys
from flask.templating import render_template
from apis.getfiles import getfiles
from apis.getcolumns import getcolumns
from apis.getdata import getdata
import os
from Files import file_path

# Getting the file path from command line
# file = sys.argv[1]

# Setting the environment variable
# os.environ['FILE_PATH'] = FILE_DIR
# os.environ['FILE_PATH_REDUCED'] = FILE_DIR_REDUCED

print(os.getenv('FILE_PATH'))

app = Flask(__name__)

# Registering the blueprint of the API files

app.register_blueprint(getfiles)
app.register_blueprint(getcolumns)
app.register_blueprint(getdata)

# index page route


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    return "<p> Page not found </p>"


if __name__ == '__main__':
    app.run()
