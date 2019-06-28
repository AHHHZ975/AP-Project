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

