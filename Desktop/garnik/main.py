from flask import Flask, render_template, request, redirect, json, session
from models import Database
from form import Registration, LoginForm, ChangePasswordForm, Update
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO, emit, send
import random, os
import datetime

db = Database("gar")
app = Flask(__name__, static_url_path='', static_folder='static')
bcrypt = Bcrypt(app)
app.secret_key = "my secret key"
app.config['UPLOAD-PATH'] = 'static'
socketio = SocketIO(app)

chat_users = {}


###########################################################################################
@app.route("/", methods=['POST', 'GET'])
def index():
    form = Registration(request.form)
    if request.method == "POST" and form.validate():
        # print('ok')
        pw_hash = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")
        db.insert("user", {"name": request.form["name"],
                           "surname": request.form["surname"],
                           "gender": request.form["gender"],
                           "email": request.form["email"],
                           "age": request.form["age"],
                           "password": pw_hash,
                           "photo": 'images/users/user1.png'})
        return redirect('/login')
    return render_template("index-register.html", form=form)


###########################################################################################
@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = db.login("user", request.form["email"])
        # print(user)
        if user:
            if bcrypt.check_password_hash(user['password'], request.form["password"]):
                session["user"] = user
                return redirect("/profil")
    return render_template('login.html', form=form)


###########################################################################################
@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop("user")
    return redirect("/login")


###########################################################################################
@app.route("/profil", methods=['POST', 'GET'])
def profil():
    d = db.get("posts")
    return render_template("/profil.html", user=session.get("user"), post=d)


###########################################################################################
@app.route("/myprofil", methods=['POST', 'GET'])
def myprofil():
    a = db.add(session.get("user")["id"])
    # print(a)
    return render_template("/myprofil.html", user=session.get("user"), a=a)


###########################################################################################
@app.route("/lyudi", methods=['POST', 'GET'])
def lyudi():
    return render_template("/lyudi.html", user=session.get("user"))


###########################################################################################
@app.route("/druzya", methods=['POST', 'GET'])
def druzya():
    i = db.getFrend(session.get("user")["id"])
    # print(i)
    return render_template("/druzya.html", user=session.get("user"), posts=i)


###########################################################################################
@app.route("/image", methods=['POST', 'GET'])
def image():
    im = db.findAll("photo", session.get("user")["id"])
    # print(im)
    return render_template("/image.html", user=session.get("user"), img=im)


###########################################################################################
@app.route("/about", methods=['POST', 'GET'])
def about():
    return render_template("/about.html", user=session.get("user"))


###########################################################################################
@app.route("/besic", methods=['POST', 'GET'])
def besic():
    form = Update(request.form)
    if request.method == "POST" and form.validate():
        db.update("user",
                  {"name": request.form["name"], "surname": request.form["surname"], "age": request.form["age"]},
                  {'id': session.get("user")['id']})
        user = db.find('user', session.get('user')['id'])
        # print(user)
        session['user'] = user
        return redirect("/profil")
    return render_template("/besic.html", user=session.get("user"), form=form)


###########################################################################################
@app.route("/album", methods=['POST', 'GET'])
def album():
    return render_template("/album.html", user=session.get("user"))


###########################################################################################
@app.route("/friends", methods=['POST', 'GET'])
def friends():
    return render_template("/friends.html", user=session.get("user"))


###########################################################################################
@app.route("/work", methods=['POST', 'GET'])
def work():
    return render_template("/work.html", user=session.get("user"))


###########################################################################################
@app.route("/interests", methods=['POST', 'GET'])
def interests():
    return render_template("/interests.html", user=session.get("user"))


###########################################################################################
@app.route("/settings", methods=['POST', 'GET'])
def settings():
    return render_template("/settings.html", user=session.get("user"))


###########################################################################################
@app.route("/password", methods=['POST', 'GET'])
def password():
    form = ChangePasswordForm(request.form)
    user = session.get("user")
    if request.method == "POST" and form.validate():
        if bcrypt.check_password_hash(user['password'], request.form["oldPassword"]):
            pw_hash = bcrypt.generate_password_hash(request.form["newPassword"]).decode("utf-8")
            db.update("user", {'password': pw_hash}, {'id': session.get("user")['id']})
            return redirect("/login")
    return render_template("/password.html", user=session.get("user"), form=form)


###########################################################################################
@app.route("/faq", methods=['POST', 'GET'])
def faq():
    return render_template("/faq.html", user=session.get("user"))


###########################################################################################
@app.route("/addPhoto", methods=['POST', 'GET'])
def addPhoto():
    photo = request.files["photo"]
    photoName = str(random.randrange(1000, 100000000001)) + photo.filename
    photoUrl = os.path.join(app.config['UPLOAD-PATH'], "images", photoName)
    photo.save(photoUrl)
    db.insert("photo", {"url": "images/" + photoName, "user_id": session.get("user")['id']})
    # print(photoName)
    return redirect('/album')


