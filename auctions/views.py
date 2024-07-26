from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

from .models import User


def index(request):
    listing = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listing": listing
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def createListing(request):
    categories = Category.objects.all()

    if request.method == "POST":
        titleListing = request.POST["title"]
        descriptionListing = request.POST["description"]
        categoryListing = request.POST["category"]
        initalBid = request.POST["bid"]
        url = request.POST["imageUrl"]
        authorId = request.user

        categoryId = int(categoryListing)
        getCategory = Category.objects.get(pk=categoryId)

        newListing = Listing(title = titleListing, description = descriptionListing, imageUrl = url, bid = initalBid, category_id = categoryListing, author_id = authorId.id)
        newListing.save()

        return HttpResponseRedirect(reverse("index"))


    return render(request, "auctions/create.html", {
        "categories": categories
    })

def listingViewById(request, id):
    getListing = Listing.objects.get(id=id)
    getCategory = Category.objects.get(id=getListing.category_id)
    getUser = request.user
    
    if request.user.is_authenticated:
        pageInList = Watchlist.objects.filter(id_user = getUser, id_listing = getListing).first
    
        if pageInList is None:
            watchlist = Watchlist(id_user = getUser, id_listing = getListing)
            watchlist.save()
 
    return render(request, "auctions/listing.html", {
        "listing": getListing,
        "category": getCategory
    })

def categoriesView(request):
    getAllCategories = Category.objects.all()

    return render(request, "auctions/categories.html", {
        "categories": getAllCategories
    })

def categoryView(request, category):
    getCategorySelected = Category.objects.get(name = category)
    getAllListingWhitCategory = Listing.objects.filter(category_id = getCategorySelected)

    return render(request, "auctions/category.html", {
        "category": getAllListingWhitCategory
    })

def watchlistWiew(request):
    getUserLogead = request.user
    getAllItemsWachedForUser = Watchlist.objects.all().filter(id_user = getUserLogead)

    return render(request, "auctions/watchlist.html", {
        "watchlist": getAllItemsWachedForUser
    })