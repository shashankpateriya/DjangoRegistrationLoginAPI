from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
import jwt
from django.db import IntegrityError
from userlogin.models import UserRegistration

def verify_token(function):
        """
        verify user token to provide access
        """
        def wrapper(self, request):
            try:
                if 'HTTP_AUTHORIZATION' not in request.META:
                    resp = JsonResponse({'message': 'Token not provided in the header'})
                    resp.status_code = 400
                    return resp
                token = request.META.get('HTTP_AUTHORIZATION')
                decoded = jwt.decode(token, 'secret', algorithms=["HS256"])
                request.data["user_id"] = decoded.get('user_id')
                user = UserRegistration.objects.get(id=request.data.get('user_id'))
                if user == None:
                    resp = JsonResponse({'message': 'User not found'})
                    resp.status_code = 400
                    return resp
                return function(self, request)
            except IntegrityError as e:
                return JsonResponse(str(e))
            except Exception as e:
                return Response(str(e)) 
        return wrapper