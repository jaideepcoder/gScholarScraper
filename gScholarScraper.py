import requests
from bs4 import BeautifulSoup
import json


args = eval(str(sys.argv))
if len(sys.argv) < 3:
	print "Incorrect Number of Arguments"
	exit()
query=""
for arg in args:
    if "--query=" in arg:
	query = arg.replace('--query=', '')

    if "-N=" in arg:
        N = arg.replace('-N=', '')

    if "--pretty=" in arg:
        pretty = arg.replace('--pretty=', '')

class gScholarScraper(object):

    def __init__(self, query, N, pretty):
        self.query = query
        self.google_scholar_url = "http://scholar.google.com/scholar"
        self.url = self.google_scholar_url+"?q="+query.replace(' ', '+')
        self.N = N,
        self.pretty = pretty

    def getContent(self, i):
        r = requests.get(self.url+'&start='+str(i*10))
        content = r.content
        file = open("output.html", 'w')
        file.write(content)
        file.close()
        return content

    def getTitle(self, paper):
        title = paper.find('h3', {'class': 'gs_rt'})
        #print title.text
        try:
            return title.text
        except Exception as e:
            return ""

    def getURL(self, paper):
        url = paper.find('h3', {'class': 'gs_rt'})
        #print url.a.get('href')
        try:
            return url.a.get('href')
        except Exception as e:
            return ""

    def getAuthors(self, paper):
        authors = paper.find('div', {'class': 'gs_a'})
        #print authors.text
        try:
            return authors.text
        except Exception as e:
            return ""

    def getAbstract(self, paper):
        abstract = paper.find('div', {'class': 'gs_rs'})
        #print abstract.text
        try:
            return abstract.text
        except Exception as e:
            return ""

    def getCited(self, paper):
        cited = paper.find('div', {'class': 'gs_fl'})
        cited = str(cited.text).replace('Cited by ', "").split(' ')[0]
        #print cited
        try:
            return cited
        except Exception as e:
            return ""

    def main(self):
        papersList = list()
        for i in xrange(int(N)):
            content = self.getContent(i)
            soup = BeautifulSoup(content)
            papers = soup.find_all('div', {'class' : 'gs_ri'})
            for paper in papers:
                paperDict = dict()
                paper = BeautifulSoup(str(paper))
                paperDict['title'] = self.getTitle(paper)
                paperDict['url'] = self.getURL(paper)
                paperDict['authors'] = self.getAuthors(paper)
                paperDict['abstract'] = self.getAbstract(paper)
                paperDict['cited'] = self.getCited(paper)
                papersList.append(paperDict)
        trues = ['true', '1', 1, 'True', 'TRUE']
        if(pretty in trues):
            print json.dumps(papersList, indent=4, separators=(',', ': '))
        else:
            print json.dumps(papersList)
            

scholar = gScholarScraper(query, N, pretty)
scholar.main()
