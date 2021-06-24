from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('reply/<int:pk>/', views.ReplyDetail.as_view()),
]
