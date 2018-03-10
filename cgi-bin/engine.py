#!/usr/bin/env python3.4
#http://g03u33.nn2000.info/cgi-bin/engine.py?function=page&page_id=1
import os,sys
import time, datetime
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout
import pymysql
# import py_sql_test_cgi
# import py_form_action

db = pymysql.connect(host='127.0.0.1', user='g03u33', passwd='mysql16', db='g03u33', charset='utf8', use_unicode=True)
cur = db.cursor()
cur.execute('SET NAMES utf8')


print('''\
Content-type:text/html\r\n
<html>
    <head>
        <meta http-equiv="Content-Type" CONTENT="text/html; charset=utf-8">
''')

qr_string = cgi.FieldStorage()
function = qr_string.getvalue('function')
page_id = qr_string.getvalue('page_id')

if 'function' not in qr_string:
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
                <a href="../cgi-bin/engine.py"><span class="main_logo">PENDOSTEAM</span></a>
                <nav class="header-nav">
                    <ul>
''')

cur.execute('SELECT `page_id`,`page_prior_navig`,`page_title`, `page_keywords`, `page_content` FROM `pymysql_pages` ORDER BY `pymysql_pages`.`page_prior_navig` DESC')
result_all = cur.fetchall()
my_url = "href='http://g03u33.nn2000.info/cgi-bin/engine.py"

for result in result_all:
    if int(result[1]) != 0:
        if int(result[0]) == int(page_id):
            print('''
                        <li><a {}?function=page&page_id={}' class="active">{}</a>
                        '''.format(my_url, result[0],  result[2]))
        else:
            print('''
                        <li><a {}?function=page&page_id={}'>{}</a>
                        '''.format(my_url, result[0],  result[2]))

print('''
                    </ul>
                </nav>
                <div class="music-player">
                	<img src="../img/search.png" alt="Music Player">
                	<img src="../img/music-player.png" alt="Search Button">
                </div>
            </div>
        </header>
