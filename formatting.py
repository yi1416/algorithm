#https://edabit.com/challenge/8pDH2SRutPoaQghgc
def relation_to_luke(name):
    relation = {'Leia':'sister',
    'Darth Vader':'father',
    'Han':'brother in law',
    'R2D2':'droid'}
    return 'Luke, I am your {}.'.format(relation[name])
    