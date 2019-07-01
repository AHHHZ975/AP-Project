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
                                                      + debtsAndAssetsOwnerObject.sumOfNonCurrentDebts + \
                                                        debtsAndAssetsOwnerObject.sumOfOwnersInvestments
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
                                           cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromIssuingShares + \
                                           cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromSalesOrIssueOfTreasuryShares + \
                                           cashFlowsFromUsedInFinancingActivitiesObject.paymentsForPurchaseOfTreasuryShares + \
                                           cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromBorrowingsClassifiedAsFinancingActivities + \
                                           cashFlowsFromUsedInFinancingActivitiesObject.repaymentsOfBorrowingsClassifiedAsFinancingActivities + \
                                           cashFlowsFromUsedInFinancingActivitiesObject.cashAtBeginningOfPeriod
        cashFlowObject.save()


@receiver(post_save, sender=cashFlowsFromUsedInInvestingActivities)
def update_cashFlow_cashAtEndOfPeriod_byCashFlowsFromUsedInInvestingActivities(**kwargs):
    cashFlowsFromUsedInInvestingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowsFromUsedInInvestingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.cashAtEndOfPeriod = cashFlowObject.cashAtEndOfPeriod + \
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
def update_cashFlow_cashAtEndOfPeriod_byInvestmentReturnsAndPaymentsOnFinancingCosts(**kwargs):
    netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.cashAtEndOfPeriod = cashFlowObject.cashAtEndOfPeriod + \
                                           netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.dividendsReceived + \
                                           netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.interestPaidOrBorrowing + \
                                           netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.interestReceivedFromOtherInvestments + \
                                           netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.dividendsPaid
        cashFlowObject.save()


@receiver(post_save, sender=cashFlowsFromUsedInOperatingActivities)
def update_cashFlow_cashAtEndOfPeriod_byCashFlowsFromUsedInOperatingActivities(**kwargs):
    netCashFlowsFromUsedInOperatingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=netCashFlowsFromUsedInOperatingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.cashAtEndOfPeriod = cashFlowObject.cashAtEndOfPeriod + \
                                           netCashFlowsFromUsedInOperatingActivitiesObject.netCashFlowsFromUsedInOperatingActivitiesOrdinary  + \
                                           netCashFlowsFromUsedInOperatingActivitiesObject.netCashFlowsFromUsedInOperatingActivitiesExceptional
        cashFlowObject.save()



















@receiver(post_save, sender=cashFlowsFromUsedInFinancingActivities)
def update_cashFlow_netIncreaseDecreaseInCash_byCashFlowsFromUsedInFinancingActivities(**kwargs):
    cashFlowsFromUsedInFinancingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowsFromUsedInFinancingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netIncreaseDecreaseInCash = cashFlowObject.netIncreaseDecreaseInCash + \
                                                   cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromIssuingShares + \
                                                   cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromSalesOrIssueOfTreasuryShares + \
                                                   cashFlowsFromUsedInFinancingActivitiesObject.paymentsForPurchaseOfTreasuryShares + \
                                                   cashFlowsFromUsedInFinancingActivitiesObject.proceedsFromBorrowingsClassifiedAsFinancingActivities + \
                                                   cashFlowsFromUsedInFinancingActivitiesObject.repaymentsOfBorrowingsClassifiedAsFinancingActivities
        cashFlowObject.save()


@receiver(post_save, sender=cashFlowsFromUsedInInvestingActivities)
def update_cashFlow_netIncreaseDecreaseInCash_byCashFlowsFromUsedInInvestingActivities(**kwargs):
    cashFlowsFromUsedInInvestingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowsFromUsedInInvestingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netIncreaseDecreaseInCash = cashFlowObject.netIncreaseDecreaseInCash + \
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
def update_cashFlow_netIncreaseDecreaseInCash_byInvestmentReturnsAndPaymentsOnFinancingCosts(**kwargs):
    netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netIncreaseDecreaseInCash = cashFlowObject.netIncreaseDecreaseInCash + \
                                                   netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.dividendsReceived + \
                                                   netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.interestPaidOrBorrowing + \
                                                   netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.interestReceivedFromOtherInvestments + \
                                                   netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.dividendsPaid
        cashFlowObject.save()


