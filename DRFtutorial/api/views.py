from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from .models import Student 
from .serializers import StudentSerialzer
from  rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        # print("request body : ", request.body)
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)

        print("stream : ",stream);
        python_data = JSONParser().parse(stream)
        print("python_data : ", python_data)
        id = python_data.get('id',None)
        print("id : ",id)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerialzer(stu)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerialzer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
        
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerialzer(data = python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': "Record successfully added to the database"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerialzer(data = python_data)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerialzer(stu,data = python_data,partial = True)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "Record successfully updated in the database"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        
    if request.method == 'DELETE': 
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerialzer(data = python_data)
        id = python_data.get('id')
        
        stu = Student.objects.get(id = id)
        stu.delete()
        
        res = {'msg': "Record successfully deleted from the database"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
        
        
        


