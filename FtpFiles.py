# Description: FTP files from a particular server to local server.
# Author: Dev

import ftplib

def openConnection(svr, usr, pwd):
    ftp = ftplib.FTP(svr, usr, pwd)
    return ftp

def getFiles(ftp, files):
    for line in files:
        file = line.split(' ')
        fp = open(file[-1], "wb")
        ftp.retrbinary('RETR {}'.format(file[-1]), fp.write)
        fp.close()

if '__main__' == __name__:
    server = '<server>'
    username = '<username>'
    password = '<password>'
    #Open a connection
    ftp = openConnection(server, username, password)
    #Extract list that start with test*
    files = []
    ftp.dir('test*', files.append)
    getFiles(ftp, files)
    ftp.quit()
    