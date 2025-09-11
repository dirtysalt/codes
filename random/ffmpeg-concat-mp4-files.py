#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import os
import sys
import subprocess
import argparse
parser = argparse.ArgumentParser(description='Use ffmpeg concat mp4 files')
parser.add_argument('--files', metavar='File', nargs='+', type=str, help='Sequence MP4(h.264) file for concatenating')
parser.add_argument('--output', metavar='Output', type=str, help='output file')
parser.add_argument('--m3u', metavar='M3U video list', type=str, help='m3u mp4 list')
parser.add_argument('--tmp', metavar='Working Dir', type=str, help='Working dir')

if __name__ == "__main__":
	files = []
	mp4_tmp = []
	wget_tmp = []
	args = parser.parse_args()
	if args.tmp == None:
		args.tmp = '/tmp'
	if args.output == None:
		args.output = '/tmp/output.mp4'
	if args.files and len(args.files):
		i = 1
		for target in args.files:
			if os.path.exists(target) and os.stat(target).st_size > 0:
				print "[Add] file("+str(i)+"): ", target
				i = i + 1
				files.append(target)
	if args.m3u:
		lines = [line.strip() for line in open(args.m3u) if line.strip()[0] != '#' and line.strip() != '']
		i = 1
		for target in lines:
			if target[0:4] == 'http':
				print "[Wget] file("+str(i)+"): ", target
				wget_target = args.tmp+'/wget_'+str(os.getpid())+'_'+str(i).zfill(2)+'_.mp4'
				i = i + 1
				cmd = [
					'wget', 
					'-O' , wget_target,
					target
				]
				subprocess.call( cmd )
				if os.path.exists(wget_target):
					wget_tmp.append(wget_target)
					if os.stat(wget_target).st_size > 0:
						files.append(wget_target)
						print "\tSave: ", wget_target
			else:
				if os.path.exists(target) and os.stat(target).st_size > 0:
					print "[Add] file("+str(i)+"): ", target
					i = i + 1
					files.append(target)

	for f in files:
		target = str(args.tmp) + '/tmp_' + os.path.basename(f)
		# ffmpeg -i f -c copy -bsf:v h264_mp4toannexb -f mpegts '/tmp/tmp_filename'
		cmd = [
			'ffmpeg', 
				'-i', f, 
				'-c', 'copy', 
				'-bsf:v', 'h264_mp4toannexb', 
				'-f', 'mpegts', 
				target
		]
		subprocess.call( cmd )
		mp4_tmp.append(target)

	if len(mp4_tmp) <= 1:
		print "No files:", mp4_tmp
		sys.exit(0)

	concat_list = "|".join(mp4_tmp)
	print
	print "concat raw files: ", concat_list
	print
	# ffmpeg -i "concat:/tmp/tmp1|/tmp/tmp2" -c copy -bsf:a aac_adtstoasc output.mp4
	cmd = [
		'ffmpeg', 
			'-i', 'concat:'+str(concat_list), 
			'-c', 'copy', 
			'-bsf:a', 'aac_adtstoasc',
			args.output ,
	]
	subprocess.call( cmd )

	for f in mp4_tmp:
		if os.path.exists(f):
			print "[Remove] mp4_tmp: ", f
			os.remove(f)
	for f in wget_tmp:
		if os.path.exists(f):
			print "[Remove] wget_tmp: ", f
			os.remove(f)

	print
	print "result: ", args.output
	print
