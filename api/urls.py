from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MovieView
from .views import CommentView

urlpatterns = {
    url(r'^movies/$', MovieView.as_view(), name='create'),
    url(r'^comments/$', CommentView.as_view(), name='create')
}


# urlpatterns = {
#     url(r'bucketlists/$',
#         CreateView.as_view(),
#         name="create"),
#     url(r'bucketlists/(?P<pk>[0-9]+)/$',
#         DetailsView.as_view(), name="default")
# }

urlpatterns = format_suffix_patterns(urlpatterns)
