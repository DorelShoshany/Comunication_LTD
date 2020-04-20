

# decorating index function with the app.route
from application import app
from flask import render_template, request, Response, json

packagesData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
   return render_template("index.html", login=False)


@app.route("/login")
def login():
    return render_template("login.html", login=False)


@app.route("/packages")
def packages():
    return render_template("packages.html",packagesData=packagesData, login=True)


@app.route("/register")
def register():
    return render_template("register.html", login=False)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form['title']
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "term": term})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if (idx == None):
        jdata = packagesData
    else:
        jdata = packagesData[int(idx)]

            # Response object =json.dumps(jdata)
    return Response(json.dumps(jdata), mimetype="application/json")


