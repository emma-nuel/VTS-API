from api.models import MyVehicle, VehicleSwitch
from api.serializers import MyVehicleSerializer, ImmobilisationSwitchSerializer
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class VehicleList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        vehicles = MyVehicle.objects.all()
        serializer = MyVehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MyVehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetCurrentVehicleDetails(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        vehicle = MyVehicle.objects.last()
        serializer = MyVehicleSerializer(vehicle)
        return JsonResponse(serializer.data)

    def post(self, request, format=None):
        serializer = MyVehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleState(APIView):
    def get(self, request, format=None):
        switch_state = VehicleSwitch.objects.last()
        serializer = ImmobilisationSwitchSerializer(switch_state)
        return JsonResponse(serializer.data)   

    def post(self, request, format=None):
        serializer = ImmobilisationSwitchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)