from django.http.response import HttpResponse


def hello_world(request):
    name = request.GET.get('name', 'Unknown user')
    age = request.GET.get('age', 'Unknown age')
    return HttpResponse('Hello {0}! {0} is {1}'.format(name, age))
