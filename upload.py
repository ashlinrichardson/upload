#!/usr/bin/python
import os
import sys
import cgi
import cgitb
import web_environment
[dataPath] = web_environment.myPaths() 
cgitb.enable(); form = cgi.FieldStorage() 

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
s+='<form enctype="multipart/form-data" action="./saveFile.py" method="post">';
s+='<p>File: <input type="file" name="filename" /></p>'
s+='<p><input type="submit" value="Upload" /></p></form>'
if(False):
  existingTextFiles = [ ] 
  if os.path.exists("fileList.txt"):
    existingTextFiles = open("fileList.txt").read().strip().split("\n");
  h = [ ] 
  s += "<h3>Review existing files</h3>"
  for f in existingTextFiles:
    ff = os.path.basename( f).strip();
    if( ff=='output.pdf'):	
      continue;
    baseName = os.path.basename(f.strip()).strip();
    linkString = '<a href="./'+ baseName +'">'+ baseName +'</a>' 
    s+=('<form enctype="multipart/form-data" action="./deleteFile.py" method="post">')
    s+=('Delete file:<input type="text" name="filetodelete" value="'+ baseName+'"/> ')
    s+=('</u>' +linkString+ '&nbsp;&nbsp;<input type="submit" value="Confirm delete" /></form>')  

print s

print """\
</body>
</html>
""" 
