#!/usr/bin/env python3.4
#http://g03u33.nn2000.info/cgi-bin/engine.py?function=page&page_id=1
import os,sys
import time, datetime
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout
import pymysql
import search_engine
import album_add
import album_rate
import albums_page

db = pymysql.connect(host='127.0.0.1', user='g03u33', passwd='mysql16', db='g03u33', charset='utf8', use_unicode=True)
cur = db.cursor()
cur.execute('SET NAMES utf8')


print('''\
Content-type:text/html\r\n
<html>
    <head>
        <meta http-equiv="Content-Type" CONTENT="text/html; charset=utf-8">
''')

form = cgi.FieldStorage()
function = form.getvalue('function')
page_id = form.getvalue('page_id')


if 'function' not in form:
    function = 'page'
    page_id = 1

cur.execute('SELECT `page_id`,`page_prior_navig`,`page_title`, `page_keywords`, `page_content` FROM `pymysql_pages` WHERE `page_id` = {}'.format(page_id))
result_one = cur.fetchone()
page_title = result_one[2]
page_keywords = result_one[3]

print('''
        <!-- result_one: -->
        <title>{} | PyPENDOS</title>
        <meta name="viewport" content="width=device-width; initial-scale=1.0">
        <link rel="shortcut icon" href="/img/favicon.png" type="image/png">
        <link rel="stylesheet" type="text/css" href="../css/main.css">
        <meta name="Keywords" content="{}">
    </head>
    <body>
'''.format(page_title, page_keywords))

print('''
        <header>
            <div class="header_stuff">
                <a href="../cgi-bin/engine.py">
                    <span class="main_logo">
                        <span>P</span>
                        <span>E</span>
                        <span>N</span>
                        <span>D</span>
                        <span>O</span>
                        <span>S</span>
                        <span>T</span>
                        <span>E</span>
                        <span>A</span>
                        <span>M</span>
                    </span>
                </a>
                <nav class="header-nav">
                    <ul>
''')

cur.execute('SELECT `page_id`,`page_prior_navig`,`page_title`, `page_keywords`, `page_content` FROM `pymysql_pages` ORDER BY `pymysql_pages`.`page_prior_navig` DESC')
result_all = cur.fetchall()
my_url = "http://g03u33.nn2000.info/cgi-bin/engine.py"

for result in result_all:
    if int(result[1]) != 0:
        if int(result[0]) == int(page_id):
            print('''
                        <li><a href='{}?function=page&page_id={}' class="active">{}</a>
                        '''.format(my_url, result[0],  result[2]))
        else:
            print('''
                        <li><a href='{}?function=page&page_id={}'>{}</a>
                        '''.format(my_url, result[0],  result[2]))

print('''
                    </ul>
                </nav>
                <div class="header-icons">
                	<!-- <img src="../img/music-player.png" alt="Music Player"> -->
                    <img class="search-button"  src="../img/search.png" alt="Search Button">
                </div>
                <div class="search-form">
                    <form  class="search-form-form" action="./engine.py" method="get" target="_self">
                        <input type="Hidden" name="function" value="page">
                        <input type="Hidden" name="page_id" value="2">
                        <input class="text" type="text" name="search_phrase" id="search_phrase" autofocus placeholder="Type an album or artist">
                        <input class="submit" type="submit" value="SEARCH">
                    </form>
                </div>
            </div>
        </header>
''')


print('''
	   <div class='main_body'>
	       <div class='main_body_content'>
	''')

if (function=="page"):

    if (int(page_id) == 2):
        search_engine.search_engine(form)

    if (int(page_id) == 3):

        albums_page.albums_page(form)

    elif (int(page_id) >= 100):
        cur.execute('SELECT * FROM albums ORDER BY albums.album_id ASC')
        albums_sql = cur.fetchall()
        counter = 0

        for album in albums_sql:
            if int(page_id) == int(album[1]):
                print('''
                    <div class="album-top"> <!-- Top Album Presentation-->
                        <div class="left-album-top">
                            <h1 class="main-h1 album-title">{}</h1>
                            <h2 class="main-h2 album-band">by {}</h2>
                            <div class="score-box"><p class="score-num">{}/10</p></div>
                        </div>
                    <img class="album-cover right-album-top" src="{}">
                    </div>
                    '''.format(album[3], album[5], album[7], album[2]))

                print('''
                    <h2 class="h2_rate">Rate the album:</h2>
                    <div class="main_score">
                    ''')

                for score_num in range(1,11):
                    print('''
                        <div class="box b{}"><div class="inside_box">
                            <form action="./engine.py" class="score_form" target="_self">
                                <input type="Hidden" name="function" value="page">
                                <input type="Hidden" name="page_id" value="{}">
                                <input type="Hidden" name="album" value="{}">
                                <input type="hidden" name="rating" value="{}">
                                <input type="submit" value="{}">
                            </form>
                        </div></div>
                        '''.format(score_num, page_id, album[3], score_num, score_num))

                print('''
                    </div>
                    ''')

                album_rate.album_rate(form)

                print(album[8])

    else:
        cur.execute('SELECT `page_id`,`page_prior_navig`,`page_title`, `page_keywords`, `page_content` FROM `pymysql_pages`  WHERE `page_id` = {}'.format(page_id))
        result_one = cur.fetchone()
        page_content = result_one[4]
        print(page_content)

print('''
            <h2 class="form-add___heading">If you want to add a new album - fill the form:</h2>
            <form  class="form-add" action="./engine.py" method="post" target="_self" enctype="multipart/form-data">
                <input type="Hidden" name="function" value="page">
                <input type="Hidden" name="page_id" value="{}">
                <div class="not-submit">
                    <input class="text" type="hidden" name="search_phrase" id="search_phrase" value="album">
                    <div class="not-submit___grid">
                        <input class="not-submit___grid___item  input" type="text" name="album-name"  placeholder="Enter an album name" required>
                        <input class="not-submit___grid___item  input" type="text" name="album-band" placeholder="Enter a band name" required>
                    </div>
                    <div class="not-submit___grid">
                        <input class="not-submit___grid___item  input" type="text" name="album-year"  placeholder="Enter an album year" required>
                        <input class="not-submit___grid___item  input" type="text" name="album-cover"  placeholder="Enter a URL to cover" required>
                        <!--<div class="file_upload not-submit___grid___item  input">
                            <button type="button">CHOOSE</button>
                            <div>Cover isn't choosen</div>
                            <input name="album-cover" type="file" accept=".jpeg, .jpg, .png" required>
                        </div>-->
                    </div>
                </div>
                <input class="submit input" type="submit" value="SUBMIT">
            </form>
'''.format(int(page_id)))

album_add.album_add(form)

print ('''
            </div>
        </div>
        ''')

with open('../public_html/footer.html', mode='r', encoding='utf-8', errors=None) as file_read:
	for line in file_read:
		print(line)

print('''
    </body>
</html>
''')
