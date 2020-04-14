from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 1
#     max_page_size = 1
#     page_size_query_param = 'size'
#     page_query_param = 'page'
#
#     '''
#     age_query_param：表示url中的页码参数
# 		page_size_query_param：表示url中每页数量参数
# 		page_size：表示每页的默认显示数量
# 		max_page_size：表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
#     '''


# class MyPageNumberPagination(LimitOffsetPagination):
#     default_limit = 1
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'
#     max_limit = 1
#
#     '''
#     default_limit：表示默认每页显示几条数据
# 		limit_query_param：表示url中本页需要显示数量参数
# 		offset_query_param：表示从数据库中的第几条数据开始显示参数
# 		max_limit：表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
#     '''


class MyPageNumberPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 1
    ordering = 'id'
    page_size_query_param = 'size'
    max_page_size = 1

    '''
    cursor_query_param：表示url中页码的参数
		page_size_query_param：表示每页显示数据量的参数
		max_page_size：表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
		ordering：表示返回数据的排序方式
    '''
