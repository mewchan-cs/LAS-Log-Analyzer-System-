from collections import Counter


class LogFileManager:
    def __init__(self, log_file_as_list):
        self.log_file_as_list = log_file_as_list
        self.distinctive_ip_set = set()
        self.distinctive_user_set = set()
        self.ip_info_dictionary = {}
        self.user_info_dictionary = {}

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
        print(self.most_frequent_user)
        print(self.most_frequent_ip)

        



    
