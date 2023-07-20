import datetime
import os.path
def readLog(filePath):
 fp = None 
 try:
   fp = open(filePath)
   line = fp.readline()  
   date=""
   dataToWriteInFile = ""
   warn=""
   error=""
   cntWrn=0
   cntErr=0
   while line:
     line = line.strip()
     record = line.split(" ") 
     if(len(record)>1):
       date_text = record[0] + " " + record[1]
       isValidDateTime = isValiddDateFormat(date_text)
       print(" date_text ::: ", date_text, " isValidDateTime ::: " + str(isValidDateTime))
       if (line.find("WARN") != -1):
         if(cntWrn>0):
           warn+="\n" 
         warn+=line
         cntWrn+=1
       if (line.find("ERROR") != -1):
         if(cntErr>0):
           error+="\n"
         error+=line
         cntErr+=1
       if(isValidDateTime):
         if(len(warn)>1):
           writeFile(os.path.abspath("C:/Users/Dheeraj/Desktop/WARN.txt"),warn)
           warn=""
         if(len(error)>1):
           writeFile(os.path.abspath("C:/Users/Dheeraj/Desktop/ERROR.txt"),error)
           error=""
       if(len(warn)>1):
         warn+="\n"
         warn+=line
       if(len(error)>1):
         warn+="\n"
         error+=line
       print(" date ::: "+date)
     else:
       if(line.isdigit()):
         date=line
     line = fp.readline()
   fp.close()
 except ValueError:
    print(ValueError)

def isValiddDateFormat(date_text):
  try:
    datetime.datetime.strptime(date_text, '%m/%d %H:%M:%S')
    return True
  except ValueError:
    return False

def writeFile(file,line):
  try:
    f = open(file,"a+")
    f.write(line)
    f.close()
  except ValueError:
    print(ValueError)     

data_folder = os.path.abspath("C:/Users/Dheeraj/Desktop/LogData.txt")
readLog((data_folder))