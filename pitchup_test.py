from itertools import combinations
 
"""
Let's find the pitch !!!
 "Join us at pitch x. x is a number between 1 and 553 such that the sum of x's
divisors (not including x) is greater than x but no subset of x's divisors add
up to exactly x.
 by Sara GAMRANI
 
"""
 
 
def divisor(root):
   """ let's get all divisors for a number  """
   divisors = []
   for i in xrange(1, root):
        if root % i == 0:
            divisors.append(i)
 
   return divisors
 
def sumCheck(divisors, total):
    """  Let's verify that the sum can't be bigger than the total     """
    return sum(divisors) > total
 
def totalSumCheck(divisors, total):
    """ Let's iterate through combinations and make sure
   nothing sums to exactly equal the total   """
    for i in xrange(2, len(divisors)):
        for j in combinations(divisors, i):
            if sum(j) == total:
                return False
 
    return True
 
def getDivisorCheck(max_amount):
    """ Finaly let's looks for the first number where the sum divisors are greater than the number but no combination of divisors sums to the number  """
    for total in xrange(max_amount):
        divisors = divisor(total)
 
        if sumCheck(divisors, total) and totalSumCheck(divisors, total):
            return total
 
if __name__ == "__main__":
    print getDivisorCheck(533)
    
