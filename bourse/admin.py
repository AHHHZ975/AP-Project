from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(company)
admin.site.register(timePeriod)

## Consolidated Balance Sheet (Tarazname) ##


admin.site.register(balanceSheet)
admin.site.register(assets)
admin.site.register(debtsAndAssetsOwner)
admin.site.register(currentAssets)
admin.site.register(nonCurrentAssets)
admin.site.register(currentDebts)
admin.site.register(nonCurrentDebts)
admin.site.register(ownerInvestment)

## Income Statement (sood o zian) ##

admin.site.register(incomeStatement) #Narenji rang ha
admin.site.register(profitOrLoss)
admin.site.register(basicEarningsLossPerShare)
admin.site.register(dilutedEarningsOrLossPerShare)
admin.site.register(statementOfIncomeAndRetainedEarnings)

## Cash Flow (jaryan vojooh naghd) ##

admin.site.register(cashFlow) #Narenji rang ha
admin.site.register(cashFlowsFromUsedInOperatingActivities)
admin.site.register(investmentReturnsAndPaymentsOnFinancingCosts)
admin.site.register(cashFlowsUsedInIncomeTax)
admin.site.register(cashFlowsFromUsedInInvestingActivities)
admin.site.register(cashFlowsFromUsedInFinancingActivities)
