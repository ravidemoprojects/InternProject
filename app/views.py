from django.shortcuts import render
from .forms import ImageForm
from .models import Image,Category
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    if request.method =='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    
    #Pagination with or without orphans for 8 images in 1 page
    img = None
    categories = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        img = Image.get_all_images_by_category_id(categoryID)
    else:
        img = Image.objects.all().order_by('id')
    paginator = Paginator(img, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/home.html', {'form':form,'page_obj':page_obj,'categories':categories})
