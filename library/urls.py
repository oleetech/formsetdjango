from django.urls import path
from .views import author_create, author_list,author_update,author_delete,author_details,find_author

urlpatterns = [
    path('author/create/', author_create, name='author_create'),
    path('author/list/', author_list, name='author_list'),
    path('author/update/<int:author_id>/', author_update, name='author_update'),
    path('author/delete/<int:author_id>/', author_delete, name='author_delete'),

    path('author/<int:author_id>/', author_details, name='author_details'),
    path('author/find/', find_author, name='find_author'),
]