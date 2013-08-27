import urllib


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
        trackinfofound = False
        f = get_url_file(self.bandcampLink)
        for line in f.readlines():
            if "<title>" in line:
                bandname = line.split("|")[1]
                bandname = bandname.split("<")[0]
                self.bandname = bandname

                recordname = line.split("|")[0]
                recordname = recordname.split(">")[1]
                self.recordname = recordname
            if "artFullsizeUrl" in line:
                self.artwork = line.split("\"")[1]

            if "info_link" in line:
                songs_sum += 1
            if "trackinfo" in line and trackinfofound is False:
                trackinfo = line
                trackinfofound = True
                trackinfo = trackinfo.split("{")
                for line in trackinfo:
                    if "mp3-128" in line:
                        link = line.split("\"")[3]
                        self.songlinks.append(link)

                        name = line.split("title")[1]
                        name = name.split("\"")[2]
                        self.songnames.append(name)
            self.songsnum = songs_sum
        f.close()

    def __init__(self, bcurl):
        self.bandcampLink = bcurl
        self.getRecordInfo()


def get_url_file(url):
    f = urllib.urlopen(url)
    return f
