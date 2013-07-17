import urllib2

from sys import argv
from bs4 import *

from urlparse import urljoin

script, startpage = argv
ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])

class Crawler:

	def isindexed(self, url):
		return False
	
	def addtoindex(self, url):
	
		print 'Indexing ' + url


	def crawl(self, pages, depth = 2):

		for i in range(depth):

			newpages = set()

			for page in pages:

				try:
			
					p = urllib2.urlopen(page)
	
				except:
	
					print "Can not open %s" % page

					continue

				soup = BeautifulSoup(p.read())

				self.addtoindex(page)



				links = soup('a')

				for link in links:

					if('href' in dict(link.attrs)):

						# join the base url with the new link
						url = urljoin(page, link['href'])

						if url.find("'") != -1: continue

						url = url.split('#')[0] # remove the location part of the url

						if url[0:4] == 'http' and not self.isindexed(url):

							newpages.add(url)

					#	linkText = self.gettextonly(link)

					#	self.addlinkref(page, url, linkText)


				#	self.dbcommit()


					pages = newpages

def main(startpage):

	pagelist = [startpage]

	crawler = Crawler()

	crawler.crawl(pagelist)

if __name__ == "__main__":
	main(startpage)
