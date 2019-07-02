import requests
from bs4 import BeautifulSoup
import urllib3

def Bank_Balance(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id':'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id':'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id':'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir':'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id':'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id':'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    main_table = soup.find("table",attrs={'class':'Grid table_wrapper'})
    vals = main_table.find_all("span")
    head = main_table.find_all("th")

    thead = list()
    if (not soup.find("table",attrs={'class':'Grid table_wrapper'})):
        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
    else:
        for i in range (1, len(head)):
            if ('Hidden' not in head[i].attrs['class']):
                thead.append(head[i].text)

        tbody = list()
        iter = -1
        for i in range (len(vals)):
            if (i % 8 == 0):
                tbody.append(list())
                iter = iter + 1

            p = vals[i].text

            if ((i % 8 != 0 and i % 8 != 4) and '/' not in p and p != '--'):
                if (p != '' and '(' not in p):
                    ps = p.split(',')
                    p = ''
                    for h in range(len(ps)):
                        p = p + ps[h]
                    p = int(p)

                elif (p != '' and '(' in p):
                    p = p.replace('(', '')
                    p = p.replace(')', '')
                    ps = p.split(',')
                    p = ''
                    for h in range(len(ps)):
                        p = p + ps[h]
                    p = int(p)
            tbody[iter].append(p)

        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)


def None_Bank_Balance(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id':'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id':'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id':'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir':'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id':'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id':'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    main_table = soup.find("table",attrs={'class':'Grid table_wrapper'})
    vals = main_table.find_all("span")
    head = main_table.find_all("th")

    thead = list()
    if (not soup.find("table",attrs={'class':'Grid table_wrapper'})):
        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
    else:
        for i in range (1, len(head)):
            if ('Hidden' not in head[i].attrs['class']):
                thead.append(head[i].text)

        tbody = list()
        iter = -1
        for i in range (len(vals)):
            if (i % 8 == 0):
                tbody.append(list())
                iter = iter + 1

            p = vals[i].text

            if ((i % 8 != 0 and i % 8 != 4) and '/' not in p and p != '--'):
                if (p != '' and '(' not in p):
                    ps = p.split(',')
                    p = ''
                    for h in range(len(ps)):
                        p = p + ps[h]
                    p = int(p)

                elif (p != '' and '(' in p):
                    p = p.replace('(', '')
                    p = p.replace(')', '')
                    ps = p.split(',')
                    p = ''
                    for h in range(len(ps)):
                        p = p + ps[h]
                    p = int(p)
            tbody[iter].append(p)

        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)


def Bank_CashFlow(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id': 'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id': 'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id': 'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir': 'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id': 'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id': 'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    head = soup.find("tr", attrs={'class': 'GridHeader'})
    side_table1 = soup.find("table", attrs={'class': 'GridCF'})

    thead = list()
    if (not soup.find("tr", attrs={'class': 'GridHeader'})):
        return ('', '', '', '', '', '', list(), list())
    else:
        for i in range(1, len(head.contents), 2):
            p = head.contents[i].text
            sudo = p.split()
            p = ''
            for j in range(len(sudo)):
                if (j != 0):
                    p = p + ' '
                p = p + sudo[j]
            thead.append(p)

        tbody = list()
        if (not soup.find("tr", attrs={'class': 'GridHeader'})):
            return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
        else:
            for i in range(1, len(side_table1.contents) - 1):
                tbody.append(list())
                for j in range(1, len(side_table1.contents[i].contents) - 1):
                    if (j == 1):
                        p = side_table1.contents[i].contents[j].text
                        sudo = p.split()
                        p = ''
                        for k in range(len(sudo)):
                            if (k != 0):
                                p = p + ' '
                            p = p + sudo[k]
                        tbody[i - 1].append(p)

                    else:
                        L = len(side_table1.contents[i].contents[j].contents)
                        if (L > 1 and len(side_table1.contents[i].contents[j].contents[1].attrs) != 0):
                            p = side_table1.contents[i].contents[j].contents[1].attrs['value']
                        elif (len(side_table1.contents[i].contents[j].attrs) != 0):
                            p = side_table1.contents[i].contents[j].contents[1].attrs['value']
                        else:
                            p = ''

                        if ('/' not in p and p != '--'):
                            if (p != '' and '(' not in p):
                                ps = p.split(',')
                                p = ''
                                for h in range(len(ps)):
                                    p = p + ps[h]
                                p = int(p)

                            elif (p != '' and '(' in p):
                                p = p.replace('(', '')
                                p = p.replace(')', '')
                                ps = p.split(',')
                                p = ''
                                for h in range(len(ps)):
                                    p = p + ps[h]
                                p = int(p)

                        tbody[i - 1].append(p)

            return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

def None_Bank_CashFlow(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id': 'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id': 'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id': 'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir': 'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id': 'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id': 'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    head = soup.find("tr", attrs={'class': 'GridHeader'})
    side_table1 = soup.find("table", attrs={'class': 'GridCF'})

    thead = list()
    if (not soup.find("tr", attrs={'class': 'GridHeader'})):
        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
    else:
        for i in range(1, len(head.contents), 2):
            p = head.contents[i].text
            sudo = p.split()
            p = ''
            for j in range(len(sudo)):
                if (j != 0):
                    p = p + ' '
                p = p + sudo[j]
            thead.append(p)

        tbody = list()

        for i in range(1, len(side_table1.contents) - 1):
            tbody.append(list())
            for j in range(1, len(side_table1.contents[i].contents) - 1):
                if (j == 1):
                    p = side_table1.contents[i].contents[j].text
                    sudo = p.split()
                    p = ''
                    for k in range(len(sudo)):
                        if (k != 0):
                            p = p + ' '
                        p = p + sudo[k]
                    tbody[i - 1].append(p)

                else:
                    L = len(side_table1.contents[i].contents[j].contents)
                    if (L > 1 and len(side_table1.contents[i].contents[j].contents[1].attrs) != 0):
                        p = side_table1.contents[i].contents[j].contents[1].attrs['value']
                    elif (len(side_table1.contents[i].contents[j].attrs) != 0):
                        p = side_table1.contents[i].contents[j].contents[1].attrs['value']
                    else:
                        p = ''

                    if ('/' not in p and p != '--'):
                        if (p != '' and '(' not in p):
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)

                        elif (p != '' and '(' in p):
                            p = p.replace('(', '')
                            p = p.replace(')', '')
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)

                    tbody[i - 1].append(p)

        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

