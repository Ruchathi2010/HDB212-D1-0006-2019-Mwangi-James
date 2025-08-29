from django.http import JsonResponse

def test_api(request):
    """
    Simple API endpoint to test frontend-backend connection.
    Returns a JSON response.
    """
    data = {
        "message": "Backend is working! Connection successful."
    }
    return JsonResponse(data)
