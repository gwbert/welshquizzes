from flask import Flask, render_template, url_for, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/index2")
def index2():
    return render_template('index2.html')

@app.route("/culture")
def culture():
    return render_template('culture.html')

@app.route("/general")
def general():
    return render_template('general.html')

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/jumbo")
def jumbo():
    return render_template('jumbo.html')

@app.route("/sport")
def sport():
    return render_template('sport.html')

@app.route("/picturequiz/<quizName>")
def picturequiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('picturequiz.html', myObject=myObject)

@app.route("/picturequiz2/<quizName>")
def picturequiz2(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('picturequiz2.html', myObject=myObject)

@app.route("/fivequiz/<quizName>")
def fivequiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('fivequiz.html', myObject=myObject)

@app.route("/tenquiz/<quizName>")
def tenquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('tenquiz.html', myObject=myObject)

@app.route("/twentyquiz/<quizName>")
def twentyquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('twentyquiz.html', myObject=myObject)

@app.route("/thirtyquiz/<quizName>")
def thirtyquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('thirtyquiz.html', myObject=myObject)

application = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)