def Bank_LossGain(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id': 'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id': 'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id': 'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir': 'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id': 'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id': 'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    head = soup.find("tr", attrs={'class': 'GridHeader'})
    side_table1 = soup.find("table", attrs={'class': 'Grid table_wrapper'})

    thead = list()
    for i in range(1, len(head.contents), 2):
        p = head.contents[i].text
        sudo = p.split()
        p = ''
        for j in range(len(sudo)):
            if (j != 0):
                p = p + ' '
            p = p + sudo[j]
        thead.append(p)

    tbody = list()
    iter = -1
    if (not soup.find("tr", attrs={'class': 'GridHeader'})):
        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
    else:
        for i in range(1, len(side_table1.contents) - 1):
            if (side_table1.contents[i].attrs['class'] != ['HiddenRow']):
                tbody.append(list())
                iter = iter + 1
                for j in range(2, len(side_table1.contents[i].contents) - 1):
                    p = side_table1.contents[i].contents[j].text
                    sudo = p.split()
                    p = ''
                    for k in range(len(sudo)):
                        if (k != 0):
                            p = p + ' '
                        p = p + sudo[k]
                    if ('/' not in p and p != '--'):
                        if (j != 2 and p != '' and '(' not in p):
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)

                        elif (j != 2 and p != '' and '(' in p):
                            p = p.replace('(', '')
                            p = p.replace(')', '')
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)
                    tbody[iter].append(p)

        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)


