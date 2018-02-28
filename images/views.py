from django.shortcuts import render, redirect
from django.views import View

from .forms import UserForm
from .models import SimpleModel


class UploadFile(View):
    user_form = UserForm

    def post(self, request):
        form = self.user_form(request.POST, request.FILES)
        context = {'form': form}

        if form.is_valid():
            image = request.FILES['image']

            m = SimpleModel(image=image)
            m.save()

            return redirect('successes')

        return render(request, 'image/index.html', context)

    def get(self, request):
        form = self.user_form(None)
        context = {'form': form}

        return render(request, 'image/index.html', context)


def successes(request):
    image = SimpleModel.objects.all()
    context = {'image': image}

    return render(request, 'image/successes.html', context)
