from django.urls import path

from users.views import AuthorView, ClientView

urlpatterns = [
    path('authors/', AuthorView.as_view(), name='author-list'),
    path('client/', ClientView.as_view(), name='client-list'),

]

app_name = "users"
