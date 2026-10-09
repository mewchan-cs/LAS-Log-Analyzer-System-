def total_report(number_of_all_logs,distinctiveip,distinctiveuser,commonipdic,commonuserdic,suclog,failog):
    print("============TOTAL REAPORT==============")
    print(f"number of all logs : {number_of_all_logs}")
    print(f"number of distinctive ip : {distinctiveip}")
    print(f"number of distinctive user : {distinctiveuser}")
    print("+++++++++++++++++++++++++++++++++")
    print(f"most repeative ip : {list(commonipdic.keys())[0]} ")
    print(f"number of attempt {list(commonipdic.keys())[0]} : {list(commonipdic.values())[0]}\n")
    print(f"most repeative user : {list(commonuserdic.keys())[0]}")
    print(f"number of attempt {list(commonuserdic.keys())[0]} : {list(commonuserdic.values())[0]}")
    print("+++++++++++++++++++++++++++++++++")
    print(f"seccessful logins: {suclog}")
    print(f"failed logins : {failog}")
    


