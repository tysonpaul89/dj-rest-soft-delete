from rest_framework import status, viewsets
from rest_framework.response import Response


from .models import Country
from .serializers import CountrySerializer

class CountryViewset(viewsets.ModelViewSet):
    """Viewset to perform CRUD operation on the Country model.

    create: To create a country.

    list: Lists all the countires.

    retrieve: To get a country data.

    update: To update all country data fields.

    partial_update: To update one or more country data fields.

    destroy: To delete a country.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def destroy(self, request, *args, **kwargs):
        """Method 1: Override destroy method of the ModelViewSet"""
        country = self.get_object()
        country.deleted = True
        country.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def perform_destroy(self, instance):
    #     """Method 2: Override perform_destroy method of the ModelViewSet
    #     https://www.django-rest-framework.org/api-guide/generic-views/#methods
    #     """
    #     instance.deleted = True
    #     instance.save()