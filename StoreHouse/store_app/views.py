from django.shortcuts import render
from .functions.sqlserver import check_login, get_query_context, get_all_cargoes, find_cargo
# Create your views here.

def main(request):
    return render(request, "main.html")

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