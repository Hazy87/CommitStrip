# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import sys

stdin, stdout = sys.stdin, sys.stdout
reload(sys)
sys.stdin, sys.stdout = stdin, stdout
sys.setdefaultencoding('utf-8')
#
# # Read in a page
def getAndStoreRandomComic():
  html = scraperwiki.scrape("http://www.commitstrip.com/?random=1")
  #
  # # Find something on the page using css selectors
  root = lxml.html.fromstring(html)
  frame = root.cssselect("div.entry-content")[0]
  url = frame.cssselect('img')[0].get('src')
  print str(url)
  ret = scraperwiki.sql.select("* from data where 'url'='"+str(url)+"'")
  print str(len(ret))
  if(len(ret) == 0):
    scraperwiki.sqlite.save(unique_keys=['url'], data={"url": str(url)})

for x in range(0,20):
  try:
    getAndStoreRandomComic();
  except:
    print "failed"
#
# # Write out to the sqlite database using scraperwiki library

#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
