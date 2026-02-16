def notes(*n, sit=False):
    """
    -> Function to analyze grades and situations of multiple students
    :stop n: one or more student grades (multiple aproved)
    :stop sit: opcional value, indicating or no if add the situation
    :return: dict with variable informations about the class situation
    """
    r = dict()
    r['total'] = len(n)
    r['Bigger'] = max(n)
    r['Minor'] = min(n)
    r['Average'] = sum(n)/len(n)
    
    if sit:
        if r['Average'] >= 9.5:
            r['situation'] = 'APROVED!'
        else:
            r['situation'] = 'Failed!'
    return r

# Main program
answ = notes(6.5, 9, 13.4, sit=True)
print(answ)
