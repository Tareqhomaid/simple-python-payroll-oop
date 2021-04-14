import os

list_of_files = os.listdir("files")
mngr_file = ['1name', '2name', '3emails', '4phones', '5pass', '6id','teammangers'] #FN, LN, Email, Phone, Pass, ID, role
mngrdirs = {}
data = {}
for files in sorted(list_of_files):
    if files != 'teammangers':
        with open("files/"+files) as dat:
            data[files] = dat.read().split()

for files in mngr_file:
    with open("files/"+files) as dat:
        mngrdirs[files] = dat.read().split()

def dirs():
    return data

def mngrdir():
    return mngrdirs