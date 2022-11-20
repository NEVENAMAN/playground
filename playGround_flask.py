from flask import Flask , render_template
app = Flask(__name__)
# ----------------------------------------------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play/<num>')
def play(num):
    return render_template("index.html",num=int(num))

@app.route('/color/<num>/<colorName>')
def color(num,colorName):
    return render_template("index.html",num=int(num),colorName =colorName)
# ----------------------------------------------------------
if __name__ =="__main__":
    app.run(debug = True)