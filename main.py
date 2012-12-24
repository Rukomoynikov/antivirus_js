# -*- coding: utf-8 -*-
import os
import re
import codecs

log_mode = raw_input('Do you want full log(type 1) or just files with virus (type 2)?')

# os.walk - recursive directory walk, as first argument - starting directory
for dirname, dirnames, filenames in os.walk('.'):
    for filename in filenames:
  	filepath = str(os.path.join(dirname, filename))
		if  not os.path.exists(filepath) or os.stat(filepath).st_size > 152926:
			if str(log_mode) == "1":print "File " + os.path.join(dirname, filename) + "is too large. Because size = "+str(os.stat(filepath).st_size)+" || or file not exist."
		else:
			try:
				with  open(os.path.join(dirname, filename), 'r+b') as f:		
					text=f.read()
					if re.search('function g\(\).*\n.*\<script src=\"http://linkfooter.org/linkfooter.js\"></script>\'\);}', text) and os.path.join(filename) != "bezr.py":
						print "Starting with " + os.path.join(dirname, filename)
						match = re.compile('function g\(\).*\n.*\<script src=\"http://linkfooter.org/linkfooter.js\"></script>\'\);}')
						s = match.sub('', text)
						#Thanks for help man from Stackoverflow - http://stackoverflow.com/questions/13960693/write-file-from-beginning
						f.seek(0)
						f.truncate()
						f.write(s)
				f.close()		
			except:
				print "Some error"
				# That should be not best practice, beacasue doesn't give eny information for developer. But, if you are developer, you could uncomment this line.