def None_Bank_LossGain(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id': 'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id': 'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id': 'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir': 'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id': 'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id': 'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    head = soup.find("tr", attrs={'class': 'GridHeader'})
    side_table1 = soup.find("table", attrs={'class': 'Grid table_wrapper'})

    thead = list()
    if (not soup.find("tr", attrs={'class': 'GridHeader'})):
        return ('', '', '', '', '', '', list(), list())
    else:
        for i in range(1, len(head.contents), 2):
            p = head.contents[i].text
            sudo = p.split()
            p = ''
            for j in range(len(sudo)):
                if (j != 0):
                    p = p + ' '
                p = p + sudo[j]
            thead.append(p)

        tbody = list()
        iter = -1
        if (not soup.find("table", attrs={'class': 'Grid table_wrapper'})):
            return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
        else :
            for i in range(1, len(side_table1.contents) - 1):
                if (side_table1.contents[i].attrs['class'] != ['HiddenRow']):
                    tbody.append(list())
                    iter = iter + 1
                    for j in range(2, len(side_table1.contents[i].contents) - 1):
                        p = side_table1.contents[i].contents[j].text
                        sudo = p.split()
                        p = ''
                        for k in range(len(sudo)):
                            if (k != 0):
                                p = p + ' '
                            p = p + sudo[k]

                        if ('/' not in p and p != '--'):
                            if (j != 2 and p != '' and '(' not in p):
                                ps = p.split(',')
                                p = ''
                                for h in range(len(ps)):
                                    p = p + ps[h]
                                p = int(p)

                            elif (j != 2 and p != '' and '(' in p):
                                p = p.replace('(', '')
                                p = p.replace(')', '')
                                ps = p.split(',')
                                p = ''
                                for h in range(len(ps)):
                                    p = p + ps[h]
                                p = int(p)
                        tbody[iter].append(p)

            return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

def Bank_Monthly(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id':'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id':'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id':'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir':'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id':'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id':'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    side_table1 = soup.findAll("table", attrs={'class':'gv'})

    thead = list()
    if (not soup.findAll("table", attrs={'class':'gv'})):
        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
    else:
        for i in range (2):
            thead.append(list())
            for j in range(1, len(side_table1[2*i].contents[1].contents), 2):
                t = side_table1[2*i].contents[1].contents[j].text
                t = t.replace('\n', '')
                thead[i].append(t)

        tbody = list()
        for i in range (2):
            tbody.append(list())
            for j in range(1, len(side_table1[2*i+1].contents) - 1):
                tbody[i].append(list())
                for k in range (1, len(side_table1[2*i+1].contents[j].contents ) - 1) :
                    p = side_table1[2*i+1].contents[j].contents[k].text
                    sudo = p.split('\n')
                    if len(sudo) == 1:
                        pass
                    else:
                        p = p.split('\n')
                        p = p[2]

                    if (k != 1 and '/' not in p and p != '--'):
                        if (p != '' and '(' not in p):
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)

                        elif (p != '' and '(' in p):
                            p = p.replace('(', '')
                            p = p.replace(')', '')
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)
                    tbody[i][j-1].append(p)

        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)


def None_Bank_Monthly(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id': 'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id': 'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id': 'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir': 'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id': 'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id': 'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    if (soup.find("table", attrs={'id': 'ctl00_cphBody_ucProduct2_dgProduction'}) is not None):
        side_table1 = soup.find("table", attrs={'id': 'ctl00_cphBody_ucProduct2_dgProduction'})
    else:
        side_table1 = soup.find("table", attrs={'id': 'ctl00_cphBody_ucProduct1_dgProduction'})

    side_table2 = soup.find("table", attrs={'class': 'gv'})

    thead = list()
    if (not soup.find("table", attrs={'class': 'gv'})):
        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
    else:
        for i in range(1, len(side_table2.contents), 2):
            tr = side_table2.contents[i].text
            tr = tr.split('\n')
            while ('' in tr):
                tr.remove('')
            thead.append(tr)

        tbody = list()
        for i in range(1, len(side_table1.contents) - 1):
            tbody.append([])
            for j in range(1, len(side_table1.contents[i].contents) - 1):
                p = side_table1.contents[i].contents[j].text
                tbody[i - 1].append(p)

        if (len(tbody[len(tbody) - 1]) > 11):
            imp_rows = [0, 5, 8, 12, 16, 20]
        else:
            imp_rows = [0, 5, 9]
        parse_last_row = list()
        for i in range(len(tbody[len(tbody) - 1])):
            if i in imp_rows:
                parse_last_row.append(tbody[len(tbody) - 1][i])

        tbody[len(tbody) - 1] = parse_last_row

        for i in range(len(tbody)):
            for j in range(len(tbody[i])):
                p = tbody[i][j]
                if (j != 0 and j != 1 and i != (len(tbody) - 1) and '/' not in p and p != '--'):
                    if (p != '' and '(' not in p):
                        ps = p.split(',')
                        p = ''
                        for h in range(len(ps)):
                            p = p + ps[h]
                        p = int(p)

                    elif (p != '' and '(' in p):
                        p = p.replace('(', '')
                        p = p.replace(')', '')
                        ps = p.split(',')
                        p = ''
                        for h in range(len(ps)):
                            p = p + ps[h]
                        p = int(p)


                elif (j != 0 and i == (len(tbody) - 1) and '/' not in p and p != '--'):
                    if (p != '' and '(' not in p):
                        ps = p.split(',')
                        p = ''
                        for h in range(len(ps)):
                            p = p + ps[h]
                        p = int(p)

                    elif (p != '' and '(' in p):
                        p = p.replace('(', '')
                        p = p.replace(')', '')
                        ps = p.split(',')
                        p = ''
                        for h in range(len(ps)):
                            p = p + ps[h]
                        p = int(p)

                tbody[i][j] = p

        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)

