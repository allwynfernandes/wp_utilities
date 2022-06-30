import pandas as pd
from . import commons


def get_report(reportName=None, fromDt:str=None, toDt:str=None, division_num:str=None, role:str=None, user:str=None, forMon:str=None, silent=True):
    '''
    reportName='mtp', # mpt |stp |dcr 
    fromDt='2022-04-10', 
    toDt='2022-04-20', 
    division_num=aipl_auto_master.get('div_num').get(div), 
    role=aipl_auto_master.get('role').get(div), 
    user=aipl_auto_master.get('user').get(div),
    forMon='4'

    '''
    if not(reportName):
        print("No report name entered")
        return None

    elif reportName=='dcr':
        count_skip_rows=0
        params = {
            'module': 'Reports',
            'menuid': '17',
            'action': 'CreateXLdcrsubmissioncontrolsheet',
            'division': division_num,
            'role': role,
            'user': user,
            'frm_date': fromDt,
            'to_date': toDt,
        }
        data='null'
        
    elif reportName=='stp':
        count_skip_rows=2
        params = {
            'module': 'Reports',
            'action': 'stpstatus',
            'all': '1',
            'return_module': 'Reports',
            'return_action': 'index',
        }
        data = {
            'division': division_num,
            'designate': role,
            'designate1': f'{role}|{division_num}',
            'user': f'{user}|{role}',
            'hdnuser': '90|4',
            'year': fromDt[:4]+'-'+toDt[2:4],
            'action': 'CreateXLstpstatus',
            'query': 'true',
            'module': 'Reports',
            'order_by': '',
            'sorder': '',
            'profile': '1',
            'currenttitle': 'SFE',
            'xldivision': '',
            'xldesignate': '',
            'xluser': '',
            'xlyear': '',
            'button': 'Create XL',
        }

    elif reportName=='mtp':
        count_skip_rows=2
        params = {
            'module': 'Reports',
            'action': 'mtpstatusrep',
            'all': '1',
            'return_module': 'Reports',
            'return_action': 'index',
        }

        data = {
            'division': division_num,
            'designate': role,
            'designate1':  f'{role}|{division_num}',
            'user':  f'{user}|{role}',
            'hdnuser': '90|4',
            'month': forMon,
            'year': fromDt[:4],
            'action': 'CreateXLmtpstatusrep',
            'query': 'true',
            'module': 'Reports',
            'monthselected': f'{forMon}#',
            'order_by': '',
            'sorder': '',
            'profile': '1',
            'currenttitle': 'SFE',
            'xldivision': '',
            'xldesignate': '',
            'xluser': '',
            'xlmonthselected': '',
            'xlyear': '',
            'button': 'Create XL',
        }

    else: 
        print("Report does not exist")
        return None
    print("Pulling: ",reportName, "\nDivision: ", division_num, "\nPeriod: ", fromDt, " ", toDt)
    report = commons.get_data(data=data, params=params, count_skip_rows=count_skip_rows)
    return report










def main():
    pass
if __name__ == '__main__':
    main()