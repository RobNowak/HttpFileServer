import os.path
from flask import Flask
from flask_autoindex import AutoIndex

app = Flask(__name__)
auto_index = AutoIndex(app, browse_root=os.path.curdir)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
