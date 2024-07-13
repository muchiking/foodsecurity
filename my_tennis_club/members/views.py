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

def isnull_or_empty(value):
    return value is None or value == "" or value == [] or value == {}

def product(request):
  data=""
  county=""
  product=""
  # print(request.GET.get('product').count())
  county = (request.GET.get('county'))
  product = (request.GET.get('product'))


    # Check and process 'county'
  if isnull_or_empty(county):
      county = None
  else:
      county = county.capitalize()

  # Check and process 'product'
  if isnull_or_empty(product):
      product = None
  else:
      product = product.capitalize()


  # print(product)
  if product != None and county != None:
    data=managedb.get_products_county_and_location(product="product",county=county,prodname=product)
  elif  product != None :
    print(product)
    data=managedb.get_products_prodname(product="product",prodname=product)
  elif county != None:
    data=managedb.get_products_county(product="product",county=county)
  else:
    data=managedb.get_products("product")
  
  template = loader.get_template('products.html') 
  # Keys for the dictionaries
  keys = ['id', 'product_name', 'product_details', 'expiry_date', 'vendor', 'location','phone','town','image']

  products = [dict(zip(keys, values)) for values in data]
  context = {
    'products': products,
  }

  return HttpResponse(template.render(context, request))

def farmequipment(request):
  template = loader.get_template('farmequipment.html')
  # data=managedb.get_products("farmequipment")
  data=""
  county=""
  product=""
  # print(request.GET.get('product').count())
  county = (request.GET.get('county'))
  product = (request.GET.get('product'))


    # Check and process 'county'
  if isnull_or_empty(county):
      county = None
  else:
      county = county.capitalize()

  # Check and process 'product'
  if isnull_or_empty(product):
      product = None
  else:
      product = product.capitalize()


  # print(product)
  if product != None and county != None:
    data=managedb.get_products_county_and_location(product="farmequipment",county=county,prodname=product)
  elif  product != None :
    # print(product)
    data=managedb.get_products_prodname(product="farmequipment",prodname=product)
  elif county != None:
    data=managedb.get_products_county(product="farmequipment",county=county)
  else:
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
  # data=managedb.get_products("farm_animal")

  data=""
  county=""
  product=""
  # print(request.GET.get('product').count())
  county = (request.GET.get('county'))
  product = (request.GET.get('product'))


    # Check and process 'county'
  if isnull_or_empty(county):
      county = None
  else:
      county = county.capitalize()

  # Check and process 'product'
  if isnull_or_empty(product):
      product = None
  else:
      product = product.capitalize()


  # print(product)
  if product != None and county != None:
    data=managedb.get_products_county_and_location(product="farm_animal",county=county,prodname=product)
  elif  product != None :
    print(product)
    data=managedb.get_products_prodname(product="farm_animal",prodname=product)
  elif county != None:
    data=managedb.get_products_county(product="farm_animal",county=county)
  else:
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