@receiver(post_save, sender=cashFlowsFromUsedInOperatingActivities)
def update_cashFlow_netIncreaseDecreaseInCash_byCashFlowsFromUsedInOperatingActivities(**kwargs):
    netCashFlowsFromUsedInOperatingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=netCashFlowsFromUsedInOperatingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netIncreaseDecreaseInCash = cashFlowObject.netIncreaseDecreaseInCash + \
                                                   netCashFlowsFromUsedInOperatingActivitiesObject.netCashFlowsFromUsedInOperatingActivitiesOrdinary  + \
                                                   netCashFlowsFromUsedInOperatingActivitiesObject.netCashFlowsFromUsedInOperatingActivitiesExceptional
        cashFlowObject.save()











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









@receiver(post_save, sender=cashFlowsFromUsedInInvestingActivities)
def update_cashFlow_netCashFlowsFromUsedInBeforeFinancingActivities_byCashFlowsFromUsedInInvestingActivities(**kwargs):
    cashFlowsFromUsedInInvestingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=cashFlowsFromUsedInInvestingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netCashFlowsFromUsedInBeforeFinancingActivities = cashFlowObject.netCashFlowsFromUsedInBeforeFinancingActivities + \
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
def update_cashFlow_netCashFlowsFromUsedInBeforeFinancingActivities_byInvestmentReturnsAndPaymentsOnFinancingCosts(**kwargs):
    netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netCashFlowsFromUsedInBeforeFinancingActivities = cashFlowObject.netCashFlowsFromUsedInBeforeFinancingActivities + \
                                                                         netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.dividendsReceived + \
                                                                         netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.interestPaidOrBorrowing + \
                                                                         netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.interestReceivedFromOtherInvestments + \
                                                                         netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCostsObject.dividendsPaid
        cashFlowObject.save()


@receiver(post_save, sender=cashFlowsFromUsedInOperatingActivities)
def update_cashFlow_netCashFlowsFromUsedInBeforeFinancingActivities_byCashFlowsFromUsedInOperatingActivities(**kwargs):
    netCashFlowsFromUsedInOperatingActivitiesObject = kwargs['instance']
    cashFlowObjects = cashFlow.objects.filter(relatedTo=netCashFlowsFromUsedInOperatingActivitiesObject.relatedTo)
    for cashFlowObject in cashFlowObjects:
        cashFlowObject.netCashFlowsFromUsedInBeforeFinancingActivities = cashFlowObject.netCashFlowsFromUsedInBeforeFinancingActivities + \
                                                                         netCashFlowsFromUsedInOperatingActivitiesObject.netCashFlowsFromUsedInOperatingActivitiesOrdinary  + \
                                                                         netCashFlowsFromUsedInOperatingActivitiesObject.netCashFlowsFromUsedInOperatingActivitiesExceptional
        cashFlowObject.save()













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

########################### Update incomeStatement ####################

@receiver(post_save, sender=profitOrLoss)
def update_incomeStatement_grossProfit(**kwargs):
    profitOrLossObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=profitOrLossObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.grossProfit = incomeStatementObject.grossProfit + \
                                             profitOrLossObject.operationIncomes + \
                                             profitOrLossObject.costOfOperationIncomes
        incomeStatementObject.save()


@receiver(post_save, sender=profitOrLoss)
def update_incomeStatement_profitOrLossFromOperatingActivities(**kwargs):
    profitOrLossObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=profitOrLossObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.profitOrLossFromOperatingActivities = incomeStatementObject.profitOrLossFromOperatingActivities + \
                                                                     profitOrLossObject.operationIncomes + \
                                                                     profitOrLossObject.costOfOperationIncomes + \
                                                                     profitOrLossObject.distributionAndAdministrativeExpense + \
                                                                     profitOrLossObject.otherIncome + \
                                                                     profitOrLossObject.otherExpense
        incomeStatementObject.save()


