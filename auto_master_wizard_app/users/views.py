import os
import uuid

import boto3
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import mixins


from auto_master_wizard_app.users.serializers import UserSerializer, UserProfileSerializer


class UsersViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    # you will get here only if the user is already authenticated!
    user_serializer = UserProfileSerializer(instance=request.user, many=False)
    return Response(data=user_serializer.data)


@api_view(['POST'])
def google_login(request):
    google_jwt = request.data['google_jwt']
    CLIENT_ID = '350644933433-e7fjnb3gfukr75ftd33pmn3t8obf35h9.apps.googleusercontent.com'
    try:
        idinfo = id_token.verify_oauth2_token(google_jwt, requests.Request(), CLIENT_ID)
        email = idinfo['email']
        try:
            user = User.objects.get(email=email)
            print('user found')
            print(user)
        except User.DoesNotExist:
            print('does not exist')
            user = User.objects.create_user(username=email, email=email, password=str(uuid.uuid4()),
                                            first_name=idinfo['given_name'], last_name=idinfo['family_name'])
        refresh = RefreshToken.for_user(user)
        return Response(data={
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    except ValueError as e:
        print(e)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_img_url(request):
    bucket_name = "auto-mater-wizard-profiles"
    filename = request.data['filename']
    _, ext = os.path.splitext(filename)
    object_name = f"profile_img_{request.user.id}_{uuid.uuid4()}{ext}"
    try:
        s3 = boto3.client('s3')
        response = s3.generate_presigned_post(bucket_name, object_name, ExpiresIn=3600)
        print(response)
        # request.user.profile.img_url = f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        # request.user.profile.save()
    except Exception:
        return Response(status=500)

    return Response(data=response)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_img(request):
    bucket_name = "auto-mater-wizard-profiles"
    file_stream = request.FILES['file'].file
    _, ext = os.path.splitext(request.FILES['file'].name)
    object_name = f"profile_img_{request.user.id}{ext}"
    try:
        s3 = boto3.client('s3')
        s3.upload_fileobj(file_stream, bucket_name, object_name)
        request.user.profile.img_url = f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        request.user.profile.save()
    except Exception:
        return Response(status=500)

    return Response()




