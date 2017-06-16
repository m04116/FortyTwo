from django.shortcuts import render
from .models import UserInformation

def info(request):
    # user = UserInformation.objects.get(id=1)
    # context = {'user': user}
    # return render(request, 'user_info/user_data.html', context)
    return render(request, 'user_info/user_data.html')
