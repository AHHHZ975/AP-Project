import datetime
from django.db import models
from django.db.models import F
from django.utils import timezone
from django.forms.models import model_to_dict

# Create your models here.


class timePeriod(models.Model):
    timePeriod = models.CharField(max_length=2, primary_key=True, default=None)
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)

    def __str__(self):
        return self.timePeriod

    def was_published_recently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)

class company(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)

## Consolidated Balance Sheet (Tarazname) ##

class balanceSheet(models.Model):
    sumOfAssets = models.IntegerField(null=True)
    sumOfDebtsAndFundsOwner = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def was_published_recently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)

class assets(models.Model):
    sumOfCurrentAssets = models.IntegerField()
    sumOfNonCurrentAssets = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)
    balanceSheet = models.ForeignKey(balanceSheet, default=None, on_delete=models.CASCADE)
    originalsumOfCurrentAssets = 0
    originalsumOfNonCurrentAssets = 0

    def wasPublishedRecently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)

    def __init__(self, *args, **kwargs):
        super(assets, self).__init__(*args, **kwargs)
        self.originalsumOfCurrentAssets = self.sumOfCurrentAssets
        self.originalsumOfNonCurrentAssets = self.sumOfNonCurrentAssets

    def save(self, *args, **kwargs):
        if self.sumOfCurrentAssets != self.originalsumOfCurrentAssets:
            if self.company.name == self.balanceSheet.company.name:
                balanceSheet.objects.filter(company__name=self.company.name).update(sumOfAssets=F('sumOfAssets') + self.sumOfCurrentAssets - self.originalsumOfCurrentAssets)
        if self.sumOfNonCurrentAssets != self.originalsumOfNonCurrentAssets:
            if self.company.name == self.balanceSheet.company.name:
                balanceSheet.objects.filter(company__name=self.company.name).update(sumOfAssets=F('sumOfAssets') + self.sumOfNonCurrentAssets - self.originalsumOfNonCurrentAssets)
        super(assets, self).save(*args, **kwargs)
        self.originalsumOfCurrentAssets = self.sumOfCurrentAssets
        self.originalsumOfNonCurrentAssets = self.sumOfNonCurrentAssets

class debtsAndAssetsOwner(models.Model):
    sumOfCurrentDebts = models.IntegerField()
    sumOfNonCurrentDebts = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)
    balanceSheet = models.ForeignKey(balanceSheet, default=None, on_delete=models.CASCADE)
    originalSumOfCurrentDebts = 0
    originalSumOfNonCurrentDebts = 0

    def was_published_recently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

    def __init__(self, *args, **kwargs):
        super(debtsAndAssetsOwner, self).__init__(*args, **kwargs)
        self.originalSumOfCurrentDebts = self.sumOfCurrentDebts
        self.originalSumOfNonCurrentDebts = self.sumOfNonCurrentDebts

    def save(self, *args, **kwargs):
        if self.sumOfCurrentDebts != self.originalSumOfCurrentDebts:
            if self.company.name == self.balanceSheet.company.name:
                balanceSheet.objects.filter(company__name=self.company.name).update(sumOfDebtsAndFundsOwner=F('sumOfDebtsAndFundsOwner') + self.sumOfCurrentDebts - self.originalSumOfCurrentDebts)
        if self.sumOfNonCurrentDebts != self.originalSumOfNonCurrentDebts:
            if self.company.name == self.balanceSheet.company.name:
                balanceSheet.objects.filter(company__name=self.company.name).update(sumOfDebtsAndFundsOwner=F('sumOfDebtsAndFundsOwner') + self.sumOfNonCurrentDebts - self.originalSumOfNonCurrentDebts)
        super(debtsAndAssetsOwner, self).save(*args, **kwargs)
        self.originalSumOfCurrentDebts = self.sumOfCurrentDebts
        self.originalSumOfNonCurrentDebts = self.sumOfNonCurrentDebts

class currentAssets(models.Model):
    cash = models.IntegerField()
    shortTermInvestments = models.IntegerField()
    commercialInputs = models.IntegerField()
    noncommercialInputs = models.IntegerField()
    inventory = models.IntegerField()
    prepaidExpenses = models.IntegerField()
    salableAssets = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class nonCurrentAssets(models.Model):
    longTermInvestments = models.IntegerField()
    longTermInputs = models.IntegerField()
    investmentInEstate = models.IntegerField()
    intangibleAssets = models.IntegerField()
    tangibleAssets = models.IntegerField()
    otherAssets = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class currentDebts(models.Model):
    commercialPayable = models.IntegerField()
    NonCommercialPayable = models.IntegerField()
    payableTaxes = models.IntegerField()
    payableDividends = models.IntegerField()
    financialFacility = models.IntegerField()
    resources = models.IntegerField()
    currentPreReceivables = models.IntegerField()
    debtsRelatedWithSalableAssets = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class nonCurrentDebts(models.Model):
    longTermPayable = models.IntegerField()
    nonCurrentPreReceivables = models.IntegerField()
    longTermFinancialFacility = models.IntegerField()
    storeOfWorkersEndServiceAdvantages = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class ownerInvestment(models.Model):
    assets = models.IntegerField()
    increaseORDecreaseOfInProcessAssets = models.IntegerField()
    stockSpends = models.IntegerField()
    treasuryStocks = models.IntegerField()
    legalSavings = models.IntegerField()
    otherSavings = models.IntegerField()
    RevaluationSurplusOfHeldForSaleAssets = models.IntegerField()
    RevaluationSurplusOfAssets = models.IntegerField()
    DifferenceInTheConvergenceDueToConversionToReportingCurrency = models.IntegerField()
    ValuationAssetsOfAssetsAndLiabilitiesOfStateOwnedEnterprises = models.IntegerField()
    accumulatedProfitORLosses = models.IntegerField()
    sumOfOwnersInvestments = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

