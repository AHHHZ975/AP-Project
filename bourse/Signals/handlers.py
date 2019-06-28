from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from ..models import *


####################### Update Balance sheet ##################################
@receiver(post_save, sender=assets)
def update_balanceSheet_sumOfAssets(**kwargs):
    assetObject = kwargs['instance']
    balanceSheets = balanceSheet.objects.filter(relatedTo=assetObject.relatedTo)
    for balancesheetObject in balanceSheets:
        balancesheetObject.sumOfAssets =  balancesheetObject.sumOfAssets\
                                          + assetObject.sumOfCurrentAssets\
                                          + assetObject.sumOfNonCurrentAssets
        balancesheetObject.save()


@receiver(post_save, sender=debtsAndAssetsOwner)
def update_balanceSheet_sumOfDebtsAndFundsOwner_byDebtsAndAssetsOwner(**kwargs):
    debtsAndAssetsOwnerObject = kwargs['instance']
    balanceSheets = balanceSheet.objects.filter(relatedTo=debtsAndAssetsOwnerObject.relatedTo)
    for balancesheetObject in balanceSheets:
        balancesheetObject.sumOfDebtsAndFundsOwner =  balancesheetObject.sumOfDebtsAndFundsOwner\
                                                      + debtsAndAssetsOwnerObject.sumOfCurrentDebts \
                                                      + debtsAndAssetsOwnerObject.sumOfNonCurrentDebts
        balancesheetObject.save()

@receiver(post_save, sender=ownerInvestment)
def update_balanceSheet_sumOfDebtsAndFundsOwner_byOwnerInvestment(**kwargs):
    ownerInvestmentObject = kwargs['instance']
    balanceSheets = balanceSheet.objects.filter(relatedTo=ownerInvestmentObject.relatedTo)
    for balancesheetObject in balanceSheets:
        balancesheetObject.sumOfDebtsAndFundsOwner =  balancesheetObject.sumOfDebtsAndFundsOwner\
                                                      + ownerInvestmentObject.sumOfOwnersInvestments
        balancesheetObject.save()

############################## Update Assets ###################################
@receiver(post_save, sender=currentAssets)
def update_assets_sumOfCurrentAssets(**kwargs):
    currentAssetsObject = kwargs['instance']
    assetsObjects = assets.objects.filter(relatedTo=currentAssetsObject.relatedTo)
    for assetsObject in assetsObjects:
        assetsObject.sumOfCurrentAssets = assetsObject.sumOfCurrentAssets + \
                                          currentAssetsObject.cash + \
                                          currentAssetsObject.salableAssets + \
                                          currentAssetsObject.shortTermInvestments + \
                                          currentAssetsObject.commercialInputs + \
                                          currentAssetsObject.noncommercialInputs + \
                                          currentAssetsObject.inventory + \
                                          currentAssetsObject.prepaidExpenses

        assetsObject.save()


@receiver(post_save, sender=nonCurrentAssets)
def update_assets_sumOfNonCurrentAssets(**kwargs):
    nonCurrentAssetsObject = kwargs['instance']
    assetsObjects = assets.objects.filter(relatedTo=nonCurrentAssetsObject.relatedTo)
    for assetsObject in assetsObjects:
        assetsObject.sumOfNonCurrentAssets = assetsObject.sumOfNonCurrentAssets + \
                                             nonCurrentAssetsObject.longTermInvestments + \
                                             nonCurrentAssetsObject.longTermInputs + \
                                             nonCurrentAssetsObject.investmentInEstate + \
                                             nonCurrentAssetsObject.intangibleAssets + \
                                             nonCurrentAssetsObject.tangibleAssets + \
                                             nonCurrentAssetsObject.otherAssets


        assetsObject.save()

########################## Update debtsAndAssetsOwner #############################
@receiver(post_save, sender=currentDebts)
def update_debtsAndAssetsOwner_sumOfCurrentDebts(**kwargs):
    currentDebtsObject = kwargs['instance']
    debtsAndAssetsOwnerObjects = debtsAndAssetsOwner.objects.filter(relatedTo=currentDebtsObject.relatedTo)
    for debtsAndAssetsOwnerObject in debtsAndAssetsOwnerObjects:
        debtsAndAssetsOwnerObject.sumOfCurrentDebts = debtsAndAssetsOwnerObject.sumOfCurrentDebts + \
                                                      currentDebtsObject.commercialPayable + \
                                                      currentDebtsObject.NonCommercialPayable + \
                                                      currentDebtsObject.payableTaxes + \
                                                      currentDebtsObject.payableDividends + \
                                                      currentDebtsObject.financialFacility + \
                                                      currentDebtsObject.resources + \
                                                      currentDebtsObject.currentPreReceivables + \
                                                      currentDebtsObject.debtsRelatedWithSalableAssets

        debtsAndAssetsOwnerObject.save()


