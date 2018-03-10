#!/usr/bin/env python3.4

import os, sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

print('''\
Content-type: text/html\r\n
<html>
	<head>
	    <title>PENDOSTEAM | Python version</title>
		<meta name="viewport" content="width=device-width; initial-scale=1.0">
	    <link rel="stylesheet" type="text/css" href="../css/main.css">
	</head>
	<body>
	''')

with open('../public_html/header.html', mode='r', encoding='utf-8', errors=None) as file_read:
	for line in file_read:
		print(line)

print('''
	<div class='main_body'>
	''')

with open('../public_html/main-body.html', mode='r', encoding='utf-8', errors=None) as file_read:
	for line in file_read:
		print(line)

print('''
	</div>
	''')

with open('../public_html/footer.html', mode='r', encoding='utf-8', errors=None) as file_read:
	for line in file_read:
		print(line)

print('''
</body>
</html>
''')
