from collections import Counter
class Log_File_Manager:
    def __init__(self,Log_File_As_List):
        self.Log_File_As_List=Log_File_As_List
        self.Distinctive_Ip_Set=set()
        self.Distinctive_User_Set=set()
        self.Ip_Info_Dictionary={}
        self.User_Info_Dictionary={}


    def Distinctive_Ip(self):
        for member in self.Log_File_As_List:
            self.Distinctive_Ip_Set.add(member[1])

        return self.Distinctive_Ip_Set


    def Distinctive_User(self):
        for member in self.Log_File_As_List:
            self.Distinctive_User_Set.add(member[2])

        return self.Distinctive_User_Set


    def Ip_Dictionary_Maker(self):
        Copy_List=[]
        for member in self.Distinctive_Ip_Set:
            Ip=member
            for member1 in self.Log_File_As_List:
                Copy_Member=member1.copy()
                if Ip in member1:
                    del Copy_Member[1]
                    Copy_List.append(Copy_Member)
                    
            self.Ip_Info_Dictionary[Ip]=Copy_List.copy()
            Copy_List.clear()

        return self.Ip_Info_Dictionary
        

    def User_Dictionary_Maker(self):
        Copy_List=[]
        for member in self.Distinctive_User_Set:
            User=member
            for member1 in self.Log_File_As_List:
                Copy_Member=member1.copy()
                if User in member1:
                    del Copy_Member[2]
                    Copy_List.append(Copy_Member)

            self.User_Info_Dictionary[User]=Copy_List.copy()
            Copy_List.clear()
        print(self.User_Info_Dictionary)

        return self.User_Info_Dictionary






class InfoCounter(Log_File_Manager):
    def __init__(self,Log_File_as_List):
        super().__init__(Log_File_as_List)
        self.Number_Of_Distinction_Ip=0
        self.Number_Of_Distinction_User=0
        self.Number_Of_All_Records=0
        self.Number_Of_Faild_Login=0
        self.Number_Of_Successfull_Login=0
        self.Most_Frequent_IP=None
        self.Most_Frequent_User=None

    def distinctive_ip(self):
        self.Number_Of_Distinction_Ip=len(self.Distinctive_Ip_Set)
        print(self.Number_Of_Distinction_Ip)
