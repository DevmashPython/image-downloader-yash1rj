import urllib
import re
file= open("imggrbr.txt","w")
link="https://www.tutorialspoint.com/"
url= urllib.urlopen(link)
html=url.read()
source= re.compile("<img.*src=\"([^ ]*)\"")
search= re.findall(source,html)
for i in search:
	if i.startswith("/"):
		print "https://www.tutorialspoint.com/" +i
		file.write("https://www.tutorialspoint.com/"+i+"\n")
	else:
		print link+i
		file.write(link+i+"\n")
file.close()