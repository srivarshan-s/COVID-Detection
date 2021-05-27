doctor = [
    {
        'id': 1,
        'name': 'Doctor1',
        'place': 'Chennai',
        'fee': 500
    },
    {
        'id': 2,
        'name': 'Doctor2',
        'place': 'Mumbai',
        'fee': 900
    },
    {
        'id': 3,
        'name': 'Doctor3',
        'place': 'Bangalore',
        'fee': 700
    },
    {
        'id': 4,
        'name': 'Doctor4',
        'place': 'Delhi',
        'fee': 1100
    },
    {
        'id': 5,
        'name': 'Doctor5',
        'place': 'Kolkata',
        'fee': 800
    },
    {
        'id': 6,
        'name': 'Doctor6',
        'place': 'Chennai',
        'fee': 400
    },
]


def printData():
    for i in doctor:
        print(i['id'], end=', ')
        print(i['name'], end=', ')
        print(i['place'])
