#!/usr/bin/env python
import os
 
desktop_path = os.environ['HOME']
myfile_path = os.path.join(desktop_path, "Desktop", "mynewgloriousfile.txt")
 
print "The following file will be created: %s" % myfile_path
 
myfile = open(myfile_path, 'w') 
 
myfile.write("This is going to end up in the file.")
 
myfile.close()
 