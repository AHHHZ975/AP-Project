import datetime
from django.db import models
from django.db.models import F
from django.utils import timezone
from django_jalali.db import models as jmodels  # For Persian Calender
from .Report import *


TYPES_COMPANY = (
    ('0' , 'Regular'),
    ('1' , 'Bank'),
    ('2' , 'Investment'),
)

TYPES_REPORT = (
    ('0' , 'FinancialStatement'),
    ('1' , 'Monthly'),
    ('2' , 'Investment'),
)
TYPES_AUDIT = (
    ('(حسابرسی شده', 'حسابرسی شده'),
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
    type_audit = models.CharField('نوع حسابرسی', max_length=16, choices=TYPES_AUDIT, blank=True, default="")
    type_date = models.CharField('بازه', max_length=2, choices=TYPES_DATE, blank=False, default="")
    type_consolidated = models.CharField('نوع تلفیقی', max_length=16, choices=TYPES_CONSOLIDATED, blank=True,
                                         default="")
    # endTo = models.DateField('End to', default=timezone.now)
    # endTo = models.CharField('End to', max_length=32, default="")
    # endTo = jmodels.jDateField('منتهی به', default="")

    def __str__(self):
        string = f"اطلاعات و صورت مالی شرکت {str(self.companyName)} {self.type_consolidated} " \
                 f" {str(self.type_audit)} {str(self.type_date)} ماهه منتهی به  "
                 # f"{str(self.endTo)}"

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
    sumOfCurrentAssets = models.IntegerField(verbose_name='جمع دارایی‌های جاری')
    sumOfNonCurrentAssets = models.IntegerField(verbose_name='جمع دارایی‌های غیرجاری')

    class Meta:
        verbose_name_plural = '1.1-دارایی ها'

    def wasPublishedRecently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)



