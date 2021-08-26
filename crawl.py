import urllib.request
import ssl
import parsers

import sys

def crawl_homepage(institute, homepage):
    context = ssl._create_unverified_context()
    page = urllib.request.urlopen(homepage, context=context)
    function_name = institute.lower().replace(' ', '_') + '_members'
    members = getattr(parsers, function_name)(page)
    return members

if __name__ == '__main__':
    homepages = [
            ('Koeln THP', 'https://www.thp.uni-koeln.de/members.html'),
            ('Koeln PH2', 'https://ph2.uni-koeln.de/das-institut/mitglieder/telefonliste'),
            ('Duesseldorf LS3', 'http://www.thphy.uni-duesseldorf.de/~ls3/people.html'),
            ('Bonn PI', 'https://www.pi.uni-bonn.de/members'),
            ('Aachen IQI', 'https://www.quantuminfo.physik.rwth-aachen.de/cms/Quantuminfo/Das-Institut/~snur/Mitarbeiter/lidx/1/'),
            ('Juelich IAS', 'https://www.fz-juelich.de/ias/DE/UeberUns/Mitarbeitende/_node.html')]

    if len(sys.argv) > 1 and sys.argv[1].lower() == 'test':
        for institute, homepage in homepages:
            if sys.argv[2].lower() == institute.lower():
                members = crawl_homepage(institute, homepage)
                print(members)
                break
        else:
            print('Institute {} does not exist'.format(sys.argv[2]))

        sys.exit(1)

    for institute, homepage in homepages:
        members = crawl_homepage(institute, homepage)

        if members:
            names = institute.split(' ')
            filename = names[0].capitalize() + names[1]
            with open(f'{filename}.txt', 'w') as f:
                f.writelines('\n'.join(members))
