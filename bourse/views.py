from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import forms
from . import models

# Create your views here

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def company(request):
    form = forms.company
    contents = {'form': form}
    return render(request, "form.html", context=contents)

def assetsFromDB(request):
    assetsList = models.assets.objects.all()
    content = {'assets': assetsList}
    return render(request, "assets.html", context=content)

def balanceSheetsFromDB(request):
    balanceSheetsList = models.balanceSheet.objects.all()
    content = {'balanceSheets': balanceSheetsList}
    return render(request, "balanceSheets.html", context=content)

def debtsAndAssetsOwnersFromDB(request):
    debtsAndAssetsOwnersList = models.debtsAndAssetsOwner.objects.all()
    content = {'debtsAndAssetsOwners': debtsAndAssetsOwnersList}
    return render(request, "debtsAndAssetsOwners.html", context=content)

def currentAssetsFromDB(request):
    currentAssetsList = models.currentAssets.objects.all()
    content = {'currentAssets': currentAssetsList}
    return render(request, "currentAssets.html", context=content)

def nonCurrentAssetsFromDB(request):
    nonCurrentAssetsList = models.nonCurrentAssets.objects.all()
    content = {'nonCurrentAssets': nonCurrentAssetsList}
    return render(request, "nonCurrentAssets.html", context=content)

def currentDebtsFromDB(request):
    currentDebtsList = models.currentDebts.objects.all()
    content = {'currentDebts': currentDebtsList}
    return render(request, "currentDebts.html", context=content)

def nonCurrentDebtsFromDB(request):
    nonCurrentDebtsList = models.nonCurrentDebts.objects.all()
    content = {'nonCurrentDebts': nonCurrentDebtsList}
    return render(request, "nonCurrentDebts.html", context=content)


def ownerInvestmentsFromDB(request):
    ownerInvestmentsList = models.ownerInvestment.objects.all()
    content = {'ownerInvestments': ownerInvestmentsList}
    return render(request, "ownerInvestments.html", context=content)

def incomeStatementsFromDB(request):
    incomeStatementsList = models.incomeStatement.objects.all()
    content = {'incomeStatements': incomeStatementsList}
    return render(request, "incomeStatements.html", context=content)

def profitOrLossesFromDB(request):
    profitOrLossesList = models.profitOrLoss.objects.all()
    content = {'profitOrLosses': profitOrLossesList}
    return render(request, "profitOrLosses.html", context=content)

def basicEarningsLossPerSharesFromDB(request):
    basicEarningsLossPerSharesList = models.basicEarningsLossPerShare.objects.all()
    content = {'basicEarningsLossPerShares': basicEarningsLossPerSharesList}
    return render(request, "basicEarningsLossPerShares.html", context=content)

def dilutedEarningsOrLossPerSharesFromDB(request):
    dilutedEarningsOrLossPerSharesList = models.dilutedEarningsOrLossPerShare.objects.all()
    content = {'dilutedEarningsOrLossPerShares': dilutedEarningsOrLossPerSharesList}
    return render(request, "dilutedEarningsOrLossPerShares.html", context=content)

def statementOfIncomeAndRetainedEarningsFromDB(request):
    statementOfIncomeAndRetainedEarningsList = models.statementOfIncomeAndRetainedEarnings.objects.all()
    content = {'statementOfIncomeAndRetainedEarnings': statementOfIncomeAndRetainedEarningsList}
    return render(request, "statementOfIncomeAndRetainedEarnings.html", context=content)

def cashFlowsFromDB(request):
    cashFlowsList = models.cashFlow.objects.all()
    content = {'cashFlows': cashFlowsList}
    return render(request, "cashFlows.html", context=content)

def cashFlowsFromUsedInOperatingActivitiesFromDB(request):
    cashFlowsFromUsedInOperatingActivitiesList = models.cashFlowsFromUsedInOperatingActivities.objects.all()
    content = {'cashFlowsFromUsedInOperatingActivities': cashFlowsFromUsedInOperatingActivitiesList}
    return render(request, "cashFlowsFromUsedInOperatingActivities.html", context=content)

def investmentReturnsAndPaymentsOnFinancingCostsFromDB(request):
    investmentReturnsAndPaymentsOnFinancingCostsList = models.investmentReturnsAndPaymentsOnFinancingCosts.objects.all()
    content = {'investmentReturnsAndPaymentsOnFinancingCosts': investmentReturnsAndPaymentsOnFinancingCostsList}
    return render(request, "investmentReturnsAndPaymentsOnFinancingCosts.html", context=content)

def cashFlowsUsedInIncomeTaxesFromDB(request):
    cashFlowsUsedInIncomeTaxesList = models.cashFlowsUsedInIncomeTax.objects.all()
    content = {'cashFlowsUsedInIncomeTaxes': cashFlowsUsedInIncomeTaxesList}
    return render(request, "cashFlowsUsedInIncomeTaxes.html", context=content)

def cashFlowsFromUsedInInvestingActivitiesFromDB(request):
    cashFlowsFromUsedInInvestingActivitiesList = models.cashFlowsFromUsedInInvestingActivities.objects.all()
    content = {'cashFlowsFromUsedInInvestingActivities': cashFlowsFromUsedInInvestingActivitiesList}
    return render(request, "cashFlowsFromUsedInInvestingActivities.html", context=content)


def cashFlowsFromUsedInFinancingActivitiesFromDB(request):
    cashFlowsFromUsedInFinancingActivitiesList = models.cashFlowsFromUsedInFinancingActivities.objects.all()
    content = {'cashFlowsFromUsedInFinancingActivities' : cashFlowsFromUsedInFinancingActivitiesList}
    return render(request, "cashFlowsFromUsedInFinancingActivities.html", context=content)






















def financialReportsFromDB(request):
    componies = models.company.objects.all()
    # for company in componies:
    financialReports = models.assets.objects.filter(company__name='Khefoola').order_by('balanceSheet__company__name')
    content = {'financialReports': financialReports}
    return render(request, "financialReports.html", context=content)
