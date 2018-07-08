#!/usr/bin/python
#-------------------------------------------------------------------------#
import cgi, cgitb, os, sys, heapq, random, uuid, web_environment #---#
[dataPath]=web_environment.myPaths() #--------#
cgitb.enable(); form = cgi.FieldStorage() #-------------------------------#
#-------------------------------------------------------------------------#
fileitem = form['filename']
message = "";
fileList ="" 
if( os.path.exists( dataPath+"/fileList.txt")):
  fileList = open(dataPath+"/fileList.txt").read().strip()
filesInList = fileList.split("\n");
if fileitem.filename:
    fn = os.path.basename(fileitem.filename);
    if( not(os.path.exists( dataPath+"/"+fn))):
      open(dataPath+"/"+fn,'wb').write(fileitem.file.read())
      if( os.path.exists( dataPath+"/"+fn)):
	cmd = "chmod	a+r	"+dataPath+"/"+fn
	a = os.system(cmd);
      message = "file "+fn+" uploaded."
      fileList+=("\n"+fn)
      open(dataPath+"/fileList.txt",'wb').write( fileList);
    else:
      message +=" please delete file first."
else:
  message = "no file uploaded."
message = "file uploaded. "
web_environment.printHTMLmsg(message);

