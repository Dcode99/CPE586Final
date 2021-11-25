# used to test consistently
.PHONY: all

all:


test: 	all
		curl http://localhost:32007/localhost:32008/helloworld.html --output tmp.html
		curl http://localhost:32007/localhost:32008/image.png --output tmp.png
		curl http://localhost:32007/localhost:32008/Test.png --output tmpT.png
		curl http://localhost:32007/localhost:32008/testing.jfif --output tmp.jfif

clean: all 
	rm tmp.html
	rm tmp.png
	rm tmpT.png
	rm tmp.jfif