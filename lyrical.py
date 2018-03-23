import mechanize
from bs4 import BeautifulSoup


class Lyrical:
    def __init__(self, url):
        self.baseURL = url

    def getLyrics(self):

        br = mechanize.Browser()
        r = br.open(self.baseURL)

        soup = BeautifulSoup(r.read(), 'html.parser')
        verses = soup.select("p.verse")

        song = ""

        for verse in verses:
            song = song + " " + verse.get_text().lower()

        return song

    def getWordCount(self, song):
        wordlist = song.split()

        x = self.wordListToFreqDict(wordlist)
        y = self.sortFreqDict(x)

        for z in y:
            print z

    def wordListToFreqDict(self, wordlist):
        wordfreq = [wordlist.count(p) for p in wordlist]
        return dict(zip(wordlist, wordfreq))

    def sortFreqDict(self, freqdict):
        aux = [(freqdict[key], key) for key in freqdict]
        aux.sort()
        aux.reverse()
        return aux


print Lyrical("http://www.metrolyrics.com/walking-on-the-moon-lyrics-the-police.html").getLyrics()
