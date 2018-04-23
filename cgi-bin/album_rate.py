def album_rate(form):
    import os,sys
    import cgi, cgitb
    import statistics
    cgitb.enable()
    sys.stderr = sys.stdout
    import os,sys
    import time, datetime
    import pymysql

    if form.getvalue('rating'):

        score = form.getvalue('rating')
        album_name = form.getvalue('album')
        page_id = form.getvalue('page_id')

        db = pymysql.connect(host='127.0.0.1', user='g03u33', passwd='mysql16', db='g03u33', charset='utf8', use_unicode=True)
        cur = db.cursor()
        cur.execute('SET NAMES utf8')

        cur.execute("INSERT INTO album_ratings (page_id, album_name, score) VALUES (%s, %s, %s)", (page_id, album_name, score))
        db.commit()

        cur.execute('SELECT * FROM album_ratings ORDER BY album_ratings.page_id ASC')
        all_ratings = cur.fetchall()
        final_score = []

        # print(page_id, all_ratings[0][1])

        for position in all_ratings:
            if (int(page_id) == position[1]):
                final_score.append(position[3])

        final_score = list(map(int, final_score))

        avg = str(round(statistics.mean(final_score), 1))

        cur.execute('SELECT * FROM albums ORDER BY albums.album_id ASC')
        all_albums = cur.fetchall()

        cur.execute('UPDATE albums SET album_score = \"{}\" WHERE page_id = \"{}\"'.format(avg, int(page_id)))

        db.commit()
        cur.close()
        db.close()

    else:
        pass
