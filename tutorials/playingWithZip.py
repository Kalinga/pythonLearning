import os
import urllib2
import socket
from pip.commands import unzip

print urllib2.getproxies()

print  "Total items" + str(len(os.environ))

for item in os.environ:
    print  item, os.environ[item]


try:
    url = urllib2.urlopen("https://github.com/Kalinga/pythonLearning/archive/master.zip")
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
    with open("master.zip", "w") as zipFile:
        zipFile.write(contents)

