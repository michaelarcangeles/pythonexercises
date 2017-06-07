from sys import argv

script, name = argv

age = raw_input("Hello %s, how old are you? " % name)
next_year = int(age) + 1

print "You will be %d next year." % next_year
