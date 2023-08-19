from flask import Flask
from refactor.corev2 import CoreV2
from refactor.core import Core

app = Flask(__name__)

@app.route('/')
def hello_world():
    core = Core()
    return core.receive()


# @app.route('/')
# def hello_world():
#     core = CoreV2()
#     return core.receive()

