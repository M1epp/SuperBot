import gspread
from gspread import Cell, Client, Spreadsheet, Worksheet
from Text.Text import Text_for_get_by_name_and_data_for_employee
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1fXGqcvNaLSOCsmjZHPcT-rUUZ9JkJgm7FNGR9djh4Lw/edit?pli=1#gid=807302821"

gc: Client = gspread.service_account("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/DataBase/service_account.json")
sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)


def get_by_name_and_data_for_employee(name: str, data: str, sh2: Spreadsheet = sh):
    ws = sh2.worksheet(name)
    cell: Cell = ws.find(data)
    row = ws.row_values(cell.row)
    new_row = ''
    i = 0
    for ex in row:
        new_row = new_row + Text_for_get_by_name_and_data_for_employee[i] + ex + "\n"
        i += 1
    return new_row


def get_by_name_and_data_for_owner(name: str, data: str, sh2: Spreadsheet = sh):
    ws = sh2.worksheet(name)
    cell: Cell = ws.find(data)
    row = ws.row_values(cell.row)
    new_row = ''
    i = 0
    for ex in row:
        new_row = new_row + Text_for_get_by_name_and_data_for_employee[i] + ex + "\n"
        i += 1
    return new_row


def get_by_data_week_from_the_report(data: str, sh2: Spreadsheet = sh):
    list_of_week: str = ''
    for i in range(7):
        data2 = data.split('.')
        if int(data2[0]) + i < 10:
            data2[0] = "0" + str(int(data2[0]) + i)
        else:
            data2[0] = str(int(data2[0]) + i)
        data_new: str = data2[0]
        for j in range(1, 3):
            data_new = data_new + '.' + data2[j]
        list_of_week = list_of_week + str(get_by_data_day_from_the_report(data_new, sh2))
    return list_of_week


def get_by_data_day_from_the_report(data: str, sh2: Spreadsheet = sh):
    ws = sh2.sheet1
    cell: Cell = ws.find(data)
    row = ws.row_values(cell.row)
    i = 0
    list_of_day: str = ''
    for ex in row:
        if i < 5:
            list_of_day += ex
            list_of_day += "\n"
        i += 1
    list_of_day += "\n"
    return list_of_day
