#!/usr/bin/python
import os
import sys
import cgi
import cgitb
import web_environment
[data_path] = web_environment.my_paths()

cgitb.enable()
form = cgi.FieldStorage() 

file_item = form['filename']
message = ""
file_list = ""

a = os.system("mkdir -p " + data_path)
a = os.system("chmod 700 " + data_path)

if os.path.exists(data_path + "/file_list.txt"):
  file_list = open(data_path + "/file_list.txt").read().strip()
# filesInList = file_list.split("\n")
if file_item.filename:
    fn = os.path.basename(file_item.filename)
    if not(os.path.exists(data_path + "/" + fn)):
      open(data_path + "/" + fn, 'wb').write(file_item.file.read())
      if( os.path.exists( data_path + "/" + fn)):
	cmd = "chmod	a+r	" + data_path + "/" + fn
	a = os.system(cmd)
      message = "file " + fn + " uploaded."
      file_list += ("\n" + fn)
      open(data_path+"/file_list.txt",'wb').write(file_list)
    else:
      message +=" please delete file first."
else:
  message = "no file uploaded."
message = "file uploaded. "
web_environment.print_html_msg(message)
