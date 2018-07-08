import os


def my_paths():
    from os.path import expanduser
    my_home = expanduser("~")
    data_path = os.path.abspath(my_home+'/public_html/upload/data') + '/'
    return [data_path]


def print_html_msg(message):
    print """\
Content-Type: text/html\n
<html>
<body>
<p>%s</p>
&nbsp;&nbsp;<a href="upload.py">click here to return to file upload</a><Br>
</body>
</html>
""" % (message)
    pass
