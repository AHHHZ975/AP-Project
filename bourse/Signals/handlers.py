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