@app.route("/getPhoto", methods=['POST', 'GET'])
def getPhoto():
    p = db.photo("photo", session.get('user')['id'])
    # print(p)
    return json.dumps(p)


@app.route("/deletePhoto", methods=['POST', 'GET'])
def deletePhoto():
    data = request.get_json()
    nkar = db.find('photo', data['id'])
    os.remove(os.path.join(app.config['UPLOAD-PATH'], nkar['url']))
    db.Delete("photo", {'id': data['id']})
    return ""


@app.route("/glavni", methods=['POST', 'GET'])
def glavni():
    data = request.get_json()
    nkar = db.find("photo", data["id"])
    # print(nkar)
    db.update("user", {'photo': nkar["url"]}, {'id': session.get("user")['id']})
    x = db.find("user", session.get("user")["id"])
    session['user'] = x
    return ""


@app.route("/serch", methods=['POST', 'GET'])
def serch():
    srch = request.get_json()
    # print(srch)
    s = db.serch("user", srch['search'])
    # print(s)
    return json.dumps(s)


@app.route("/add", methods=['POST', 'GET'])
def add():
    add = request.get_json()
    db.insert("addFrend", {'from_id': session.get('user')['id'], 'to_id': add['id']})
    return ""


@app.route("/accept", methods=['POST', 'GET'])
def accept():
    accept = request.get_json()
    db.insert("drug", {"user_1_id": session.get("user")["id"], "user_2_id": accept["id"]})
    db.Delete("addfrend", {'from_id': accept['id'], 'to_id': session.get('user')['id']})
    return ""


@app.route("/delete", methods=['POST', 'GET'])
def delete():
    delete = request.get_json()
    # print(delete)
    # print(session.get('user')['id'])
    db.Delete("addfrend", {'from_id': delete['id'], 'to_id': session.get('user')['id']})
    return ""


@app.route("/addPost", methods=['POST', 'GET'])
def addPost():
    if request.method == "POST":
        if 'img' in request.files and request.files['img'].filename != '':
            img = request.files["img"]
            imgName = str(random.randrange(1000, 100000000001)) + img.filename
            imgUrl = os.path.join(app.config['UPLOAD-PATH'], "images", imgName)
            img.save(imgUrl)
            # print(imgUrl)
            # print(request.form['texts'])
            now = datetime.datetime.now()
            dt_string = str(now.strftime("%Y/%m/%d %H:%M:%S"))
            db.insert("posts", {"img_url": "images/" + imgName, "user_id": session.get("user")['id'],
                                'text': request.form['texts'], "time": dt_string})
            return redirect('/profil')
    return ''


@app.route("/friend/<id>", methods=['POST', 'GET'])
def friend(id):
    fr = db.find("user", id)
    d = db.get("posts")
    return render_template("/friend.html", user=session.get("user"), friend=fr, len=d)


@app.route("/like", methods=['POST', 'GET'])
def like():
    return ""


@app.route("/dislike", methods=['POST', 'GET'])
def dislike():
    return ""


@app.route("/comment", methods=['POST', 'GET'])
def comment():
    return ""


############------MESSAGES------------######################################################
# + chat
@app.route("/messages", methods=['POST', 'GET'])
def messages():
    chatFriends = db.getFrend(session.get("user")["id"])
    # print(mess)
    return render_template("/messages.html", user=session.get("user"), chatFriends=chatFriends)


@socketio.on('my event')
def handle_my_custom_event(json):
    # print(json)
    # print(request.sid)
    chat_users[session.get('user')['id']] = request.sid
    # print(chat_users)


# @app.route('/sendMessage', methods=['GET', 'POST'])
# def message():
#     data = request.get_json()
#     print(data)
#     db.insert('messages', {"from_id": session.get('user')['id'], "to_id": data['activeUser'], "message": data['messageText']})
#     messages = db.messenger(session.get('user')['id'], data['activeUser'])
#     print(messages)
#     messages = json.dumps(messages)
#     return messages


@app.route('/getMessages', methods=['GET', 'POST'])
def getMessage():
    data = request.get_json()
    messages = db.messenger(session.get('user')['id'], data['activeUser'])
    # print(messages)
    messages = json.dumps(messages)
    return messages

@socketio.on('/getMessages')
def getMessage(json_data):
    # print(json_data)
    messages = db.messenger(session.get('user')['id'], json_data['activeUser'])
    print(messages)
    emit('getMessages', {'messages': messages})


@socketio.on('sendMessage')
def sendMessage(data):
    db.insert('messages',
              {"from_id": session.get('user')['id'], "to_id": data['activeUser'], "message": data['messageText']})
    messages = db.messenger(session.get('user')['id'], data['activeUser'])
    messages = json.dumps(messages)
    if int(data['activeUser']) in chat_users:
        emit('getMessages', {'messages': messages}, broadcast=True, room=chat_users[data['activeUser']])
    emit('getMessages', {'messages': messages}, broadcast=True, room=chat_users[session.get('user')['id']])


# app.run ( debug=True )
socketio.run(app, debug=True)
