def search_user(ip_dictionary,user_dictionary):
    search_choise =input("Search by ip or search by user (i for ip and u for user)?\n")

    def search_by_ip(ip_dictionary):
        selected_ip=input("Enter the ip you want:\n")
        if selected_ip not in ip_dictionary:
            print("This ip not found.....")
        for i in ip_dictionary:
            if i == selected_ip:
                print(f"ip:{i}:\n")
                for j in ip_dictionary[i]:
                    print(f"{j}\n")
            

    def search_by_user(user_dictionary):
        selected_user=input("Enter the user you want:\n")
        if selected_user not in user_dictionary:
            print("This user not found....")
        for i in user_dictionary:
            if i == selected_user:
                print(f"user:{i}:\n")
                for j in user_dictionary[i]:
                    print(f"{j}\n")


    if search_choise=="i":
        search_by_ip(ip_dictionary)

    elif search_choise=="u":
        search_by_user(user_dictionary)

    else:
        print("Character is not valid!!!!!!!!!")

