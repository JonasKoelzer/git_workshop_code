from bs4 import BeautifulSoup

def koeln_thp_members(html):
    members = []
    soup = BeautifulSoup(html, 'html5lib')
    member_table = soup.find('div', class_ = 'textcontainer_mitte').table
    group = None

    include_groups = set(['Professors', 'Scientific members', 'Administration'])
    for row in member_table.find_all('tr'):
        if cols := row.find_all('th'):
            group = ''.join(cols[1].strings).strip()
            continue

        if group in include_groups:
            cols = list(row.find_all('td'))
            members.append(cols[1].string)

    return members

def koeln_ph2_members(html):
    pass

def duesseldorf_ls3_members(html):
    pass

def bonn_pi_members(html):
    pass

def aachen_iqi_members(html):
    pass

def juelich_ias_members(html):
    pass
