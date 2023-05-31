from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

def logout_vews(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        logout(request)
        return redirect("login")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(password=password, username=username)
        return redirect('login')
    return render(request, 'register.html')

def login_views(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')

    return render(request, 'login.html',)

def index(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        num_cleaner = Cleaner.objects.count()
        num_helper = Helper.objects.count()
        num_machine = Machine.objects.count()
        context = {
            'earning_infos': Earning_Info.objects.last(),
            'num_cleaner': num_cleaner,
            'num_helper' : num_helper,
            'num_machine' : num_machine
        }
    return render(request, 'import_screen.html', context)

#SPARES
def add_spares(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            kg = request.POST.get('kg')
            status = request.POST.get('status', None)
            spares = Spares.objects.create(
                name = name,
                description = description,
                price = price,
                kg=kg,
                status = status,
            )
            return redirect('spares_list')
        return render(request, 'add-spares.html')


def edit_spares(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Spares.objects.get(id=pk)
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            kg = request.POST.get('kg')
            status = request.POST.get('status', None)
            i.name = name
            i.price = price
            i.description = description
            i.kg = kg
            i.status = status
            i.save()
            return redirect('spares_list')
        return render(request, 'edit-spares.html')

def spares_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            spares = Spares.objects.filter(name__icontains=q)
        else:
            spares = Spares.objects.all()
        context = {
            'spares': spares
        }
        return render(request, 'spares-list.html', context)

def delete_spares(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Spares.objects.get(id=pk).delete()
        return redirect('spares_list')

#FEATURED_PRODUCT
def add_featured_product(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            photo = request.FILES['photo']
            featured_product = Featured_Products.objects.create(
                name = name,
                description = description,
                price = price,
                photo = photo,
            )
            return redirect('featured_product_list')
        return render(request, 'add-featured-product.html')

def edit_featured_product(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Featured_Products.objects.get(id=pk)
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            photo = request.FILES['photo']
            i.name = name
            i.description = description
            i.price = price
            i.photo = photo
            i.save()
            return redirect('featured_product_list')
        return render(request, 'edit-featured-product.html')

def featured_product_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            data = Featured_Products.objects.filter(name__icontains=q)
        else:
            data = Featured_Products.objects.all()
        context = {
            'data': data
        }
        return render(request, 'featured-product-list.html', context)

def delete_featured_product(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Featured_Products.objects.get(id=pk).delete()
        return redirect('featured_product_list')

#HELPERS
def add_helper(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            year = request.POST.get('year')
            paycheck = request.POST.get('paycheck')
            work_time = request.POST.get('work_time')
            task_id = request.POST.get('task')
            helper = Helper.objects.create(
                first_name = first_name,
                last_name = last_name,
                year = year,
                paycheck = paycheck,
                task_id = task_id,
                work_time = work_time,
            )
            return redirect('helper_list')
        return render(request, 'add-helper.html', {'task_id': Helpers_Task.objects.all()})

def edit_helper(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Helper.objects.get(id=pk)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            year = request.POST.get('year')
            paycheck = request.POST.get('paycheck')
            task_id = request.POST.get('task')
            work_time = request.POST.get('work_time')
            i.first_name = first_name
            i.last_name = last_name
            i.year = year
            i.paycheck = paycheck
            i.task_id = task_id
            i.work_time = work_time
            i.save()
            return redirect('helper_list')
        return render(request, 'edit-helper.html', {'task_id': Helpers_Task.objects.all()})

def helper_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            helper = Helper.objects.filter(first_name__icontains=q)
        else:
            helper = Helper.objects.all()
        context = {
            'helper': helper
        }
        return render(request, 'helper-list.html', context)

def delete_helper(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Helper.objects.get(id=pk).delete()
        return redirect('helper_list')

#PARTNER
def add_partner(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            company = request.POST.get('company')
            what_spares = request.POST.get('what_spares')
            partner = Partner.objects.create(
                company = company,
                what_spares = what_spares,
            )
            return redirect('partner_list')
        return render(request, 'add-partner.html')

def edit_partner(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Partner.objects.get(id=pk)
            company = request.POST.get('company')
            what_spares = request.POST.get('what_spares')
            i.company = company
            i.what_spares = what_spares
            i.save()
            return redirect('partner_list')
        return render(request, 'edit-partner.html')

def partner_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            partner = Partner.objects.filter(company__icontains=q)
        else:
            partner = Partner.objects.all()
        context = {
            'partner': partner
        }
        return render(request, 'partner-list.html', context)

def delete_partner(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Partner.objects.get(id=pk).delete()
        return redirect('partner_list')

#INFO
def add_info(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            tel = request.POST.get('tel')
            adress = request.POST.get('adress')
            email = request.POST.get('email')
            logo = request.FILES['logo']
            info = Info.objects.create(
                tel = tel,
                adress = adress,
                email = email,
                logo = logo,
            )
            return redirect('info_list')
        return render(request, 'add-info.html')

def edit_info(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Info.objects.get(id=pk)
            tel = request.POST.get('tel')
            adress = request.POST.get('adress')
            email = request.POST.get('email')
            logo = request.FILES['logo']
            i.tel = tel
            i.adress = adress
            i.email = email
            i.logo = logo
            i.save()
            return redirect('info_list')
        return render(request, 'edit-info.html')

def info_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        
        context = {
            'info': Info.objects.all()
        }
        return render(request, 'info-list.html', context)

def delete_info(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Info.objects.get(id=pk).delete()
        return redirect('info_list')

#DEBT
def add_debt(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            people_name = request.POST.get('people_name')
            a_thing_for_collateral = request.POST.get('a_thing_for_collateral')
            debt_price = request.POST.get('debt_price')
            debt = Debt.objects.create(
                people_name = people_name,
                a_thing_for_collateral = a_thing_for_collateral,
                debt_price = debt_price,
            )
            return redirect('debt_list')
        return render(request, 'add-debt.html')

def edit_debt(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Debt.objects.get(id=pk)
            people_name = request.POST.get('people_name')
            a_thing_for_collateral = request.POST.get('a_thing_for_collateral')
            debt_price = request.POST.get('debt_price')
            i.people_name = people_name
            i.a_thing_for_collateral = a_thing_for_collateral
            i.debt_price = debt_price
            i.save()
            return redirect('debt_list')
        return render(request, 'edit-debt.html')

def debt_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'debt': Debt.objects.all()
        }
        return render(request, 'debt-list.html', context)

def delete_debt(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Debt.objects.get(id=pk).delete()
        return redirect('debt_list')

#Earning Info
def add_earning_info(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            earnings = request.POST.get('earnings')
            info = Earning_Info.objects.create(
                earnings = earnings
            )
            return redirect('earning_list')
        return render(request, 'add-earning-info.html')

def edit_earning_info(request, pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Earning_Info.objects.get(id=pk)
            earnings = request.POST.get('earnings')
            i.earnings = earnings
            i.save()
            return redirect('earning_list')
        return render(request, 'edit-earning.html')

def earning_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'earning_list': Earning_Info.objects.all()
        }
        return render(request, 'earning-list.html', context)

def delete_earning_info(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Earning_Info.objects.get(id=pk).delete()
        return redirect('earning_list')
 
#Machine
def add_machine(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            what_produces = request.POST.get('what_produces')
            price = request.POST.get('price')
            machine = Machine.objects.create(
                what_produces = what_produces,
                price = price,
            )
            return redirect('machine_list')
    return render(request, 'add-machine.html')

def edit_machine(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Machine.objects.get(id=pk)
            what_produces = request.POST.get('what_produces')
            price = request.POST.get('price')
            i.what_produces = what_produces
            i.price = price
            i.save()
            return redirect('machine_list')
        return render(request, 'edit-machine.html')

def machine_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        context = {
            'machine': Machine.objects.all()
        }
        return render(request, 'machine-list.html', context)

def delete_machine(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Machine.objects.get(id=pk).delete()
        return redirect('machine_list')

#The_deliveryman
def add_deliveryman(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            paychek = request.POST.get('paychek')
            the_city_he_goes = request.POST.get('the_city_he_goes')
            work_time = request.POST.get('work_time')
            the_deliveryman = The_deliveryman.objects.create(
                name = name,
                paychek = paychek,
                the_city_he_goes = the_city_he_goes,
                work_time = work_time,
            )
            return redirect('the_deliveryman_list')
        return render(request, 'add-deliveryman.html')

def edit_deliveryman(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = The_deliveryman.objects.get(id=pk)
            name = request.POST.get('name')
            paychek = request.POST.get('paychek')
            the_city_he_goes = request.POST.get('the_city_he_goes')
            work_time = request.POST.get('work_time')
            i.name = name
            i.paychek = paychek
            i.the_city_he_goes = the_city_he_goes
            i.work_time = work_time
            i.save()
            return redirect('the_deliveryman_list')
        return render(request, 'edit-deliveryman.html')

def the_deliveryman_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            the_deliveryman = The_deliveryman.objects.filter(name__icontains=q)
        else:
            the_deliveryman = The_deliveryman.objects.all()
        context = {
            'the_deliveryman_list': the_deliveryman
        }
    return render(request, 'deliveryman-list.html',context)

def delete_deliveryman(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        The_deliveryman.objects.get(id=pk).delete()
        return redirect('the_deliveryman_list')

#Cleaner
def add_cleaner(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            paychek = request.POST.get('paychek')
            cleaning_days = request.POST.get('cleaning_days')
            cleaning_location_id = request.POST.get('cleaning_location')
            cleaner = Cleaner.objects.create(
                name = name,
                paychek = paychek,
                cleaning_days = cleaning_days,
                cleaning_location_id = cleaning_location_id,
            )
            return redirect('cleaner_list')
        return render(request, 'add-cleaner.html', {'cleaning_location_id': Cleaning_location.objects.all()})

def edit_cleaner(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if request.method == 'POST':
            i = Cleaner.objects.get(id=pk)
            name = request.POST.get('name')
            paychek = request.POST.get('paychek')
            cleaning_days = request.POST.get('cleaning_days')
            cleaning_location_id = request.POST.get('cleaning_location')
            i.name = name
            i.paychek = paychek
            i.cleaning_days = cleaning_days
            i.cleaning_location_id = cleaning_location_id
            i.save()
            return redirect('cleaner_list')
        return render(request, 'edit-cleaner.html', {'cleaning_location_id': Cleaning_location.objects.all()})

def cleaner_list(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        if 'q' in request.GET:
            q = request.GET['q']
            cleaner = Cleaner.objects.filter(name__icontains=q)
        else:
            cleaner = Cleaner.objects.all()
        context = {
            'cleaner': cleaner
        }
        return render(request, 'cleaner-list.html', context)

def delete_cleaner(request,pk):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    else:
        Cleaner.objects.get(id=pk).delete()
        return redirect('cleaner_list')





        


