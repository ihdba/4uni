from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render


from .models import Supplier

# def suppliers(request):
#     return render(request, 'suppliers/suppliers.html')



def SupplierList(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()#.order_by('-updated'
        context = {'suppliers':suppliers}
        return render(request, 'suppliers/suppliers.html', context)

    if request.method == 'POST':
        supplier = Suppliers.objects.create(
            name=request.POST.get('name')
        )
        supplier.save()
        return redirect('suppliers')