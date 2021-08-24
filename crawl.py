import urllib.request
import ssl
import parsers

if __name__ == '__main__':
    homepages = [
            ('koeln THP', 'https://www.thp.uni-koeln.de/members.html'),
            ('koeln PH2', 'https://ph2.uni-koeln.de/das-institut/mitglieder/telefonliste'),
            ('duesseldorf LS3', 'http://www.thphy.uni-duesseldorf.de/~ls3/people.html'),
            ('bonn PI', 'https://www.pi.uni-bonn.de/members'),
            ('aachen IQI', 'https://www.quantuminfo.physik.rwth-aachen.de/cms/Quantuminfo/Das-Institut/~snur/Mitarbeiter/lidx/1/'),
            ('juelich IAS', 'https://www.fz-juelich.de/ias/DE/UeberUns/Mitarbeitende/_node.html')]

    for institute, homepage in homepages:
        context = ssl._create_unverified_context()
        page = urllib.request.urlopen(homepage, context=context)

        function_name = institute.lower().replace(' ', '_') + '_members'
        members = getattr(parsers, function_name)(page)
        if members:
            names = institute.split(' ')
            filename = names[0].capitalize() + names[1]
            with open(f'{filename}.txt', 'w') as f:
                f.writelines('\n'.join(members))
