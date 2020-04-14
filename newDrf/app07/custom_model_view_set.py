from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView
from .custom_json_response import JSONResponse


class ListModelMixin(object):
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            print(page)
            serializer = self.get_serializer(page, many=True)
            print('我走到这里了')
            return JSONResponse(data=serializer.data, msg='success', status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        return JSONResponse(data=serializer.data, msg='success', status=status.HTTP_200_OK)


class CreateModelMixin(object):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class ListModelMixin(ListModelMixin,
                     CreateModelMixin,
                     GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
