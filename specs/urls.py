from django.urls import path
from .views import BaseSpecView, NewCategoryView, CreateNewFeature, NewProductFeature

urlpatterns = [
    path('', BaseSpecView.as_view(), name='base-spec'),
    path('new-category/', NewCategoryView.as_view(), name='new-category'),
    path('new-feature/', CreateNewFeature.as_view(), name='new-feature'),
    path('new-product-feature/', NewProductFeature.as_view(), name='new-product-feature')
]