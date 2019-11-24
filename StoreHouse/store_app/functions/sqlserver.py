from django.db import connection,transaction
import os

class record:
    record_time = ""
    cargo_name = ""
    cargo_number = ""
    cargo_unit = ""

    def __init__(self, data):
        self.record_time = data[0]
        self.cargo_name = data[1]
        self.cargo_number = data[2]
        self.cargo_unit = data[3]

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

def query(sql):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'StoreHouse.settings'
    cursor = connection.cursor()
    cursor.execute(sql)
    transaction.commit()
    rows = cursor.fetchall()
    ans = format_ans(rows)
    return ans

def exec(sql):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'StoreHouse.settings'
    cursor = connection.cursor()
    cursor.execute(sql)
    transaction.commit()

def get_all_cargo_name():
    sql = "select cargo_name from cargo"
    items = query(sql)
    ans = []
    for item in items:
        ans.append(item[0])
    return ans

def get_all_cargo_units():
    sql = "select distinct cargo_unit from cargo"
    items = query(sql)
    ans = []
    for item in items:
        ans.append(item[0])
    return ans

def get_all_cargoes():
    sql = "select * from cargo"
    items = query(sql)
    ans = []
    for item in items:
        ans.append(cargo(item))
    return ans

def check_login(user_name, user_password):
    sql = "select * from [user] where user_name = '{0}' and user_password='{1}'".format(user_name, user_password)
    items = query(sql)
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
    items = query(sql)
    all_cargoes = []
    for item in items:
        all_cargoes.append(cargo(item))
    return all_cargoes

def in_cargo_exist_sql(cargo_name, cargo_number):
    sql = "exec input_cargo_exist @cargo_name = '{0}', @cargo_number = {1}".format(cargo_name, cargo_number)
    exec(sql)

def in_cargo_new_sql(cargo_name, cargo_number, cargo_unit):
    sql = "exec input_cargo_new @cargo_name = '{0}', @cargo_number = {1}, @cargo_unit = '{2}'".format(cargo_name, cargo_number, cargo_unit)
    exec(sql)

def out_cargo_sql(cargo_name, cargo_number):
    sql = "exec output_cargo @cargo_name = '{0}', @cargo_number = {1}".format(cargo_name, cargo_number)
    exec(sql)

def get_total_number_of_cargo(cargo_name):
    sql = "select cargo_number from cargo where cargo_name = '{0}'".format(cargo_name)
    items = query(sql)
    ans = items[0][0]
    return ans

def get_cargo_unit(cargo_name):
    sql = "select cargo_unit from cargo where cargo_name = '{0}'".format(cargo_name)
    items = query(sql)
    ans = items[0][0]
    return ans

def already_exist_cargo_name(cargo_name):
    sql = "select * from cargo where cargo_name = '{0}'".format(cargo_name)
    items = query(sql)
    return len(items)

def get_all_input_record():
    records = []
    sql = "select * from input_view"
    items = query(sql)
    for item in items:
        records.append(record(item))
    return records

def get_all_output_record():
    records = []
    sql = "select * from output_view"
    items = query(sql)
    for item in items:
        records.append(record(item))
    return records

def find_in_record(cargo_name, cargo_number, cargo_unit, record_time):
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
    if len(record_time) == 0:
        record_time = style_like
    else:
        record_time = "like '%{0}%'".format(record_time)

    sql = "select * from input_view where cargo_name {0} and cargo_number {1} and cargo_unit {2} and convert(varchar,cargo_input_time,20) {3} ".format(
        cargo_name, cargo_number, cargo_unit, record_time)
    items = query(sql)
    all_records = []
    for item in items:
        all_records.append(record(item))
    return all_records

def find_out_record(cargo_name, cargo_number, cargo_unit, record_time):
    print("hello find out")
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
    if len(record_time) == 0:
        record_time = style_like
    else:
        record_time = "like '%{0}%'".format(record_time)

    sql = "select * from output_view where cargo_name {0} and cargo_number {1} and cargo_unit {2} and convert(varchar,cargo_output_time,20) {3} ".format(
        cargo_name, cargo_number, cargo_unit, record_time)
    items = query(sql)
    all_records = []
    for item in items:
        all_records.append(record(item))
    return all_records

if __name__ == '__main__':
    already_exist_cargo_name('苹果')