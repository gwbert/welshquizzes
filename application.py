from flask import Flask, render_template, url_for, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/email")
def email():
    return render_template('email.html')

@app.route("/errata")
def errata():
    return render_template('errata.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/blog/<blogName>")
def blogentry(blogName):
    import blog
    myObject = getattr(blog, blogName)
    return render_template('blog.html', myObject=myObject)

@app.route("/shortblog/<blogName>")
def shortblogentry(blogName):
    import blog
    myObject = getattr(blog, blogName)
    return render_template('shortblog.html', myObject=myObject)

@app.route("/blog2")
def blog2():
    return render_template('blog2.html')

@app.route("/suggest")
def suggest():
    return render_template('suggest.html')

@app.route("/culture")
def culture():
    return render_template('culture.html')

@app.route("/regions")
def regions():
    return render_template('regions.html')

@app.route("/general")
def general():
    return render_template('general.html')

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/geography")
def geography():
    return render_template('geography.html')

@app.route("/transport")
def transport():
    return render_template('transport.html')

@app.route("/jumbo")
def jumbo():
    return render_template('jumbo.html')

@app.route("/sport")
def sport():
    return render_template('sport.html')

@app.route("/chloropethCounties")
def chloropethCounties():
    return render_template('chloropethCounties.html')

@app.route("/mapquiz/<quizName>")
def mapquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('mapquiz.html', myObject=myObject)

@app.route("/picturequiz/<quizName>")
def picturequiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('picturequiz.html', myObject=myObject)

@app.route("/jumbopicturequiz/<quizName>")
def jumbopicturequiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('jumbopicturequiz.html', myObject=myObject)

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

@app.route("/smallquiz/<quizName>")
def smallquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('smallquiz.html', myObject=myObject)

@app.route("/mediumquiz/<quizName>")
def mediumquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('mediumquiz.html', myObject=myObject)

@app.route("/tenquiz/<quizName>")
def tenquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('tenquiz.html', myObject=myObject)

@app.route("/elevenquiz/<quizName>")
def elevenquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('elevenquiz.html', myObject=myObject)

@app.route("/fifteenquiz/<quizName>")
def fifteenquiz(quizName):
    import quizzes
    myObject = getattr(quizzes, quizName)
    return render_template('fifteenquiz.html', myObject=myObject)

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
    app.run()