@receiver(post_save, sender=profitOrLoss)
def update_incomeStatement_profitOrLossBeforeTax(**kwargs):
    profitOrLossObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=profitOrLossObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.profitOrLossBeforeTax = incomeStatementObject.profitOrLossBeforeTax + \
                                                       profitOrLossObject.operationIncomes + \
                                                       profitOrLossObject.costOfOperationIncomes + \
                                                       profitOrLossObject.distributionAndAdministrativeExpense + \
                                                       profitOrLossObject.otherIncome + \
                                                       profitOrLossObject.otherExpense + \
                                                       profitOrLossObject.financeCosts + \
                                                       profitOrLossObject.otherNonOperatingIncomeAndExpensesIncomeInvestments + \
                                                       profitOrLossObject.otherNonOperatingIncomeAndExpensesMiscellaneousItems
        incomeStatementObject.save()


@receiver(post_save, sender=profitOrLoss)
def update_incomeStatement_profitOrLoss(**kwargs):
    profitOrLossObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=profitOrLossObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.profitOrLoss = incomeStatementObject.profitOrLoss + \
                                              profitOrLossObject.operationIncomes + \
                                              profitOrLossObject.costOfOperationIncomes + \
                                              profitOrLossObject.distributionAndAdministrativeExpense + \
                                              profitOrLossObject.otherIncome + \
                                              profitOrLossObject.otherExpense + \
                                              profitOrLossObject.financeCosts + \
                                              profitOrLossObject.otherNonOperatingIncomeAndExpensesIncomeInvestments + \
                                              profitOrLossObject.otherNonOperatingIncomeAndExpensesMiscellaneousItems + \
                                              profitOrLossObject.taxPerIncome + \
                                              profitOrLossObject.profitOrLossFromContinuingOperations + \
                                              profitOrLossObject.profitOrLossFromDiscontinuedOperations

        incomeStatementObject.save()


@receiver(post_save, sender=statementOfIncomeAndRetainedEarnings)
def update_incomeStatement_adjustedRetainedEarningsBeginningBalance(**kwargs):
    statementOfIncomeAndRetainedEarningsObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=statementOfIncomeAndRetainedEarningsObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.adjustedRetainedEarningsBeginningBalance = incomeStatementObject.adjustedRetainedEarningsBeginningBalance + \
                                                                          statementOfIncomeAndRetainedEarningsObject.retainedEarningsAtBeginningOfPeriod + \
                                                                          statementOfIncomeAndRetainedEarningsObject.priorPeriodAdjustments

        incomeStatementObject.save()


@receiver(post_save, sender=statementOfIncomeAndRetainedEarnings)
def update_incomeStatement_unallocatedRetainedEarningsAtTheBeginningOfPeriod(**kwargs):
    statementOfIncomeAndRetainedEarningsObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=statementOfIncomeAndRetainedEarningsObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.unallocatedRetainedEarningsAtTheBeginningOfPeriod = incomeStatementObject.unallocatedRetainedEarningsAtTheBeginningOfPeriod + \
                                                                                   statementOfIncomeAndRetainedEarningsObject.retainedEarningsAtBeginningOfPeriod + \
                                                                                   statementOfIncomeAndRetainedEarningsObject.priorPeriodAdjustments + \
                                                                                   statementOfIncomeAndRetainedEarningsObject.dividendsDeclaredAndPaidOrPayable + \
                                                                                   statementOfIncomeAndRetainedEarningsObject.changesInCapitalFromRetainedEarnings

        incomeStatementObject.save()


@receiver(post_save, sender=statementOfIncomeAndRetainedEarnings)
def update_incomeStatement_distributableEarnings_byStatementOfIncomeAndRetainedEarnings(**kwargs):
    statementOfIncomeAndRetainedEarningsObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=statementOfIncomeAndRetainedEarningsObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.distributableEarnings = incomeStatementObject.distributableEarnings + \
                                                       statementOfIncomeAndRetainedEarningsObject.retainedEarningsAtBeginningOfPeriod + \
                                                       statementOfIncomeAndRetainedEarningsObject.priorPeriodAdjustments + \
                                                       statementOfIncomeAndRetainedEarningsObject.dividendsDeclaredAndPaidOrPayable + \
                                                       statementOfIncomeAndRetainedEarningsObject.changesInCapitalFromRetainedEarnings + \
                                                       statementOfIncomeAndRetainedEarningsObject.transferFromOtherEquityItems

        incomeStatementObject.save()



