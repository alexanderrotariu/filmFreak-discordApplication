import feedparser
import unicodedata
import re

#playing with letterboxd RSS

#======================================================   FEED INITIALIZATION   ======================================================
#my letterbox'd url
#can construct parameterized url later
letterboxdURL = "https://letterboxd.com/sk33ee/rss/" 
#use feedparser to return entries
parser = feedparser.parse(letterboxdURL)
#======================================================   FEED INITIALIZATION   ======================================================

#======================================================   PLAYING WITH PARSER CHANNEL ELEMENTS   ======================================================
#example feed in discord channel from LB
rawFeed = parser['feed']

#gets title of the RSS feed
#this returns: "Letterboxd - alex"
feedTitle = parser['feed']['title']

feedTitle2 = parser.feed.title
feedLink = parser.feed.link
feedDescription = parser.feed.description

'''
Letterboxd - alex
-----------------------------------------------
https://letterboxd.com/sk33ee/
-----------------------------------------------
Letterboxd - alex
-----------------------------------------------


print(feedTitle2)
print("-----------------------------------------------")
print(feedLink)
print("-----------------------------------------------")
print(feedDescription)
print("-----------------------------------------------")

'''
'''
for entry in parser.entries:
        print(entry.title.encode("utf-8"))
        print("-----------------------------------------------")
        print(entry.links[0].href.encode("utf-8"))
        print("-----------------------------------------------")
        print(entry.content[0].value.encode("utf-8"))
        print("-----------------------------------------------")
'''
#======================================================   PLAYING WITH PARSER CHANNEL ELEMENTS   ======================================================
#======================================================   PLAYING WITH PARSER ITEM ELEMENTS   ======================================================

#for a single entry of the RSS
feedEntryTitle = parser.entries[0].title
feedEntryLink = parser.entries[0].link
feedEntryDescription = parser.entries[0].description
feedEntryPublished = parser.entries[0].published
feedEntryID = parser.entries[0].id 

'''
#dont know how normalization works yet, need to look into                                     !!!!
normalizedTitle = unicodedata.normalize('NFD', feedEntryTitle)
print(normalizedTitle)
'''



#just getting title 
#rawTitle = re.search("([a-z A-Z]*, \d{4})", feedEntryTitle)
#print("{}".format(rawTitle.group()))

'''
#Encoded bytes 
print("Entry Title: {}".format(feedEntryTitle.encode("utf-8")))
print("Entry Link: {}".format(feedEntryLink.encode("utf-8")))
print("Entry Description: {}".format(feedEntryDescription.encode("utf-8")))
print("Entry Publish Date: {}".format(feedEntryPublished.encode("utf-8")))
print("Entry Letterbox'd ID: {}".format(feedEntryID.encode("utf-8")))
'''

print("===============================================================================")

def regexTitleSearch(title):
    titleRegex = re.search("([a-z A-Z\d.:]*, \d{4})", title)
    return titleRegex.group()

for entry in parser.entries:
    rawTitle = entry.title
    try:
        print("{}".format(regexTitleSearch(rawTitle)))
    except: 
        #means thats either we hit the first entry which is some weird stuff or movie doesnt has some weird titling thing.
        pass