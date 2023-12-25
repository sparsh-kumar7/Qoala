from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from django.http import JsonResponse

from .utils import extract_dates_and_english_text
from .models import OCRResult
from .serializers import OCRResultSerializer
from rest_framework import status

@api_view(['POST'])
def ocr_endpoint(request):
    image_path = request.FILES['image'].temporary_file_path()
    results = extract_dates_and_english_text(image_path)
    serializer = OCRResultSerializer(data=results)
    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data)

    
@api_view(['GET'])
def getData(request):
    app = OCRResult.objects.all()
    serializer = OCRResultSerializer(app, many=True)
    return Response(serializer.data)

def index(request):
    return render(request, 'homepage.html')


@api_view(['DELETE'])
def delete_result(request, pk):
	result = get_object_or_404(OCRResult, pk=pk)
	result.delete()
	return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def update_result(request, pk):
    result = get_object_or_404(OCRResult, pk=pk)
    print(result)
    data = OCRResultSerializer(instance=result, data=request.data)
    print(data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    
@api_view(['GET'])
def get_result(request, pk):
    app = OCRResult.objects.all()
    app = app.filter(identification_number=pk)
    serializer = OCRResultSerializer(app, many=True)
    return Response(serializer.data)