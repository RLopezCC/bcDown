import urllib
import re


class record:
    bandname = ""
    recordname = ""
    bandcampLink = ""
    artwork = ""
    songsnum = 0
    songnames = []
    songlinks = []

    def getRecordInfo(self):
        f = get_url_file(self.bandcampLink)
        for line in f.readlines():
            if "artist : " in line:
                self.bandname = re.search("\"(.+)\"", line).group(1)
            if "album_title : " in line:
                self.recordname = re.search("\"(.+)\"", line).group(1)
            if "artFullsizeUrl" in line:
               self.artwork = re.search("(http://.+?.jpg)", line).group(1)
            if "trackinfo :" in line:
                self.trackinfo = line
        self.songlinks = re.findall("mp3-128\":\"(.+?\.0)", self.trackinfo)
        self.songnames = re.findall("\"title\":\"(.+?)\"", self.trackinfo)
        self.songsnum = len(self.songlinks)
        f.close()

    def __init__(self, bcurl):
        self.bandcampLink = bcurl
        self.getRecordInfo()


def get_url_file(url):
    f = urllib.urlopen(url)
    return f
