from rest_framework import viewsets
from rest_framework import permissions
{%for n in cookiecutter.models.name %}
from .models import {{n}}
from .serializers import {{n}}Serializer
{% endfor %}


{%for n in cookiecutter.models.name %}
class {{n}}ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = {{n}}.objects.all()
    serializer_class = {{n}}Serializer
    # permission_classes = [permissions.IsAuthenticated]
{% endfor %}


