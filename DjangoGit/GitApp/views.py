from django.shortcuts import render,HttpResponse
import requests

# Create your views here.

def profile(request):
	my_json=[]
	if request.method == 'POST':
    	username = request.POST.get('user')
		req = requests.get('https://api.github.com/users/'+ username)
		my_json.append(json.loads(req.content))
		parsedData=[]
		UserData={}
		for data in my_json:
			userData['name']=data['name']
			userData['blog'] = data['blog']
        	userData['email'] = data['email']
        	userData['public_gists'] = data['public_gists']
        	userData['public_repos'] = data['public_repos']
        	userData['avatar_url'] = data['avatar_url']
        	userData['followers'] = data['followers']
        	userData['following'] = data['following']

    	parsedData.append(userData)
    return render(request, 'app/profile.html',{'data':parsedData})

	