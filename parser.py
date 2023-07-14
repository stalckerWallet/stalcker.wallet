import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('http://www.google.com/')
soup = BeautifulSoup(page)

x = soup.body.find('div', attrs={'class' : 'container'}).text
