import pandas as pd
from .utils import commons, helpers

def get_all_div_dcr_submission(fromDt, toDt):
    aipl_auto_master = commons.get_aipl_automation_master()
    combine_df=(pd.concat([
        helpers.get_report(
            reportName='dcr', 
            fromDt=fromDt, 
            toDt=toDt, 
            division_num=aipl_auto_master.get('div_num').get(div), 
            role=aipl_auto_master.get('role').get(div), 
            user=aipl_auto_master.get('user').get(div),
            forMon=None
            ) 
        for div in list(aipl_auto_master.index)
        ]) )
    return combine_df

def get_report_general(reportName,fromDt, toDt):
    aipl_auto_master = commons.get_aipl_automation_master()
    combine_df=(pd.concat([
        helpers.get_report(
            reportName=reportName, 
            fromDt=fromDt, 
            toDt=toDt, 
            division_num=aipl_auto_master.get('div_num').get(div), 
            role=aipl_auto_master.get('role').get(div), 
            user=aipl_auto_master.get('user').get(div),
            forMon=None
            ) 
        for div in list(aipl_auto_master.index)
        ]) )
    return combine_df
    


def main():
    pass
if __name__ == '__main__':
    main()