''')


print('''
	   <div class='main_body'>
	''')

print('''
	       <div class='main_body_content'>
	''')
if (function=="page"):

    # if (int(page_id)==2):
    #     # py_sql_test_cgi.py_sql_test_cgi()
    #     pass
    # elif (int(page_id)==6):
    #     # py_form_action.py_form_action()
    #     pass
    # else:
        cur.execute('SELECT `page_id`,`page_prior_navig`,`page_title`, `page_keywords`, `page_content` FROM `pymysql_pages`  WHERE `page_id` = {}'.format(page_id))
        result_one = cur.fetchone()
        page_content = result_one[4]
        print(page_content)

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

# datetime_now=str(datetime.datetime.now()).split(' ')
# str_time_now_sec=datetime_now[1].split(":")
# time_now_sec=float(str_time_now_sec[2])+60.*float(str_time_now_sec[1])+3600.*float(str_time_now_sec[0])
# print("\n<!--\n",datetime_now, time_now_sec, "\n-->\n")
# with open('../tmp/page_visits.txt', mode='a', encoding="utf-8", errors=None, newline=None, closefd=True, opener=None) as page_visits_a:
#     page_visits_a.write("%20s %10s %10s\n" % (page_title, os.environ[ "REMOTE_ADDR" ],  datetime.datetime.now() ))
#
#
# cur.execute("""CREATE TABLE IF NOT EXISTS `py_page_visits` (
#   `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `page_title` varchar(255) NOT NULL,
#   `page_ip` varchar(255) NOT NULL,
#   `page_date` date NOT NULL,
#   `page_time` time NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;""")
# db.commit()
# cur.execute("""INSERT INTO `g00u00`.`py_page_visits` (`id`, `page_title`, `page_ip`, `page_date`, `page_time`) VALUES ('%s', '%s', '%s', '%s', '%s')""" % ('Null' , page_title, os.environ[ "REMOTE_ADDR" ], time.strftime('%Y-%m-%d'), time.strftime('%H:%M:%S')))
# db.commit()
# cur.execute("""SELECT `id`, `page_title`, `page_ip`, `page_date`, `page_time` FROM `py_page_visits` ORDER BY `id` DESC LIMIT 0 , 1""")
# result_one = cur.fetchone()
# print("\n<!--\nresult_one:\n",result_one, "\n-->\n")
# print("\n<!--",datetime.timedelta(), "\n-->\n")
#
# cur.execute("""SELECT `page_title`, COUNT( `page_title` ) FROM `g00u00`.`py_page_visits` GROUP BY `page_title` ORDER BY `page_title`""")
# result_all = cur.fetchall()
# print("\n<!--\nЗаголовки-result_all:\n",result_all, "\n-->\n")

# db.close()

# """
# DROP TABLE IF EXISTS `sql_pages`;
# CREATE TABLE `sql_pages` (
#   `page_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `page_prior_navig` int(10),
#   `page_title` varchar(255) NOT NULL,
#   `page_keywords` varchar(255) NOT NULL,
#   `page_content` text NOT NULL,
#   PRIMARY KEY (`page_id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
#
# INSERT INTO `pymysql_pages` (`page_id`, `page_prior_navig`, `page_title`, `page_keywords`, `page_content`) VALUES
# (1, 999, 'Название первой страницы', 'Ключевые слова первой страницы', 'Содержание первой страницы'),
# (2, 400, 'Название второй страницы', 'Ключевые слова второй страницы', 'Содержание второй страницы'),
# (3, 600, 'Название третьей страницы', 'Ключевые слова третьей страницы', 'Содержание третьей страницы'),
# (4, 600, 'Название третьей страницы', 'Ключевые слова третьей страницы', 'Содержание третьей страницы'),
# (5, 0, 'cgi-тестирование', '', ''),
# (6, 350, 'html-forma', 'ключевые слова формы',
# <form  action="./engine.py"   target=''_self'' method=''get''>
#     <p>
#         <input type="Hidden" name="function" value="page">
#         <input type="Hidden" name="page_id" value="6">
#         Фамилия: <input type="Text" name="last_name" value="Петров" size=8 >
#         Имя: <input type="Text"  name="first_name" value="" size=10 >
#         Отчество: <input type="Text"  name="second_name" value="Петрович" size=10 >
#     </p>
#     <p>
#         Место проживания:
#             <input type="Radio" name="place" value="Moscow">Москва
#             <input type="Radio" name="place" value="Nizhny">Нижний
#             <input type="Radio" name="place" value="Бор" checked>Бор
#     </p>
#     <p>
#         Опыт работы:
#             <input type="Checkbox" name="market"  value="Y" checked >Маркетологом
#             <input type="Checkbox" name="econom"  value="Y" checked >Экономистом
#             <input type="Checkbox" name="manager"  value="Y">менеджер
#             <input type="Checkbox" name="programmer"  value="Y">программист
#     </p>
#     <p>
#         Знание английского
#             <select name="languages">
#                 <OPTION value="good">Владею свободно</OPTION>
#                 <OPTION value="bad">Читаю и перевожу со словарем</OPTION>
#                 <OPTION value="No">Не владею</OPTION>
#             </select>
#     </p>
#     <p>
#         Дополнительная информация:
#             <TEXTAREA name="info" value="TEXTAREA" rows=4 cols=24></TEXTAREA>
#     </p>
#     <p>
#         Пароль:
#             <input type="Password" name="password" value="123"  size=9>
#     </p>
#         <!--Нижерасположенные фрагменты перемещать нельзя-->
#     <p>
#         <input type="Hidden" name="file_name" value="file.txt" >
#     </p>
#     <p>
#         <input type="Reset"  name="Reset" value="Reset">
#         <input type="Submit" name="Submit" value="Submit">
#         <!--<input type="image" src="src.jpg" name="submit" value="submit">-->
#     </p>
# </form>

# (7, 100, 'Обработка данных формы', 'Ключевые слова для обработки формы', '');
#
# DROP TABLE IF EXISTS `py_page_visits`;
# CREATE TABLE IF NOT EXISTS `py_page_visits` (
#   `page_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
#   `page_title` varchar(255) NOT NULL,
#   `page_ip` varchar(255) NOT NULL,
#   `page_date` date NOT NULL,
#   `page_time` time NOT NULL,
#   PRIMARY KEY (`page_id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
#
# INSERT INTO `g00u00`.`py_page_visits` (
# `page_id`, `page_title`, `page_ip`, `page_date`, `page_time`)
# VALUES (
# 'Null' , 'Заголовок страницы', '192.168.1.1.', CURRENT_DATE( ) , CURRENT_TIME( ))
# """
#
# """
# SELECT `page_title`, COUNT( `page_title` ) FROM `g00u00`.`py_page_visits` GROUP BY `page_title` ORDER BY `page_title`
# SELECT `page_date`, COUNT( `page_date` ) FROM `g00u00`.`py_page_visits` GROUP BY `page_date` ORDER BY `page_date`
# SELECT `page_date`, `page_title`, COUNT( `page_date` ) FROM `g00u00`.`py_page_visits` GROUP BY `page_date`, `page_title`  ORDER BY `page_date`
# """
