def albums_page(form):
	import os,sys
	import cgi, cgitb
	cgitb.enable()
	sys.stderr = sys.stdout
	import os,sys
	import time, datetime
	import pymysql

	filter_topics = ['id', 'year', 'band', 'name']

	print('''
				<div class="album_filter">
					<p>FILTER</p>
		''')

	for topic in filter_topics:
		print('''
					<div class="album_filter_part">
						<p>by {}</p>
						<form action="./engine.py" class="album_filter_form">
							<input type="Hidden" name="function" value="page">
							<input type="Hidden" name="page_id" value="3">
							<input type="hidden" name="data_type" value="album_{}">
							<input type="hidden" name="data_value" value="DESC">
							<input type="submit" value="&#9660;">
						</form>
						<form action="./engine.py" class="album_filter_form">
							<input type="Hidden" name="function" value="page">
							<input type="Hidden" name="page_id" value="3">
							<input type="hidden" name="data_type" value="album_{}">
							<input type="hidden" name="data_value" value="ASC">
							<input type="submit" value="&#9650;">
						</form>
					</div>
		'''.format(topic, topic, topic))

	print('''
				</div>
		''')

	print('''
				<div class="search-body">
					<div class="head-container">
						<h1 class="search-h1">Albums</h1>
					</div>
					<div class="results-container">
	''')

	db = pymysql.connect(host='127.0.0.1', user='g03u33', passwd='mysql16', db='g03u33', charset='utf8', use_unicode=True)
	cur = db.cursor()
	cur.execute('SET NAMES utf8')

	if form.getvalue("data_type"):
		data_type = form.getvalue("data_type")
		data_value = form.getvalue("data_value")
		cur.execute('SELECT * FROM `albums` ORDER BY `albums`.`{}` {}'.format(data_type, data_value))

	else:
		cur.execute('SELECT * FROM `albums` ORDER BY `albums`.`album_id` DESC')


	albums = cur.fetchall()
	my_url = "http://g03u33.nn2000.info/cgi-bin/engine.py"
	global_counter = 0


	for album in albums:
		print('''
							<a href="{}?function=page&page_id={}" class="search-result" style="background-image: url('{}')">
								<p class="album-name">{}</p>
								<p class="album-year">{}</p>
								<p class="album-band"><span>{}</span></p>
							</a>
		'''.format(my_url, album[1], album[2], album[3], album[4], album[5]))
		global_counter += 1


	if global_counter == 0:
		print('''
							<h1 class="search-wrong-h1">Sorry, but there is no any album yet.</h1>
							<!--<img class="img-404" src="../img/404.png">-->
		''')

	print('''
					</div>
				</div>
	''')
