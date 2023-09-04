from django.shortcuts import render


def home(requests):
    return render (requests, 'home.html')

def inner_page(requests):
    return render(requests, 'inner-page.html')

def portfolio_details(requests):
    return render(requests, 'portfolio-details.html')