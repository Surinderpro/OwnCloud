#!/usr/bin/python
import cgi
import subprocess

print("Content-type: text/html")
print("")

form = cgi.FieldStorage()
image_name = form.getvalue('image')

if image_name:
    CMD = f"sudo docker run -d {image_name}"
    output = subprocess.getoutput(CMD)
    print("<pre>")
    print(output)
    print("</pre>")
else:
    print("<pre>Error: No image name provided.</pre>")

