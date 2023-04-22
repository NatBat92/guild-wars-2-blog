from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AddPost, PostList, PostDetail, PostLike, \
    UpdatePostView, DeletePostView, UserEditView, PasswordsChangeView
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('new/', views.AddPost.as_view(), name='new_post'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success', views.password_success, name='password_success'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='edit_post'),
    path('<slug:slug>/delete/', DeletePostView.as_view(), name='delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
