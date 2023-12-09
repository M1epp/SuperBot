import sqlite3


def who_is_user(telegram_id):
    with sqlite3.connect("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/DataBase/DB_SQL.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_id FROM users WHERE Admin = 1")
        result_admin: list[int] = []
        for ex in cur:
            result_admin += ex
        cur.execute("SELECT user_id FROM users WHERE Employee = 1")
        result_employee: list[int] = []
        for ex in cur:
            result_employee += ex
        if telegram_id in result_admin:
            return 0
        elif telegram_id in result_employee:
            return 1


def user_is_admin(telegram_id):
    with sqlite3.connect("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/DataBase/DB_SQL.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_id FROM users WHERE Admin = 1")
        result_admin: list[int] = []
        for ex in cur:
            result_admin += ex
        if telegram_id in result_admin:
            return True


def user_is_employee(telegram_id):
    with sqlite3.connect("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/DataBase/DB_SQL.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_id FROM users WHERE Employee = 1")
        result_employee: list[int] = []
        for ex in cur:
            result_employee += ex
        if telegram_id in result_employee:
            return True


def get_name_for_employee(telegram_id):
    with sqlite3.connect("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/DataBase/DB_SQL.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_id, name FROM users WHERE Employee = 1")
        result = cur.fetchall()
        for i in range(len(result)):
            if result[i][0] == telegram_id:
                return result[i][1]


def get_list_of_employee():
    with sqlite3.connect("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/DataBase/DB_SQL.db") as con:
        cur = con.cursor()
        cur.execute("SELECT user_id, name FROM users WHERE Employee = 1")
        list_of_employee_str = ''
        result = cur.fetchall()
        for ex in result:
            list_of_employee_str = list_of_employee_str + "T-Id: " + str(ex[0]) + " - " + str(ex[1]) + "\n"
        return list_of_employee_str


def add_delete_employee_bd(telegram_id: int, name: str):
    with sqlite3.connect("/Users/Дмитрий/PycharmProjects/TeleBot_Iogram3/DataBase/DB_SQL.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Employee FROM users WHERE user_id = ?", (telegram_id,))
        current_state = int(cur.fetchone()[0])
        if current_state == 1:
            cur.execute("UPDATE users SET Employee = 0, name = ? WHERE user_id = ?", (name, telegram_id,))
        else:
            cur.execute("UPDATE users SET Employee = 1, name = ? WHERE user_id = ?", (name, telegram_id,))


class DataB:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exist(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchone()
            return result

    def add_user(self, user_id):
        try:
            with self.connection:
                return self.cursor.execute("INSERT OR IGNORE INTO 'users' ('user_id') VALUES (?)", (user_id,))
        except sqlite3.IntegrityError:
            print(f"Пользователь с user_id={user_id} уже существует в базе данных.")
            # Дополнительные действия при необходимости
            return None

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id,))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users").fetchall()
