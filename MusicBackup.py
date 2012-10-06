#!/usr/bin/python

import os, os.path, re, io, string, subprocess, httplib, ConfigParser
config = ConfigParser.ConfigParser()
config.read('client.cfg')

# open our log file.
log = io.open(config.get('defaults', 'log_file'),'w+')

local_path = config.get('defaults', 'local_folder')
server_path = config.get('defaults', 'server_folder')
call_rsync = 'rsync --progress --ignore-existing -avzu --exclude=".*/" "' + local_path + '" "' + server_path + '"'
rsync = 1 #subprocess.call(call_rsync, shell=True)

if rsync == 0:
	con = httplib.HTTPConnection(config.get('urls', 'server'))
	con.request( 'GET', config.get('urls', 'server_path') )
	resp = con.getresponse()
	print resp.read()
