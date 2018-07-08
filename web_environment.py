#webEnvironment.py
import os; 
def myPaths():
  from os.path import expanduser
  myHome = expanduser("~")
  dataPath   = os.path.abspath(myHome+'/public_html/upload/data')+'/';
  return( [dataPath]);

def printHTMLmsg(message):
  print """\
Content-Type: text/html\n
<html>
<body>
<p>%s</p>
&nbsp;&nbsp;<a href="upload.py">return to file Upload</a><Br>
</body>
</html>
""" % (message)
  pass;
