def album_add(form):
	import os,sys
	import cgi, cgitb
	cgitb.enable()
	sys.stderr = sys.stdout
	import os,sys
	import time, datetime
	import pymysql
	import base64
	from PIL import Image
	import io


	album_name = form.getvalue('album-name')

	if album_name is None:
		pass

	else:
		album_name = form.getvalue('album-name').title()
		album_band = form.getvalue('album-band').title()
		album_year = form.getvalue('album-year').title()
		album_cover = form.getvalue('album-cover')
		# album_cover = form['album-cover'] #this is for file uploads

		db = pymysql.connect(host='127.0.0.1', user='g03u33', passwd='mysql16', db='g03u33', charset='utf8', use_unicode=True)
		cur = db.cursor()
		cur.execute('SET NAMES utf8')

		cur.execute('SELECT * FROM albums ORDER BY albums.album_id ASC')
		already_exist_stack = cur.fetchall()
		counter = 0

		keywords = []

		keywords.extend(album_name.lower().split())
		keywords.extend(album_band.lower().split())
		keywords.extend(album_year.lower().split())

		keywords = str(','.join(keywords) + ',album')

		for already_exist in already_exist_stack:
			if (album_name == already_exist[3] and album_band == already_exist[5] and album_year == already_exist[4]):
				cur.execute('UPDATE albums SET album_cover = "{}" WHERE album_id = {}'.format(album_cover, already_exist[0]))
				counter += 1
				print("<p>The '{}' album by '{}' was changed.</p>".format(album_name, album_band))

		if counter == 0:
			cur.execute("INSERT INTO pymysql_pages (page_prior_navig, page_title) VALUES (%s, %s)", (int(0), album_name))

			cur.execute('SELECT page_id FROM pymysql_pages ORDER BY pymysql_pages.page_id DESC')
			page_ids = cur.fetchall()

			new_album_id = page_ids[0][0]

			cur.execute("INSERT INTO albums (page_id, album_cover, album_name, album_year, album_band, album_keywords, album_score) VALUES (%s, %s, %s, %s, %s, %s, %s)", (new_album_id, album_cover, album_name, album_year, album_band, keywords, str('NA')))
			print("<p>The new album '{}' by '{}' was uploaded.</p>".format(album_name, album_band))

		db.commit()
		cur.close()
		db.close()


		# try: # Windows needs stdio set for binary mode.
		# 	import msvcrt
		# 	msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
		# 	msvcrt.setmode (1, os.O_BINARY) # stdout = 1
		# except ImportError:
		# 	pass

		# # Test if the file was uploaded
		# if album_cover.filename:

		#     # strip leading path from file name
		#     # to avoid directory traversal attacks
		# 	fn = os.path.basename(album_cover.filename)
		# 	open(r'../img/' + fn, 'wb').write(album_cover.file.read())
		# 	message = 'The album "' + fn + '" was uploaded successfully'

		# else:
		# 	message = 'No album was uploaded'

		# print ("""<p>%s</p>""" % (message,))

		# # with open('files/album_covers/' + os.path.basename(album_cover.filename), 'rb') as f:
		# # 	data = sys.stdout.flush() # <---
		# # 	sys.stdout.buffer.write(f.read())

		# # print ("<img src='data:image/jpg;base64," + data + "'>")

		# # db = pymysql.connect(host='127.0.0.1', user='g03u33', passwd='mysql16', db='g03u33', charset='utf8', use_unicode=True)
		# # cur = db.cursor()
		# # cur.execute('SET NAMES utf8')

		# # cur.execute('SELECT * FROM `albums` ORDER BY `albums`.`album_id` ASC')
		# # already_exist_stack = cur.fetchall()
		# # counter = 0


		# # for already_exist in already_exist_stack:
		# #     if (album_name == already_exist[3] and album_band == already_exist[5] and album_year == already_exist[4]):
		# #         cur.execute('UPDATE albums SET album_cover = {} WHERE id = {}'.format(cover_path, already_exist[0]))
		# #         counter += 1

		# # if counter == 0:
		# #     cur.execute("INSERT INTO albums (album_name, album_year, album_band, album_cover) VALUES (%s, %s, %s, %s)", (album_name, album_year, album_band, cover_path))

		# # db.commit()
		# # cur.close()
		# # db.close()
