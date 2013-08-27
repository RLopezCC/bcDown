#BandCamp downloader.
# ex: python bcdMain.py http://folk-o-rama.bandcamp.com/album/folk-o-rama-volume-two

import urllib
import sys
import bcd
from bcd import record

def main():
	#Taking arguments from command line to initialize rec, a record.
	rec = record(sys.argv[1])
	print str(rec.songsnum)+" songs found!"
	
	#If there are zero songs, that means an error occured.
	if rec.songsnum==0: 
		print "Exiting"
		sys.exit(1) #We must exit quickly, before everything blows up.
	
	#Show some information on the standard output.
	print "Artist: "+rec.bandname
	print "Record: "+rec.recordname
	print "Downloading artwork: "+ rec.artwork
	
	#Download artwotk, name it "Record Name_art.jpg" 
	urllib.urlretrieve(rec.artwork, rec.recordname+"_art.jpg")
	
	#Iterate the links list:
	for link in rec.songlinks:
		index=rec.songlinks.index(link) #Item's Index + 1 is used later in the file name.
		
		#This will make names formatted like "1- Estoy saliendo con un chabon.mp3" 
		filename = str(index+1)+ "- "+ rec.songnames[index]+ ".mp3"
		
		print "Downloading "+ link + " to " + filename
		urllib.urlretrieve(link, filename)

if __name__ == "__main__":
	main()
