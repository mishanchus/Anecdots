from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Anecdot, Category
from .forms import AnecForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    model = Anecdot
    template_name = 'home.html'
    context_object_name = 'anecs'
    paginate_by = 8
    def get_queryset(self):
        return Anecdot.objects.order_by('-pub_date')

class AnecByCat(ListView):
    model = Anecdot
    template_name = 'home.html'
    context_object_name = 'anecs'
    paginate_by = 8
    def get_queryset(self):
        return Anecdot.objects.order_by('-pub_date').filter(category=self.kwargs['category_id'])


class AddAnec(LoginRequiredMixin, CreateView):
    form_class = AnecForm
    template_name = 'add_anec.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnecDetail(DetailView):
    model = Anecdot
    context_object_name = 'anecs'
    template_name = 'detail_anec.html'

# def add_anec(request):
#     if request.method == 'POST':
#         form = AnecForm(request.POST)
#         if form.is_valid():
# #            Anecdot.objects.create(**form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AnecForm()
#     return render(request, 'add_anec.html', {'form':form})


# def home_page(request):
#     # categories = Category.objects.all()
#     anecs = Anecdot.objects.order_by('-pub_date')
#     context = {
#         # 'categories': categories,
#         'anecs': anecs
#     }
#     return render(request,'home.html', context)

# def anec_by_cat(request,category_id):
#     anecs = Anecdot.objects.order_by('-pub_date').filter(category=category_id)
#     # cats = Category.objects.all()
#     context = {
#         # 'categories':cats,
#         "anecs": anecs}
#     return render(request,'home.html', context)