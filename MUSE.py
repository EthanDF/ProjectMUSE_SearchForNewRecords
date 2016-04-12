__author__ = 'fenichele'

import urllib.request
import requests
import csv
import tkinter
import os
from _datetime import datetime

root = tkinter.Tk()
root.withdraw()

# collID = 111

# urlbase = 'http://muse.jhu.edu/cgi-bin/book_marc_html.cgi?action=marcRecord&type=customUpdate&fromDate='+str(sDate)+'&toDate='+str(eDate)+'&collectionID='+str(collID)

def testURL(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()

        return html

def downloadMarc(directory, url,collIDName):
    todayDate = datetime.now()
    eDate = str(todayDate.year)+'-'+str(todayDate.month)+'-'+str(todayDate.day)
    req = requests.get(url)
    marcfileName = 'Project_MUSE_UPCC_'+str(collIDName)+'_'+str(eDate).replace("-", '')+'.mrc'
    path = directory
    fileName = os.path.join(path, marcfileName)

    with open(fileName, 'wb') as x:
        x.write(req.content)
    print('saved '+fileName)

def askDate():
    aDate = input('What date? "YYYY-MM-DD"\n')
    return aDate

def chooseSaveDirectory():
    from tkinter import filedialog
    saveDirect = tkinter.filedialog.askdirectory()
    return saveDirect

def getCollIDs():
    collectionIDs = {}
    collectionFile = 'museCollections.csv'
    with open(collectionFile, 'r') as f:
        reader = csv.reader(f)
        cList = list(reader)

    for row in cList:
        collectionIDs[row[0]] = str(row[1])

    return collectionIDs

def getURLs(sDate, eDate, collID):
    urlbase = 'http://muse.jhu.edu/cgi-bin/book_marc_html.cgi?action=marcRecord&type=customUpdate&fromDate='+str(sDate)+'&toDate='+str(eDate)+'&collectionID='+str(collID)

    return urlbase

def buildURL():

    #choose save directory
    print("this program will help you check Project MUSE's site for new files \nto start, choose a save directory")
    saveD = chooseSaveDirectory()
    print('\nThanks! I will use '+str(saveD)+'\n...')

    #preassign dates based on the current date
    todayDate = datetime.now()
    sDate = '2016-01-01'
    eDate = str(todayDate.year)+'-'+str(todayDate.month)+'-'+str(todayDate.day)

    #offer possibility to choose a different start date
    userSDate = input('Do you want to enter a start date? '
                      '\nIf you select "n," i will use the first of the year... y/n\n')
    if userSDate == 'y':
        sDate = askDate()
        #check that the start date isn't later than today's date
        # if sDate > todayDate:
        #     print('invalid date... try again\n')
        #     sDate = askDate()

	
    collIDs = getCollIDs()
    print('using '+str(sDate))
    #phrase will be found if no records are available for search
    alert = 'No records were found for this time period'
    # urlList = []
    for i in collIDs:
        u = getURLs(sDate, eDate, i)
        h = testURL(u)
        print('checking collection ID: '+str(i)+', '+str(collIDs[str(i)]))

        if alert in h.decode():
            print('no updates')
            continue
        else:
            print('updates!')
            urlSt = str(u)
            downloadMarc(saveD, u, collIDs[str(i)].replace(' ', '_'))

buildURL()