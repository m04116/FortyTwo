from django.shortcuts import render
from django.http import JsonResponse
from .models import UserInformation, Request

def info(request):
    user = UserInformation.objects.get(id=1)
    request_list_all = Request.objects.all()
    new_requests_nmb = request_list_all.filter(is_viewed=False)

    if new_requests_nmb:
        new_nmb = request_list_all.filter(is_viewed=False).count()

    context = {'user': user,
               'new_requests': new_nmb}
    return render(request, 'user_info/user_data.html', context)
    
def requests(request):
    request_list_all = Request.objects.all()
    new_requests_nmb = request_list_all.filter(is_viewed=False).count()
    for req in request_list_all:
        req.is_viewed=True
        req.save()
    request_list = Request.objects.all()[:10]
    
    context = {'request_list': request_list,
               'new_requests': new_requests_nmb}

    return render (request, 'user_info/requests.html', context)

def check_requests(request):
    if request.method == 'GET':
        return_dict = dict()
        request_list_all = Request.objects.all()
        new_requests_nmb = request_list_all.filter(is_viewed=False).count()
        if new_requests_nmb:
            return_dict['new_requests_nmb'] = new_requests_nmb
            
        return JsonResponse(return_dict)

def edit_form(request):
    user = UserInformation.objects.get(id=1)
    return render (request, 'user_info/user_form.html', {'user': user})
