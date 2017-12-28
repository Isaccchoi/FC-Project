from django.conf.urls import url, include

from . import managements, details
from ..views import restaurant_list_view, CommentUpdateDestroyView

urlpatterns = [
    # /restaurants/<pk(restaurant pk)>/
    url(r'^(?P<pk>\d+)/', include(details, namespace='detail')),
    # /restaurants/management/
    url(r'^management/', include(managements, namespace='management')),

    # /restaurants/
    url(r'^$', restaurant_list_view, name='restaurant-list'),
    # /restaurants/<pk>/
    # /restaurants/comments/<pk(comment pk)>/
    url(r'^comments/(?P<pk>\d+)/$', CommentUpdateDestroyView.as_view(), name='comment-update-destroy'),
    # Management

]
