from LAS_Classes import InfoCounter
import Search_User
import Total_Report
print("========== Wellcome to LAS (Log Analyzer System) ==========")
run=1
while run==1:

    print("\n1- Enter a log file's path to analyze")
    print("2- Search user by ip or username (in current log file)")
    print("3- Total report of your log file (in current log file)")
    print("4- |-----Exit-----|")
    choice=input("Enter the number you choosed:\n")
    try:
        if choice=="1":
            log_file_path = input("\nPlease enter your log file's path:\n")
            print("------------------------------")
            with open(log_file_path, "r", encoding="utf-8") as file:
                log_file_as_list = [line.strip().split(" | ") for line in file]
            info_counter = InfoCounter(log_file_as_list)
            number_of_all_logs=info_counter.count_all_logs()
            info_counter.extract_distinctive_users()
            distinctiveuser=info_counter.count_distinctive_users()
            info_counter.extract_distinctive_ips()
            distinctiveip=info_counter.count_distinctive_ips()
            commonipdic,commonuserdic=info_counter.count_most_frequent_ip_and_user()
            suclog,failog=info_counter.number_of_status_login()
            ip_dictionary=info_counter.make_ip_dictionary()
            user_dictionary=info_counter.make_user_dictionary()
            ipsusdic=info_counter.suspicious_ip()
            
            continue

        elif choice=="2":
           Search_User.search_user(ip_dictionary,user_dictionary,ipsusdic)
           continue

        elif choice=="3":
            Total_Report.total_report(number_of_all_logs,distinctiveip,distinctiveuser,commonipdic,commonuserdic,suclog,failog)
            continue

        elif choice=="4":
            run=0
            print("Thankyou for using my program :).....\n")
            continue
        else:
            print("your choice is not valid !!!!!\n")
            continue
    except:
        print("You should Enter log file")

         

