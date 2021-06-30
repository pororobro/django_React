from django.conf.urls import url
from .views import Boards
urlpatterns = [
    url('/postwrite', Boards.as_view())
]