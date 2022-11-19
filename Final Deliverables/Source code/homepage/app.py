from flask import *
# from ibm_db import connect

application=Flask(__name__)
# host="b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
# port=31249
# connection=connect("DATABASE=bludb;HOSTNAME=host;PORT=port;UID=xrt20091;PASSWORD=V5OmeldYywr42BXW;SECURITY=SSL;PROTOCOL=TCPIP","","")
# if connection:
#     print('works')

@application.route('/')
@application.route('/home')

def func():
    return render_template('index.html')



@application.route('/signup')

def signupPage():
    return render_template('Sign-up.html')

@application.route('/signin')
def signinPage():
    # if request.method=='POST':
    #     usermail=request.form['uemail']
    #     userpassword=request.form['upassword']
    #     login="SELECT * FROM"

    return render_template('Sign-in.html')


application.run(debug=True)



