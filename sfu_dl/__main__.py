import sfu_dl.browsercookie as browsercookie
import http.cookiejar as cookielib
import sfu_dl.youtube_dl as youtube_dl
import os
import sys

if __name__ == "__main__":
	temp_cookie_file = 'sfu_dl/temp_cookies'
	open(temp_cookie_file, 'w').close()
	cookie_jar_chrome = browsercookie.chrome()
	cookie_jar_local = cookielib.MozillaCookieJar(temp_cookie_file)
	for cookie in cookie_jar_chrome:
		cookie_jar_local.set_cookie(cookie)
	cookie_jar_local.save(temp_cookie_file, ignore_discard=True, ignore_expires=True)
	
	opts = {
		'cookiefile': r"sfu_dl/temp_cookies",
		'outtmpl': r"sfu_dl/output/%(title)s.%(ext)s",
		'ignoreerrors': True,
		'socket_timeout': 5,
	}
	youtube_dl.YoutubeDL(opts).download([sys.argv[1]]);

	os.remove(temp_cookie_file)

