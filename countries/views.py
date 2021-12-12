from rest_framework import viewsets

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
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer