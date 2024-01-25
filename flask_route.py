from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def add_file(data):
    return data + 5

@app.route("/")
def hello():
    return "<h1>Hello world!</h1>"

@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d " % message_id

@app.route("/first/<int:message_id>")
def get_first(message_id):
    data = add_file(message_id)
    return "<h1>%d</h1>" % data

@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login.html')

@app.route('login')
def login():
    username = request.args.get('user_name')
    passwd = request.args.get('pw')
    email = request.args.get('email_address')

    if username == 'dave':
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    
    return jsonify(return_data)

if __name__ == '__name__':
    app.run(host='0.0.0.0', port='8081')