import sqlite3


global autentification
autentification = [False]
def getA():
    return autentification[0]

def setA(value):
    autentification[0] = value


def sign_in(u , p):
    co = sqlite3.connect('tables/tables.db')
    cur = co.cursor()
    r = cur.execute('select 1 from users where user=? and password=?', (u,p,)).fetchall()
    co.close()
    if(r != []):
        setA(True)
    return getA()

def sign_up(u , p):
        co = sqlite3.connect('tables/tables.db')
        cur = co.cursor()
        r = cur.execute('select 1 from users where user=?', (u,)).fetchall()
        if(r != []):
            return 'Utilisateur déjà existant'
        insert = cur.execute('insert into users values (?,?)' , (u , p))
        co.commit()
        setA(True)
        co.close()
        return getA()

def sign_out():
    setA(False)