from openpyxl import load_workbook, Workbook
from openpyxl.styles.borders import Border, Side
from sys import exit

#Account that should be deleted
new_bot = "Inunction"
pw = "test.python"
email = "checkmeout1337@gmail.com"


def  check_memory():
    wb = load_workbook(filename="./data/data.xlsx")
    w_bot = wb["Bots"]
    for row in w_bot.iter_cols(min_row=1, min_col=1, max_row=1, values_only=True):
        if new_bot in row:
            exit("Bot already in bot memory!")

def bot_memory():
    wb = load_workbook(filename="./data/data.xlsx")
    w_bot = wb["Bots"]
    new_col = w_bot.max_column
    new_col += 1
    bot_num = w_bot.cell(row=1,column=new_col,value=new_bot).border = Border(bottom=Side(style="thick"),left=Side(style="thick"))
    wb.save("data.xlsx")
    print("New bot memory created:",new_bot)


def check_account():
    wb = load_workbook(filename="./data/data.xlsx")
    w_bot = wb["Account-Daten"]
    for row in w_bot.iter_rows(min_row=2, min_col=1, max_col=3, values_only=True):
        if new_bot in row:
            exit("Bot already in account list!")

def bot_account():
    wb = load_workbook(filename="./data/data.xlsx")
    w_bot = wb["Account-Daten"]
    new_row = w_bot.max_row
    new_row += 1
    w_bot.cell(row=new_row, column=1, value=new_bot)
    w_bot.cell(row=new_row, column=2, value=pw).border = Border(left=Side(style="thick"))
    w_bot.cell(row=new_row, column=3, value=email).border = Border(left=Side(style="thick"))
    wb.save("data.xlsx")
    print("New bot account in list:",new_bot)

check_account()
bot_account()
check_memory()
bot_memory()
