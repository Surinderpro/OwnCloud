#!/usr/bin/python
import cgi
import subprocess

print("Content-type: text/html")
print("")
CMD = "sudo docker ps -a"
output = subprocess.getoutput(CMD)
print("<pre>")
print(output)
print("</pre>")

