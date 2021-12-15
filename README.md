# Django REST Framework - Soft Delete

This is an example project to show how to soft delete model in using rest_framework.viewsets.ModelViewSet

``` bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py runserver
```

## Solution:

``` python
class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def destroy(self, request, *args, **kwargs):
        """Method 1: Override destroy method of the ModelViewSet"""
        country = self.get_object()
        country.deleted = True
        country.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """Method 2: Override perform_destroy method of the ModelViewSet
        https://www.django-rest-framework.org/api-guide/generic-views/#methods
        """
        instance.deleted = True
        instance.save()

```