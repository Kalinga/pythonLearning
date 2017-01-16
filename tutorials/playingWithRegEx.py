import re
search = re.search('Ox',"a quick brown fox jumps over a lazy dog", re.IGNORECASE)
print search
if search:
    print search.group()

mat = re.match('Ox',"a quick brown fox jumps over a lazy dog", re.IGNORECASE)
print mat
if mat:
    print type(mat)
    print mat.group()

mat1 = re.match('a quick',"a quick brown fox jumps over a lazy dog", re.IGNORECASE)
print mat1
if mat1:
    print type(mat1)
    print mat1.group()
    print mat1.start()
    print mat1.end()
    print mat1.span()

pattern = re.compile(r"(..)+")
str =  "edureka"

print pattern.match( str).group()
print pattern.match(str).groups()
print pattern.match(str).group(1)
print pattern.match(str).groups(1)
print pattern.match(str).group(0)
print pattern.match(str).groups(0)

print "TODO: Name to a group in RE:\n"
print "TODO: Try pallindrome in RE:\n"
print "TODO: 'time' module:\n"