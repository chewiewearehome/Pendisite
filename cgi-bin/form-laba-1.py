#!/usr/bin/env python3.4

import os, sys
import cgi, cgitb
import re
cgitb.enable()
sys.stderr = sys.stdout

form = cgi.FieldStorage()

data = form.getfirst("data", "False")
search_word = form.getfirst("search-word", "False")

data = html.escape(data) #экранируем нежелательные символы вида html
search_word = html.escape(search_word)

if bool(data.strip()) == False:
    print("<h3>Some field is empty!</h3>")

data = open("{}".fotmat(data), "r" )
data = re.split(r"[.|!|?|…]", data)

output = []
count = 0

for sent in range(len(data)):
    data[sent] = list(data[sent].split(' '))
    for word in range(len(data[sent])):
        if data[sent][word] == search_word:
            output = output.append(' '.join(data[sent]))
            count += 1
            break

if count != 0:
    print("<h3>There are all the sentences with the '{}' word:".format(search_word), outout, "</h3>")
else:
    print("<h3>There is no such a word in document!</h3>")
