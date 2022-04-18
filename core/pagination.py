from collections import OrderedDict
from django.http import request
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationWithCount(PageNumberPagination):
    def get_page_number(self, request, paginator):
        return super().get_page_number(request, paginator)

    def get_paginated_response(self, data):
        current_page = int(self.get_page_number(
            self.request, self.django_paginator_class))
        events_per_page = self.get_page_size(self.request)
        total_events = self.page.paginator.count
        total_pages, last_page_count = divmod(total_events, events_per_page)
        last_page_number = total_pages if last_page_count == 0 else total_pages + 1

        return Response(OrderedDict([
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('previous_page_number', current_page -1 if current_page != 1 else None),
            ('current_page_number', current_page),
            ('next_page_number', current_page +
             1 if current_page < last_page_number else None),
            ('count', total_events),
            ('per_page', events_per_page),
            ('results', data),
        ]))
