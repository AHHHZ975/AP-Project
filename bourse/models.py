import datetime
from django.db import models
from django.db.models import F
from django.utils import timezone
from django_jalali.db import models as jmodels  # For Persian Calender

TYPES_AUDIT = (
    ('حسابرسی شده', 'حسابرسی شده'),
    ('حسابرسی نشده', 'حسابرسی نشده'),
)
TYPES_DATE = (
    ('1', 'ماهه 1'),
    ('3', 'ماهه 3'),
    ('6', 'ماهه 6'),
    ('9', 'ماهه 9'),
    ('12', 'ماهه 12'),
)
TYPES_CONSOLIDATED = (
    ('تلفیقی', 'تلفیقی'),
    ('غیرتلفیقی', 'غیرتلفیقی'),
)


# Create your models here.


# financial statements اطلاغات و صورت های مالی
class FinancialStatements(models.Model):
    # id = models.IntegerField(primary_key=True)
    companyName = models.CharField('نام شرکت', max_length=32, default="")

    type_audit = models.CharField('نوع حسابرسی', max_length=16, choices=TYPES_AUDIT, blank=False, default="")
    type_date = models.CharField('بازه', max_length=2, choices=TYPES_DATE, blank=False, default="")
    type_consolidated = models.CharField('نوع تلفیقی', max_length=16, choices=TYPES_CONSOLIDATED, blank=False,
                                         default="")
    # endTo = models.DateField('End to', default=timezone.now)
    endTo = jmodels.jDateField('منتهی به', default="")

    def __str__(self):
        string = f"اطلاعات و صورت مالی شرکت {str(self.companyName)} {self.type_consolidated} " \
                 f" {str(self.type_audit)} {str(self.type_date)} ماهه منتهی به  " \
                 f"{str(self.endTo)}"

        return string

    class Meta:
        verbose_name_plural = '0-اطلاعات و صورت های مالی'

    def was_published_recently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)

    # def __str__(self):
    #     string = f"اطلاعات و صورت مالی شرکت {str(self.name)} {self.type_consolidated} " \
    #              f" {str(self.type_audit)} {str(self.type_date)} ماهه منتهی به  " \
    #              f"{str(self.endTo)}"

    # string += str(self.name)
    # string += self.type_consolidated
    # string += str(self.type_audit)
    # string += str(self.type_date)
    # string += "ماهه "
    # string += "منتهی به"
    # string += str(self.endto)


class company(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)


class performanceIndexes(models.Model):
    s = models.FloatField()
    p = models.FloatField()
    pToE = models.FloatField()
    pToB = models.FloatField()
    pToS = models.FloatField()
    publicDate = models.DateTimeField('Publication Date', default=timezone.now)


