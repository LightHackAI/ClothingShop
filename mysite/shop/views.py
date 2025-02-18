from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from .forms import LoginForm, RegisterForm, CommentForm
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from cart.forms import CartAddProductForm



def login_user(request):
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')

            else:
                context ={'login_form': login_form, 'attention': f'Пользователь с именем {username} не был найден'}

    return render(request, 'shop/login.html', context)


def about(request):
    productabout = ProductAbout.objects.all()
    return render(request, 'shop/about.html', {'productabout': productabout})

def index(request):
    product = Product.objects.all()
    return render(request, 'shop/index.html', {'product': product})


def category(request):
    product = Product.objects.all()
    return render(request, 'shop/category.html', {'product': product})

def logout_user(request):
    logout(request)
    return redirect('login')

def contact(request):
    product = Product.objects.all()
    return render(request, 'shop/contact.html', {'product': product})

def product(request):
    product = Product.objects.all()
    return render(request, 'shop/product.html', {'product': product})

def cart(request):
    product = Product.objects.all()
    return render(request, 'shop/cart.html', {'product': product})

def products(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product.html', {'product': product, 'cart_product_form': cart_product_form})

def checkout(request):
    return render(request, 'shop/checkout.html')

class Register(TemplateView):
    template_name = 'shop/register.html'

    def get(self, request):
        user_add = RegisterForm()
        context = {'user_add': user_add}
        return render(request, 'shop/register.html', context)

    def post(self, request):
        user_add = RegisterForm(request.POST)
        if user_add.is_valid():
            user = user_add.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('index')

        context = {'user_add': user_add}
        return render(request, 'shop/register.html', context)


def category(request):
    product = Product.objects.all()
    return render(request, 'shop/category.html', {'product': product})


def post_detail(request, product_slug):
    post = get_object_or_404(Product, slug=product_slug)
    comments = post.comments.filter()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'shop/comment.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def post_show(request, product_slug):
    post = get_object_or_404(Product, slug=product_slug)
    comments = post.comments.filter()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'shop/showcomment.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def ProductNewForMen(request):
    productnew = Product.objects.all()
    return render(request, 'shop/ProductNewForMen.html', {'productnew': productnew})

def ProductCoatForMen(request):
    productcoat = Product.objects.all()
    return render(request, 'shop/ProductCoatForMen.html', {'productcoat': productcoat})

def ProductSweaterForMen(request):
    productsweater = Product.objects.all()
    return render(request, 'shop/ProductSweaterForMen.html', {'productsweater': productsweater})

def ProductHoodieForMen(request):
    producthoodie = Product.objects.all()
    return render(request, 'shop/ProductHoodieForMen.html', {'producthoodie': producthoodie})

def ProductShirtForMen(request):
    productshirt = Product.objects.all()
    return render(request, 'shop/ProductShirtForMen.html', {'productshirt': productshirt})

def ProductTshirtForMen(request):
    productshirt = Product.objects.all()
    return render(request, 'shop/ProductTshirtForMen.html', {'productshirt': productshirt})

def ProductPantsForMen(request):
    productpants = Product.objects.all()
    return render(request, 'shop/ProductPantsForMen.html', {'productpants': productpants})

def ProductShoesForMen(request):
    productshoes = Product.objects.all()
    return render(request, 'shop/ProductShoesForMen.html', {'productshoes': productshoes})

def ProductNewForWomen(request):
    productnew = Product.objects.all()
    return render(request, 'shop/ProductNewForWomen.html', {'productnew': productnew})

def ProductCoatForWomen(request):
    productcoat = Product.objects.all()
    return render(request, 'shop/ProductCoatForWomen.html', {'productcoat': productcoat})

def ProductBlazerForWomen(request):
    productblazer = Product.objects.all()
    return render(request, 'shop/ProductBlazerForWomen.html', {'productblazer': productblazer})

def ProductDressForWomen(request):
    productdress = Product.objects.all()
    return render(request, 'shop/ProductDressForWomen.html', {'productdress': productdress})

def ProductShirtForWomen(request):
    productshirt = Product.objects.all()
    return render(request, 'shop/ProductShirtForWomen.html', {'productshirt': productshirt})

def ProductTshirtForWomen(request):
    productshirt = Product.objects.all()
    return render(request, 'shop/ProductTshirtForWomen.html', {'productshirt': productshirt})

def ProductSweaterForWomen(request):
    productsweater = Product.objects.all()
    return render(request, 'shop/ProductSweaterForWomen.html', {'productsweater': productsweater})

def ProductPantsForWomen(request):
    productpants = Product.objects.all()
    return render(request, 'shop/ProductPantsForWomen.html', {'productpants': productpants})

def ProductJeansForWomen(request):
    productjeans = Product.objects.all()
    return render(request, 'shop/ProductJeansForWomen.html', {'productjeans': productjeans})

def ProductShoesForWomen(request):
    productshoes = Product.objects.all()
    return render(request, 'shop/ProductShoesForWomen.html', {'productshoes': productshoes})

def ProductJewerlyForMen(request):
    productjewerly = Product.objects.all()
    return render(request, 'shop/ProductJewerlyForMen.html', {'productjewerly': productjewerly})

def ProductJewerlyForWomen(request):
    productjewerly = Product.objects.all()
    return render(request, 'shop/ProductJewerlyForWomen.html', {'productjewerly': productjewerly})

def ProductWatchForMen(request):
    productwatch = Product.objects.all()
    return render(request, 'shop/ProductWatchForMen.html', {'productwatch': productwatch})

def ProductWatchForWomen(request):
    productwatch = Product.objects.all()
    return render(request, 'shop/ProductWatchForWomen.html', {'productwatch': productwatch})

def AlexanderMcQueen(request):
    alexandermcqueen = Product.objects.all()
    return render(request, 'shop/AlexanderMcQueen.html', {'alexandermcqueen': alexandermcqueen})

def Balenciaga(request):
    balenciaga = Product.objects.all()
    return render(request, 'shop/Balenciaga.html', {'balenciaga': balenciaga})

def Moncler(request):
    moncler = Product.objects.all()
    return render(request, 'shop/Moncler.html', {'moncler': moncler})

def OffWhite(request):
    offwhite = Product.objects.all()
    return render(request, 'shop/OffWhite.html', {'offwhite': offwhite})

def Valentino(request):
    valentino = Product.objects.all()
    return render(request, 'shop/Valentino.html', {'valentino': valentino})

def ProductMen(request):
    productmen = Product.objects.all()
    return render(request, 'shop/ProductMen.html', {'productmen': productmen})

def ProductWomen(request):
    productwomen = Product.objects.all()
    return render(request, 'shop/ProductWomen.html', {'productwomen': productwomen})

def ProductSneakersForMen(request):
    productsneakers = Product.objects.all()
    return render(request, 'shop/ProductSneakersForMen.html', {'productsneakers': productsneakers})

def ProductSneakersForWomen(request):
    productsneakers = Product.objects.all()
    return render(request, 'shop/ProductSneakersForWomen.html', {'productsneakers': productsneakers})

def Chopard(request):
    chopard = Product.objects.all()
    return render(request, 'shop/Chopard.html', {'chopard': chopard})

def deGRISOGONO(request):
    degrisogono = Product.objects.all()
    return render(request, 'shop/deGRISOGONO.html', {'degrisogono': degrisogono})

def GirardPerregaux(request):
    girardperregaux = Product.objects.all()
    return render(request, 'shop/GirardPerregaux.html', {'girardperregaux': girardperregaux})

def Hublot(request):
    hublot = Product.objects.all()
    return render(request, 'shop/Hublot.html', {'hublot': hublot})

def Breitling(request):
    breitling = Product.objects.all()
    return render(request, 'shop/Breitling.html', {'breitling': breitling})

def TAGHeuer(request):
    tagheuer = Product.objects.all()
    return render(request, 'shop/TAGHeuer.html', {'tagheuer': tagheuer})

def Tudor(request):
    tudor = Product.objects.all()
    return render(request, 'shop/Tudor.html', {'tudor': tudor})

def Chanel(request):
    chanel = Product.objects.all()
    return render(request, 'shop/Chanel.html', {'chanel': chanel})


def news(request):
    news = News.objects.all()
    return render(request, 'shop/news.html', {'news': news})

class SearchResultsView(ListView):

    model = Product
    template_name = 'shop/ProductSearch.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  Product.objects.filter(Q(title__icontains=query))
        return object_list


