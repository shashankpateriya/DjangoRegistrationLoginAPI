from django.http import JsonResponse
import jwt
from rest_framework.views import APIView
from notes.serializers import NotesSerializer
from django.db import IntegrityError
from notes.models import Notes

class NotesRegister(APIView):
    """
    register a note by serializing data with rest framework using CRUD operations
    return: notes data
    """
    def post(self, request):
        try:
            serializer = NotesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                notedata = serializer.data
                success_message = {"message" : "Notes saved",
                "data" : notedata}
                return JsonResponse(success_message)
            else:
                return JsonResponse(serializer.errors)
        except IntegrityError as e:
            return JsonResponse(e.__cause__)
        except TypeError:
            return JsonResponse("Invalid data")
    
    def get(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            decoded = jwt.decode(token, 'secret', algorithms=["HS256"])
            notes = Notes.objects.filter(user_id=decoded['id'])
            print(notes)
            if notes is not None:
                serializer = NotesSerializer(notes, many=True)
                notesdata = {
                    "message" : "Notes for user",
                    "data" : serializer.data
                }
                return JsonResponse(notesdata, safe=False) 
            else:
                return JsonResponse("User is not present")
        except IntegrityError as e:
            return JsonResponse(e.__cause__)
        except TypeError:
            return JsonResponse("Invalid data")

    def put(self, request):
        try:
            notes = Notes.objects.get(id=request.data.get("id"))
            serializer = NotesSerializer(notes, data=request.data)
            if serializer.is_valid():
                serializer.save()
                updatednote = {
                    "message" : "Note has been updated",
                    "data" : serializer.data
                }
                return JsonResponse(updatednote, safe=False)
            else:
                return JsonResponse(serializer.errors, status=400)
        except TypeError:
            return JsonResponse("Invalid data")

    def delete(self, request):
        try:
            notes = Notes.objects.filter(id=request.data.get("id"))
            if notes is not None:
                notes.delete()
                delete_message = {"message": "Note deleted"},
                return JsonResponse(delete_message, safe=False)
        except TypeError:
            return JsonResponse("Invalid data")