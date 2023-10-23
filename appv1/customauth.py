from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

class StaticPasswordAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        password = request.META.get('HTTP_X_PASSWORD')

        if not username or not password:
            return None

        # Replace 'your_static_username' and 'your_static_password' with the desired static credentials
        if username == 'abhinay' and password == 'dalchawal@1':
            return (None, None)  # Authentication succeeded

        raise AuthenticationFailed('Static authentication failed')