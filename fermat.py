import random


def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)


# Time complexity 0(n^3)
# Space complexity 0(n^2)
# We use a recursive algorithm with intermediate computations modulo N to make sure number doesn't grow too large
def mod_exp(x, y, N):
    # base case
    if y == 0:
        return 1
    
    # recursive call
    z = mod_exp(x, y // 2, N)


    if y % 2 == 0:
        #even y's
        return z**2 % N

    else:
        # odd y's
        return x * (z**2) % N
	

def fprobability(k):
    # the error probability is 1 /2 **k, so we subtract from one to get the success probability
    return 1 - (1 / 2**k)


def mprobability(k):
    # the error probability is 1 /4 **k, so we subtract from one to get the success probability
    return 1 - (1 / 4 ** k)

# Time complexity 0(n^3 * k)
# Space complexity 0(n^2)
def fermat(N,k):
    # we loop through k times with a different base and call mod_exp(). We return composite immediately if the return value of mod_exp != 1
    for x in range(k):
        randBase = random.randint(1, N-1)
        if mod_exp(randBase, N-1, N) != 1:
            return 'composite'

    # if get to the end of the loop, we conclude that N is prime
    return 'prime'

# Time complexity 0(n^4 * k)
# Space complexity
def miller_rabin(N,k):
    #if its even, return composite
    if N%2 == 0 and N != 2:
        return 'composite'

   # for k times, perform the miller rabin test, if a test returns composite, return composite
    for x in range(k):
        a = random.randint(1, N-1)
        solution = miller_rabin_helper(a, N)

        if solution == 'composite':
            return 'composite'

    #return prime if all tests pass
    return 'prime'

# Time complexity 0(n^4)
def miller_rabin_helper(a, N):
    power = N-1

    # while the power is even, call mod_exp
    while power % 2 == 0:
        power_output = mod_exp(a, power, N)

        # if a ** power mod N is -1, return prime
        if power_output == N-1:
            return 'prime'

        # if a ** power mod N is anything but -1 or 1, return prime
        elif power_output != 1:
            return 'composite'

        #update power
        power = power / 2

    # the final test if the final power is odd and we haven't returned yet
    power_output = mod_exp(a, power, N)

    # if a ** power mod N is is -1 or 1, return prime
    if power_output == 1 or power_output == N-1:
        return 'prime'
    else:
        return 'composite'

