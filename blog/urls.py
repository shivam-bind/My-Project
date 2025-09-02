from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', views.home, name='home'),
    path('',views.post_list, name='post-list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('create/<int:pk>/post/', views.create_post, name='create_post'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('select/', views.select_post, name='select_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),


]
