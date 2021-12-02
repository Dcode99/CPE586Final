#!/bin/bash

# This was written to make standard network testing 
# and to make it easier to make changes to the code.


red=`tput setaf 1`
green=`tput setaf 2`
blue=`tput setaf 4`
reset=`tput sgr0`


	# set up servers sleep used to help with the ports
	# and with the connections
	python3 MultiThreadedCache.py&
	sleep 1

	python3 MultiThreadedMain.py&
	sleep 1


	fallocate -l 1G test.mp4 # used to not waste space if needed.

	echo "$blue Files created redy to test $reset"

	curl http://localhost:32007/localhost:32008/helloworld.html --output tmp.html

	sleep 1
		
	echo "$blue Pulled helloworld.html$reset"

	curl http://localhost:32007/localhost:32008/image.png --output tmp.png

	sleep 1
		
	echo "$blue Pulled image.png$reset"

	curl http://localhost:32007/localhost:32008/Test.png --output tmpT.png

	sleep 1
		
	echo "$blue Pulled Test.png$reset"

	curl http://localhost:32007/localhost:32008/testing.jfif --output tmp.jfif

	sleep 1
		
	echo "$blue Pulled testing.jfif$reset"

	curl http://localhost:32007/localhost:32008/video.mp4 --output tmp.mp4

	sleep 1
		
	echo "$blue Pulled video.mp4$reset"

	curl http://localhost:32007/localhost:32008/test.mp4 --output large.mp4

	sleep 1

	echo "$blue Pulled test.mp4$reset"

	# this is code I (Andrew Donovan) made for another class

	# https://linuxcommand.org/lc3_man_pages/readh.html
	# this was added to see how easy it would be to pass parameters
	# from user input
	read -n1 -p " Would you like to clean the test files? And Kill the servers? [y,n] " clean_test

	# https://stackoverflow.com/questions/5542016/bash-user-input-if
	# found this and its great 

	case $clean_test in

		y|Y)rm tmp.html
			rm tmp.png
			rm tmpT.png
			rm tmp.jfif
			rm tmp.mp4
			rm large.mp4
			rm test.mp4 
			# fallocate can get compressed by the kernal so rebuilding 
			# each time is neccasy to get proper timing
			
			# Can be dangerous
			pkill python3
 
			echo "$red Cleaned. $reset"
			;;

		n|N) echo "$green Not cleaned. $reset"
			 ;;

		*) 	echo "$red (Unkonwn command) Not cleaned.$reset"
			 ;;
	esac



# allow a second

sleep 1 