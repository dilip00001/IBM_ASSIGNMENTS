from connect import execDB, execReturn


def addUser(username, email, password):
    sql_fd = f"SELECT * FROM user WHERE username='{username}'"
    r = execReturn(sql_fd)

    if r != []:
        return "Username Exists"

    sql_st = f"INSERT INTO user(username , email , pass ) values ( '{username}' , '{email}' , '{password}' )"
    r = execDB(sql_st)
    return "User registered successfully"


def getPassword(username):
    sql_fd = f"SELECT pass FROM user WHERE username='{username}'"
    r = execReturn(sql_fd)
    print("SERNAME "+u+"PASS"+r)
    return r[0]['PASS']


def fetchFinanceRecord(username):
    sql_fd = f"SELECT * FROM financee WHERE username='{username}'"
    r = execReturn(sql_fd)
    return r


def createFinanceRecord(username, amount, category, description, date):
    sql_st = f"INSERT INTO financee(username , amount , category , description , date ) values ( '{username}' , '{amount}' , '{category}' , '{description}' , '{date}' )"
    r = execDB(sql_st)
    return "Record created successfully"
