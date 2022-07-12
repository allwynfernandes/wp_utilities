import datetime
import pandas as pd
from . import commons
from .. import automations
from io import BytesIO


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
    # forMon = datetime.datetime.strptime(fromDt, '%Y-%m-%d').month
    forMon = fromDt.month
    print(fromDt)

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
            'year': str(fromDt)[:4]+'-'+str(toDt)[2:4],
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
            'year': str(fromDt)[:4],
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






def get_ready_report(excelName='dcr_excel', fromDt=None, toDt=None):
    if excelName=='dcr_excel':
        df = automations.get_report_general(reportName='dcr', fromDt=fromDt, toDt=toDt)
        df = df.rename(columns={"DAYS 'R'":'wd'})
        df.loc[df.wd == 0, 'DCR Count Category'] = '0 - No DCR'
        df.loc[(df.wd >=1) & (df.wd<=3), 'DCR Count Category'] = '1-3'
        df.loc[(df.wd >=4) & (df.wd<=6), 'DCR Count Category'] = '4-6'
        df.loc[df.wd >6, 'DCR Count Category'] = '< 6'

        output = BytesIO()
        with pd.ExcelWriter(output) as writer:
            for div in df.Division.unique():
                df[df['Division']== div].pivot_table(index=['Division', 'Zone', 'Designation'], columns='DCR Count Category', values='Emp code', aggfunc='count', margins=True, margins_name='Total').to_excel(writer, sheet_name=div)
        processed_data = output.getvalue()
    return processed_data    



def main():
    pass
if __name__ == '__main__':
    main()