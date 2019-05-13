from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    url('form', views.company, name='form'),
    url('assets', views.assetsFromDB, name='assetsFromDB'),
    url('balanceSheets', views.balanceSheetsFromDB, name='balanceSheetsFromDB'),
    url('basicEarningsLossPerShares', views.basicEarningsLossPerSharesFromDB, name='basicEarningsLossPerSharesFromDB'),
    url('cashFlows', views.cashFlowsFromDB, name='cashFlowsFromDB'),
    url('cashFlowsFromUsedInFinancingActivities', views.cashFlowsFromUsedInFinancingActivitiesFromDB, name='cashFlowsFromUsedInFinancingActivitiesFromDB'),
    url('cashFlowsFromUsedInInvestingActivities', views.cashFlowsFromUsedInInvestingActivitiesFromDB, name='cashFlowsFromUsedInInvestingActivitiesFromDB'),
    url('cashFlowsFromUsedInOperatingActivities', views.cashFlowsFromUsedInOperatingActivitiesFromDB, name='cashFlowsFromUsedInOperatingActivitiesFromDB'),
    url('cashFlowsUsedInIncomeTaxes', views.cashFlowsUsedInIncomeTaxesFromDB, name='cashFlowsUsedInIncomeTaxesFromDB'),
    url('currentAssets', views.currentAssetsFromDB, name='currentAssetsFromDB'),
    url('currentDebts', views.currentDebtsFromDB, name='currentDebtsFromDB'),
    url('debtsAndAssetsOwners', views.debtsAndAssetsOwnersFromDB, name='debtsAndAssetsOwnersFromDB'),
    url('dilutedEarningsOrLossPerShares', views.dilutedEarningsOrLossPerSharesFromDB, name='dilutedEarningsOrLossPerSharesFromDB'),
    url('incomeStatements', views.incomeStatementsFromDB, name='incomeStatementsFromDB'),
    url('investmentReturnsAndPaymentsOnFinancingCosts', views.investmentReturnsAndPaymentsOnFinancingCostsFromDB, name='investmentReturnsAndPaymentsOnFinancingCostsFromDB'),
    url('nonCurrentAssets', views.nonCurrentAssetsFromDB, name='nonCurrentAssetsFromDB'),
    url('nonCurrentDebts', views.nonCurrentDebtsFromDB, name='nonCurrentDebtsFromDB'),
    url('ownerInvestments', views.ownerInvestmentsFromDB, name='ownerInvestmentsFromDB'),
    url('profitOrLosses', views.profitOrLossesFromDB, name='profitOrLossesFromDB'),
    url('statementOfIncomeAndRetainedEarnings', views.statementOfIncomeAndRetainedEarningsFromDB, name='statementOfIncomeAndRetainedEarningsFromDB'),
    url('financialReports', views.financialReportsFromDB, name='financialReports')
]
