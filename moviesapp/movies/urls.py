# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('api/all/', view=views.MovieListView.as_view(), name='all'),
    path('<int:id>/', view=views.MovieRetrieveUpdateView.as_view(), name='detail'),
    path('create/', view=views.MovieCreateView.as_view(), name='create'),
    path('update/<int:id>/', view=views.MovieRetrieveUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', view=views.MovieDeleteView.as_view(), name='delete'),
    path('<int:movie_id>/vote/', views.vote, name='vote'),
]
