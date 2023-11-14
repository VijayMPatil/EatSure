from django.urls import path
from apps.vendor.views import VendorListAPIView, VendorSearchAPIView,VendorDetailsAPIView, MenuListAPIView


urlpatterns = [
    # For Vendor
    path('list/', VendorListAPIView.as_view(), name="vendor-list"),
    path('search/vendor/', VendorSearchAPIView.as_view(), name='vendor-search'),
    path('details/<int:id>', VendorDetailsAPIView.as_view(), name='vendor-details'),
    path('menu_list/<int:id>/', MenuListAPIView.as_view(), name="menu-list"),

    # url(r'^(?P<id>[0-9]+)/menu_search/$', MenuSearchAPIView.as_view(), name='vendor-search'),

]
