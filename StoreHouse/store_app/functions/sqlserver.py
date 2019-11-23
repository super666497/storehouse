from django.db import connection,transaction
import os

class user:
    user_name = ""
    user_password = ""

    def __init__(self, data):
        self.user_name = data[0]
        self.user_password = data[1]

class cargo:
    cargo_name = ""
    cargo_unit = ""
    cargo_number = 0

    def __init__(self, data):
        self.cargo_name = data[0]
        self.cargo_number = data[1]
        self.cargo_unit = data[2]

def format_ans(rows):
    ans = []
    for row in rows:
        items = []
        for clo in row:
            items.append(str.strip(str(clo)))
        ans.append(items)
    return ans

def exec(sql):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'StoreHouse.settings'
    cursor = connection.cursor()
    cursor.execute(sql)
    transaction.commit()
    rows = cursor.fetchall()
    ans = format_ans(rows)
    return ans

def get_all_cargo_name():
    sql = "select cargo_name from cargo"
    items = exec(sql)
    ans = []
    for item in items:
        ans.append(item[0])
    return ans

def get_all_cargo_units():
    sql = "select distinct cargo_unit from cargo"
    items = exec(sql)
    ans = []
    for item in items:
        ans.append(item[0])
    return ans

def get_all_cargoes():
    sql = "select * from cargo"
    items = exec(sql)
    ans = []
    for item in items:
        ans.append(cargo(item))
    return ans

def check_login(user_name, user_password):
    sql = "select * from [user] where user_name = '{0}' and user_password='{1}'".format(user_name, user_password)
    items = exec(sql)
    if len(items) > 0:
        return 1
    else:
        return 0

def get_query_context():
    context = {'all_cargo_names': get_all_cargo_name(), 'all_units': get_all_cargo_units()}
    return context

def find_cargo(cargo_name, cargo_number, cargo_unit):
    style_like = "like '%'"
    style_equals = "= '{0}'"
    if len(cargo_name) == 0:
        cargo_name = style_like
    else:
        cargo_name = style_equals.format(cargo_name)
    cargo_number = str(cargo_number)
    if len(cargo_number) == 0:
        cargo_number = style_like
    else:
        cargo_number = style_equals.format(cargo_number)
    if len(cargo_unit) == 0:
        cargo_unit = style_like
    else:
        cargo_unit = style_equals.format(cargo_unit)

    sql = "select * from cargo where cargo_name {0} and cargo_number {1} and cargo_unit {2}".format(
        cargo_name, cargo_number, cargo_unit)
    items = exec(sql)
    all_cargoes = []
    for item in items:
        all_cargoes.append(cargo(item))
    return all_cargoes

if __name__ == '__main__':
    get_all_cargo_name()