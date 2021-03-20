
from django.urls import path
from . import views
from.views import TweetListView,TweetCreateView,TweetUpdateView,TweetDeleteView

urlpatterns = [

    path('feed/',TweetListView.as_view(), name='home'),
    path('search/',views.search,name='search'),
    path('create/',TweetCreateView.as_view(), name='postcreate'),
    path('tweet/<int:pk>/update/',TweetUpdateView.as_view(), name='postupdate'),
    path('tweet/<int:pk>/delete/',TweetDeleteView.as_view(), name='postdelete'),
    
]