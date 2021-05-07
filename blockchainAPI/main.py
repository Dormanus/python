import blockchain
import block
import function
import sqlite3
from flask import Flask,request,jsonify,render_template,redirect,url_for
import json
import connection
from hashlib import sha256

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    if(request.method == 'GET'):
        return render_template('sign_in.html')
    u = sha256(request.form["user"].encode('utf-8')).hexdigest()
    p = sha256(request.form["password"].encode('utf-8')).hexdigest()
    connect =  connection.sign_in(u,p)
    if(connect):
        return redirect('/')
    else : 
        return render_template('sign_in.html')

@app.route('/sign_up', methods=['POST','GET'])
def sign_up():
    if(request.method == 'GET'):
        return render_template('sign_up.html', alreadyExist = False)
    user = sha256(request.form["user"].encode('utf-8')).hexdigest()
    password = sha256(request.form["password"].encode('utf-8')).hexdigest()
    connect = connection.sign_up(user,password)
    if(isinstance(connect, str)):
        return render_template('sign_up.html')
    else : 
        return redirect(url_for('.home', sign_up = True))

@app.route('/sign_out', methods=['GET'])
def sign_out():
    connection.sign_out()
    return redirect('/sign_in')

@app.route('/', methods=['GET', 'POST'])
def home():
    if(not connection.getA()):
        return redirect('/sign_in')
        
    else:
        return redirect('/films')


      

@app.route('/films', methods=['GET'])
def all_films():
    if(not connection.getA()):
        return home()
    co = sqlite3.connect('tables/tables.db')
    co.row_factory = dict_factory
    cur = co.cursor()
    films = cur.execute('select * from films').fetchall()
    co.close()
    return render_template('films.html', films = films)


@app.route('/films/add_film', methods=['POST', 'GET'])
def add_film():
    if(connection.getA()):
        if(request.method == 'GET'):
            return render_template('add_film.html')
        co = sqlite3.connect('tables/tables.db')
        sql_request = '''INSERT INTO films(id,previous_hash, timestamp, film, 
                            producer, release_year, hash, nonce)
                            VALUES(?,?,?,?,?,?,?,?)'''
        cur = co.cursor()
        film = request.form["film"]
        producer = request.form["producer"]
        release_year = request.form["release_year"]
        r = cur.execute('select id, hash from films order by id desc limit 1', ).fetchall()
        b = block.Block(film, producer, release_year)
        id = -1
        if(r != []):
            (id, hash) = r[0]
        if(id != -1):
            b = blockchain.addBlock(b ,id, hash )
            r = cur.execute('select 1 from films where film = ? and producer = ? and release_year = ?', (film, producer, release_year)).fetchall()
            if(r == []):
                insert = cur.execute(sql_request , (b.id,b.previous_hash,b.timestamp,b.film,b.producer,b.release_year,b.hash,b.nonce))
                co.commit()
                co.close()
                return home()
            else:
                co.close()
                return render_template('add_film.html')
        else : 
            b = function.compute_hash(b)
            insert = cur.execute(sql_request , (b.id,b.previous_hash,b.timestamp,b.film,b.producer,b.release_year,b.hash,b.nonce))
            co.commit()
            co.close()
            return 
    else:
        return home()


@app.route('/films/search', methods=['GET', 'POST'])
def getFilms():
    if(not connection.getA()):
        return home()
    if(request.method == 'GET'):
        return render_template('search_films.html', found = False)
    co = sqlite3.connect('tables/tables.db')
    co.row_factory = dict_factory
    cur = co.cursor()
    title = request.form["film"]
    producer = request.form["producer"]
    release_year = request.form["release_year"]
    sql_request = '''select * from films  '''
    params = ()
    if(title):
        sql_request += 'where film like ?'
        if(producer or release_year):
            sql_request += ' and '
        params += ('%'+ title + '%' ,)
    if(producer):
        if(not title):
            sql_request += ' where '
        sql_request += 'producer like ?'
        if(release_year):
            sql_request += ' and '
        params += ('%' + producer +'%' ,)
    if(release_year):
        if(not title and not producer):
            sql_request += ' where '
        sql_request += 'release_year like  ?'
        params += ('%' + release_year + '%' ,)
    filmsSearch =  cur.execute(sql_request , params).fetchall()
    co.close()    
    filename = request.form["filename"]
    if(filename != ""):
        filecreated = exportData(filmsSearch,filename)
        if(not filecreated):
            return render_template('search_films.html', notDownload = True)
        return render_template('search_films.html', found = True, films= filmsSearch, fileCreated = True)
    return render_template('search_films.html', found = True, films= filmsSearch)

@app.route('/film/<id>', methods=['GET'])
def get_film(id):
    if(not connection.getA()):
        return home()
    co = sqlite3.connect('tables/tables.db')
    co.row_factory = dict_factory
    cur = co.cursor()
    film = cur.execute('select * from films where id=' + id).fetchone()
    co.close()
    return render_template('film.html', film = film)


def exportData(filmsSearch,filename):
    try:
        with open(filename + ".txt", 'x') as file:
            for s in filmsSearch:
                file.write(str(s) + "\n")
        return True
    except:
        return False


app.run()

