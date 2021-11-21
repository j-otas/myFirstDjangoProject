from django.shortcuts import render

def main_admin_panel(request):
    return render(request, 'admin_panel/main_admin_list_page.html')
