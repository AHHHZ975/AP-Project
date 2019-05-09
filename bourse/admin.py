from django.contrib import admin
from .models import *

# Register your models here.


## Consolidated Balance Sheet (Tarazname) ##

admin.site.register(Company)
admin.site.register(BalanceSheet)
admin.site.register(Assets)
admin.site.register(DebtsAndAssetsOwner)
admin.site.register(CurrentAssets)
admin.site.register(NonCurrentAssets)
admin.site.register(CurrentDebts)
admin.site.register(NonCurrentDebts)
admin.site.register(OwnerInvestment)

## Income Statement (sood o zian) ##

admin.site.register(IncomeStatement) #Narenji rang ha
admin.site.register(ProfitOrLoss)
admin.site.register(BasicEarningsLossPerShare)
admin.site.register(DilutedEarningsOrLossPerShare)
admin.site.register(StatementOfIncomeAndRetainedEarnings)

## Cash Flow (jaryan vojooh naghd) ##

admin.site.register(CashFlow) #Narenji rang ha
admin.site.register(CashFlowsFromUsedInOperatingActivities)
admin.site.register(InvestmentReturnsAndPaymentsOnFinancingCosts)
admin.site.register(CashFlowsUsedInIncomeTax)
admin.site.register(CashFlowsFromUsedInInvestingActivities)
admin.site.register(CashFlowsFromUsedInFinancingActivities)
