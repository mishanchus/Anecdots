from django.urls import path
from .views import home_page, anec_by_cat, add_anec

urlpatterns = [

    path('', home_page, name = 'home'),
    path('category/<int:category_id>/', anec_by_cat ,name = 'cats'),
    path('new_anec/',add_anec, name = 'add_anec')

]