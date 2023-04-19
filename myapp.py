from flask import Flask

app = Flask(__name__)  #建立application物件

#建立网站首页的相应方式

@app.route("/")
def index():
    return "helloworld"

@app.route("/hellomytest/1")
def mytest():
    return "the world"



app.run()

