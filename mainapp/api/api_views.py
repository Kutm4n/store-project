# from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
# from rest_framework.response import Response
# from collections import OrderedDict
# from rest_framework.filters import SearchFilter
# from rest_framework.pagination import PageNumberPagination
# from .serializers import CategorySerializer, SmartphoneSerializer, CustomerSerializer
# from ..models import Category, Customer
#
#
# class CategoryPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 10
#
#     def get_paginated_response(self, data):
#         return Response(OrderedDict([
#             ('objects_count', self.page.paginator.count),
#             ('next', self.get_next_link()),
#             ('previous', self.get_previous_link()),
#             ('items', data)
#         ]))
#
#
# class CategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):
#     serializer_class = CategorySerializer
#     pagination_class = CategoryPagination
#     queryset = Category.objects.all()
#     lookup_field = 'id'
#
#
# class SmartphoneListAPIView(ListAPIView):
#     serializer_class = SmartphoneSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['price', 'title']
#
#
# class SmartphoneDetailAPIView(RetrieveAPIView):
#     serializer_class = SmartphoneSerializer
#     lookup_field = 'id'
#
#
# class CustomersListAPIView(ListAPIView):
#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()
