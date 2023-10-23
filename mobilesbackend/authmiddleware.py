# custom_middleware.py

from django.http import JsonResponse


class RequireHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for the presence of required headers
        username = request.META.get('HTTP_X_USERNAME')
        password = request.META.get('HTTP_X_PASSWORD')

        if username is None or password is None:
            response_data = {'error': 'Missing required headers: X-Username and X-Password'}
            return JsonResponse(response_data, status=400)

        response = self.get_response(request)
        return response
