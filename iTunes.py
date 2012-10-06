#!/usr/bin/python

import os, os.path, re, io, string, subprocess, urlparse

print "Content-Type: text/plain;charset=utf-8"
print

qs = urlparse.parse_qs(os.environ['QUERY_STRING'], True)

if 'mode' in qs:
    mode = qs['mode'][0].lower()
else:
    mode = 'list'

print mode

for root, dirs, files in os.walk('/Shared Media/Music'):
    if re.search('.itlp', root) == None:
        for file in files:
            if re.search('(.mp3|.m4a|.wav)', file):
                path = str(root + '/' + file)
                print path + "\n"
                
                if mode != None and mode == 'update':
                    
                    p = subprocess.Popen(['osascript', '/Library/WebServer/CGI-Executables/addToiTunes.applescript', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                    out, err = p.communicate()
                
                    if p.returncode:
                        print 'ERROR:', err
                    else:
                        print out