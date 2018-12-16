from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.http.response import JsonResponse
from django.core.exceptions import ValidationError

from api.models import User
from .common_view import CommonView

import json


class SignUpView(CommonView):

    def create(self, request):
        try:
            data = json.loads(request.body)
        except:
            # JSONの読み込みに失敗
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        user = User.objects
        username = data['username']
        if user.filter(username=username).exists():
            return JsonResponse({'message': 'Duplicate entry username'}, status=400)

        email = data['email']
        if user.filter(email=email).exists():
            return JsonResponse({'message': 'Duplicate entry email'}, status=400)

        try:
            password = data['password']
            validate_password(password)
            data['password'] = make_password(password)
            user = User.objects.create(**data)
            result = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'profile': user.profile,
            }
            return JsonResponse(result, status=201)

        except ValidationError as e:
            return JsonResponse({'message': e.messages[0]}, status=403)
