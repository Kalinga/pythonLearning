sequence = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

for (index, day) in enumerate(sequence):
    print "index=", index, "Day(value)=", day

for day in sequence:
    print "Day(value)=", day

print "\nIndexed List from the sequence is below:"
for day in enumerate(sequence):
    print "->", day

print "\nIndexed List(reversed) from the sequence is below:"
for day in enumerate(sequence[::-1]):
    print "->", day


