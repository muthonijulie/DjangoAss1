from django.urls import path # type: ignore
from .views import post_list,post_detail,post_update,post_delete,post_create,post_about,post_search
urlpatterns=[
    path('',post_list,name='list'),
    path('detail/<int:id>/',post_detail,name='detail'),
    path('create/',post_create,name='create'),
    path('update/<int:id>/',post_update,name='update'),
    path('delete/<int:id>/',post_delete,name='delete'),
    path('about/',post_about,name='about'),
    path('search/',post_search,name='search'),
]

