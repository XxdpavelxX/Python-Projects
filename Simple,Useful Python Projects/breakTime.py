import webbrowser
import time
break_count=0
print "This program started at: "+time.ctime() #time.ctime() tells us the current time

while break_count<3:
	time.sleep(	10) #time.sleep() is what causes the program to wait 10seconds before running)
	webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')  #opens the web browser.
	break_count=break_count+1
	
print "This program ended at: "+time.ctime()