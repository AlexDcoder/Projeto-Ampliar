from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Psychologist
from .serializer import PsychologistSerializer

@api_view(['GET'])
def getPsychologistList(request):
    """
    Retrieve a list of all psychologists.
    """
    psychologists = Psychologist.objects.all()
    serializer = PsychologistSerializer(psychologists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPyschologistById(request, pk):
    """
    Retrieve a psychologist by their ID.
    """
    try:
        psychologist = Psychologist.objects.get(id=pk)
    except Psychologist.DoesNotExist:
        return Response({'error': 'Psychologist not found'}, status=404)

    serializer = PsychologistSerializer(psychologist)
    return Response(serializer.data)

@api_view(['POST'])
def createPyschologist(request):
    """
    Create a new psychologist.
    """
    serializer = PsychologistSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updatePsychologist(request, pk):
    """
    Update an existing psychologist.
    """
    try:
        psychologist = Psychologist.objects.get(id=pk)
    except Psychologist.DoesNotExist:
        return Response({'error': 'Psychologist not found'}, status=404)

    serializer = PsychologistSerializer(psychologist, data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deletePsychologist(request, pk):
    """
    Delete a psychologist by their ID.
    """
    try:
        psychologist = Psychologist.objects.get(id=pk)
        psychologist.delete()
        return Response({'message': 'Psychologist deleted successfully'}, status=204)
    except Psychologist.DoesNotExist:
        return Response({'error': 'Psychologist not found'}, status=404)