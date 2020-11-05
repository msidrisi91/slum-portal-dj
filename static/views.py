from django.shortcuts import render, redirect
import subprocess

def index(request):
    return redirect('/home/0')

def home(request, pk):
    return render(request,'index.html',{'is_auth' : pk})

def event(request, pk):
    return render(request,'events.html',{'is_auth' : pk}) # auth == 1 mean user is authenticated

def register(request):
    return render(request,'signup.html',{})

def login(request):
    return render(request,'login.html',{})

def post_issue(request):
    return render(request,'post.html',{})

def review(request):
    return render(request,'review.html',{})

def map(request, pk):
    return render(request,'map.html',{'is_auth' : pk})

def mapop(request, id, pk):
    return render(request,'mappo.html',{'is_auth' : pk, 'map_id' : id})

# delhi=0, mumbai=1, chennai=2, kolkata=3
def upload(img):
    with open('/media/shaheem/Data/Projects/PycharmProjects/djangoProject/slum-segmentation/slums/test_images/img.jpg', 'wb+') as destination:
        for chunk in img.chunks():
            destination.write(chunk)
    subprocess.run(['python', '/media/shaheem/Data/Projects/PycharmProjects/djangoProject/slum-segmentation/a.py'])

def segmentation(request):
    print(request.FILES['upload'])
    upload(request.FILES['upload'])

    return redirect('/stat/results/pred.jpg')

