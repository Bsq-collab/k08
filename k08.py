from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

app = Flask (__name__)  
app.secret_key = os.urandom(32)

username = "bob"
password = "bobbins"


@app.route("/",methods=['POST','GET'])
def hello_world():
    '''
    checks user info and displays greet or login
    returns html page greet or login
    '''
    print("\n\n")
    print("Cookie username: ", session.get('username'))
    print("Cookie password: ",session.get('password'))
    if session.get('username') == username and session.get('password') == password:
       # print url_for('greet')
        #return redirect(url_for("greet", user= session.get("username")))
        return render_template('greet.html',user=session.get('username'))
    else:
        return render_template("login.html")

@app.route("/greet",methods=['POST','GET'])
def greet():
    '''
    sets user info keys
    returns greet or error html pages
    '''
    print("\n\n")
    print("Form username: ", request.form.get('username'))
    print("Form password: ", request.form.get('password'))
    session['username'] = request.form.get('username')
    session['password'] = request.form.get('password')
    if session.get('username')== username and session.get('password')==password:
        return render_template( 'greet.html', user = session.get('username') )
    elif session.get('username') != username:
        flash("USERNAME INCORRECT!")
        #return render_template('error.html', error = "Username incorrect!")
    else:
        flash("PASSWORD INCORRECT!")
        #return render_template('error.html', error = "Password incorrect!")
    return redirect(url_for("hello_world"))

@app.route("/logout",methods=['POST','GET'])
def logout():
    '''
    clears cookies
    returns login html page
    '''
    session.pop("username")
    session.pop("password")
    return redirect(url_for("hello_world"))

if __name__ == "__main__":
    app.debug = True;
    app.run()