## Consolidated Balance Sheet (Tarazname) ##
class balanceSheet(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    sumOfAssets = models.IntegerField(null=True)
    sumOfDebtsAndFundsOwner = models.IntegerField()

    class Meta:
        verbose_name_plural = '1-ترازنامه'

class assets(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    sumOfCurrentAssets = models.IntegerField()
    sumOfNonCurrentAssets = models.IntegerField()

    class Meta:
        verbose_name_plural = '1.1-دارایی ها'

    def wasPublishedRecently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)



class debtsAndAssetsOwner(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    sumOfCurrentDebts = models.IntegerField()
    sumOfNonCurrentDebts = models.IntegerField()
    sumOfOwnersInvestments = models.IntegerField()

    class Meta:
        verbose_name_plural = '1.2-بدهی ها و حقوق صاحبان سهم'


class currentAssets(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    cash = models.IntegerField()
    shortTermInvestments = models.IntegerField()
    commercialInputs = models.IntegerField()
    noncommercialInputs = models.IntegerField()
    inventory = models.IntegerField()
    prepaidExpenses = models.IntegerField()
    salableAssets = models.IntegerField()

    class Meta:
        verbose_name_plural = '1.1.1-دارایی ها جاری'


class nonCurrentAssets(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    longTermInvestments = models.IntegerField()
    longTermInputs = models.IntegerField()
    investmentInEstate = models.IntegerField()
    intangibleAssets = models.IntegerField()
    tangibleAssets = models.IntegerField()
    otherAssets = models.IntegerField()

    class Meta:
        verbose_name_plural = '1.1.2-دارایی ها غیرجاری'

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class currentDebts(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    commercialPayable = models.IntegerField()
    NonCommercialPayable = models.IntegerField()
    payableTaxes = models.IntegerField()
    payableDividends = models.IntegerField()
    financialFacility = models.IntegerField()
    resources = models.IntegerField()
    currentPreReceivables = models.IntegerField()
    debtsRelatedWithSalableAssets = models.IntegerField()


    class Meta:
        verbose_name_plural = '1.2.1-بدهی های جاری'


    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class nonCurrentDebts(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    longTermPayable = models.IntegerField()
    nonCurrentPreReceivables = models.IntegerField()
    longTermFinancialFacility = models.IntegerField()
    storeOfWorkersEndServiceAdvantages = models.IntegerField()

    class Meta:
        verbose_name_plural = '1.2.2-بدهی های غیر جاری'

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class ownerInvestment(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
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

    class Meta:
        verbose_name_plural = '1.2.3-حقوق صاحبان سهم'

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


## Income Statement (sood o zian) ##

class incomeStatement(models.Model):  # Narenji rang ha

    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    grossProfit = models.IntegerField()
    profitOrLossFromOperatingActivities = models.IntegerField()
    profitOrLossBeforeTax = models.IntegerField()
    profitOrLoss = models.IntegerField()
    basicEarningsLossPerShare = models.IntegerField()
    dilutedEarningsLossPerShare = models.IntegerField()
    adjustedRetainedEarningsBeginningBalance = models.IntegerField()
    unallocatedRetainedEarningsAtTheBeginningOfPeriod = models.IntegerField()
    distributableEarnings = models.IntegerField()
    retainedEarningsAtEndOfPeriod = models.IntegerField()
    earningsPerShareAfterTax = models.IntegerField()
    listedCapital = models.IntegerField()

    class Meta:
        verbose_name_plural = '2-صورت سود و زیان'


class profitOrLoss(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    operationIncomes = models.IntegerField()
    costOfOperationIncomes = models.IntegerField()
    distributionAndAdministrativeExpense = models.IntegerField()
    otherIncome = models.IntegerField()
    otherExpense = models.IntegerField()
    financeCosts = models.IntegerField()
    otherNonOperatingIncomeAndExpensesIncomeInvestments = models.IntegerField()
    otherNonOperatingIncomeAndExpensesMiscellaneousItems = models.IntegerField()
    taxPerIncome = models.IntegerField()
    profitLossFromContinuingOperations = models.IntegerField()
    profitOrLossFromDiscontinuedOperation = models.IntegerField()

    class Meta:
        verbose_name_plural = '2.1-سود(زیان) خالص'


class basicEarningsLossPerShare(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    basicEarningsOrLossPerShareFromContinuingOperationsOperating = models.IntegerField()
    basicEarningsOrLossPerShareFromContinuingOperationsNonOperating = models.IntegerField()
    basicEarningsOrLossPerShareFromDiscontinuingOperations = models.IntegerField()
    basicEarningsOrLossPerShare = models.IntegerField()

    class Meta:
        verbose_name_plural = '2.2-سود (زیان) پایه هر سهم'




class dilutedEarningsOrLossPerShare(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    dilutedEarningsOrLossPerShareFromContinuingOperationsOperating = models.IntegerField()
    dilutedEarningsOrLossPerShareFromContinuingOperationsNonOperating = models.IntegerField()
    dilutedEarningsOrLossPerShareFromDiscontinuingOperations = models.IntegerField()
    dilutedEarningsOrLossPerShare = models.IntegerField()

    class Meta:
        verbose_name_plural = '2.3-سود (زیان) تقلیل یافته هر سهم'



class statementOfIncomeAndRetainedEarnings(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    retainedEarningsAtBeginningOfPeriod = models.IntegerField()
    priorPeriodAdjustments = models.IntegerField()
    dividendsDeclaredAndPaidOrPayable = models.IntegerField()
    changesInCapitalFromRetainedEarnings = models.IntegerField()
    transferFromOtherEquityItems = models.IntegerField()
    transferToStatutoryReserve = models.IntegerField()
    transferToOtherReserve = models.IntegerField()

    class Meta:
        verbose_name_plural = '2.4-گردش حساب سود (زیان) انباشته'



## Cash Flow (jaryan vojooh naghd) ##


class cashFlow(models.Model):  # Narenji rang ha
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    netCashFlowsFromUsedInOperatingActivities = models.IntegerField()
    netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts = models.IntegerField()
    netCashFlowsFromUsedInInvestingActivities = models.IntegerField()
    netCashFlowsFromUsedInBeforeFinancingActivities = models.IntegerField()
    netCashFlowsFromUsedInFinancingActivities = models.IntegerField()
    netIncreaseDecreaseInCash = models.IntegerField()
    cashAtEndOfPeriod = models.IntegerField()

    class Meta:
        verbose_name_plural = '3-جریان وجوه نقد'

class cashFlowsFromUsedInOperatingActivities(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    netCashFlowsFromUsedInOperatingActivitiesOrdinary = models.IntegerField()
    netCashFlowsFromUsedInOperatingActivitiesExceptional = models.IntegerField()

    class Meta:
        verbose_name_plural = '3.1-فعالیت‌های عملیاتی'


class investmentReturnsAndPaymentsOnFinancingCosts(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    dividendsReceived = models.IntegerField()
    interestPaidOrBorrowing = models.IntegerField()
    interestReceivedFromOtherInvestments = models.IntegerField()
    dividendsPaid = models.IntegerField()

    class Meta:
        verbose_name_plural = '3.2-بازده سرمایه گذاری‌ها و سود پرداختی بابت تأمین مالی'

class cashFlowsUsedInIncomeTax(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    incomeTaxesPaid = models.IntegerField()

    class Meta:
        verbose_name_plural = '3.3-مالیات بر درآمد'


class cashFlowsFromUsedInInvestingActivities(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
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

    class Meta:
        verbose_name_plural = '3.4-فعالیت‌های سرمایه گذاری'

class cashFlowsFromUsedInFinancingActivities(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    proceedsFromIssuingShares = models.IntegerField()
    proceedsFromSalesOrIssueOfTreasuryShares = models.IntegerField()
    paymentsForPurchaseOfTreasuryShares = models.IntegerField()
    proceedsFromBorrowingsClassifiedAsFinancingActivities = models.IntegerField()
    repaymentsOfBorrowingsClassifiedAsFinancingActivities = models.IntegerField()
    cashAtBeginningOfPeriod = models.IntegerField()
    effectOfExchangeRateChangesOnCash = models.IntegerField()
    NonCashTransactions = models.IntegerField()

    class Meta:
        verbose_name_plural = '3.5-فعالیت‌های تأمین مالی'

############################ Dynamic Models ############################################
# fields = {
#     'first_name': models.CharField('واحد', max_length=255),
#     '__module__': __name__,
# }
# MyModel2 = type('MyModel2', (models.Model,), fields)


column = ['واحد', 'مقدار/تعداد تولید', 'نرخ فروش (ریال)', 'مبلغ فروش (میلیون ریال)']
column2 = ['قراردادها->تاریخ عقد قرارداد', 'قراردادها->مدت قرارداد (ماه)',
           'درآمد شناسایی شده->درآمد شناسایی شده طی دوره یک ماهه منتهی به 1398/01/31',
           'درآمد شناسایی شده->درآمد شناسایی شده از اول سال مالی تا پایان دوره مالی منتهی به 1398/01/31',
           'درآمد شناسایی شده->درامد شناسایی شده تا پایان دوره مالی منتهی به 1397/12/29',
           ]

# example for single dynamic model
# fields = dict()
#
# fields['relatedTo'] = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT)
# for i in range(len(column)):
#     fields['column'+str(i)] = models.IntegerField(column[i])
# fields['__module__'] = __name__
# MyModel = type('MyModel', (models.Model,), fields)

columns = [column, column2]

for i in range(len(columns)):
    fields = dict()
    fields['relatedTo'] = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')

    for j in range(len(columns[i])):
        fields['column' + str(j)] = models.IntegerField(columns[i][j])
    from django.contrib import admin

    fields['__module__'] = __name__
    Dynamic_Model = type('گزارش فعالیت ماهانه ' + str(i), (models.Model,), fields)

    admin.site.register(Dynamic_Model)

