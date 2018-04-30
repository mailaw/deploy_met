from django.urls import path

from . import views

app_name = 'themet'
urlpatterns = [
    # /themet/
	path('', views.index, name='index'),
    path('pie_chart/', views.demo_piechart, name='demo_pie_chart'),
    # ex./themet/paintings
    path('paintings/', views.painting_list, name='painting_list'),
    # ex./themet/paintings/5
	path('paintings/portraits', views.ppainting_list, name='ppainting_list'),
    path('paintings/<int:pk>/', views.painting_detail, name='painting_detail')

]