class debtsAndAssetsOwner(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    sumOfCurrentDebts = models.IntegerField(verbose_name='جمع بدهی‌های جاری')
    sumOfNonCurrentDebts = models.IntegerField(verbose_name='جمع بدهی‌های غیرجاری')
    sumOfOwnersInvestments = models.IntegerField(verbose_name='جمع حقوق صاحبان سهام')

    class Meta:
        verbose_name_plural = '1.2-بدهی ها و حقوق صاحبان سهم'


class currentAssets(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    cash = models.IntegerField(verbose_name='موجودی نقد')
    shortTermInvestments = models.IntegerField(verbose_name='سرمایه‌گذاری‌‌های کوتاه مدت')
    commercialInputs = models.IntegerField(verbose_name='دریافتنی‌‌های تجاری')
    noncommercialInputs = models.IntegerField(verbose_name='دریافتنی‌‌های غیرتجاری')
    inventory = models.IntegerField(verbose_name='موجودی مواد و کالا')
    prepaidExpenses = models.IntegerField(verbose_name='پیش پرداخت‌ها و سفارشات')
    salableAssets = models.IntegerField(verbose_name='دارایی‌های نگهداری شده برای فروش')

    class Meta:
        verbose_name_plural = '1.1.1-دارایی ها جاری'


class nonCurrentAssets(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    longTermInvestments = models.IntegerField(verbose_name='دریافتنی‌‌های بلندمدت')
    longTermInputs = models.IntegerField(verbose_name='سرمایه‌گذاری‌های بلندمدت')
    investmentInEstate = models.IntegerField(verbose_name='سرمایه‌گذاری در املاک')
    intangibleAssets = models.IntegerField(verbose_name='دارایی‌های نامشهود')
    tangibleAssets = models.IntegerField(verbose_name='دارایی‌های ثابت مشهود')
    otherAssets = models.IntegerField(verbose_name='سایر دارایی‌ها')

    class Meta:
        verbose_name_plural = '1.1.2-دارایی ها غیرجاری'

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class currentDebts(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    commercialPayable = models.IntegerField(verbose_name='پرداختنی‌های تجاری')
    NonCommercialPayable = models.IntegerField(verbose_name='پرداختنی‌های غیرتجاری')
    payableTaxes = models.IntegerField(verbose_name='مالیات پرداختنی')
    payableDividends = models.IntegerField(verbose_name='سود سهام پرداختنی')
    financialFacility = models.IntegerField(verbose_name='تسهیلات مالی')
    resources = models.IntegerField(verbose_name='ذخایر')
    currentPreReceivables = models.IntegerField(verbose_name='پیش‌دریافت‌های جاری')
    debtsRelatedWithSalableAssets = models.IntegerField(verbose_name
                                                        ='بدهی‌های مرتبط با دارایی‌های نگهداری شده برای فروش')

    class Meta:
        verbose_name_plural = '1.2.1-بدهی های جاری'


    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class nonCurrentDebts(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    longTermPayable = models.IntegerField(verbose_name='پرداختنی‌های بلندمدت')
    nonCurrentPreReceivables = models.IntegerField(verbose_name='پیش‌دریافت‌های غیرجاری')
    longTermFinancialFacility = models.IntegerField(verbose_name='تسهیلات مالی بلندمدت')
    storeOfWorkersEndServiceAdvantages = models.IntegerField(verbose_name='ذخیره مزایای پایان خدمت کارکنان')

    class Meta:
        verbose_name_plural = '1.2.2-بدهی های غیر جاری'

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


class ownerInvestment(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    assets = models.IntegerField(verbose_name='سرمایه')
    increaseORDecreaseOfInProcessAssets = models.IntegerField(verbose_name='افزایش (کاهش) سرمایه در جریان')
    stockSpends = models.IntegerField(verbose_name='صرف (کسر) سهام')
    treasuryStocks = models.IntegerField(verbose_name='سهام خزانه')
    legalSavings = models.IntegerField(verbose_name='ادندوخته قانونی')
    otherSavings = models.IntegerField(verbose_name='سایر اندوخته‌ها')
    RevaluationSurplusOfHeldForSaleAssets = models.IntegerField(verbose_name='مازاد تجدید ارزیابی دارایی‌های نگهداری شده برای فروش')
    RevaluationSurplusOfAssets = models.IntegerField(verbose_name='مازاد تجدید ارزیابی دارایی‌ها')
    DifferenceInTheConvergenceDueToConversionToReportingCurrency = models.IntegerField(verbose_name='تفاوت تسعیر ناشی از تبدیل به واحد پول گزارشگری')
    ValuationAssetsOfAssetsAndLiabilitiesOfStateOwnedEnterprises = models.IntegerField(verbose_name='اندوخته تسعیر ارز دارایی‌ها و بدهی‌های شرکت‌های دولتی')
    accumulatedProfitORLosses = models.IntegerField(verbose_name='سود(زیان) انباشته')

    class Meta:
        verbose_name_plural = '1.2.3-حقوق صاحبان سهم'

    def wasPublishedRecently(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)


## Income Statement (sood o zian) ##

class incomeStatement(models.Model):  # Narenji rang ha

    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    grossProfit = models.IntegerField(verbose_name='سود (زیان) ناخالص')
    profitOrLossFromOperatingActivities = models.IntegerField(verbose_name='سود (زیان) عملیاتی')
    profitOrLossBeforeTax = models.IntegerField(verbose_name='سود (زیان) عملیات در حال تداوم قبل از مالیات')
    profitOrlossFromContinuingOperations = models.IntegerField(verbose_name='سود (زیان) خالص عملیات در حال تداوم')
    profitOrLoss = models.IntegerField(verbose_name='سود (زیان) خالص')
    basicEarningsLossPerShare = models.IntegerField(verbose_name='سود (زیان) پایه هر سهم')
    dilutedEarningsLossPerShare = models.IntegerField(verbose_name='سود (زیان) تقلیل یافته هر سهم')
    adjustedRetainedEarningsBeginningBalance = models.IntegerField(verbose_name='سود (زیان) انباشته ابتدای دوره تعدیل ‌شده')
    unallocatedRetainedEarningsAtTheBeginningOfPeriod = models.IntegerField(verbose_name='سود (زیان) انباشته ابتدای دوره تخصیص نیافته')
    distributableEarnings = models.IntegerField(verbose_name='سود قابل تخصیص')
    retainedEarningsAtEndOfPeriod = models.IntegerField(verbose_name='سود (زیان) انباشته‌ پايان‌ دوره')
    earningsPerShareAfterTax = models.IntegerField(verbose_name='سود (زیان) خالص هر سهم– ریال')
    listedCapital = models.IntegerField(verbose_name='سرمایه')

    class Meta:
        verbose_name_plural = '2-صورت سود و زیان'


class profitOrLoss(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    operationIncomes = models.IntegerField(verbose_name='درآمدهای عملیاتی')
    costOfOperationIncomes = models.IntegerField(verbose_name='بهای تمام ‌شده درآمدهای عملیاتی')
    distributionAndAdministrativeExpense = models.IntegerField(verbose_name='هزینه‌های فروش، اداری و عمومی')
    otherIncome = models.IntegerField(verbose_name='سایر درآمدهای عملیاتی')
    otherExpense = models.IntegerField(verbose_name='سایر هزینه‌های عملیاتی')
    financeCosts = models.IntegerField(verbose_name='هزینه‌های مالی')
    otherNonOperatingIncomeAndExpensesIncomeInvestments = models.IntegerField(verbose_name='سایر درآمدها و هزینه‌های غیرعملیاتی- درآمد سرمایه‌گذاری‌ها')
    otherNonOperatingIncomeAndExpensesMiscellaneousItems = models.IntegerField(verbose_name='سایر درآمدها و هزینه‌های غیرعملیاتی- اقلام متفرقه')
    taxPerIncome = models.IntegerField(verbose_name='مالیات بر درآمد')
    profitOrLossFromDiscontinuedOperations = models.IntegerField(verbose_name='سود (زیان) عملیات متوقف ‌شده پس از اثر مالیاتی')

    class Meta:
        verbose_name_plural = '2.1-سود(زیان) خالص'


class basicEarningsLossPerShare(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    basicEarningsOrLossPerShareFromContinuingOperationsOperating = models.IntegerField(verbose_name='سود (زیان) پایه هر سهم ناشی از عملیات در حال تداوم- عملیاتی')
    basicEarningsOrLossPerShareFromContinuingOperationsNonOperating = models.IntegerField(verbose_name='سود (زیان) پایه هر سهم ناشی از عملیات در حال تداوم- غیرعملیاتی')
    basicEarningsOrLossPerShareFromDiscontinuingOperations = models.IntegerField(verbose_name='سود (زیان) پایه هر سهم ناشی از عملیات متوقف‌ شده')

    class Meta:
        verbose_name_plural = '2.2-سود (زیان) پایه هر سهم'




class dilutedEarningsOrLossPerShare(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    dilutedEarningsOrLossPerShareFromContinuingOperationsOperating = models.IntegerField(verbose_name='سود (زیان) تقلیل یافته هر سهم ناشی از عملیات در حال تداوم- عملیاتی')
    dilutedEarningsOrLossPerShareFromContinuingOperationsNonOperating = models.IntegerField(verbose_name='سود (زیان) تقلیل یافته هر سهم ناشی از عملیات در حال تداوم- غیرعملیاتی')
    dilutedEarningsOrLossPerShareFromDiscontinuingOperations = models.IntegerField(verbose_name='سود (زیان) تقلیل یافته هر سهم ناشی از عملیات متوقف ‌شده')

    class Meta:
        verbose_name_plural = '2.3-سود (زیان) تقلیل یافته هر سهم'



class statementOfIncomeAndRetainedEarnings(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    retainedEarningsAtBeginningOfPeriod = models.IntegerField(verbose_name='سود (زیان) انباشته ابتدای دوره')
    priorPeriodAdjustments = models.IntegerField(verbose_name='تعدیلات سنواتی')
    dividendsDeclaredAndPaidOrPayable = models.IntegerField(verbose_name='سود سهام‌ مصوب')
    changesInCapitalFromRetainedEarnings = models.IntegerField(verbose_name='تغییرات سرمایه از محل سود (زیان) انباشته')
    transferFromOtherEquityItems = models.IntegerField(verbose_name='انتقال از سایر اقلام حقوق صاحبان سهام')
    transferToStatutoryReserve = models.IntegerField(verbose_name='انتقال به اندوخته‌ قانوني‌')
    transferToOtherReserve = models.IntegerField(verbose_name='انتقال به سایر اندوخته‌ها')

    class Meta:
        verbose_name_plural = '2.4-گردش حساب سود (زیان) انباشته'



## Cash Flow (jaryan vojooh naghd) ##


class cashFlow(models.Model):  # Narenji rang ha
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    netCashFlowsFromUsedInOperatingActivities = models.IntegerField(verbose_name='جریان خالص ورود (خروج) وجه نقد ناشی از فعالیت‌های عملیاتی')
    netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts = models.IntegerField(verbose_name='جریان خالص ورود (خروج) وجه نقد ناشی از بازده سرمایه‌گذاری‌ها و سود پرداختی بابت تأمین مالی')
    # Income taxes paid = ...
    netCashFlowsFromUsedInInvestingActivities = models.IntegerField(verbose_name='جریان خالص ورود (خروج) وجه نقد ناشی از فعالیت‌های سرمایه‌گذاری')
    netCashFlowsFromUsedInBeforeFinancingActivities = models.IntegerField(verbose_name='جریان خالص ورود (خروج) وجه نقد قبل از فعالیت‌های تأمین مالی')
    netCashFlowsFromUsedInFinancingActivities = models.IntegerField(verbose_name='جریان خالص ورود (خروج) وجه نقد ناشی از فعالیت‌های تأمین مالی')
    netIncreaseDecreaseInCash = models.IntegerField(verbose_name='خالص افزایش (کاهش) در موجودی نقد')
    cashAtEndOfPeriod = models.IntegerField(verbose_name='موجودی نقد در پایان دوره')

    class Meta:
        verbose_name_plural = '3-جریان وجوه نقد'

class cashFlowsFromUsedInOperatingActivities(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    netCashFlowsFromUsedInOperatingActivitiesOrdinary = models.IntegerField(verbose_name='جریان خالص ورود (خروج) وجه نقد ناشی از فعالیت‌های عملیاتی- عادی')
    netCashFlowsFromUsedInOperatingActivitiesExceptional = models.IntegerField(verbose_name='جریان خالص ورود (خروج) وجه نقد ناشی از فعالیت‌های عملیاتی')

    class Meta:
        verbose_name_plural = '3.1-فعالیت‌های عملیاتی'


class investmentReturnsAndPaymentsOnFinancingCosts(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    dividendsReceived = models.IntegerField(verbose_name='سود سهام دریافتی')
    interestPaidOrBorrowing = models.IntegerField(verbose_name='سود پرداختی بابت استقراض')
    interestReceivedFromOtherInvestments = models.IntegerField(verbose_name='سود دریافتی بابت سایر سرمایه‌گذاری‌ها')
    dividendsPaid = models.IntegerField(verbose_name='سود سهام پرداختی')

    class Meta:
        verbose_name_plural = '3.2-بازده سرمایه گذاری‌ها و سود پرداختی بابت تأمین مالی'

class cashFlowsUsedInIncomeTax(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    incomeTaxesPaid = models.IntegerField(verbose_name='مالیات بر درآمد پرداختی')

    class Meta:
        verbose_name_plural = '3.3-مالیات بر درآمد'


class cashFlowsFromUsedInInvestingActivities(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    proceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities = models.IntegerField(verbose_name='وجوه دریافتی بابت فروش دارایی‌های ثابت مشهود')
    purchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities = models.IntegerField(verbose_name='وجوه پرداختی بابت خرید دارایی‌های ثابت مشهود')
    proceedsFromSalesOfIntangibleAssetsClassifiedAsInvestingActivities = models.IntegerField(verbose_name='وجوه دریافتی بابت فروش دارایی‌های نامشهود')
    purchaseOfOnTangibleAssetsClassifiedAsInvestingActivities = models.IntegerField(verbose_name='وجوه پرداختی بابت خرید دارایی‌های نامشهود‌')
    proceedsFromSalesOfNonCurrentInvestments = models.IntegerField(verbose_name='وجوه دریافتی بابت فروش سرمایه‌گذاری‌های بلندمدت')
    facilitiesGrantedToIndividuals = models.IntegerField(verbose_name='تسهیلات اعطایی به اشخاص')
    extraditionFacilitiesGrantedToIndividuals = models.IntegerField(verbose_name='استرداد تسهیلات اعطایی به اشخاص')
    purchaseOfNonCurrentInvestments = models.IntegerField(verbose_name='وجوه پرداختی بابت خرید سرمایه‌گذاری‌های بلندمدت')
    proceedsFromSalesOfCurrentInvestments = models.IntegerField(verbose_name='وجوه دریافتی بابت فروش سرمایه‌گذاری‌های کوتاه‌مدت')
    purchaseOfCurrentInvestments = models.IntegerField(verbose_name='وجوه پرداختی بابت خرید سرمایه‌گذاری‌های کوتاه‌مدت')
    proceedsFromSalesOfInvestmentProperty = models.IntegerField(verbose_name='وجوه دریافتی بابت فروش سرمایه‌گذاری‌ در املاک')
    purchaseOfInvestmentProperty = models.IntegerField(verbose_name='وجوه پرداختی بابت خرید سرمایه‌گذاری در املاک')

    class Meta:
        verbose_name_plural = '3.4-فعالیت‌های سرمایه گذاری'


class cashFlowsFromUsedInFinancingActivities(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    proceedsFromIssuingShares = models.IntegerField(verbose_name='وجوه دریافتی حاصل از افزایش سرمایه')
    proceedsFromSalesOrIssueOfTreasuryShares = models.IntegerField(verbose_name='وجوه دریافتی بابت فروش سهام خزانه')
    paymentsForPurchaseOfTreasuryShares = models.IntegerField(verbose_name='وجوه پرداختی بابت خرید سهام خزانه')
    proceedsFromBorrowingsClassifiedAsFinancingActivities = models.IntegerField(verbose_name='وجوه دریافتی حاصل از استقراض')
    repaymentsOfBorrowingsClassifiedAsFinancingActivities = models.IntegerField(verbose_name='بازپرداخت اصل استقراض')
    cashAtBeginningOfPeriod = models.IntegerField(verbose_name='موجودی نقد در ابتدای دوره')
    effectOfExchangeRateChangesOnCash = models.IntegerField(verbose_name='تآثیر تغییرات نرخ ارز')
    NonCashTransactions = models.IntegerField(verbose_name='مبادلات غیرنقدی')

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

# column3 = ['نام محصول', 'واحد' , 'از ابتدای سال مالی تا پایان مورخ 1398/02/31->مقدار/تعداد تولید',
#            'از ابتدای سال مالی تا پایان مورخ 1398/02/31->مقدار/تعداد فروش',
#            ... ,
#            'مقدار/تعداد تولید->مقدار/تعداد فروش',
#            'مقدار/تعداد تولید->مقدار/تعداد فروش',
#            ...]

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

##############################################  BANK    ###################################################

# # ##### ترازنامه ###########

class balanceSheet_bank(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')

    totalLiabilities = models.IntegerField(verbose_name=' جمع بدهی‌ها ')
    totalEquity = models.IntegerField(verbose_name=' جمع حقوق صاحبان سهام ')
    totalAssets = models.IntegerField(verbose_name='جمع دارایی‌ها')
    totalequityAndLiabilities = models.IntegerField(verbose_name='جمع بدهی‌ها و حقوق صاحبان سهام')

    class Meta:
        verbose_name_plural = '(بانک ها)1-ترازنامه'

class assets_bank(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    cash = models.IntegerField(verbose_name=' موجودی نقد ')
    cashAndBankBalancesAtCentralBanks = models.IntegerField(verbose_name=' مطالبات از بانک‌های مرکزی ')
    loansAndAdvancesToBanks = models.IntegerField(verbose_name=' مطالبات از بانک‌ها و سایر موسسات اعتباری ')
    receivablesFromGovernment = models.IntegerField(verbose_name=' مطالبات از دولت ')
    loansAndReceivablesFromGovernmentalPartiesOtherThanBanks = models.IntegerField(verbose_name=' تسهیلات اعطایی و مطالبات از اشخاص دولتی به غیر از بانک‌ها ')
    loansAndReceivablesFromNonGovernmentalPartiesOtherThanBanks = models.IntegerField(verbose_name=' تسهیلات اعطایی و مطالبات از اشخاص غیردولتی به غیر از بانک‌ها ')
    investmentInSecurities = models.IntegerField(verbose_name=' سرمایه‌گذاری در سهام و سایر اوراق بهادار ')
    otherReceivables = models.IntegerField(verbose_name=' سایر حساب‌ها و اسناد دریافتنی ')
    investmentProperty = models.IntegerField(verbose_name=' سرمایه‌گذاری در املاک ')
    intangibleAssetsOtherThanGoodwill = models.IntegerField(verbose_name=' دارایی‌های نامشهود ')
    propertyPlantAndEquipment = models.IntegerField(verbose_name=' دارایی‌های ثابت مشهود ')
    totalCurrentAssets = models.IntegerField(verbose_name=' دارایی‌های نگهداری شده برای فروش ')
    otherAssets = models.IntegerField(verbose_name=' سایر دارایی‌ها ')

    class Meta:
        verbose_name_plural = '(بانک ها)1.1-دارایی ها'

    def wasPublishedRecently(self):
        return self.publicDate >= timezone.now() - datetime.timedelta(days=1)


class debts_bank(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    liabilitiesDueToCentralBanks = models.IntegerField(verbose_name=' بدهی به بانک مرکزی و صندوق توسعه ملی ')
    depositsFromBanksAndOtherFinancialInstitutions = models.IntegerField(verbose_name=' بدهی به بانک‌ها و سایر موسسات اعتباری ')
    balancesOnDemandDepositsFromCustomers = models.IntegerField(verbose_name=' سپرده‌های دیداری و مشابه ')
    balancesOnSavingDepositsFromCustomers = models.IntegerField(verbose_name=' سپرده‌های پس‌انداز و مشابه ')
    balancesOnTermDepositsFromCustomers = models.IntegerField(verbose_name=' سپرده‌های سرمایه‌گذاری مدت‌دار ')
    balancesOnOtherDepositsFromCustomers = models.IntegerField(verbose_name=' سایر سپرده‌ها ')
    currentTaxLiabilities = models.IntegerField(verbose_name=' مالیات پرداختنی ')
    dividendPayables = models.IntegerField(verbose_name=' سود سهام پرداختنی ')
    provisions = models.IntegerField(verbose_name='ذخایر')
    provisionsForEmployeeBenefits = models.IntegerField(verbose_name=' ذخیره مزایای پایان خدمت کارکنان ')
    liabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale = models.IntegerField(verbose_name=' بدهی‌های مرتبط با دارایی‌های نگهداری شده برای فروش ')
    otherLiabilities = models.IntegerField(verbose_name=' سایر بدهی‌ها ')

    class Meta:
        verbose_name_plural = '(بانک ها)2.1-بدهی های جاری'


class ownerInvestment_bank(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    issuedCapital = models.IntegerField(verbose_name=' سرمایه ')
    inProcessCapitalIncrease = models.IntegerField(verbose_name=' افزایش (کاهش) سرمایه در جریان ')
    sharePremium = models.IntegerField(verbose_name=' صرف (کسر) سهام ')
    treasuryShares = models.IntegerField(verbose_name=' سهام خزانه ')
    statutoryReserve = models.IntegerField(verbose_name=' اندوخته قانونی ')
    otherReserves = models.IntegerField(verbose_name=' سایر اندوخته‌ها ')
    revaluationSurplusOfNonCurrentAssetsHeldForSale = models.IntegerField(verbose_name=' مازاد تجدید ارزیابی دارایی‌های نگهداری شده برای فروش ')
    revaluationSurplus = models.IntegerField(verbose_name=' مازاد تجدید ارزیابی دارایی‌ها ')
    exchangeDifferencesOnTranslation = models.IntegerField(verbose_name=' تفاوت تسعیر ناشی از تبدیل به واحد پول گزارشگری ')
    exchangeReserveForGovernmentalCorporationsAssetsAndLiabilities = models.IntegerField(verbose_name=' اندوخته تسعیر ارز دارایی‌ها و بدهی‌های شرکت‌های دولتی ')
    retainedEarnings = models.IntegerField(verbose_name=' سود (زیان) انباشته ')


    class Meta:
        verbose_name_plural = '(بانک ها)2.1-حقوق صاحبان سهم'

# ###### سود و زیان ########


class incomeStatement_bank(models.Model):  # Narenji rang ha

    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    totalJointRevenue = models.IntegerField(verbose_name=' جمع درآمدهای مشاع ')
    interestExpenseOnDepositsFromCustomers = models.IntegerField(verbose_name=' سهم سود سپرده‌گذاران ')
    bankShareFromJointRevenue = models.IntegerField(verbose_name=' سهم بانک از درآمدهای مشاع ')
    totalNonJointRevenue = models.IntegerField(verbose_name=' جمع درآمدهای غیرمشاع ')
    totalRevenueByNature = models.IntegerField(verbose_name=' جمع درآمدها ')
    totalExpenseByNature = models.IntegerField(verbose_name=' جمع هزینه‌ها ')
    profitLossBeforeTax = models.IntegerField(verbose_name=' سود (زیان) عملیات در حال تداوم قبل از مالیات ')
    profitLossFromContinuingOperations = models.IntegerField(verbose_name=' سود (زیان) خالص عملیات در حال تداوم ')
    profitLoss = models.IntegerField(verbose_name=' سود (زیان) خالص ')
    basicEarningsLossPerShare = models.IntegerField(verbose_name=' سود (زیان) پایه هر سهم ')
    dilutedEarningsLossPerShare = models.IntegerField(verbose_name=' سود (زیان) تقلیل یافته هر سهم ')
    # profitLoss = models.IntegerField(verbose_name=' سود (زیان) خالص ')
    adjustedRetainedEarningsBeginningBalance = models.IntegerField(verbose_name=' سود (زیان) انباشته ابتدای دوره تعدیل ‌شده ')
    unallocatedRetainedEarningsAtTheBeginningOfPeriod = models.IntegerField(verbose_name=' سود (زیان) انباشته ابتدای دوره تخصیص نیافته ')
    distributableEarnings = models.IntegerField(verbose_name=' سود قابل تخصیص ')
    retainedEarningsAtEndOfPeriod = models.IntegerField(verbose_name=' سود (زیان) انباشته‌ پايان‌ دوره ')
    earningsPerShareAfterTax = models.IntegerField(verbose_name=' سود (زیان) خالص هر سهم– ریال ')
    listedCapital = models.IntegerField(verbose_name=' سرمایه ')

    class Meta:
        verbose_name_plural = '(بانک ها)2-صورت سود و زیان'


class jointRevenue_bank(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    interestIncomeOnLoansAndAdvancesToCustomers = models.IntegerField(verbose_name=' سود و وجه التزام تسهیلات اعطایی ')
    investmentIncomeAndInterestIncomeOnDeposits = models.IntegerField(verbose_name=' سود (زیان) حاصل از سرمایه‌گذاری‌ها و سپرده‌گذاری‌ها ')
    onAccountPaymentsOnInvestmentDeposits = models.IntegerField(verbose_name=' سود علی‌الحساب سپرده‌های سرمایه‌گذاری ')
    differenceBetweenOnAccountPaymentsAndInterestExpenseOnInvestmentDeposits = models.IntegerField(verbose_name=' تفاوت سود قطعی و علی‌الحساب سپرده‌های سرمایه‌گذاری ')

    class Meta:
        verbose_name_plural = '(بانک ها)1.2-درآمدهای مشاع'


class nonJointRevenue_bank (models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    incomeOnNonJointActivities = models.IntegerField(verbose_name=' سود و وجه التزام فعالیت‌های غیرمشاع ')
    feeAndCommissionIncome = models.IntegerField(verbose_name=' درآمد کارمزد ')
    gainsLossesOnExchangeDifferencesOnTranslationRecognisedInProfitOrLoss = models.IntegerField(verbose_name=' نتیجه مبادلات ارزی ')
    otherGains = models.IntegerField(verbose_name=' سایر درآمدها ')

    class Meta:
        verbose_name_plural = '(بانک ها)1.2-درآمدهای غیرمشاع'


class expenseByNature_bank(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    employeeBenefitsExpense = models.IntegerField(verbose_name=' هزینه‌های کارکنان ')
    administrativeExpense = models.IntegerField(verbose_name=' سایر هزینه‌های اجرایی ')
    provisionForLoansAndAdvances = models.IntegerField(verbose_name=' هزینه مطالبات مشکوک‌الوصول ')
    financeCosts = models.IntegerField(verbose_name=' هزینه‌های مالی ')
    feeAndCommissionExpense = models.IntegerField(verbose_name=' هزینه کارمزد ')

    incomeTaxExpenseContinuingOperations = models.IntegerField(verbose_name=' مالیات بر درآمد ')

    profitLossFromDiscontinuedOperations = models.IntegerField(verbose_name=' سود (زیان) عملیات متوقف ‌شده پس از اثر مالیاتی ')

    class Meta:
        verbose_name_plural = '(بانک ها)2.2-هزینه ها'

class basicEarningsPerShare_bank(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    basicEarningsLossPerShareFromContinuingOperations = models.IntegerField(verbose_name=' سود (زیان) پایه هر سهم ناشی از عملیات در حال تداوم ')
    basicEarningsLossPerShareFromDiscontinuedOperations = models.IntegerField(verbose_name=' سود (زیان) پایه هر سهم ناشی از عملیات متوقف‌ شده ')

    class Meta:
        verbose_name_plural = '(بانک ها)3.2-سود (زیان) پایه هر سهم'


class dilutedEarningsPerShare_bank(models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')
    dilutedEarningsLossPerShareFromContinuingOperations = models.IntegerField(verbose_name=' سود (زیان) تقلیل یافته هر سهم ناشی از عملیات در حال تداوم ')
    dilutedEarningsLossPerShareFromDiscontinuedOperations = models.IntegerField(verbose_name=' سود (زیان) تقلیل یافته هر سهم ناشی از عملیات متوقف ‌شده ')

    class Meta:
        verbose_name_plural = '(بانک ها)4.2-سود (زیان) تقلیل یافته هر سهم'


class statementOfIncomeAndRetainedEarnings_bank (models.Model):
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')

    RetainedEarningsAtBeginningOfPeriod = models.IntegerField(verbose_name=' سود (زیان) انباشته ابتدای دوره ')
    priorPeriodAdjustments = models.IntegerField(verbose_name=' تعدیلات سنواتی ')

    dividendsDeclaredAndPaidOrPayable = models.IntegerField(verbose_name=' سود سهام‌ مصوب ')
    changesInCapitalFromRetainedEarnings = models.IntegerField(verbose_name=' تغییرات سرمایه از محل سود (زیان) انباشته ')

    transferFromOtherEquityItems = models.IntegerField(verbose_name=' انتقال از سایر اقلام حقوق صاحبان سهام ')

    transferToStatutoryReserve = models.IntegerField(verbose_name=' انتقال به اندوخته‌ قانوني‌ ')
    transferToOtherReserves = models.IntegerField(verbose_name=' انتقال به سایر اندوخته‌ها ')

    class Meta:
        verbose_name_plural = '(بانک ها)5.2-گردش حساب سود (زیان) انباشته'


#### جربان وحوه نقد ##

class cashFlow_bank(models.Model):  # Narenji rang ha
    relatedTo = models.ForeignKey(FinancialStatements, default=None, on_delete=models.PROTECT, verbose_name='مربوط به')

    class Meta:
        verbose_name_plural = '(بانک ها)3-جریان وجوه نقد'


########################################### Automate the storing in database ###########################################
# name = input ('Please Enter the name of the company')
# num = input ('Please Enter the first flag')
# flag = input ('Please Enter the second flag')

companySymbol = 'خپارس'
companyNum = '0'
reportNum = '0'

[report, number] = Report_Extractor(companySymbol, companyNum, reportNum)
# print(number)
if  'تلفیقی' in report[0][0][1]:
    fs = FinancialStatements(companyName=report[0][0][0], type_audit=report[0][0][5],
                             type_date=report[0][0][2], type_consolidated='تلفیقی')
else:
    fs = FinancialStatements(companyName=report[0][0][0], type_audit=report[0][0][5],
                             type_date=report[0][0][2], type_consolidated='غیرتلفیقی')
fs.save()


print(report[0][0])
print(report[2][0])
print(report[4][0])
############################# Regualar Balancesheet ###################################################################
ca = currentAssets(relatedTo_id=1,cash=report[0][0][7][2][1], shortTermInvestments=report[0][0][7][3][1],
                   commercialInputs=report[0][0][7][4][1], noncommercialInputs=report[0][0][7][5][1],
                   inventory=report[0][0][7][6][1], prepaidExpenses=report[0][0][7][7][1],
                   salableAssets=report[0][0][7][8][1])
ca.save()


nca = nonCurrentAssets(relatedTo_id=1, longTermInputs=report[0][0][7][11][1],
                       longTermInvestments=report[0][0][7][12][1], investmentInEstate=report[0][0][7][13][1],
                       intangibleAssets=report[0][0][7][14][1], tangibleAssets=report[0][0][7][15][1],
                       otherAssets=report[0][0][7][16][1])
nca.save()

a = assets(relatedTo_id=1, sumOfCurrentAssets=report[0][0][7][9][1], sumOfNonCurrentAssets=report[0][0][7][17][1])
a.save()



cd = currentDebts(relatedTo_id=1,commercialPayable=report[0][0][7][2][5], NonCommercialPayable=report[0][0][7][3][5],
                   payableTaxes=report[0][0][7][4][5], payableDividends=report[0][0][7][5][5],
                   financialFacility=report[0][0][7][6][5], resources=report[0][0][7][7][5],
                   currentPreReceivables=report[0][0][7][8][5], debtsRelatedWithSalableAssets=report[0][0][7][9][5])
cd.save()


ncd = nonCurrentDebts(relatedTo_id=1, longTermPayable=report[0][0][7][12][5],
                       nonCurrentPreReceivables=report[0][0][7][13][5], longTermFinancialFacility=report[0][0][7][14][5],
                       storeOfWorkersEndServiceAdvantages=report[0][0][7][15][5])
ncd.save()

oi = ownerInvestment(relatedTo_id=1, assets=report[0][0][7][19][5], increaseORDecreaseOfInProcessAssets=report[0][0][7][20][5],
                     stockSpends=report[0][0][7][21][5], treasuryStocks=report[0][0][7][22][5],
                     legalSavings=report[0][0][7][23][5], otherSavings=report[0][0][7][24][5],
                     RevaluationSurplusOfAssets=report[0][0][7][25][5], RevaluationSurplusOfHeldForSaleAssets=report[0][0][7][26][5],
                     DifferenceInTheConvergenceDueToConversionToReportingCurrency=report[0][0][7][27][5],
                     ValuationAssetsOfAssetsAndLiabilitiesOfStateOwnedEnterprises=report[0][0][7][28][5],
                     accumulatedProfitORLosses=report[0][0][7][29][5])
oi.save()

daao = debtsAndAssetsOwner(relatedTo_id=1, sumOfCurrentDebts=report[0][0][7][10][5], sumOfNonCurrentDebts=report[0][0][7][16][5],
                           sumOfOwnersInvestments=report[0][0][7][30][5])
daao.save()

bs = balanceSheet(relatedTo_id=1, sumOfAssets=report[0][0][7][31][1], sumOfDebtsAndFundsOwner=report[0][0][7][31][5])
bs.save()


###################################### Regualar Income Statements #####################################################
pol = profitOrLoss(relatedTo_id=1,operationIncomes=report[2][0][7][2][1], costOfOperationIncomes=report[2][0][7][3][1],
                   distributionAndAdministrativeExpense=report[2][0][7][5][1],
                   otherIncome=report[2][0][7][6][1], otherExpense=report[2][0][7][7][1],
                   financeCosts=report[2][0][7][9][1],
                   otherNonOperatingIncomeAndExpensesIncomeInvestments=report[2][0][7][10][1],
                   otherNonOperatingIncomeAndExpensesMiscellaneousItems=report[2][0][7][11][1],
                   taxPerIncome=report[2][0][7][13][1],
                   profitOrLossFromDiscontinuedOperations=report[2][0][7][15][1])
pol.save()


belps = basicEarningsLossPerShare(relatedTo_id=1,
                                  basicEarningsOrLossPerShareFromContinuingOperationsOperating=report[2][0][7][18][1],
                                  basicEarningsOrLossPerShareFromContinuingOperationsNonOperating=report[2][0][7][19][1],
                                  basicEarningsOrLossPerShareFromDiscontinuingOperations=report[2][0][7][20][1])
belps.save()

deolps = dilutedEarningsOrLossPerShare(relatedTo_id=1,
                                  dilutedEarningsOrLossPerShareFromContinuingOperationsOperating=report[2][0][7][23][1],
                                  dilutedEarningsOrLossPerShareFromContinuingOperationsNonOperating=report[2][0][7][24][1],
                                  dilutedEarningsOrLossPerShareFromDiscontinuingOperations=report[2][0][7][25][1])
deolps.save()


soiare = statementOfIncomeAndRetainedEarnings(relatedTo_id=1,
                                  retainedEarningsAtBeginningOfPeriod=report[2][0][7][29][1],
                                  priorPeriodAdjustments=report[2][0][7][30][1],
                                  dividendsDeclaredAndPaidOrPayable=report[2][0][7][32][1],
                                  changesInCapitalFromRetainedEarnings=report[2][0][7][33][1],
                                  transferFromOtherEquityItems=report[2][0][7][35][1],
                                  transferToStatutoryReserve=report[2][0][7][37][1],
                                  transferToOtherReserve=report[2][0][7][38][1])
soiare.save()

IS = incomeStatement(relatedTo_id=1,grossProfit=report[2][0][7][4][1],
                     profitOrLossFromOperatingActivities=report[2][0][7][8][1],
                     profitOrLossBeforeTax=report[2][0][7][12][1],
                     profitOrlossFromContinuingOperations=report[2][0][7][14][1],
                     profitOrLoss=report[2][0][7][16][1],
                     basicEarningsLossPerShare=report[2][0][7][21][1],
                     dilutedEarningsLossPerShare=report[2][0][7][26][1],
                     adjustedRetainedEarningsBeginningBalance=report[2][0][7][31][1],
                     unallocatedRetainedEarningsAtTheBeginningOfPeriod=report[2][0][7][34][1],
                     distributableEarnings=report[2][0][7][36][1],
                     retainedEarningsAtEndOfPeriod=report[2][0][7][39][1],
                     earningsPerShareAfterTax=report[2][0][7][40][1],
                     listedCapital=report[2][0][7][41][1])
IS.save()

###################################### Regular Cash Flow #########################################
cffuioa = cashFlowsFromUsedInOperatingActivities(relatedTo_id=1,
                                                 netCashFlowsFromUsedInOperatingActivitiesOrdinary=report[4][0][7][1][1],
                                                 netCashFlowsFromUsedInOperatingActivitiesExceptional=report[4][0][7][2][1])
cffuioa.save()

irapofc = investmentReturnsAndPaymentsOnFinancingCosts(relatedTo_id=1,
                                                 dividendsReceived=report[4][0][7][5][1],
                                                 interestPaidOrBorrowing=report[4][0][7][6][1],
                                                 interestReceivedFromOtherInvestments=report[4][0][7][7][1],
                                                 dividendsPaid=report[4][0][7][8][1])
irapofc.save()

cfuia = cashFlowsFromUsedInInvestingActivities(relatedTo_id=1,
                                                 proceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities=report[4][0][7][13][1],
                                                 purchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities=report[4][0][7][14][1],
                                                 proceedsFromSalesOfIntangibleAssetsClassifiedAsInvestingActivities=report[4][0][7][15][1],
                                                 purchaseOfOnTangibleAssetsClassifiedAsInvestingActivities=report[4][0][7][16][1],
                                                 proceedsFromSalesOfNonCurrentInvestments=report[4][0][7][17][1],
                                                 facilitiesGrantedToIndividuals=report[4][0][7][18][1],
                                                 extraditionFacilitiesGrantedToIndividuals=report[4][0][7][19][1],
                                                 purchaseOfNonCurrentInvestments=report[4][0][7][20][1],
                                                 proceedsFromSalesOfCurrentInvestments=report[4][0][7][21][1],
                                                 purchaseOfCurrentInvestments=report[4][0][7][22][1],
                                                 proceedsFromSalesOfInvestmentProperty=report[4][0][7][23][1],
                                                 purchaseOfInvestmentProperty=report[4][0][7][24][1])
cfuia.save()

cfuifa = cashFlowsFromUsedInFinancingActivities(relatedTo_id=1,
                                                 proceedsFromIssuingShares=report[4][0][7][28][1],
                                                 proceedsFromSalesOrIssueOfTreasuryShares=report[4][0][7][29][1],
                                                 paymentsForPurchaseOfTreasuryShares=report[4][0][7][30][1],
                                                 proceedsFromBorrowingsClassifiedAsFinancingActivities=report[4][0][7][31][1],
                                                 repaymentsOfBorrowingsClassifiedAsFinancingActivities=report[4][0][7][32][1],
                                                 cashAtBeginningOfPeriod=report[4][0][7][35][1],
                                                 effectOfExchangeRateChangesOnCash=report[4][0][7][36][1],
                                                 NonCashTransactions=report[4][0][7][38][1])
cfuifa.save()

cf = cashFlow(relatedTo_id=1,
                                                 netCashFlowsFromUsedInOperatingActivities=report[4][0][7][3][1],
                                                 netCashFlowsFromUsedInInvestmentReturnsAndPaymentsOnFinancingCosts=report[4][0][7][9][1],
                                                 netCashFlowsFromUsedInInvestingActivities=report[4][0][7][25][1],
                                                 netCashFlowsFromUsedInBeforeFinancingActivities=report[4][0][7][26][1],
                                                 netCashFlowsFromUsedInFinancingActivities=report[4][0][7][33][1],
                                                 netIncreaseDecreaseInCash=report[4][0][7][34][1],
                                                 cashAtEndOfPeriod=report[4][0][7][35][1])
cf.save()

cfuiit = cashFlowsUsedInIncomeTax(relatedTo_id=1, incomeTaxesPaid=report[4][0][7][11][1])
cfuiit.save()