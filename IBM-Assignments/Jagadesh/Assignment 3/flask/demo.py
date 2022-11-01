from flask import *
import ibm_db
from ibm_db import connect

app = Flask(__name__)
app.secret_key = "hggfgdgghhjkhj"
#db_info below

database = "bludb"
host = "b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
port = "31249"
password = "V5OmeldYywr42BXW",
username = "xrt20091"
dsn = ("DATABASE={0};"
        "HOSTNAME={1};"
        "PORT={2};"
        "PROTOCOL=TCPIP;"
        "UID={3};"
        "PWD={4};"
        "SECURITY=SSL").format(database,host,port,username,password)

#connecting db
conn = connect(dsn,"","")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        uemail = request.form['usermail']
        upass = request.form['pass']
        sql  = "select * from user_data where user_name = ?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,uname)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        if account:
            return "<h1>Hello {}</h1>".format(account['USER_NAME'])
        else:
            insert_sql = "insert into user_data values(?,?,?)"
            stmt = ibm_db.prepare(conn,insert_sql)
            ibm_db.bind_param(stmt,1,uname)
            ibm_db.bind_param(stmt,2,upass)
            ibm_db.bind_param(stmt,3,uemail)
            ibm_db.execute(stmt)
            return "Please return to homepage for login"
    else:
        return redirect(url_for('home'))
        

app.run(debug=True)