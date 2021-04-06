from flask import Flask

MESSAGE = 'SECRET MESSAGE!'
app = Flask(__name__)

@app.route('/')
def message():
    return MESSAGE + '\n'

if __name__=='__main__':
    app.run(debug=True, port=8090)