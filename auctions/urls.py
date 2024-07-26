from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="create"),
    path("listing/<int:id>", views.listingViewById, name="listing"),
    path("categories", views.categoriesView, name="categories"),
    path("categories/<str:category>", views.categoryView, name="category"),
    path("watchlist", views.watchlistWiew, name="watchlist")
]
