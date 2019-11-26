from django.shortcuts import render
from .functions.sqlserver import check_login, get_query_context, \
    get_all_cargoes, find_cargo, in_cargo_exist_sql,in_cargo_new_sql,\
    out_cargo_sql, get_total_number_of_cargo, get_cargo_unit, already_exist_cargo_name,\
    get_all_input_record, get_all_output_record, find_in_record, find_out_record
# Create your views here.

def main(request):
    return render(request, "main.html")

def quit(request):
    message_context = {'message': ''}
    return render(request, "main.html", message_context)

def manage(request):
    context = get_query_context()
    cargo_context = {'all_cargoes': get_all_cargoes()}
    context.update(cargo_context)
    return render(request, "manage.html", context)

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        if check_login(user_name, user_password):
            context = get_query_context()
            cargo_context = {'all_cargoes': get_all_cargoes()}
            context.update(cargo_context)
            return render(request, "manage.html", context)
    message_context = {'message': '用户名或密码错误!'}
    return render(request, "main.html", message_context)

def query(request):
    if request.method == 'POST':
        cargo_name = request.POST['cargo_name']
        cargo_number = request.POST['cargo_number']
        cargo_unit = request.POST['cargo_unit']
        all_cargoes = find_cargo(cargo_name, cargo_number, cargo_unit)
        context = get_query_context()
        cargo_context = {'all_cargoes': all_cargoes}
        context.update(cargo_context)
        return render(request, "manage.html", context)
    context = get_query_context()
    cargo_context = {'all_cargoes': get_all_cargoes()}
    context.update(cargo_context)
    return render(request, "manage.html", context)

def in_cargo(request, cargo_name):
    # 在in_out.html提交数据过来的话
    if request.method == 'POST':
        cargo_number = float(request.POST['cargo_number'])
        if cargo_number < 0:
            context = {'title': '进货', 'cargo_name': cargo_name, 'cargo_unit': get_cargo_unit(cargo_name), 'submit_type': '进货', 'message': '进货数量错误！'}
            return render(request, "in_out.html", context)
        in_cargo_exist_sql(cargo_name, cargo_number)
        context = {'title': '进货', 'cargo_name': cargo_name, 'cargo_unit': get_cargo_unit(cargo_name), 'submit_type': '进货', 'message': '进货成功!'}
        return render(request, "in_out.html", context)
    # 从manage,html导航过来
    context = {'title': '进货', 'cargo_name': cargo_name, 'cargo_unit': get_cargo_unit(cargo_name), 'submit_type': '进货'}
    return render(request, "in_out.html", context)

def out_cargo(request, cargo_name):
    # 在in_out.html提交数据过来的话
    if request.method == 'POST':
        cargo_number = float(request.POST['cargo_number'])
        if cargo_number < 0 or cargo_number > float(get_total_number_of_cargo(cargo_name)):
            context = {'title': '出货', 'cargo_name': cargo_name, 'cargo_unit': get_cargo_unit(cargo_name), 'submit_type': '出货', 'message': '出货数量错误！'}
            return render(request, "in_out.html", context)
        out_cargo_sql(cargo_name, cargo_number)
        context = {'title': '出货', 'cargo_name': cargo_name, 'cargo_unit': get_cargo_unit(cargo_name), 'submit_type': '出货', 'message': '出货成功!'}
        return render(request, "in_out.html", context)
    # 从manage,html导航过来
    context = {'title': '出货', 'cargo_name': cargo_name, 'cargo_unit': get_cargo_unit(cargo_name), 'submit_type': '出货'}
    return render(request, "in_out.html", context)

def in_new_cargo(request):
    # 在in_out.html提交数据过来的话
    if request.method == 'POST':
        cargo_name = request.POST['cargo_name']
        cargo_number = float(request.POST['cargo_number'])
        cargo_unit = request.POST['cargo_unit']
        if cargo_number < 0:
            context = {'title': '进货', 'cargo_name': cargo_name, 'cargo_unit': cargo_unit, 'submit_type': '进货',
                       'message': '进货数量错误！'}
            return render(request, "in_out.html", context)
        if already_exist_cargo_name(cargo_name):
            context = {'title': '进货', 'cargo_name': cargo_name, 'cargo_unit': cargo_unit, 'submit_type': '进货',
                       'message': '货物已存在！'}
            return render(request, "in_out.html", context)
        in_cargo_new_sql(cargo_name, cargo_number, cargo_unit)
        context = {'title': '进货', 'cargo_name': cargo_name, 'cargo_unit': cargo_unit, 'submit_type': '进货',
                   'message': '进货成功!'}
        return render(request, "in_out.html", context)
    # 从manage,html导航过来
    context = {'title': '进货', 'submit_type': '进货'}
    return render(request, "in_out.html", context)

def check_in(request):
    context = {'title': '进货记录', 'record_type': '进货', 'records': get_all_input_record()}
    return render(request, "check.html", context)

def check_out(request):
    context = {'title': '出货记录', 'record_type': '出货', 'records': get_all_output_record()}
    return render(request, "check.html", context)

def check_query_in(request):
    if request.method == 'POST':
        cargo_name = request.POST['cargo_name']
        cargo_number = request.POST['cargo_number']
        cargo_unit = request.POST['cargo_unit']
        record_time = request.POST['record_time']
        records = find_in_record(cargo_name, cargo_number, cargo_unit, record_time)
        context = {'title': '进货记录', 'record_type': '进货', 'records': records}
        return render(request, "check.html", context)
    context = {'title': '进货记录', 'record_type': '进货', 'records': get_all_input_record()}
    context.update(context)
    return render(request, "check.html", context)

def check_query_out(request):
    if request.method == 'POST':
        cargo_name = request.POST['cargo_name']
        cargo_number = request.POST['cargo_number']
        cargo_unit = request.POST['cargo_unit']
        record_time = request.POST['record_time']
        records = find_out_record(cargo_name, cargo_number, cargo_unit, record_time)
        context = {'title': '出货记录', 'record_type': '出货', 'records': records}
        return render(request, "check.html", context)
    context = {'title': '出货记录', 'record_type': '出货', 'records': get_all_input_record()}
    context.update(context)
    return render(request, "check.html", context)