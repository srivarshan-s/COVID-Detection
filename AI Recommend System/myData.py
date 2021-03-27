doctor = [
    {
        'id': 1,
        'name': 'Doctor1',
        'place': 'Chennai'
    },
    {
        'id': 2,
        'name': 'Doctor2',
        'place': 'Mumbai'
    },
    {
        'id': 3,
        'name': 'Doctor3',
        'place': 'Bangalore'
    },
    {
        'id': 4,
        'name': 'Doctor4',
        'place': 'Delhi'
    },
    {
        'id': 5,
        'name': 'Doctor5',
        'place': 'Kolkata'
    },
    {
        'id': 6,
        'name': 'Doctor6',
        'place': 'Chennai'
    },
]


def printData():
    for i in doctor:
        print(i['id'], end=', ')
        print(i['name'], end=', ')
        print(i['place'])
