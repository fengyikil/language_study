def test1():
    import cal.cal_add  
    print(cal.cal_add.add(1,1))

def test2():
    import cal.cal_add as cal 
    print(cal.add(2,2))

def test3():
    from cal import cal_add 
    print(cal_add.add(3,3))

def test4():
    from cal.cal_add  import add
    print(add(4,4))

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()