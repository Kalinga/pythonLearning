import os
import urllib2
import socket
from zipfile import ZipFile

import shutil

print urllib2.getproxies()

print  "Total items" + str(len(os.environ))

for item in os.environ:
    print  item, os.environ[item]

#isZipFile = False
isZipFile = True
zipLink = "https://github.com/Kalinga/pythonLearning/archive/master.zip"
httpLink = "https://www.google.co.in/?gfe_rd=cr&ei=FoFvWPaYG-ft8AfCjIaQCg#q=faq+python+"
link =  httpLink if not isZipFile else zipLink
try:
    url = urllib2.urlopen(link)
except urllib2.URLError, urlErr:
    print("URLError")
    print str(urlErr)
    print urlErr.reason
except urllib2.HTTPError:
    print("HTTPError")
except socket.error:
    print("SocketError")
except:
    print("UnExpectedError")
else:
    print url.geturl()
    contents = url.read()
    if "<!doctype html>" in contents:
        with open("response.html", "w") as htmlFile:
            htmlFile.write(contents)
    else:
        with open("master.zip", "w") as zipFile:
            zipFile.write(contents)

if (isZipFile):
    with ZipFile("master.zip") as zipFile:
        zipFile.extractall("/tmp/")

shutil.copy("/tmp/pythonLearning-master/README.md", os.getcwd())
shutil.rmtree("/tmp/pythonLearning-master")