import re
import mechanize
import urllib2
import csv
import os
from bs4 import BeautifulSoup
br = mechanize.Browser()
br.set_handle_robots(False)   
br.set_handle_refresh(False)
br.addheaders =[('User-agent', 'Firefox')]
file_path = "/media/rafa/Data/sales"  # current file path
index = 0
link_url = ""
abc=""
currdir = os.getcwd()
def mkdir(new):
	newpath = currdir + new
	if not os.path.exists(newpath):
    		os.makedirs(newpath)
def get_soup(link):
	try:
		response = br.open(link)
	except:
		print ("Something wrong with link or internet")
		print a		

	else:	
		response1 = br.response()  
		assert br.viewing_html()
		page = response.read()
		return BeautifulSoup(page, "html.parser")




with open("links.txt","r") as f:
	for a in f:
		index += 1
		soup = get_soup(a)
		#with open("imou.html","w") as f:
		for scri in soup.findAll("script"):
		#		f.write(scri.text)
			print scri
			if "descUrl" in scri.text:

				print scri.text
				link_url = scri.text
				print link_url
		for line in link_url.split("\n"):
			if "descUrl" in line:
				abc = line
		
			abc.replace("""window.runParams.descUrl="//""","")
			abc.replace('''";''',"")
			print abc