def an_bisect(an):
    if (an % 4 == 0) and (an % 100 != 0 or an % 400 == 0):
        return True 
    return False

def test_an_bisect():
    assert an_bisect(2019) == False, "Nu este an bisect"
    assert an_bisect(2024) == True, "Nu este an bisect"
    assert an_bisect(1989) == False, "Nu este an bisect"
    assert an_bisect(2100) == True, "Nu este an bisect"


test_an_bisect()