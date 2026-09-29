from LAS_Classes import Log_File_Manager as lfm
from LAS_Classes import InfoCounter 
Log_File_As_List=[]
Log_File=input("PLease Enter your Log file's path:\n")
with open(Log_File,"r",encoding='utf-8') as Log_File:
    for line in Log_File:
        line=line.strip()
        Splited_Log_File=line.split(" | ")
        Log_File_As_List.append(Splited_Log_File)

ob1=InfoCounter(Log_File_As_List)
ob1.Distinctive_Ip()
ob1.distinctive_ip()