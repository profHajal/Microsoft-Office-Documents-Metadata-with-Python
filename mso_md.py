import os
import zipfile
import re
import xml.dom.minidom
from datetime import datetime
import csv 
import glob
def getAllFiles(allDocInfo,path):
    for filename in glob.iglob(path+'/**/*.*',recursive = True): 
        allDocInfo.append(getFileInfo(filename)) 

def getFileInfo(f):
    myFile = zipfile.ZipFile(f,'r')
    doc = xml.dom.minidom.parseString(myFile.read('docProps/core.xml'))
    xml.dom.minidom.parseString(myFile.read('docProps/core.xml')).toprettyxml()

    docInfo = {} 
    docInfo['fileName'] = f
    try:
        docInfo['title'] = doc.getElementsByTagName('dc:title')[0].childNodes[0].data
    except:
        docInfo['title'] =''

    try:
        docInfo['Description'] = doc.getElementsByTagName('dc:description')[0].childNodes[0].data
    except:
        docInfo['Description'] =''

    try:
        docInfo['creator'] = doc.getElementsByTagName('dc:creator')[0].childNodes[0].data
    except:
        docInfo['creator'] =''

    try:
        docInfo['lastModifiedBy'] = doc.getElementsByTagName('cp:lastModifiedBy')[0].childNodes[0].data
    except:
        docInfo['lastModifiedBy'] =''

    try:
        docInfo['DateCreated'] = doc.getElementsByTagName('dcterms:created')[0].childNodes[0].data
    except:
        docInfo['DateCreated'] =''

    try:
        docInfo['DateModified'] = doc.getElementsByTagName('dcterms:modified')[0].childNodes[0].data
    except:
        docInfo['DateModified'] =''

    return docInfo

def savetoCSV(allDocInfo, filename): 
  
    # specifying the fields for csv file 
    fields = ['fileName', 'title', 'Description', 'creator', 'lastModifiedBy', 'DateCreated','DateModified'] 
  
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(allDocInfo) 
      
if(__name__=="__main__"):
    allDocInfo = [] 
    getAllFiles(allDocInfo,'.\Student_work')
    savetoCSV(allDocInfo,'results.csv')
    print('DONE')
