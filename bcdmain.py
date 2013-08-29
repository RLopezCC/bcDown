#BandCamp downloader.
# ex: python bcdMain.py http://folk-o-rama.bandcamp.com/album/folk-o-rama-volume-two

import urllib
import sys
from bcd import record


def main():
    rec = record(sys.argv[1])
    print(str(rec.songsnum) + " songs found!")
    if rec.songsnum == 0:
        print("Exiting")
        sys.exit(1)
    print("Artist: " + rec.bandname)
    print("Record: " + rec.recordname)
    print("Downloading artwork: " +  rec.artwork)
    urllib.urlretrieve(rec.artwork, rec.recordname + "_art.jpg")
    for link in rec.songlinks:
        index = rec.songlinks.index(link)
        filename = str(index+1) + "- " + rec.songnames[index] + ".mp3"
        print("Downloading " + link + " to " + filename)
        urllib.urlretrieve(link, filename)

if __name__ == "__main__":
    main()
