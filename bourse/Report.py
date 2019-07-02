from selenium import webdriver
from math import floor
from time import sleep
from .Functions import *


def Report_Extractor (company_name, company_num, report_num):
    driver = webdriver.Chrome(executable_path='C:\selenium_driver\chromedriver.exe')
    driver.implicitly_wait(10)

    num_of_results_path = '//*[@id="divLetterFormList"]/div/span'
    link_paths = list()
    for i in range(1, 21):
        link_paths.append(f'//*[@id="divLetterFormList"]/table/tbody/tr[{i}]/td[4]/span/a')

    if ((company_num == '0' or company_num == '1') and report_num == '0'):
        Letter_Code = 'ن-10'
        url = f'https://codal.ir/ReportList.aspx?search&Symbol={company_name}&' \
        f'LetterCode={Letter_Code}&LetterType=-1&FromDate=1395%2F01%2F01&Isic=341008&AuditorRef=-1&PageNumber=1&' \
        f'Audited&NotAudited&IsNotAudited=false&Childs=false&Mains&Publisher=false&CompanyState=-1&Category=-1&CompanyType=-1&Consolidatable&NotConsolidatable'
        driver.get(url)
        sleep(2)
        if (not len(driver.find_elements_by_xpath(num_of_results_path)) > 0):
            driver.close()
            return [list(), 0]
        else:
            num_of_results = driver.find_element_by_xpath(num_of_results_path)
            num_of_results = int(num_of_results.text)
            rounds = floor(num_of_results / 20) + 1


    elif ((company_num == '0' or company_num == '1') and report_num == '1'):
        Letter_Code = 'ن-30'
        url = f'https://codal.ir/ReportList.aspx?search&Symbol={company_name}&' \
        f'LetterCode={Letter_Code}&LetterType=-1&FromDate=1395%2F01%2F01&Isic=341008&AuditorRef=-1&PageNumber=1&' \
        f'Audited&NotAudited&IsNotAudited=false&Childs=false&Mains&Publisher=false&CompanyState=-1&Category=-1&CompanyType=-1&Consolidatable&NotConsolidatable'
        driver.get(url)
        sleep(2)
        if (not len(driver.find_elements_by_xpath(num_of_results_path)) > 0):
            driver.close()
            return [list(), 0]
        else:
            num_of_results = driver.find_element_by_xpath(num_of_results_path)
            num_of_results = int(num_of_results.text)
            rounds = floor(num_of_results / 20) + 1

    elif (company_num == '2'):
        Letter_Code = 'ن-31'
        url = f'https://codal.ir/ReportList.aspx?search&Symbol={company_name}&' \
        f'LetterCode={Letter_Code}&LetterType=-1&FromDate=1395%2F01%2F01&Isic=341008&AuditorRef=-1&PageNumber=1&' \
        f'Audited&NotAudited&IsNotAudited=false&Childs=false&Mains&Publisher=false&CompanyState=-1&Category=-1&CompanyType=-1&Consolidatable&NotConsolidatable'
        driver.get(url)
        sleep(2)
        if (not len(driver.find_elements_by_xpath(num_of_results_path)) > 0):
            driver.close()
            return [list(), 0]
        else:
            num_of_results = driver.find_element_by_xpath(num_of_results_path)
            num_of_results = int(num_of_results.text)
            rounds = floor(num_of_results / 20) + 1



    links = list()
    descriptions = list()
    for i in range(rounds):
        if (i != 0):
            new_url = url.replace(f'PageNumber={i}', f'PageNumber={i + 1}')
            driver.get(new_url)
            sleep(2)
        for j in range(20):
            if (20*i + j < num_of_results):
                val = driver.find_element_by_xpath(link_paths[j])
                h = val.get_attribute('href')
                h = h + '&sheetId=0'
                links.append(h)
                descriptions.append(val.text)



    driver.close()

    Report = list()

    if (company_num == '0' and report_num == '0'):
        Balance = list()
        Loss_Gain = list()
        CashFlow = list()
        Collective_Balance = list()
        Collective_Loss_Gain = list()
        Collective_CashFlow = list()
        for i in range(len(links)):
            Balance.append(list())
            Collective_Balance.append(list())

            Loss_Gain.append(list())
            Collective_Loss_Gain.append(list())

            CashFlow.append(list())
            Collective_CashFlow.append(list())

            address = links[i]
            #None_Bank_Balance_Function_Calling
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody) = None_Bank_Balance(
                address)
            Balance[len(Balance) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

            address = address.replace('sheetId=0', 'sheetId=1')
            #None_Bank_LossGain_Function_Calling
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody) = None_Bank_LossGain(
                address)
            Loss_Gain[len(Loss_Gain) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

            address = address.replace('sheetId=1', 'sheetId=9')
            #None_Bank_CashFlow_Function_Calling
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody) = None_Bank_CashFlow(
                address)
            CashFlow[len(CashFlow) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)


            if ('تلفیقی' in descriptions[i]):
                address = address.replace('sheetId=9', 'sheetId=12')
                # None_Bank_Balance_Function_Calling
                (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody) = None_Bank_Balance(
                    address)
                Collective_Balance[len(Balance) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

                address = address.replace('sheetId=12', 'sheetId=13')
                # None_Bank_LossGain_Function_Calling
                (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody) = None_Bank_LossGain(
                    address)
                Collective_Loss_Gain[len(Loss_Gain) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

                address = address.replace('sheetId=13', 'sheetId=14')
                # None_Bank_CashFlow_Function_Calling
                (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody) = None_Bank_CashFlow(
                    address)
                Collective_CashFlow[len(CashFlow) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

        Report = [Balance, Collective_Balance, Loss_Gain, Collective_Loss_Gain, CashFlow, Collective_CashFlow]


    elif (company_num == '0' and report_num == '1'):
        Monthly = list()
        for i in range(len(links)):
            Monthly.append(list())
            address = links[i]
            # None_Bank_Balance_Function_Calling
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
             tbody) = None_Bank_Monthly(address)
            Monthly[i] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

        Report = Monthly


    elif (company_num == '1' and report_num == '0'):
        Balance = list()
        Loss_Gain = list()
        CashFlow = list()
        Collective_Balance = list()
        Collective_Loss_Gain = list()
        Collective_CashFlow = list()
        for i in range(len(links)):
            Balance.append(list())
            Collective_Balance.append(list())

            Loss_Gain.append(list())
            Collective_Loss_Gain.append(list())

            CashFlow.append(list())
            Collective_CashFlow.append(list())

            address = links[i]
            # Bank_Balance_Function_Calling
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
             tbody) = Bank_Balance(
                address)
            Balance[len(Balance) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

            address = address.replace('sheetId=0', 'sheetId=1')
            # Bank_LossGain_Function_Calling
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
             tbody) = Bank_LossGain(
                address)
            Loss_Gain[len(Loss_Gain) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

            address = address.replace('sheetId=1', 'sheetId=9')
            # Bank_CashFlow_Function_Calling
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
             tbody) = Bank_CashFlow(address)
            CashFlow[len(CashFlow) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

            if ('تلفیقی' in descriptions[i]):
                address = address.replace('sheetId=9', 'sheetId=12')
                # Bank_Balance_Function_Calling
                (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
                 tbody) = Bank_Balance(
                    address)
                Collective_Balance[len(Balance) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

                address = address.replace('sheetId=12', 'sheetId=13')
                # Bank_LossGain_Function_Calling
                (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
                 tbody) = Bank_LossGain(
                    address)
                Collective_Loss_Gain[len(Loss_Gain) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

                address = address.replace('sheetId=13', 'sheetId=14')
                # Bank_CashFlow_Function_Calling
                (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
                 tbody) = Bank_CashFlow(
                    address)
                Collective_CashFlow[len(CashFlow) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

        Report = [Balance, Collective_Balance, Loss_Gain, Collective_Loss_Gain, CashFlow, Collective_CashFlow]


    elif (company_num == '1' and report_num == '1'):
        Monthly = list()
        for i in range(len(links)):
            Monthly.append(list())
            address = links[i]
            # Bank_Balance_Function_Calling
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
             tbody) = Bank_Monthly(address)
            Monthly[i] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

        Report = Monthly


    elif (company_num == '2'):
        Investment = list()
        for i in range(len(links)):
            Investment.append(list())
            address = links[i]

            address = address.replace('sheetId=0', 'sheetId=4')
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
             tbody) = Invest_Stock(address)
            Investment[len(Investment) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

            Investment.append(list())
            address = address.replace('sheetId=4', 'sheetId=5')
            (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead,
             tbody) = Invest_NonStock(address)
            Investment[len(Investment) - 1] = (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

        Report = Investment

    return [Report, num_of_results]



