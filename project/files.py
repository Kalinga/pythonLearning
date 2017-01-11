import os
import string
import  sys

print  "Current Working Directory"
print (os.getcwd())

l = (dir("os"))

print filter(lambda x: string.find(x, "_") , l)

print os.stat("/")
print "os.name: " + os.name
print "platform: " + sys.platform
print "os.uname: "
print os.uname()

print os.environ

#path = "/home/kalinga/"
#path = "/media/kalinga/5A9E6A779E6A4B97" #18 GB Volume
path = "/media/kalinga/9260C0A960C0957F" #47 GB Volume Windows C

tree = os.walk(path)
print type(tree)

directories = list()
files = list()

for root, dir, file in tree:
#    print root
    for d in dir:
        directories.append(d)
        #print d

    for f in file:
        files.append(f)
        #print f

print "Building of List is done \n"

#print directories
#print files

print "Dir count: " + str(len(directories))
print "Files count: " + str(len(files))

xclude = ["xml", "gif",
          "py", "jar",
          "css", "properties",
          "json", "bat",
          "png", "html",
          "htm", "manifest",
          "cat", "dll",
          "mui", "exe",
          "nlp", "browser",
          "desktop", "sys"]

countList = list()
files.sort()
for f in files:
    count = files.count(f)
    countList.append(count)
    if count > 1:
        for xtn in xclude:
            try:
                splited = string.split(f, ".", 1)[1]
                if (-1 != string.find(splited, xtn)):
                    found = True
                    #print "File found to be excluded with xtn: " + xtn
                    break;
            except IndexError:
                pass
        else:
            print f