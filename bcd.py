import urllib2
import urllib
import sys
import re
from urllib2 import HTTPError, URLError

class record:
	bandname = ""
	recordname = ""
	bandcampLink = ""
	artwork = ""
	songsnum = 0
	songnames = []
	songlinks = []
	
	def getRecordInfo(self):
		songs_sum = 0
		trackinfofound=False
		f = getURLFile(self.bandcampLink)
		for line in f.readlines():
			if "<title>" in line:
				bandname = line.split('|')[1]
				bandname = bandname.split('<')[0]
				
				recordname = line.split('|')[0]
				recordname = recordname.split('>')[1]
			if "artFullsizeUrl" in line:
				self.artwork = line.split("\"")[1]
			if "info_link" in line:
				songs_sum+=1
			if "trackinfo" in line and trackinfofound==False:
				trackinfo = line
				trackinfofound=True
				trackinfo = trackinfo.split("{")
				for line in trackinfo:
					if "mp3-128" in line:
						link = line.split("\"")[3]
						self.songlinks.append(link)
						
						name = line.split("title")[1]
						name = name.split("\"")[2]
						self.songnames.append(name)

		f.close()
		self.bandname = bandname
		self.recordname = recordname
		self.songsnum = songs_sum
		
	def __init__(self, bcurl):
		self.bandcampLink = bcurl
		self.getRecordInfo()
		

def getURLFile(url):
		f= urllib2.urlopen(url)
		return f
