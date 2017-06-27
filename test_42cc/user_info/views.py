from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UserInformation, Request

def info(request):

    if request.user.is_authenticated():
                return redirect('edit_form')

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
    if request.method == 'POST':

        name = request.POST['name']
        last_name = request.POST['last_name']
        birth_date = request.POST['birth_date']
        photo = request.POST['photo']
        email = request.POST['email']
        jabber = request.POST['jabber']
        skype = request.POST['skype']
        other_contacts = request.POST['other_contacts']
        bio = request.POST['bio']

        print('start')
        print(name)
        print(last_name)
        print(birth_date)
        print(photo)
        print(email)
        print(jabber)
        print(skype)
        print(other_contacts)
        print(bio)
        print('request.POST:')
        print(request.POST)
        print('end')


    return render (request, 'user_info/user_form.html', {'user': user})
