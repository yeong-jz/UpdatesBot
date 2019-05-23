import feedparser
from bs4 import BeautifulSoup as bs


feed = feedparser.parse("https://rss.app/feeds/X16Cm8dsU7VBEHVp.xml")
summary = feed['entries'][0]['summary']
cleantext = bs(summary, "lxml").text