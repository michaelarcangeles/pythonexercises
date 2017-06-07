from sys import argv

script, input_file = argv
# reads all contents of file
def print_all(f):
  print f.read()
# goes back to beginning of file
def rewind(f):
  f.seek(0)
# prints one line of the file contents
def print_a_line(line_count, f):
  print line_count, f.readline()
# opens the file object and puts it in variable called current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
