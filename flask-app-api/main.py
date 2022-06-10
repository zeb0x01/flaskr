import os
import sys
import subprocess
from flask import Flask

print("maybe working")

app = Flask(__name__)

@app.route('/api')

def hello_world():
    return '<p>api gateway</p>'

if __name__ == '__main__':
    app.run()

