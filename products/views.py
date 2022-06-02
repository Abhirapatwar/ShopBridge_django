from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Entries_form
from .models import Entries
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_data(request):
    if request.method == 'POST':
        form_var = Entries_form(request.POST)

        # method 1 to save entered data into table
        # if form_var.is_valid():
        #     form_var.save()

        # method2
        if form_var.is_valid():
            nm = form_var.cleaned_data['name']
            pi = form_var.cleaned_data['price']
            ty = form_var.cleaned_data['type']
            de = form_var.cleaned_data['description']
           
            reg = Entries(name=nm, price=pi, type=ty,
                          description=de)
            reg.save()
        form_var = Entries_form()
        products = Entries.objects.all().order_by('id')

    else:
        form_var = Entries_form()
        if 'q' in request.GET:
            q = request.GET['q']
            if q != "":
                products = Entries.objects.filter(name=q)
            else:
                products = Entries.objects.all().order_by('id')    
        else:
            # form_var = Entries_form()
            products = Entries.objects.all().order_by('id')

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'getting.html', {'form': form_var, 'products': products, 'page_obj': page_obj})


def delete_data(request, id):
    if request.method == 'POST':
        to_del = Entries.objects.get(pk=id)
        to_del.delete()
        return HttpResponseRedirect('/')


def updatedata(request, id):
    if request.method == 'POST':
        to_update = Entries.objects.get(pk=id)
        updated_data = Entries_form(request.POST, instance=to_update)
        if updated_data.is_valid():
            updated_data.save()
    else:
        to_update = Entries.objects.get(pk=id)
    toupdated_data = Entries_form(instance=to_update)
    return render(request, 'update.html', {'toupdated_data': toupdated_data})
