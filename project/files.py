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
#path = "/media/kalinga/9260C0A960C0957F" #47 GB Volume Windows C
path = "/media/kalinga/ca6f935d-a7c5-4276-af49-5b2e44cb2f0e" #34 GB Volume Ubuntu

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

xclude = ['JPG', 'RSA', 'SF', 'bat', 'bin', 'browser', 'c', 'cache', 'cat', 'class', 'cmd', 'conf', 'cpp', 'css',
          'desktop', 'dll', 'exe', 'frag', 'gif', 'gitignore', 'h', 'htm', 'html', 'idl', 'jar', 'java', 'jpg',
          'js', 'json', 'ko', 'manifest', 'mm', 'mm', 'mui', 'nlp', 'otf', 'pd', 'placeholder', 'plxarc', 'pm',
          'png', 'pod', 'profile', 'properties', 'prs', 'py', 'so', 'svg', 'sys', 'tga', 'ttf', 'txt', 'vert',
          'wav', 'xml', 'yml','gitattributes', 'metadata', 'options', 'pl']

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
print "Finished searching for duplicate files. Thank You!!"