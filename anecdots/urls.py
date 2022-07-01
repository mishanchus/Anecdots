from django.urls import path
from .views import HomePageView, AnecByCat, AddAnec

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('', home_page, name = 'home'),
    path('category/<int:category_id>/', AnecByCat.as_view() ,name = 'cats'),
    # path('category/<int:category_id>/', anec_by_cat ,name = 'cats'),
    path('new_anec/',AddAnec.as_view(), name = 'add_anec'),
    # path('new_anec/',add_anec, name = 'add_anec')

]