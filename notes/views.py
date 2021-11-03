from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from notes.serializers import NotesSerializer
from django.db import IntegrityError
from notes.models import Notes
from notes.utility import verify_token
from userlogin.models import UserRegistration

class NotesRegister(APIView):
    """
    register a note by serializing data with rest framework using CRUD operations
    verifying user token before giving the access
    return: user notes data
    """

    @verify_token
    def post(self, request):
        """
        adding a note to user
        """
        try:
            serializer = NotesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
            {
                "message": "Notes added successfully",
                "data": {"notelist": serializer.data},
            },
        )
            else:
                return JsonResponse(serializer.errors)
        except IntegrityError as e:
            return JsonResponse(str(e))
        except ValidationError:
            return Response(
                {
                    "message": "User not validated",
                    "data": {"note": serializer.errors},
                })
        except Exception as e:
            return Response(str(e))

    @verify_token
    def get(self, request):
        """
        get the user notes data
        """
        try:
            note = Notes.objects.filter(user_id=request.data.get('user_id'))
            if note.exists():
                serializer = NotesSerializer(note, many=True)
                return Response(
                    {
                        "message": "Welcome to our notes",
                        "data": {"notes": serializer.data},
                    }
                )
            else:
                return JsonResponse("User is not present")
        except IntegrityError as e:
            return JsonResponse(e.__cause__)
        except ValidationError:
            return Response(
                {
                    "message": "User not validated",
                    "data": {"note": serializer.errors},
                })
        except Exception as e:
            return Response(str(e))

    @verify_token
    def put(self, request):
        """
        update a existing note of a user
        """
        try:
            usernote = Notes.objects.get(id=request.data.get("id"))
            serializer = NotesSerializer(usernote, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                {
                    "message": "Notes updated successfully",
                    "data": {"note": serializer.data},
                }
            )
            else:
                return JsonResponse(serializer.errors, status=400)
        except TypeError:
            return JsonResponse("Invalid data")
        except ValidationError:
            return Response(
                {
                    "message": "User not validated",
                    "data": {"note": serializer.errors},
                })
        except Exception as e:
            return Response(str(e))

    @verify_token
    def delete(self, request):
        """
        delete a note
        """
        try:
            usernote = Notes.objects.get(id=request.data.get("id"))
            usernote.delete()
            return Response(
                {
                    "message": "Note deleted successfully",
                    "data": {},
                })
        except TypeError:
            return JsonResponse("Invalid data")
        except Exception as e:
            return Response(str(e))