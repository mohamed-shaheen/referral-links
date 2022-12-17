from django.shortcuts import render
from profiles.models import Profile



def main_view(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
    except:
        pass

    print(request.session.get_expiry_age())    

    return render(request, 'main.html', {})