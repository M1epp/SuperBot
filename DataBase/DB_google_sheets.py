import gspread
from gspread import Cell, Client, Spreadsheet
from Text.Text import Text_for_get_by_name_and_data_for_employee, Text_for_get_by_data_to_data
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


def get_by_data_to_data_from_the_report(data: str, data1: str):
    list_of_data_to_data: str = ''
    data_ = data.split(".")
    data1_ = data1.split(".")

    for i in range(int(data_[0]), int(data1_[0]) + 1):
        data_i = data_
        if int(data_i[0]) < 10:
            data_i[0] = "0" + str(int(data_i[0]))
        data_new: str = data_i[0]
        for j in range(1, 3):
            data_new = data_new + '.' + data_i[j]
        data_[0] = str(int(data_[0]) + 1)
        one_day_list: str = get_by_data_day_from_the_report(data_new)
        list_of_data_to_data = list_of_data_to_data + str(one_day_list)
    return list_of_data_to_data


def get_by_data_day_from_the_report(data: str, sh2: Spreadsheet = sh):
    ws = sh2.sheet1
    cell: Cell = ws.find(data)
    row = ws.row_values(cell.row)
    i = 0
    list_of_day: str = ''
    for ex in row:
        if i < 12:
            list_of_day += Text_for_get_by_data_to_data[i]
            list_of_day += ex
            list_of_day += "\n"
        i += 1
    list_of_day += "\n"
    return list_of_day
