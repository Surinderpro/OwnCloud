#!/usr/bin/python
import cgi
import subprocess

print("Content-type: text/html")
print("")

form = cgi.FieldStorage()
container_name = form.getvalue('name')

if container_name:
    CMD = f"sudo docker start {container_name}"
    output = subprocess.getoutput(CMD)
    print("<pre>")
    print(output)
    print("</pre>")
else:
    print("<pre>Error: No container name provided.</pre>")

