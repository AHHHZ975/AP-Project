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

    type_audit = models.CharField('نوع حسابرسی', max_length=16, choices=TYPES_AUDIT, blank=True, default="")
    type_date = models.CharField('بازه', max_length=2, choices=TYPES_DATE, blank=False, default="")
    type_consolidated = models.CharField('نوع تلفیقی', max_length=16, choices=TYPES_CONSOLIDATED, blank=True,
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

