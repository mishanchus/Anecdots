from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView
from .models import Anecdot, Category
from .forms import AnecForm


def home_page(request):
    # categories = Category.objects.all()
    anecs = Anecdot.objects.order_by('-pub_date')
    context = {
        # 'categories': categories,
        'anecs': anecs
    }
    return render(request,'home.html', context)


def anec_by_cat(request,category_id):
    anecs = Anecdot.objects.order_by('-pub_date').filter(category=category_id)
    # cats = Category.objects.all()
    context = {
        # 'categories':cats,
        "anecs": anecs}
    return render(request,'home.html', context)


def add_anec(request):
    if request.method == 'POST':
        form = AnecForm(request.POST)
        if form.is_valid():
#            Anecdot.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AnecForm()
    return render(request, 'add_anec.html', {'form':form})
