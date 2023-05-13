from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy


from .models import Product, Supplier
from .forms import ProductForm, SupplierForm


# def eshop(request):
#     products = Product.objects.all()
#     context = {
#         'products':products
#     }
#     return render(request, 'eshop/home.html', context)

# def Eshop(request):
#     return render(request, 'eshop/home.html')


# class ProductListPageView(ListView):
#     model = Product
    
#     template_name = 'eshop/product_list.html'


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "eshop/add_product.html"
    success_url = reverse_lazy('eshop')



# class SupplierPageView(ListView):
#     model = Supplier

#     template_name = 'eshop/supplier.html'

# class AddSupplierView(CreateView):
#     model = Supplier
#     form_class = SupplierForm
#     template_name = "eshop/add_supplier.html"
#     success_url = reverse_lazy('supplier')


# class ProductUpdateView(UpdateView):
#    model=Product
#    fields="__all__"
#    template_name='update_product.html'
#    success_url= reverse_lazy('eshop')

#    def form_valid(self, form):
#     messages.success(self.request, "The product was updated successfully.")
#     return super(ProductUpdateView, self).form_valid(form)



# def success(request):
#    return render(request,'eshop.html')


def ProductList(request):
    if request.method == 'GET':
        products = Product.objects.all()#.order_by('-updated'
        context = {'products':products}
        return render(request, 'eshop/home.html', context)

    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST.get('name')
        )
        product.save()
        return redirect('home')

## ------------------------------------------------------

def ProductDetail(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        context = {'product':product}
        return render(request, 'eshop/product_detail.html', context)

    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        product.product_description = request.POST.get('product_description')
        product.save()
        return redirect('eshop')
        #success_url = reverse_lazy('eshop')

## ------------------------------------------------------

def ProductDelete(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('eshop')

    context = {'product':product}   
    return render(request, 'eshop/delete.html', context)