## Income Statement (sood o zian) ##

class incomeStatement(models.Model): # Narenji rang ha
    grossProfit = models.IntegerField()
    profitOrLossFromOperatingActivities = models.IntegerField()
    profitOrLossBeforeTax = models.IntegerField()
    profitLossFromContinuingOperations = models.IntegerField()
    profitOrLoss = models.IntegerField()
    basicEarningsLossPerShare = models.IntegerField()
    dilutedEarningsLossPerShare = models.IntegerField()
    adjustedRetainedEarningsBeginningBalance = models.IntegerField()
    unallocatedRetainedEarningsAtTheBeginningOfPeriod = models.IntegerField()
    distributableEarnings = models.IntegerField()
    retainedEarningsAtEndOfPeriod = models.IntegerField()
    earningsPerShareAfterTax = models.IntegerField()
    listedCapital = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class profitOrLoss(models.Model):
    Revenue = models.IntegerField()
    costOfSales = models.IntegerField()
    distributionAndAdministrativeExpense = models.IntegerField()
    otherIncome = models.IntegerField()
    otherExpense = models.IntegerField()
    financeCosts = models.IntegerField()
    otherNonOperatingIncomeAndExpensesIncomeInvestments = models.IntegerField()
    OtherNonOperatingIncomeAndExpensesMiscellaneousItems = models.IntegerField()
    incomeTaxExpenseContinuingOperations = models.IntegerField()
    profitOrLossFromDiscontinuedOperation = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class basicEarningsLossPerShare(models.Model):
    basicEarningsOrLossPerShareFromContinuingOperationsOperating = models.IntegerField()
    basicEarningsOrLossPerShareFromContinuingOperationsNonOperating = models.IntegerField()
    basicEarningsOrLossPerShareFromDiscontinuingOperations = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class dilutedEarningsOrLossPerShare(models.Model):
    dilutedEarningsOrLossPerShareFromContinuingOperationsOperating = models.IntegerField()
    dilutedEarningsOrLossPerShareFromContinuingOperationsNonOperating = models.IntegerField()
    dilutedEarningsOrLossPerShareFromDiscontinuingOperations = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class statementOfIncomeAndRetainedEarnings(models.Model):
    retainedEarningsAtBeginningOfPeriod = models.IntegerField()
    priorPeriodAdjustments = models.IntegerField()
    dividendsDeclaredAndPaidOrPayable = models.IntegerField()
    changesInCapitalFromRetainedEarnings = models.IntegerField()
    transferFromOtherEquityItems = models.IntegerField()
    transferToStatutoryReserve = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

## Cash Flow (jaryan vojooh naghd) ##

class cashFlow(models.Model):   # Narenji rang ha
    netCashFlowsFromUsedInOperatingActivities = models.IntegerField()
    netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts = models.IntegerField()
    incomeTaxesPaid = models.IntegerField()
    netCashFlowsFromUsedInInvestingActivities = models.IntegerField()
    netCashFlowsFromUsedInBeforeFinancingActivities = models.IntegerField()
    netCashFlowsFromUsedInFinancingActivities = models.IntegerField()
    netIncreaseDecreaseInCash = models.IntegerField()
    cashAtEndOfPeriod = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class cashFlowsFromUsedInOperatingActivities(models.Model):
    netCashFlowsFromUsedInOperatingActivitiesOrdinary = models.IntegerField()
    netCashFlowsFromUsedInOperatingActivitiesExceptional = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class investmentReturnsAndPaymentsOnFinancingCosts(models.Model):
    dividendsReceived = models.IntegerField()
    interestPaidOrBorrowing = models.IntegerField()
    interestReceivedFromOtherInvestments = models.IntegerField()
    dividendsPaid = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class cashFlowsUsedInIncomeTax(models.Model):
    pass;

class cashFlowsFromUsedInInvestingActivities(models.Model):
    proceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities = models.IntegerField()
    purchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities = models.IntegerField()
    proceedsFromSalesOfIntangibleAssetsClassifiedAsInvestingActivities = models.IntegerField()
    purchaseOfOnTangibleAssetsClassifiedAsInvestingActivities = models.IntegerField()
    proceedsFromSalesOfNonCurrentInvestments = models.IntegerField()
    facilitiesGrantedToIndividuals = models.IntegerField()
    extraditionFacilitiesGrantedToIndividuals = models.IntegerField()
    purchaseOfNonCurrentInvestments = models.IntegerField()
    proceedsFromSalesOfCurrentInvestments = models.IntegerField()
    purchaseOfCurrentInvestments = models.IntegerField()
    proceedsFromSalesOfInvestmentProperty = models.IntegerField()
    purchaseOfInvestmentProperty = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class cashFlowsFromUsedInFinancingActivities(models.Model):
    proceedsFromIssuingShares = models.IntegerField()
    proceedsFromSalesOrIssueOfTreasuryShares = models.IntegerField()
    paymentsForPurchaseOfTreasuryShares = models.IntegerField()
    proceedsFromBorrowingsClassifiedAsFinancingActivities = models.IntegerField()
    repaymentsOfBorrowingsClassifiedAsFinancingActivities = models.IntegerField()
    cashAtBeginningOfPeriod = models.IntegerField()
    effectOfExchangeRateChangesOnCash = models.IntegerField()
    NonCashTransactions = models.IntegerField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)
    company = models.ForeignKey(company, default=None, on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(timePeriod, default=None, on_delete=models.CASCADE)

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)
