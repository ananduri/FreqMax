def test1():
    kmax = KMax()
    data = ['1', '2', '3', '0', '1', '2', '3', '3', '1', '3', '3', '0']
    for d in data:
        kmax.add(d)
    print(kmax.display())
    
def test2():
    kmax = KMax()
    data = ['1', '2', '3', '0', '1', '2', '3', '3', '1', '3', '3', '0']
    for d in data:
        kmax.add(d)
    g = kmax.getmax(3)
    assert(list(g) == ['3', '1', '2'])
