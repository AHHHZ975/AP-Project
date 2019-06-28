from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from ..models import *

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
def update_balanceSheet_sumOfDebtsAndFundsOwner(**kwargs):
    debtsAndAssetsOwnerObject = kwargs['instance']
    balanceSheets = balanceSheet.objects.filter(relatedTo=debtsAndAssetsOwnerObject.relatedTo)
    for balancesheetObject in balanceSheets:
        balancesheetObject.sumOfDebtsAndFundsOwner =  balancesheetObject.sumOfDebtsAndFundsOwner\
                                                      + debtsAndAssetsOwnerObject.sumOfCurrentDebts \
                                                      + debtsAndAssetsOwnerObject.sumOfNonCurrentDebts
        balancesheetObject.save()

