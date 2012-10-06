#!/usr/bin/python

import os, os.path, re, io, string, subprocess, urlparse, ConfigParser

config = ConfigParser.ConfigParser()
config.read('server.cfg')

qs = urlparse.parse_qs(os.environ['QUERY_STRING'], True)

if 'mode' in qs:
    mode = qs['mode'][0].lower()
else:
    mode = 'list'

print mode

print "Content-Type: text/plain;charset=utf-8"
print

processFolder(config.get('defaults', 'base_music_folder'))
                    
def proessFolder(folder):
    for root, dirs, files in os.walk(folder):
    if re.search('.itlp', root) == None:
        for file in files:
            if re.search('(.mp3|.m4a|.wav)', file):
                file_path = str(root + '/' + file)
                print file_path + "\n"
                
                if mode == 'update':
                    runUpdateScript(file_path)

def runUpdateScript(path):
    p = subprocess.Popen(['osascript', config.get('defaults', 'osascript_file'), path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
    out, err = p.communicate()

    if p.returncode:
        print 'ERROR:', err
    else:
        print out