from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.ListPostsView.as_view(),name='posts'),
    path('article/<int:pk>',views.DetailPostView.as_view(),name='article-detail'),
    path('add_post',views.AddPostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>',views.UpdatePostView.as_view(),name='update_post'),
    path('article/delete/<int:pk>',views.DeletePostView.as_view(),name='delete_post'),
    #path('add_category',views.AddCategoryView.as_view(),name='add_category'),
    #path('category/<str:cats>',views.category,name='category'),
    path('like/<int:pk>',views.Likeview,name='like_post'),
    path('article/<int:pk>/comment/',views.AddCommentView.as_view(),name='add_comment'),
]
