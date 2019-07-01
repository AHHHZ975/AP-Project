from django.contrib import admin
from .models import *

# Register your models here.

## Consolidated Balance Sheet (Tarazname) ##

admin.site.register(FinancialStatements)
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

# #### bank #### #
admin.site.register(balanceSheet_bank)
admin.site.register(assets_bank)
admin.site.register(debts_bank)
admin.site.register(ownerInvestment_bank)

admin.site.register(incomeStatement_bank)
admin.site.register(jointRevenue_bank)
admin.site.register(nonJointRevenue_bank)

admin.site.register(expenseByNature_bank)
admin.site.register(basicEarningsPerShare_bank)
admin.site.register(dilutedEarningsPerShare_bank)
admin.site.register(statementOfIncomeAndRetainedEarnings_bank)

admin.site.register(cashFlow_bank)
admin.site.register(cashFlowsFromUsedInOperatingActivities_bank)
admin.site.register(investmentReturnsAndPaymentsOnFinancingCosts_bank)
admin.site.register(cashFlowsFromUsedInInvestingActivities_bank)

