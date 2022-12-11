from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypeSerializer
from .models import SuperType


@api_view(['GET'])
def type_list(request):
    type = SuperType.objects.all()
    serializer = SuperTypeSerializer(type, many=True)


    return Response(serializer.data)
