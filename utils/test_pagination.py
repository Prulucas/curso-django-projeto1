from unittest import TestCase
from utils.pagination import make_pagination_range, make_pagination
from django.test import RequestFactory


class PaginationTest(TestCase):
    def setUp(self):
        # Instancia o gerador de requisições
        self.rf = RequestFactory()
        self.queryset = [1, 2, 3, 4, 5, 6]

    def test_make_pagination_range_returns_a_pagination_range(self):  # noqa: E501
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_then_middle_page(self):  # noqa: E501
        # Current page = 1 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # Current page = 2 - Qty Page = 2 - Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # Current page = 3 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

    def test_make_sure_middle_ranges_are_correct(self):
        # Current page = 10 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        # Current page = 12 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=12,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):  # noqa: E501
        # Current page = 18 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Current page = 19 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Current page = 20 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # Current page = 21 - Qty Page = 2 - Middle Page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

    def test_make_pagination_returns_page_two(self):
        request = self.rf.get('/?page=2')

        page_obj, pagination_range = make_pagination(
            request,
            self.queryset,
            per_page=2
        )

        self.assertEqual(page_obj.number, 2)
        self.assertEqual(len(page_obj.object_list), 2)
        self.assertEqual(pagination_range['current_page'], 2)

    def test_make_pagination_falls_back_to_page_one_if_page_is_invalid(self):
        request = self.rf.get('/?page=abc')

        page_obj, pagination_range = make_pagination(
            request,
            self.queryset,
            per_page=2
        )

        self.assertEqual(page_obj.number, 1)
        self.assertEqual(pagination_range['current_page'], 1)


""" # noqa: E501
Test no teminal
python -m pytest utils/test_pagination.py -v
"""