def Invest_NonStock(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id': 'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id': 'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id': 'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir': 'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id': 'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id': 'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    head = soup.find("tr", attrs={'class': 'GridHeader'})

    side_table = soup.findAll("td")

    if (not soup.findAll("td")):
        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
    else:
        thead = list()
        thead.append(list())
        for i in range(1, len(head.contents) - 1):
            # if (len(head.contents[i].contents) != 0):
            thead[0].append(head.contents[i].contents)

        head = head.nextSibling
        thead.append(list())
        for i in range(1, len(head.contents) - 1):
            thead[1].append(head.contents[i].contents)

        index = [4, 6, 8]
        tbody = list()
        length = int(len(side_table) / len(thead[1]))
        for i in range(length):
            tbody.append(list())
            for j in range(len(thead[1])):
                p = side_table[i * len(thead[1]) + j].text
                if (j != 0 and j != 7 and i != length - 1):
                    if ('/' not in p and p != '--'):
                        if (p != '' and '(' not in p):
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)

                        elif (p != '' and '(' in p):
                            p = p.replace('(', '')
                            p = p.replace(')', '')
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)

                elif (j == 7 and i != length - 1):
                    p = float(p)

                elif (i == length - 1):
                    if (j not in index and j == 0):
                        pass
                    elif (j not in index):
                        p = ''
                    else:
                        if ('/' not in p and p != '--'):
                            if (p != '' and '(' not in p):
                                ps = p.split(',')
                                p = ''
                                for h in range(len(ps)):
                                    p = p + ps[h]
                                p = int(p)

                            elif (p != '' and '(' in p):
                                p = p.replace('(', '')
                                p = p.replace(')', '')
                                ps = p.split(',')
                                p = ''
                                for h in range(len(ps)):
                                    p = p + ps[h]
                                p = int(p)

                tbody[i].append(p)

        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)


def Invest_Stock(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    soup = BeautifulSoup(requests.get(url, verify=False).text, features='html.parser')

    alias = soup.find("span", attrs={'id': 'ctl00_txbSymbol'})
    alias = alias.text

    rep_id = soup.find("span", attrs={'id': 'ctl00_lblReportName'})
    rep_id = rep_id.text

    rep_nmonth = soup.find("span", attrs={'id': 'ctl00_lblPeriod'})
    rep_nmonth = rep_nmonth.text

    rep_month_end = soup.find("bdo", attrs={'dir': 'ltr'})
    rep_month_end = rep_month_end.text

    rep_audit = soup.find("span", attrs={'id': 'ctl00_lblIsAudited'})
    rep_audit = rep_audit.text

    rep_year_end = soup.find("span", attrs={'id': 'ctl00_lblYearEndToDate'})
    rep_year_end = rep_year_end.text

    head = soup.find("tr", attrs={'class': 'GridHeader'})

    side_table = soup.findAll("td")

    if (not soup.findAll("td")):
        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, list(), list())
    else:
        thead = list()
        thead.append(list())
        for i in range(1, len(head.contents) - 1):
            # if (len(head.contents[i].contents) != 0):
            thead[0].append(head.contents[i].contents)

        head = head.nextSibling
        thead.append(list())
        for i in range(1, len(head.contents) - 1):
            thead[1].append(head.contents[i].contents)

        index = [4, 5, 7, 8, 10, 11, 14]
        tbody = list()
        length = int(len(side_table) / len(thead[1]))
        for i in range(length):
            tbody.append(list())
            for j in range(len(thead[1])):
                p = side_table[i * len(thead[1]) + j].text
                if (j != 0 and j != 9 and i != length - 1):
                    if ('/' not in p and p != '--'):
                        if (p != '' and '(' not in p):
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)

                        elif (p != '' and '(' in p):
                            p = p.replace('(', '')
                            p = p.replace(')', '')
                            ps = p.split(',')
                            p = ''
                            for h in range(len(ps)):
                                p = p + ps[h]
                            p = int(p)

                elif (j == 7 and i != length - 1):
                    p = float(p)

                elif (i == length - 1):
                    if (j not in index and j == 0):
                        pass
                    elif (j not in index):
                        p = ''
                    else:
                        if ('/' not in p and p != '--'):
                            if (p != '' and '(' not in p):
                                ps = p.split(',')
                                p = ''
                                for h in range(len(ps)):
                                    p = p + ps[h]
                                p = int(p)

                            elif (p != '' and '(' in p):
                                p = p.replace('(', '')
                                p = p.replace(')', '')
                                ps = p.split(',')
                                p = ''
                                for h in range(len(ps)):
                                    p = p + ps[h]
                                p = int(p)

                tbody[i].append(p)

        return (alias, rep_id, rep_nmonth, rep_month_end, rep_year_end, rep_audit, thead, tbody)






