def teste(p1, p2):    
    try:
        assert p1.distânciaAté(p2) == p2.distânciaAté(p1)
        return True
    except AssertionError:
        return False