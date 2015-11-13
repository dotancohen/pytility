#!/usr/bin/python3

import requests

url = 'http://github.com'
profile_folder = '/home/user/.mozilla/firefox/f00b4r.default'



def get_cookie_jar(profile_folder):
	"""
	Protocol implementation for handling gsocmentors.com transactions
	Author: Noah Fontes nfontes AT cynigram DOT com
	License: MIT
	Original: http://blog.mithis.net/archives/python/90-firefox3-cookies-in-python

	Ported to Python 3 by Dotan Cohen
	"""

	import http.cookiejar
	import os
	import sqlite3
	from io import StringIO

	sql_file = os.path.join(profile_folder, 'cookies.sqlite')
 
	con = sqlite3.connect(sql_file)
	cur = con.cursor()
	cur.execute("SELECT host, path, isSecure, expiry, name, value FROM moz_cookies")

	ftstr = ["FALSE","TRUE"]

	s = StringIO()
	s.write("""\
# Netscape HTTP Cookie File
# http://www.netscape.com/newsref/std/cookie_spec.html
# This is a generated file!  Do not edit.
""")

	for item in cur.fetchall():
		s.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
			item[0], ftstr[item[0].startswith('.')], item[1],
			ftstr[item[2]], item[3], item[4], item[5])
		)

	s.seek(0)
	cookie_jar = http.cookiejar.MozillaCookieJar()
	cookie_jar._really_load(s, '', True, True)

	return cookie_jar



cj = get_cookie_jar(profile_folder)
response = requests.get(url, cookies=cj)

if 'Signed in as' in response.text:
	print('Confirmed signed into Github!')
else:
	print('Cannot confirmed that you are signed into Github.')
	print('Please ensure that you are singed into Github in Firefox before testing.')

