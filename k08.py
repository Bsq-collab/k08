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
    print("Session username: ", session.get('username'))
    print("Session password: ",session.get('password'))
    print("\n\n")
    
    if session.get('username') == username and session.get('password') == password:
        return render_template('greet.html',user=session.get('username'))
    else:
        return render_template("login.html")

@app.route("/greet",methods=['POST','GET'])
def greet():
    '''
    sets user info keys
    redirects to root route or flashes error message
    '''
    usr= request.form.get('username')
    pwd= request.form.get('password')
    print("\n\n")
    print("Form username: ", usr)
    print("Form password: ", pwd)
    print("\n\n")
    
    session['username'] = usr
    session['password'] = pwd

    if session.get('username')== username and session.get('password')==password:
        return render_template( 'greet.html', user = session.get('username') )
    elif session.get('username') != username:
        flash("USERNAME INCORRECT!")
    else:
        flash("PASSWORD INCORRECT!")
    return redirect(url_for("hello_world"))

@app.route("/logout",methods=['POST','GET'])
def logout():
    '''
    clears cookies
    redirects to root route
    '''
    session.pop("username")
    session.pop("password")
    return redirect(url_for("hello_world"))

if __name__ == "__main__":
    app.debug = True;
    app.run()
