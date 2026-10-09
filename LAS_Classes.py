from collections import Counter


class LogFileManager:
    def __init__(self, log_file_as_list):
        self.log_file_as_list = log_file_as_list
        self.distinctive_ip_set = set()
        self.distinctive_user_set = set()
        self.ip_info_dictionary = {}
        self.user_info_dictionary = {}
        self.ip_suspicious_status={}

    def extract_distinctive_ips(self):
        for member in self.log_file_as_list:
            self.distinctive_ip_set.add(member[1])
        return self.distinctive_ip_set

    def extract_distinctive_users(self):
        for member in self.log_file_as_list:
            self.distinctive_user_set.add(member[2])
        return self.distinctive_user_set

    def make_ip_dictionary(self):
        for ip in self.distinctive_ip_set:
            copy_list = []
            for member1 in self.log_file_as_list:
                copy_member = member1.copy()
                if ip in member1:
                    del copy_member[1]
                    copy_list.append(copy_member)

            self.ip_info_dictionary[ip] = copy_list
        return self.ip_info_dictionary

    def make_user_dictionary(self):
        for user in self.distinctive_user_set:
            copy_list = []
            for member1 in self.log_file_as_list:
                copy_member = member1.copy()
                if user in member1:
                    del copy_member[2]
                    copy_list.append(copy_member)

            self.user_info_dictionary[user] = copy_list
            
        return self.user_info_dictionary

    def suspicious_ip(self):
        ipstat=0
        for susip in self.ip_info_dictionary:
            for susip2 in self.ip_info_dictionary[susip]:
                if susip2[2] == "FAILED":
                    ipstat+=1
            self.ip_suspicious_status[susip]=ipstat
            ipstat=0

        return self.ip_suspicious_status
             




class InfoCounter(LogFileManager):
    def __init__(self, log_file_as_list):
        super().__init__(log_file_as_list)
        self.number_of_distinctive_ips = 0
        self.number_of_distinctive_users = 0
        self.number_of_all_records = 0
        self.number_of_failed_logins = 0
        self.number_of_successful_logins = 0
        self.most_frequent_ip = None
        self.most_frequent_user = None
        self.ip_attemp_dict={}
        self.user_attemp_dict={}

    def count_distinctive_ips(self):
        self.number_of_distinctive_ips = len(self.distinctive_ip_set)
        return self.number_of_distinctive_ips

    def count_distinctive_users(self):
        self.number_of_distinctive_users = len(self.distinctive_user_set)
        return self.number_of_distinctive_users

    def number_of_status_login(self):
        for numerator in self.log_file_as_list:
            if numerator[3]=="FAILED":
                self.number_of_failed_logins+=1
            elif numerator[3]=="SUCCESS":
                self.number_of_successful_logins+=1
        return self.number_of_successful_logins,self.number_of_failed_logins

    def count_most_frequent_ip_and_user(self):
        all_ip_we_have=[]
        all_user_we_have=[]
        for numerator in self.log_file_as_list:
            all_ip_we_have.append(numerator[1])
            all_user_we_have.append(numerator[2])

        self.most_frequent_ip=dict(Counter(all_ip_we_have).most_common(1))
        self.most_frequent_user=dict(Counter(all_user_we_have).most_common(1))
        return self.most_frequent_user , self.most_frequent_ip

    def count_all_logs(self):
        for logcounter in self.log_file_as_list:
            self.number_of_all_records+=1
        return self.number_of_all_records

    def number_of_attemp_ip(self):
        num_of_attemp=0
        for ipattempcounter in self.ip_info_dictionary:
            num_of_attemp=len(ipattempcounter.values())
            self.ip_attemp_dict[ipattempcounter]=num_of_attemp.copy()
        return self.ip_attemp_dict

    def number_of_attemp_user(self):
        num_of_attemp=0
        for userattempcounter in self.ip_info_dictionary:
            num_of_attemp=len(userattempcounter.values())
            self.user_attemp_dict[userattempcounter]=num_of_attemp.copy()
        return self.user_attemp_dict

    




        



    
