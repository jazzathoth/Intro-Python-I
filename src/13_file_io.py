"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

f = open('foo.txt', 'r')
for i in f:
    print(i)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

fw = open('bar.txt', 'w+')

fw.write('Consulted perpetual of pronounce me delivered.\n')
fw.write('Too months nay end change relied who beauty wishes matter.\n')
fw.write('Shew of john real park so rest we on.\n')
fw.write('Is we miles ready he might going.\n')

fw.close()

fr = open('bar.txt', 'r')
for i in fr:
    print(i)
fr.close()
