#This Program is for Python 2.X version
import re
import glob

outputPath = "C:\Users\Nancy\Downloads\EmailResult.arff"
saveFile = open(outputPath,'a')

#Initialize
rowCnt = 0
newFlag = False
mailCnt = 0
fileCnt = 0

for name in glob.glob('C:\Users\Nancy\Downloads\*.txt'):
        
        file = open(name,"r")

        for block in file:

                if rowCnt == 0:
                        saveFile.write("@relation EmailResult \n@attribute Date string \n@attribute Context string \n@data \n")
                # Remove \r\n for .arff format
                emailList = block.rstrip()
                      
                # Email Date
                if emailList.find("Sent:") != -1:
                        mailFlag = True
                        mailCnt = mailCnt +1
                        if fileCnt == 0 and rowCnt == 1:
                                emailContext = " \n'" + emailList[6:] + "','"
                        else:
                                emailContext = "' \n'" + emailList[6:] + "','"
                        saveFile.write(emailContext)
                # Ignore Subject
                elif emailList.find("Subject:") != -1:
                        newFlag = False
                        # Remove special character
                        newFlag = False
                # Ignore From
                elif emailList.find("From:") != -1:
                        newFlag = False
                # Ignore To
                elif emailList.find("To") != -1:
                        newFlag = False
                # Ignore cc
                elif emailList.find("cc") != -1:
                        newFlag = False
                # Ignore Original Message
                elif emailList.find("Original Message") != -1:
                        newFlag = False                
                # Ignore Attachement
                elif emailList.find("Attachments:") != -1:
                        newFlag = False
                else:
                        newFlag = False
                        # Remove special character
                        emailContext = emailList.translate(None, "'")
                        #print emailContext
                        saveFile.write(emailContext)
                rowCnt = rowCnt + 1        
        fileCnt = fileCnt + 1
        
saveFile.write("\n")        
file.close()        
print "Finish! Total ",mailCnt, "mails, ", fileCnt ,"files, Output is at:", outputPath

saveFile.close()
