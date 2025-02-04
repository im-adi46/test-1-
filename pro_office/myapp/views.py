from django.shortcuts import render, redirect, get_object_or_404
from.models import Office
# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404
from .models import Office

def office_list(request):
    offices = Office.objects.all()
    return render(request, 'office_list.html', {'offices': offices})

def office_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        emp_count = request.POST.get('emp_count')
        Office.objects.create(name=name, location=location, emp_count=emp_count)
        return redirect('office_list')
    return render(request, 'office_create.html')

def office_detail(request, office_id):
    office = get_object_or_404(Office, id=office_id)
    return render(request, 'office_detail.html', {'office': office})

def office_delete(request, office_id):
    office = get_object_or_404(Office, id=office_id)
    office.delete()
    return redirect('office_list')





























































# def office_list(request):
#     pro = Office.objects.all()
#     return render(request,'office_list.html',{'pro':pro})

# def office_create(request):
#     if request.method == 'POST':
#        name = request.POST.get('name')
#        location = request.POST.get('location')
#        emp_count = request.POST.get('emp_coun')
#        Office.objects.create(name=name, location = location, emp_count = emp_count)
#        return redirect('office_list')
#     return render(request,'office_create.html')

# def product_detail(request, emp_id):
#     pro = get_object_or_404(Office, id=emp_id) 
#     return render(request, 'office_detail.html', {'product': pro})

# def product_delete(request, emp_id):
#     pro = get_object_or_404(Office, id=emp_id)
#     pro.delete()
#     return redirect('office_list')