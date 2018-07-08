#!/usr/bin/python
import os
import sys
import cgi
import cgitb
import web_environment

[data_path] = web_environment.my_paths()

cgitb.enable()
form = cgi.FieldStorage()

print """\
Content-Type: text/html; charset=utf-8\n
<html>
<body>
<h1>File upload </h1>
"""
print """\
<hr>
"""
s = "<h3>Upload file</h3>"
s += '<form enctype="multipart/form-data" '
s += 'action="./save_file.py" method="post">'
s += '<p>File: <input type="file" name="filename" /></p>'
s += '<p><input type="submit" value="Upload" /></p></form>'
if(False):
    existing_text_files = []
    if os.path.exists("fileList.txt"):
        existing_text_files = open("fileList.txt").read().strip().split("\n")
    h = []
    s += "<h3>Review existing files</h3>"
    for f in existing_text_files:
        ff = os.path.basename(f).strip()
        if ff == 'output.pdf':
            continue
        base_name = os.path.basename(f.strip()).strip()
        link_string = '<a href="./' + base_name + '">' + base_name + '</a>'
        s += '<form enctype="multipart/form-data" '
        s += 'action="./delete_file.py" method="post">'
        s += 'Delete file:'
        s += '<input type="text" name="filetodelete" value="'
        s += (base_name + '"/> ')
        s += '</u>' + link_string
        s += '&nbsp;&nbsp;'
        s += '<input type="submit" value="Confirm delete" />'
        s += '</form>'

print s

print """
</body>
</html>
"""
