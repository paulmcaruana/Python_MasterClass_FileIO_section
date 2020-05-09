# jabber = open("D:\\python-masterclass\\original.txt",'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()
#tider version

# with open("D:\\python-masterclass\\original.txt",'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("D:\\python-masterclass\\original.txt",'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

#above prints full text without the lines in between

# with open("D:\\python-masterclass\\original.txt",'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("D:\\python-masterclass\\original.txt",'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("D:\\python-masterclass\\original.txt",'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')

# readline reads a single line at a time from a file and returns a string
# readlines reads the entire file and returns a list of strings
# read reads the entire file and if text and returns a string returning the contents of the file