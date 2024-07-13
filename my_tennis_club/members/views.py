from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import Member
import members.managedb as managedb

# "{% static 'my_app/example.jpg' %}"

def home(request):
  template = loader.get_template('home.html')
  # print("hi")
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  # print("hi")
  return HttpResponse(template.render())


def members1(request):
    d=managedb.get_products("product")
    print(d)
    return HttpResponse("Hello world!")

def product(request):
  data=managedb.get_products("product")
  template = loader.get_template('products.html') 
  # Keys for the dictionaries
  keys = ['id', 'product_name', 'product_details', 'expiry_date', 'vendor', 'location','phone','town','image']

  products = [dict(zip(keys, values)) for values in data]

  # # Initialize the list of dictionaries
  # products = []

  # # Loop through the data and create dictionaries
  # for values in data:
  #     product = {}
  #     for key, value in zip(keys, values):
  #         product[key] = value
  #     products.append(product)
  context = {
    'products': products,
  }

  return HttpResponse(template.render(context, request))

def farmequipment(request):
  template = loader.get_template('farmequipment.html')
  data=managedb.get_products("farmequipment")
  keys = ['id', 'name', 'county', 'location', 'vendor','phone','image','details']
  products = [dict(zip(keys, values)) for values in data]
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))

  

def farmanimals(request):
  template = loader.get_template('farmanimals.html')
  # Animal Name county location vendor phone
  data=managedb.get_products("farm_animal")
  keys = ['Animal_name', 'County', 'Location', 'vendor','phone','id','image','details']
  products = [dict(zip(keys, values)) for values in data]
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))
    



def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def memberslist(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
