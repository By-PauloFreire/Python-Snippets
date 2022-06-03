# This code will receive a file path as input,
# and search the log file for PDF's HTTP requests
# with a 200 OK status.

# The output will be a list with the name of the different
# PDF's written in a new file

# THIS is the log file structure that this code
# is expecting
#
# URL1 - - [19/Mar/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# URL2 - - [19/Mar/1995:00:00:11 -0400] "GET /shuttle/countdown/testing.html HTTP/1.0" 304 0
# URL2 - - [19/Mar/1995:00:00:12 -0400] "GET /images/file1.pdf HTTP/1.0" 304 0
# URL2 - - [19/Mar/1995:00:00:12 -0400] "GET /shuttle/countdown/video/file2.pdf HTTP/1.0" 200 0
# URL3 - - [19/Mar/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# URL1 - - [19/Mar/1995:00:00:14 -0400] "GET /shuttle/countdown/file3.pdf HTTP/1.0" 200 40310
# URL1 - - [19/Mar/1995:00:00:14 -0400] "GET /images/file1.pdf HTTP/1.0" 200 786
# URL1 - - [19/Mar/1995:00:00:14 -0400] "GET /images/file4.pdf HTTP/1.0" 200 1204
# URL3 - - [19/Mar/1995:00:00:15 -0400] "GET /shuttle/countdown/file3.pdf HTTP/1.0" 200 40310
# URL3 - - [19/Mar/1995:00:00:15 -0400] "GET /images/file1.pdf HTTP/1.0" 200 786

import re

def find(file_path):

    pdf = set()

    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()
        for values in lines:
            if values.split()[8] == '200':
                regex = re.search('.pdf', values.split()[6])
                if regex:
                    ret = values.split()[6].split('/')
                    pdf.add(ret[-1])


    try:
        for values in pdf:
            with open('output.txt', 'a') as write_output:
                write_output.write(values + '\n')
                print(values)
    except:
        print('Error')

