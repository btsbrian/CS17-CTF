#!/usr/bin/python
import socket
import time
import string

x = 0
y = 0
dX = 0
dY = 1
maze = {(0,1,'N')}
clockwisedirs = {"N":"W", "W":"S", "S":"E", "E":"N"}
ccw = {"N":"E", "E":"S", "S":"W", "W":"N"}
backwards = {"N":"S", "S":"N", "E":"W", "W":"E"}
mylastdirection = "N"
deltas = {"N":(0,1), "S":(0,-1), "E":(1,0), "W":(-1,0)}
sock = socket.create_connection( ("easybee1.bruti.us", 25001) )
time.sleep(0.5)
while ( not((x == -40) and (y == 48))):
	worktext = sock.recv(2000)
	print worktext
	placeholder = worktext.find("following directions: ")
	dirlist = worktext[placeholder+22:worktext.find(".",placeholder)]
	directions=map(string.strip,dirlist.split(","))
	print x, y, directions
	
	if (ccw[mylastdirection] in directions):
		mylastdirection = ccw[mylastdirection]
	elif (mylastdirection in directions):
		mylastdirection = mylastdirection
	elif (clockwisedirs[mylastdirection] in directions):
		mylastdirection = clockwisedirs[mylastdirection]
	else:
		mylastdirection = backwards[mylastdirection]	
	if ((x,y,mylastdirection) in maze):
		print "Looping!"
	maze.add ( (x,y,mylastdirection) )
	(dX, dY) = deltas[mylastdirection]
	x += dX
	y += dY
   
	data = mylastdirection + "\n"
	sock.sendall(data)
	print data
	time.sleep(0.05)

time.sleep(0.5)
print sock.recv(4000)
print maze
sock.close()