@receiver(post_save, sender=nonCurrentDebts)
def update_debtsAndAssetsOwner_sumOfNonCurrentDebts(**kwargs):
    nonCurrentDebtsObject = kwargs['instance']
    debtsAndAssetsOwnerObjects = debtsAndAssetsOwner.objects.filter(relatedTo=nonCurrentDebtsObject.relatedTo)
    for debtsAndAssetsOwnerObject in debtsAndAssetsOwnerObjects:
        debtsAndAssetsOwnerObject.sumOfNonCurrentDebts = debtsAndAssetsOwnerObject.sumOfNonCurrentDebts + \
                                                      nonCurrentDebtsObject.longTermPayable + \
                                                      nonCurrentDebtsObject.nonCurrentPreReceivables + \
                                                      nonCurrentDebtsObject.longTermFinancialFacility + \
                                                      nonCurrentDebtsObject.storeOfWorkersEndServiceAdvantages


        debtsAndAssetsOwnerObject.save()


@receiver(post_save, sender=ownerInvestment)
def update_debtsAndAssetsOwner_sumOfOwnersInvestments(**kwargs):
    ownerInvestmentObject = kwargs['instance']
    debtsAndAssetsOwnerObjects = debtsAndAssetsOwner.objects.filter(relatedTo=ownerInvestmentObject.relatedTo)
    for debtsAndAssetsOwnerObject in debtsAndAssetsOwnerObjects:
        debtsAndAssetsOwnerObject.sumOfOwnersInvestments = debtsAndAssetsOwnerObject.sumOfOwnersInvestments + \
                                                           ownerInvestmentObject.assets + \
                                                           ownerInvestmentObject.increaseORDecreaseOfInProcessAssets + \
                                                           ownerInvestmentObject.stockSpends + \
                                                           ownerInvestmentObject.treasuryStocks + \
                                                           ownerInvestmentObject.legalSavings + \
                                                           ownerInvestmentObject.otherSavings + \
                                                           ownerInvestmentObject.RevaluationSurplusOfHeldForSaleAssets + \
                                                           ownerInvestmentObject.RevaluationSurplusOfAssets + \
                                                           ownerInvestmentObject.DifferenceInTheConvergenceDueToConversionToReportingCurrency + \
                                                           ownerInvestmentObject.ValuationAssetsOfAssetsAndLiabilitiesOfStateOwnedEnterprises + \
                                                           ownerInvestmentObject.accumulatedProfitORLosses
        debtsAndAssetsOwnerObject.save()

################################## Update cashFlow ###########################
@receiver(post_save, sender=cashFlowsFromUsedInFinancingActivities)
def update_cashFlow_cashAtEndOfPeriod_byCashFlowsFromUsedInFinancingActivities(**kwargs):
    cashFlowsFromUsedInFinancingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowsFromUsedInFinancingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.cashAtEndOfPeriod = cashFlowObject.cashAtEndOfPeriod + \
                                           cashFlowsFromUsedInFinancingActivities.cashAtBeginningOfPeriod
        cashFlowObject.save()

# @receiver(post_save, sender=cashFlow)
# def update_cashFlow_cashAtEndOfPeriod_byCashFlow(**kwargs):
#     cashFlowPrimeObject = kwargs['instance']
#     cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowPrimeObject.relatedTo)
#     for cashFlowObject in cashFlowObjects:
#         cashFlowObject.cashAtEndOfPeriod = cashFlowObject.cashAtEndOfPeriod + \
#                                            cashFlowPrimeObject.netIncreaseDecreaseInCash
#         cashFlowObject.save()
#

