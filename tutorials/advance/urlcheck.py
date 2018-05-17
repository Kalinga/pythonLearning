import requests
#line="http://www.google.com/laksdjf"
line="laksdjf"
works=-1
if (line.find("//")> -1):
    domain=line.split("//")[1].split("/")[0]
    try:
        request = requests.get(line)
    except Exception:
        print "Exception"

    if request.status_code == 200:
        works=1
    else:
        works=0

print works

