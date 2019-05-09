import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

## Consolidated Balance Sheet (Tarazname) ##


class Company(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    def __str__(self):
        return self.name


class BalanceSheet(models.Model):
    # publicDate = models.DateTimeField('Data published')
    time = models.CharField(max_length=2)
    sumOfAssets = models.IntegerField()
    sumOfDebtsAndFundsOwner = models.IntegerField()

    # def wasPublishedRecently(self):
    #     return self.publicDate >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.time



class Assets(models.Model):
    time = models.CharField(max_length=2)
    sumOfCurrentAssets = models.IntegerField()
    sumOfNonCurrentAssets = models.IntegerField()
    # publicDate = models.DateTimeField('Data published')

    # def wasPublishedRecently(self):
    #     return self.publicDate >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.time


class DebtsAndAssetsOwner(models.Model):
    time = models.CharField(max_length=2)
    sumOfCurrentDebts = models.IntegerField()
    sumOfNonCurrentDebts = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class CurrentAssets(models.Model):
    time = models.CharField(max_length=2)
    cash = models.IntegerField()
    shortTermInvestments = models.IntegerField()
    commercialInputs = models.IntegerField()
    noncommercialInputs = models.IntegerField()
    inventory = models.IntegerField()
    prepaidExpenses = models.IntegerField()
    salableAssets = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class NonCurrentAssets(models.Model):
    time = models.CharField(max_length=2)
    longTermInvestments = models.IntegerField()
    longTermInputs = models.IntegerField()
    investmentInEstate = models.IntegerField()
    intangibleAssets = models.IntegerField()
    tangibleAssets = models.IntegerField()
    otherAssets = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class CurrentDebts(models.Model):
    time = models.CharField(max_length=2)
    commercialPayable = models.IntegerField()
    NonCommercialPayable = models.IntegerField()
    payableTaxes = models.IntegerField()
    payableDividends = models.IntegerField()
    financialFacility = models.IntegerField()
    resources = models.IntegerField()
    currentPreReceivables = models.IntegerField()
    debtsRelatedWithSalableAssets = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class NonCurrentDebts(models.Model):
    time = models.CharField(max_length=2)
    longTermPayable = models.IntegerField()
    nonCurrentPreReceivables = models.IntegerField()
    longTermFinancialFacility = models.IntegerField()
    storeOfWorkersEndServiceAdvantages = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class OwnerInvestment(models.Model):
    time = models.CharField(max_length=2)
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

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)




## Income Statement (sood o zian) ##



class IncomeStatement(models.Model): # Narenji rang ha
    time = models.CharField(max_length=2)
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

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class ProfitOrLoss(models.Model):
    time = models.CharField(max_length=2)
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

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class BasicEarningsLossPerShare(models.Model):
    time = models.CharField(max_length=2)
    basicEarningsOrLossPerShareFromContinuingOperationsOperating = models.IntegerField()
    basicEarningsOrLossPerShareFromContinuingOperationsNonOperating = models.IntegerField()
    basicEarningsOrLossPerShareFromDiscontinuingOperations = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

class DilutedEarningsOrLossPerShare(models.Model):
    time = models.CharField(max_length=2)
    dilutedEarningsOrLossPerShareFromContinuingOperationsOperating = models.IntegerField()
    dilutedEarningsOrLossPerShareFromContinuingOperationsNonOperating = models.IntegerField()
    dilutedEarningsOrLossPerShareFromDiscontinuingOperations = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class StatementOfIncomeAndRetainedEarnings(models.Model):
    time = models.CharField(max_length=2)
    retainedEarningsAtBeginningOfPeriod = models.IntegerField()
    priorPeriodAdjustments = models.IntegerField()
    dividendsDeclaredAndPaidOrPayable = models.IntegerField()
    changesInCapitalFromRetainedEarnings = models.IntegerField()
    transferFromOtherEquityItems = models.IntegerField()
    transferToStatutoryReserve = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)







## Cash Flow (jaryan vojooh naghd) ##







class CashFlow(models.Model):   # Narenji rang ha
    time = models.CharField(max_length=2)
    netCashFlowsFromUsedInOperatingActivities = models.IntegerField()
    netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts = models.IntegerField()
    incomeTaxesPaid = models.IntegerField()
    netCashFlowsFromUsedInInvestingActivities = models.IntegerField()
    netCashFlowsFromUsedInBeforeFinancingActivities = models.IntegerField()
    netCashFlowsFromUsedInFinancingActivities = models.IntegerField()
    netIncreaseDecreaseInCash = models.IntegerField()
    cashAtEndOfPeriod = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)





class CashFlowsFromUsedInOperatingActivities(models.Model):
    time = models.CharField(max_length=2)
    netCashFlowsFromUsedInOperatingActivitiesOrdinary = models.IntegerField()
    netCashFlowsFromUsedInOperatingActivitiesExceptional = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class InvestmentReturnsAndPaymentsOnFinancingCosts(models.Model):
    time = models.CharField(max_length=2)
    dividendsReceived = models.IntegerField()
    interestPaidOrBorrowing = models.IntegerField()
    interestReceivedFromOtherInvestments = models.IntegerField()
    dividendsPaid = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class CashFlowsUsedInIncomeTax(models.Model):
    pass;

class CashFlowsFromUsedInInvestingActivities(models.Model):
    time = models.CharField(max_length=2)
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

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class CashFlowsFromUsedInFinancingActivities(models.Model):
    time = models.CharField(max_length=2)
    proceedsFromIssuingShares = models.IntegerField()
    proceedsFromSalesOrIssueOfTreasuryShares = models.IntegerField()
    paymentsForPurchaseOfTreasuryShares = models.IntegerField()
    proceedsFromBorrowingsClassifiedAsFinancingActivities = models.IntegerField()
    repaymentsOfBorrowingsClassifiedAsFinancingActivities = models.IntegerField()
    cashAtBeginningOfPeriod = models.IntegerField()
    effectOfExchangeRateChangesOnCash = models.IntegerField()
    NonCashTransactions = models.IntegerField()

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

