from flask import Flask
app = Flask(name)
@app.route('/greet')
def greet():
return 'Hello from Backend Microservice!'
if name == 'main':
app.run(host='0.0.0.0', port=5000)
