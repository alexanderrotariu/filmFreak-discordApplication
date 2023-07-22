import feedparser
import unicodedata
import re

def toUTF8(entry):
    return entry.encode("utf-8")

def getFeed(link):
    return feedparser.parse(link)

def getProfileName(link):
    return getFeed.feed.title

def getProfileLink(link):
    return getFeed.feed.link

def getProfileDescription(link):
    return getFeed.feed.description
#======================================================   FEED INITIALIZATION   ======================================================

lbLink = "https://letterboxd.com/sk33ee/rss/" 


print("===============================================================================")

