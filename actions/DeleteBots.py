from openpyxl import load_workbook, Workbook

#Account that should be deleted
search_object = "checkmeout1337"

#NOT WORKING FOR NOW!!!
wb = load_workbook(filename="data.xlsx")
w_accounts = wb["Account-Daten"]
i = 1
for row in w_accounts.iter_rows(min_row=2, min_col=1, max_col=3, values_only=True):
    i += 1
    if search_object in row:
        account = row
        print(account)
        w_accounts.delete_rows(i,1)
        print("Deleted Account in row:",i)
wb.save("data.xlsx")
