#Clears the Account from the list to re-enable them in the Like-Bot
def ClearDataList():
    data = open("like","r")
    datasheet = data.readlines()
    data.close()
    new_data = open("like","w")
    for line in datasheet:
        for element in clear_accounts:
            if line.strip("\n") != element:
                print("Deleted:",element)
                new_data.write(line)
    new_data.close()
    print("Finished")
#Type in the accounts that should be cleared from the list
clear_accounts = ["renaldo_3h"]
ClearDataList()
