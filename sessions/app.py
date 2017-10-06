from flask import Flask, request, session, redirect, url_for
import os

app = Flask (__name__)

the_username = "user" #Hardcoded username
the_password = "pwd"  #Hardcoded password
app.secret_key = os.urandom(32)

@app.route("/")
def hello_world():
    '''
    If session has a record of the correct username and password input, the user is logged in
    Otherwise, the login page is displayed
    '''
    if "username" in session.keys():
        return redirect(url_for("loggedin.html", name = session["username"]))
    return redirect(url_for("login.html", message = ""))


@app.route("/loggedin")
def logged_in():
   input_name = request.args["username"]
   input_pass = request.args["password"]

   #Validation process, what went wrong (if anything)?
   if input_name == the_username:
      if input_pass == the_password:
         session["username"] = input_name #Creates a new session
         return redirect(url_for("loggedin.html", name = input_name))
      else:
         return redirect(url_for("login.html", message = "Error: Wrong password"))
   else:
      return redirect(url_for("login.html", message =  "Error: Wrong username"))

@app.route("/logout")
def logged_out():
    session.pop("username") #Ends session
    return redirect("/") #Redirecting to login

if __name__ == '__main__':
    app.debug = True
    app.run()
