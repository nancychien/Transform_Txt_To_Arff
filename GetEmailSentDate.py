#This Program is for Python 2.X version
import re
import glob

outputPath = "EmailDate.txt"
saveFile = open(outputPath,'a')

#Initialize
rowCnt = 0
mailCnt = 0
fileCnt = 0
endPos = 0
q1Cnt = 0
q2Cnt = 0
q3Cnt = 0
q4Cnt = 0
MondayCnt    = 0
TuesdayCnt   = 0
WednesdayCnt = 0
ThursdayCnt  = 0
FridayCnt    = 0
SaturdayCnt  = 0
SundayCnt    = 0

# Import all arff files in current folder
for name in glob.glob('*.arff'):
        
        file = open(name,"r")

        for block in file:
                #print "rowCnt="+ str(rowCnt)
                if rowCnt > 4:
                        
                        emailList = block
                              
                        # Get Email Date
                        endPos = emailList.find("','")
                        if emailList[0:10].find("Sent:	") != -1:                                
                                emailContext = emailList[7:endPos].strip() + "\n" 
                        elif emailList[0:3].find(":\t") != -1:
                                emailContext = emailList[3:endPos].strip() + "\n" 
                        elif emailList[0:3].find(": ") != -1:
                                emailContext = emailList[3:endPos].strip() + "\n" 
                        elif emailList[0:5].find("nt: ") != -1:
                                emailContext =  emailList[6:endPos].strip() + "\n"
                        elif emailList[0:5].find("nt:\t") != -1:
                                emailContext =  emailList[4:endPos].strip() + "\n"
                        #Need to revise
                        elif emailList[0:10].find("> Sent:\t") != -1:
                                emailContext = emailList[8:endPos].strip() + "\n"
                        else:
                                emailContext = emailList[1:endPos].strip() + "\n" 

                        mailCnt = mailCnt +1
                        
                        # Extract Day
                        allList = emailContext.split(",")
                        sDay = allList[0].strip()

                        if sDay.find("Monday")!= -1:
                                MondayCnt = MondayCnt +1
                        if sDay.find("Tuesday")!= -1:
                                TuesdayCnt = TuesdayCnt +1
                        if sDay.find("Wednesday")!= -1:
                                WednesdayCnt = WednesdayCnt +1
                        if sDay.find("Thursday")!= -1:
                                ThursdayCnt = ThursdayCnt +1
                        if sDay.find("Friday")!= -1:
                                FridayCnt = FridayCnt +1
                        if sDay.find("Saturday")!= -1:
                                SaturdayCnt = SaturdayCnt +1
                        if sDay.find("Sunday")!= -1:
                                SundayCnt = SundayCnt +1

                        if emailContext.find("January")!= -1 or emailContext.find("February")!= -1 or emailContext.find("March")!= -1:
                                q1Cnt = q1Cnt+1
                        elif emailContext.find("April")!= -1 or emailContext.find("May")!= -1 or emailContext.find("June")!= -1:
                                q2Cnt = q2Cnt+1
                        elif emailContext.find("July")!= -1 or emailContext.find("August")!= -1 or emailContext.find("September")!= -1:
                                q3Cnt = q3Cnt+1
                        elif emailContext.find("October")!= -1 or emailContext.find("November")!= -1 or emailContext.find("December")!= -1:
                                q4Cnt = q4Cnt+1
                        
                
                rowCnt = rowCnt + 1
        saveFile.write("File Name = '"+ name + "', Monday Count: "+str(MondayCnt)+ ", Tuesday Count: "+str(TuesdayCnt)+ ", Wednesday Count: "+str(WednesdayCnt)+ ", Thursday Count: "+str(ThursdayCnt)+ ", Friday Count: "+str(FridayCnt)+ ", Saturday Count: "+str(SaturdayCnt)+ ", Sunday Count: "+str(SundayCnt)+"\n") 
        saveFile.write("File Name = '"+ name + "', Q1 Count: "+str(q1Cnt)+ ", Q2 Count: "+str(q2Cnt)+ ", Q3 Count: "+str(q3Cnt)+ ", Q4 Count: "+str(q4Cnt)+"\n")        
        fileCnt = fileCnt + 1
        MondayCnt    = 0
        TuesdayCnt   = 0
        WednesdayCnt = 0
        ThursdayCnt  = 0
        FridayCnt    = 0
        SaturdayCnt  = 0
        SundayCnt    = 0
        q1Cnt = 0
        q2Cnt = 0
        q3Cnt = 0
        q4Cnt = 0
        
        
file.close()        
print "Finish! Total ",mailCnt, "mails, ", fileCnt ,"files, Output is at:", outputPath

saveFile.close()

