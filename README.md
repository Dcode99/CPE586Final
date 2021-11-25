# CPE586 Final Project
Final Project for CPE 586
Creating a server and client web system for users to download and upload videos, images, and text. Currently limited to 5 clients at a time.

Instructions to run:
1. Make sure server and proxy server are running
  - Ex: python3 MultiThreadedMain.py || python3 MultiThreadedCache.py
3. Run client side with desired file as the extension, for example: http://localhost:32007/localhost:32008/helloworld.html to download helloworld.html when running it all on the same machine
  - curl http://localhost:32007/localhost:32008/helloworld.html

Use the make file that is included to do consistent testing with speed stattiscs via curl.
  Make commands:
    test: runs the curl commands on all of the provided files.
    clean: removes all of the downloaded files for a cleaner directory.
