from .forms import LungForm
from django.shortcuts import render
from .utils import predict
from django.conf import settings
import os
import pyrebase

# Create your views here.

config = {
    "apiKey": "AIzaSyDZUcBGyaOZE-E_X52JNty8cc__mEEUoXw",
    "authDomain": "lifesaver-ca4a8.firebaseapp.com",
    "projectId": "lifesaver-ca4a8",
    "storageBucket": "lifesaver-ca4a8.appspot.com",
    "messagingSenderId": "1028288490018",
    "appId": "1:1028288490018:web:9fb999f91b98dceaa2f87b",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


def model_form_upload(request):
    if request.method == 'POST':
        form = LungForm(request.POST, request.FILES)
        fileName = request.FILES['input_image'].name
        if form.is_valid():
            form.save()
            mes = predict(os.path.join(settings.INPUT_IMG_ROOT, fileName))
            storage.child(
                "input_image/"+fileName).put(os.path.join(settings.INPUT_IMG_ROOT, fileName))
            plt = mes[1]
            fileName = fileName.split('.')
            fileName = fileName[0] + '.jpg'
            output_url = os.path.join(settings.OUTPUT_IMG_ROOT, fileName)
            plt.savefig(output_url)
            storage.child("output_image/"+fileName).put(output_url)

            return render(request, 'result.html', {
                'fileName': storage.child("output_image/"+fileName).get_url(token=None),
                'message': mes[0]
            })
    else:
        form = LungForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
