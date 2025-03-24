import unittest
##Statement coverage
def f(a):
    if a > 0:
        a -= 1

    if a == 0:
        print('hello')
    return a

##Branch coverage
##A
def f2(a, b):
    if a > 0 and b > 0:
        a += 1
    else:
        b += 1
    return a + b

##B
def f3(a, b):
    if a > 0 and b > 0:
        a += 1
    return a + b

##C
def f4(a):
    def g(a):
        if a < 0: #test a inside g
            raise ValueError("a should be positive") #raise exception inside g
        return a - 1
    
    if a <= 0: #test a inside f4
        raise ValueError("a should be positive") #raise exception inside f4
        
    return g(a + 1)


##Minimal test
def f5(a, b):
    if (a == 1): 
        print('hello')
    
    if (b == 1):
        print('world')

    return a + b

class TestCases(unittest.TestCase):
    def test_f(self):
        self.assertEqual( f(0), 0)
        self.assertEqual( f(1), 0)
        self.assertEqual( f(-1), -1)
    
    # def test_f2_statement(self):
    #     self.assertEqual( f2(1, 1), 3) #both > 0
    #     self.assertEqual( f2(1, -1), 1) #b < 0
    #     self.assertEqual( f2(-1, 1), 1) #a < 0
    #     self.assertEqual( f2(-1, -1), -1) #both < 0

    def test_f2_statement(self):
        self.assertEqual( f2(1, 1), 3) #a > 0
        self.assertEqual( f2(1, -1), 1) # b <= 0

    def test_f2_branch(self):
        self.assertEqual( f2(1, 1), 3) #a > 0
        self.assertEqual( f2(1, -1), 1) # b <= 0
    
    def test_f3_statement(self):
        self.assertEqual( f3(1, 1), 3)
    
    def test_f3_branch(self):
        self.assertEqual( f3(1, 1), 3) # a > 0 true, b > 0 true
        self.assertEqual( f3(1, -1), 0) # a > 0 true, b > 0 false
    
    def test_f4_statement(self):
        self.assertEqual(f4(1), 1) #a > 0
        try: 
            self.assertEqual(f4(0), 0) #a = 0
        except ValueError:
            pass
        try: 
            self.assertEqual(f4(-1), -2) #a < 0
        except ValueError:
            pass
    
    # def test_f5(self):
    #     self.assertEqual(f5(1, 0), 1)
    #     self.assertEqual(f5(0, 1), 1)
    
    def test_f5_minimal_statement(self):
        self.assertEqual(f5(1, 1), 2)
    
    def test_f5_minimal_branch(self):
        self.assertEqual(f5(1, 0), 2) # a true, b false hello 
        self.assertEqual(f5(0, 1), 1) # a false, b true world
        
if __name__ == "__main__":
    unittest.main()

##Coverage
## coverage run Week5.py
## coverage report -m
## coverage html