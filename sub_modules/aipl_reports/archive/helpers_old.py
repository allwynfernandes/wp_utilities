
def get_dcr_submission_df(reportAction=None, fromDt:str=None, toDt:str=None, division_num:str=None, role:str=None, user:str=None, forMon:str=None, silent=True):
    '''
    reportAction='mtpstatusrep'|'dcrsubmissioncontrolsheet'| 'stpstatus'
    fromDt='2022-06-10'
    toDt='2022-06-20'
    division_num='1'
    role='32'
    user='551'
    forMon='7'
    forYear='2021-2022'
    silet=True

    '''

    # param data selection based on report name
    if reportAction=='dcrsubmissioncontrolsheet':
        df_num=2
        data = 'null'
        params = {
            'module': 'Reports',
            'action': reportAction,
            'query': 'true',
            'lstmodule': 'Reports',
            'lstaction': 'Reports_subsectionlistView',
            'lstcase': 'Reports',
            'division': division_num,
            'role': role, # Con
            'user': user, # 
            'frm_date': fromDt,
            'to_date': toDt,
            'where': '',
        }

    if reportAction=='mtpstatusrep':
        df_num=24
        data = {
            'division': division_num,
            'designate': role,
            'designate1': f'{role}|{division_num}',
            'user': f'{user}|{role}',
            'hdnuser': '90|4',
            'month': forMon,
            'year': fromDt[:4],
            'action': reportAction,
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
            'button': 'Generate',
            }
        params = {
            'module': 'Reports',
            'action': reportAction,
            'all': '1',
            'return_module': 'Reports',
            'return_action': 'index',
            }

    if reportAction=='stpstatus':
        df_num=24
        data = {
            'division': division_num,
            'designate': role,
            'designate1': f'{role}|{division_num}',
            'user': f'{user}|{role}',
            'hdnuser': '90|4',
            'month': forMon,
            'year': fromDt[:4]+'-'+toDt[2:4],
            'action': reportAction,
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
            'button': 'Generate',
            }
        params = {
            'module': 'Reports',
            'action': reportAction,
            'all': '1',
            'return_module': 'Reports',
            'return_action': 'index',
        }

    if not(silent):
        print(data)

    print("Pulling: ",reportAction, "\nDivision: ", division_num, "\nPeriod: ", fromDt, " ", toDt)

    cookies, headers = commons.get_login('sfe', 'user@123')
    response = requests.post('https://mywallace.in/Wallace/index.php', params=params, cookies=cookies, headers=headers, data=data)

    # Final df selection based on selected report
    html_df = pd.read_html(response.text)#[df_num]
    # xl_df = pd.read_excel(response.content, engine='xlrd') 

    # DF Processing
    if reportAction=='stpstatus':
        html_df=html_df.droplevel(level=0, axis=1)
    
    return html_df





def get_all_div_dcr_submission(fromDt, toDt, forMon):
    aipl_auto_master = get_aipl_automation_master()
    combine_df=(pd.concat([
        get_dcr_submission_df(
            reportAction='dcrsubmissioncontrolsheet', 
            fromDt=fromDt, 
            toDt=toDt, 
            division_num=aipl_auto_master.get('div_num').get(div), 
            role=aipl_auto_master.get('role').get(div), 
            user=aipl_auto_master.get('user').get(div),
            forMon=forMon
            ) 
        for div in list(aipl_auto_master.index)
        ]) )
    return combine_df

