from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product
import random

# Create your views here.
def home(request):
	products = Product.objects
	items = Product.objects.all()
	random_item = random.choice(items)
	return render(request, 'product/home.html', {'products': products, 'random_item': random_item})

def all(request):
	data=[]
	products = Product.objects.all().values_list('title','tag','hunter','votes_total')
	for i in products:
		title=i[0]
		tag=i[1]
		hunter=i[2]
		votes_total=i[3]
		name=User.objects.filter(id=int(hunter)).values_list('username')
		for i in name:
			name1=i[0]
		data.append(title,tag,name1,votes_total)
		#data.append([btn,"<a href='/edit_product/"+str(product_id)+"' class='btn'><i class='fas fa-edit'></i> Edit</a>"])
		#data=[1,2]
	return render(request, 'product/all.html', {'products': products, 'data': data,})

@login_required(login_url='/account/signup')
def create(request):
	if request.method=='POST':
		if request.POST['title'] and request.POST['tag'] and request.POST['summary'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
			product = Product()
			product.title = request.POST['title']
			product.tag = request.POST['tag']
			product.summary = request.POST['summary']
			product.body = request.POST['body']
			if request.POST['url'].startswith('https://'):
				product.url = request.POST['url']
			else:
				product.url = 'https://' + request.POST['url']
			product.image = request.FILES['image']
			product.icon = request.FILES['icon']
			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect('/product/' + str(product.id))

		else:
			return render(request, 'product/create.html', {'error': 'All fields are required!'})
	return render(request, 'product/create.html')

def detail(request, product_id):
	product = get_object_or_404(Product, pk = product_id)
	return render(request, 'product/detail.html', {'product': product})

@login_required(login_url='/account/signup')
def upvote(request, product_id):
	if request.method=='POST':
		product = get_object_or_404(Product, pk = product_id)
		product.votes_total = product.votes_total + 1
		product.save()
		return redirect('/product/' + str(product.id))