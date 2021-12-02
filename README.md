# CPE586 Final Project
Final Project for CPE 586
Creating a server and client web system for users to download and upload videos, images, and text. Currently limited to 5 clients at a time.

Instructions to run:
  - ./test.sh
    - sets up servers and creates the needed files 
    - cleans both the server processes and tmp files
      - This is based on user input 
        - If y or Y it deletes test files and kills the server process's
        - If n or N it does not delete test files and kills the server process's
        - All other inputs does not not delete test files and kills the server process's
      - Has nice colored output
      
  - Uses Curl to test networking speed and statisics 
    - Prints to terminal
    - With Network Statistics

    ### WARNING THIS SCRIPT USES PKILL ON PYTHON3 ###

To create some of the larger files used for tesing:
  - fallocate -l 1G test.mp4
    - This is done via the test.sh file