@receiver(post_save, sender=profitOrLoss)
def update_incomeStatement_distributableEarnings_byProfitOrLoss(**kwargs):
    profitOrLossObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=profitOrLossObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.distributableEarnings = incomeStatementObject.distributableEarnings + \
                                                       profitOrLossObject.operationIncomes + \
                                                       profitOrLossObject.costOfOperationIncomes + \
                                                       profitOrLossObject.distributionAndAdministrativeExpense + \
                                                       profitOrLossObject.otherIncome + \
                                                       profitOrLossObject.otherExpense + \
                                                       profitOrLossObject.financeCosts + \
                                                       profitOrLossObject.otherNonOperatingIncomeAndExpensesIncomeInvestments + \
                                                       profitOrLossObject.otherNonOperatingIncomeAndExpensesMiscellaneousItems + \
                                                       profitOrLossObject.taxPerIncome + \
                                                       profitOrLossObject.profitLossFromContinuingOperations + \
                                                       profitOrLossObject.profitOrLossFromDiscontinuedOperation

        incomeStatementObject.save()


@receiver(post_save, sender=statementOfIncomeAndRetainedEarnings)
def update_incomeStatement_retainedEarningsAtEndOfPeriod_byStatementOfIncomeAndRetainedEarnings(**kwargs):
    statementOfIncomeAndRetainedEarningsObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=statementOfIncomeAndRetainedEarningsObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.retainedEarningsAtEndOfPeriod = incomeStatementObject.retainedEarningsAtEndOfPeriod + \
                                                       statementOfIncomeAndRetainedEarningsObject.retainedEarningsAtBeginningOfPeriod + \
                                                       statementOfIncomeAndRetainedEarningsObject.priorPeriodAdjustments + \
                                                       statementOfIncomeAndRetainedEarningsObject.dividendsDeclaredAndPaidOrPayable + \
                                                       statementOfIncomeAndRetainedEarningsObject.changesInCapitalFromRetainedEarnings + \
                                                       statementOfIncomeAndRetainedEarningsObject.transferFromOtherEquityItems + \
                                                       statementOfIncomeAndRetainedEarningsObject.transferToStatutoryReserve + \
                                                       statementOfIncomeAndRetainedEarningsObject.transferToOtherReserve

        incomeStatementObject.save()


@receiver(post_save, sender=profitOrLoss)
def update_incomeStatement_retainedEarningsAtEndOfPeriod_byProfitOrLoss(**kwargs):
    profitOrLossObject = kwargs['instance']
    incomeStatementObjects = incomeStatement.objects.filter(relatedTo=profitOrLossObject.relatedTo)
    for incomeStatementObject in incomeStatementObjects:
        incomeStatementObject.retainedEarningsAtEndOfPeriod = incomeStatementObject.retainedEarningsAtEndOfPeriod + \
                                                       profitOrLossObject.operationIncomes + \
                                                       profitOrLossObject.costOfOperationIncomes + \
                                                       profitOrLossObject.distributionAndAdministrativeExpense + \
                                                       profitOrLossObject.otherIncome + \
                                                       profitOrLossObject.otherExpense + \
                                                       profitOrLossObject.financeCosts + \
                                                       profitOrLossObject.otherNonOperatingIncomeAndExpensesIncomeInvestments + \
                                                       profitOrLossObject.otherNonOperatingIncomeAndExpensesMiscellaneousItems + \
                                                       profitOrLossObject.taxPerIncome + \
                                                       profitOrLossObject.profitLossFromContinuingOperations + \
                                                       profitOrLossObject.profitOrLossFromDiscontinuedOperation

        incomeStatementObject.save()
