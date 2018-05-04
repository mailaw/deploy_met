from django.urls import path

from . import views

app_name = 'themet'
urlpatterns = [
    # /themet/
	path('', views.index, name='index'),
    path('pie_chart/', views.demo_piechart, name='demo_pie_chart'),
    # ex./themet/paintings
    path('paintings/', views.painting_list, name='painting_list'),
	path('paintings/france', views.france_painting_list, name='france_painting_list'),
	path('paintings/american', views.american_painting_list, name='american_painting_list'),
	path('paintings/britain', views.britain_painting_list, name='britain_painting_list'),
	path('paintings/italian', views.italian_painting_list, name='italian_painting_list'),
	path('paintings/dutch', views.dutch_painting_list, name='dutch_painting_list'),
	path('paintings/swiss', views.swiss_painting_list, name='swiss_painting_list'),
    # ex./themet/paintings/5
	path('paintings/portraits', views.ppainting_list, name='ppainting_list'),
    path('paintings/<int:pk>/', views.painting_detail, name='painting_detail')

]
