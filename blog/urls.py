from django.urls import path  
from .views import post_list, post_detail, post_edit, post_delete, comment_edit, comment_delete

urlpatterns = [  
    path('', post_list, name='post_list'),  
    path('post/<int:post_id>/', post_detail, name='post_detail'),  
    path('post/edit/<int:post_id>/', post_edit, name='post_edit'),  
    path('post/delete/<int:post_id>/', post_delete, name='post_delete'),
    path('post/<int:post_id>/commentEdit/<int:comment_id>/', comment_edit, name='comment_edit'),
    path('post/<int:post_id>/commentDelete/<int:comment_id>/', comment_delete, name='comment_delete'), 
]  