from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


# def customer_list(request):
#     customer = Customer.objects.filter(created_date__lte=timezone.now())
#     return render(request, 'portfolio/customer_list.html',
#                   {'customers': customer})
#
#
# def customer_edit(request, pk):
#     customer = get_object_or_404(Customer, pk=pk)
#     if request.method == "POST":
#         # update
#         form = CustomerForm(request.POST, instance=customer)
#         if form.is_valid():
#             customer = form.save(commit=False)
#             customer.updated_date = timezone.now()
#             customer.save()
#             customer = Customer.objects.filter(created_date__lte=timezone.now())
#             return render(request, 'portfolio/customer_list.html',
#                           {'customers': customer})
#     else:
#         # edit
#         form = CustomerForm(instance=customer)
#     return render(request, 'portfolio/customer_edit.html', {'form': form})
#
#
# def customer_delete(request, pk):
#     customer = get_object_or_404(Customer, pk=pk)
#     customer.delete()
#     return redirect('portfolio:customer_list')
#

now = timezone.now()


def home(request):
    return render(request, 'portfolio/home.html',
                  {'portfolio': home})


@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/customer_list.html',
                  {'customers': customer})

@user_passes_test(lambda user: user.is_superuser or user.is_FinancialAdvisor)
@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'portfolio/customer_list.html',
                          {'customers': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'portfolio/customer_edit.html', {'form': form})

@user_passes_test(lambda user: user.is_superuser or user.is_FinancialAdvisor)
@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('portfolio:customer_list')


@login_required
def stock_list(request):
    stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
    return render(request, 'portfolio/stock_list.html', {'stocks': stocks})

@user_passes_test(lambda user: user.is_superuser or user.is_FinancialAdvisor)
@login_required
def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_date = timezone.now()
            stock.save()
            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'portfolio/stock_list.html',
                          {'stocks': stocks})
    else:
        form = StockForm()
        # print("Else")
    return render(request, 'portfolio/stock_new.html', {'form': form})

@user_passes_test(lambda user: user.is_superuser or user.is_FinancialAdvisor)
@login_required
def stock_edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save()
            # stock.customer = stock.id
            stock.updated_date = timezone.now()
            stock.save()
            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
            return render(request, 'portfolio/stock_list.html', {'stocks': stocks})
    else:
        # print("else")
        form = StockForm(instance=stock)
    return render(request, 'portfolio/stock_edit.html', {'form': form})

@user_passes_test(lambda user: user.is_superuser or user.is_FinancialAdvisor)
@login_required
def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    stock.delete()
    return redirect('/stock_list/')


@login_required
def investment_list(request):
    investment = Investment.objects.all()
    return render(request, 'portfolio/investment_list.html', {'investment': investment})


@user_passes_test(lambda user: user.is_superuser or user.is_FinancialAdvisor)
@login_required
def investment_edit(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            investmentform = form.save(commit=False)
            investmentform.save()
            messages.success(request, f'Your Customer has been updated')
            return redirect('/investment_list/')

    else:
        # edit
        investmentform = InvestmentForm(instance=investment)
        return render(request, 'portfolio/investment_edit.html', {'investmentform': investmentform})


@user_passes_test(lambda user: user.is_superuser or user.is_FinancialAdvisor)
@login_required
def investment_new(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investmentform = form.save(commit=False)
            investmentform.created_date = timezone.now()
            investmentform.save()
            messages.success(request, f'Your New Board has been updated')
            return redirect('/investment_list/')

    else:
        # edit
        investmentform = InvestmentForm()
        return render(request, 'portfolio/investment_new.html', {'investmentform': investmentform})


@user_passes_test(lambda user: user.is_superuser or user.is_FinancialAdvisor)
@login_required
def investment_delete(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    investment.delete()
    return redirect('/investment_list/')
