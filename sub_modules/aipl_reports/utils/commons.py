import requests
import pandas as pd
def get_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://mywallace.in/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'frame',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.head('https://mywallace.in/Wallace/index.php', headers=headers)
    return response.headers, response.cookies

def get_login(user, password):
    headers, cookies = get_page()
    payload = {
        'module': 'Users',
        'action': 'Authenticate',
        'return_module': 'Users',
        'return_action': 'Login',
        'user_name': 'sfe',
        'user_password': 'user@123',
        'Login': 'LOGIN'

    }

    with requests.Session() as session:
        r = session.post(r'https://mywallace.in/Wallace/index.php', data=payload)

        return r.cookies, r.headers





def get_session():
    s = requests.Session()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    # get root page
    print('root page')
    response = s.get('https://mywallace.in/', headers=headers)

    # get login page
    print('login')
    response = s.get('https://mywallace.in/Wallace/index.php', headers=headers)
    pa, ua = list(get_aipl().values[0])
    data = {
        'module': 'Users',
        'action': 'Authenticate',
        'return_module': 'Users',
        'return_action': 'Login',
        'user_name': pa,
        'user_password': ua,
        'Login': 'LOGIN',
    }
    # get page post login
    response = s.post('https://mywallace.in/Wallace/index.php', data=data)


    params = {
        'action': 'index',
        'module': 'Home',
    }
    # Get home page after login
    response = s.get('https://mywallace.in/Wallace/index.php', params=params)


    params = {
        'module': 'Reports',
        'action': 'index',
        'smodule': 'STANDARD',
    }
    # Get standard reports page
    response = s.get('https://mywallace.in/Wallace/index.php', params=params)
    print('standard page')

    return s




def get_data(data=None, params=None, count_skip_rows=None):

    session = get_session()
    # Generate report as Xls
    response = session.post('https://mywallace.in/Wallace/index.php', params=params, data=data)
    print('xls generated')
    
    xldata = pd.read_excel(response.content, skiprows=count_skip_rows)
    return xldata





def get_aipl_automation_master():
    return pd.read_csv('https://docs.google.com/spreadsheets/d/1SXliYc5rGqJw3u1fR4BEMNMH9I8SnBdrmJII3CJ51Sw/export?format=csv&gid=1451827471').set_index('division')





def get_aipl():
    return pd.read_csv('https://docs.google.com/spreadsheets/d/1SXliYc5rGqJw3u1fR4BEMNMH9I8SnBdrmJII3CJ51Sw/export?format=csv&gid=732906079')








def main():
    pass
if __name__ == '__main__':
    main()


