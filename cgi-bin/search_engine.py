def search_engine(form):
    import os,sys
    import cgi, cgitb
    cgitb.enable()
    sys.stderr = sys.stdout
    import os,sys
    import time, datetime
    import pymysql

    print('''
                <div class="search-body">
                    <div class="head-container">
                        <h1 class="search-h1">Search Results</h1>
                    </div>
                    <div class="results-container">
    ''')

    search_phrase_raw = form.getvalue('search_phrase')

    if search_phrase_raw is None:
        print('''
                            <h1 class="search-wrong-h1">Sorry, but you didn't type anything in the search field...</h1>
                            <!--<img class="img-404" src="../img/404.png">-->
        ''')

    else:
        search_phrase = search_phrase_raw.lower().split()

        db = pymysql.connect(host='127.0.0.1', user='g03u33', passwd='mysql16', db='g03u33', charset='utf8', use_unicode=True)
        cur = db.cursor()
        cur.execute('SET NAMES utf8')

        cur.execute('SELECT * FROM `albums` ORDER BY `albums`.`album_id` ASC')
        search_results = cur.fetchall()
        global_counter = 0
        my_url = "http://g03u33.nn2000.info/cgi-bin/engine.py"


        for search in search_results:
            keywords = search[6].lower().split(',')
            counter = 0

            for keyword in keywords:
                for search_word in search_phrase:
                    if keyword == search_word:
                        counter += 1

            if counter != 0:
                global_counter += 1
                print('''
                                    <a href="{}?function=page&page_id={}" class="search-result" style="background-image: url('{}')">
                                        <p class="album-name">{}</p>
                                        <p class="album-year">{}</p>
                                        <p class="album-band"><span>{}</span></p>
                                    </a>
                '''.format(my_url, search[1], search[2], search[3], search[4], search[5]))

        if global_counter == 0:
            print('''
                                <h1 class="search-wrong-h1">Sorry, but there is no such thing as <span class='underline'>'{}'</span>.</h1>
                                <!--<img class="img-404" src="../img/404.png">-->
            '''.format(search_phrase_raw))

        print('''
                        </div>
                    </div>
        ''')