# @receiver(post_save, sender=cashFlow)
# def update_cashFlow_netIncreaseDecreaseInCash(**kwargs):
#     cashFlowPrimeObject = kwargs['instance']
#     cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowPrimeObject.relatedTo)
#     for cashFlowObject in cashFlowObjects:
#         cashFlowObject.netIncreaseDecreaseInCash = cashFlowObject.netIncreaseDecreaseInCash + \
#                                                    cashFlowPrimeObject.netCashFlowsFromUsedInFinancingActivities + \
#                                                    cashFlowPrimeObject.netCashFlowsFromUsedInBeforeFinancingActivities
#         cashFlowObject.save()

@receiver(post_save, sender=cashFlowsFromUsedInFinancingActivities)
def update_cashFlow_netCashFlowsFromUsedInFinancingActivities(**kwargs):
    cashFlowsFromUsedInFinancingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowsFromUsedInFinancingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netCashFlowsFromUsedInFinancingActivities = cashFlowObject.netCashFlowsFromUsedInFinancingActivities + \
                                                                   cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromIssuingShares + \
                                                                   cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromSalesOrIssueOfTreasuryShares + \
                                                                   cashFlowsFromUsedInFinancingActivitiesObject.paymentsForPurchaseOfTreasuryShares + \
                                                                   cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromBorrowingsClassifiedAsFinancingActivities + \
                                                                   cashFlowsFromUsedInFinancingActivitiesObject.repaymentsOfBorrowingsClassifiedAsFinancingActivities
        cashFlowObject.save()


# @receiver(post_save, sender=cashFlow)
# def update_cashFlow_netCashFlowsFromUsedInBeforeFinancingActivities(**kwargs):
#     cashFlowPrimeObject = kwargs['instance']
#     cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowPrimeObject.relatedTo)
#     for cashFlowObject in cashFlowObjects:
#         cashFlowObject.netCashFlowsFromUsedInBeforeFinancingActivities  = cashFlowObject.netCashFlowsFromUsedInBeforeFinancingActivities  + \
#                                                                           cashFlowPrimeObject.netCashFlowsFromUsedInInvestingActivities + \
#                                                                           cashFlowPrimeObject.netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts + \
#                                                                           cashFlowPrimeObject.netCashFlowsFromUsedInOperatingActivities
#         cashFlowObject.save()


@receiver(post_save, sender=cashFlowsFromUsedInInvestingActivities)
def update_cashFlow_netCashFlowsFromUsedInInvestingActivities(**kwargs):
    cashFlowsFromUsedInInvestingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowsFromUsedInInvestingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netCashFlowsFromUsedInInvestingActivities = cashFlowObject.netCashFlowsFromUsedInInvestingActivities + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.proceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.purchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.proceedsFromSalesOfIntangibleAssetsClassifiedAsInvestingActivities + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.purchaseOfOnTangibleAssetsClassifiedAsInvestingActivities + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.proceedsFromSalesOfNonCurrentInvestments + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.facilitiesGrantedToIndividuals + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.extraditionFacilitiesGrantedToIndividuals + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.purchaseOfNonCurrentInvestments + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.proceedsFromSalesOfCurrentInvestments + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.purchaseOfCurrentInvestments + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.proceedsFromSalesOfInvestmentProperty + \
                                                                   cashFlowsFromUsedInInvestingActivitiesObject.purchaseOfInvestmentProperty
        cashFlowObject.save()


@receiver(post_save, sender=investmentReturnsAndPaymentsOnFinancingCosts)
def update_cashFlow_netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts(**kwargs):
    netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts = cashFlowObject.netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts + \
                                                                   netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.dividendsReceived + \
                                                                   netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.interestPaidOrBorrowing + \
                                                                   netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.interestReceivedFromOtherInvestments + \
                                                                   netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.dividendsPaid
        cashFlowObject.save()



@receiver(post_save, sender=cashFlowsFromUsedInOperatingActivities)
def update_cashFlow_netCashFlowsFromUsedInOperatingActivities(**kwargs):
    netCashFlowsFromUsedInOperatingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=netCashFlowsFromUsedInOperatingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netCashFlowsFromUsedInOperatingActivities = cashFlowObject.netCashFlowsFromUsedInOperatingActivities + \
                                                                   netCashFlowsFromUsedInOperatingActivitiesObject.netCashFlowsFromUsedInOperatingActivitiesOrdinary  + \
                                                                   netCashFlowsFromUsedInOperatingActivitiesObject.netCashFlowsFromUsedInOperatingActivitiesExceptional
        cashFlowObject.save()
