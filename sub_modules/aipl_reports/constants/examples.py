from utils import helpers
from automations import get_all_div_dcr_submission


aipl_auto_master = helpers.get_aipl_automation_master()
div='dc'
mtp = helpers.get_report(
    reportName='mtp', 
    fromDt='2022-04-10', 
    toDt='2022-04-20', 
    division_num=aipl_auto_master.get('div_num').get(div), 
    role=aipl_auto_master.get('role').get(div), 
    user=aipl_auto_master.get('user').get(div),
    forMon='4'
    )

# Get all divisions data
g = get_all_div_dcr_submission(fromDt='2022-04-10', toDt='2022-04-20')