## ------- Binary Gap -----------------
# A binary gap within a positive integer N is any maximal sequence of consecutive
# zeros that is surrounded by ones at both ends in the binary representation of N.
# For example, number 9 has binary representation 1001 and contains a binary gap
# of length 2. The number 529 has binary representation 1000010001 and contains
# two binary gaps: one of length 4 and one of length 3. The number 20 has binary
# representation 10100 and contains one binary gap of length 1. The number 15 has
# binary representation 1111 and has no binary gaps. The number 32 has binary
# representation 100000 and has no binary gaps.

# Write a function that given a positive integer N, returns the length of its
# longest binary gap. The function should return 0 if N doesn't contain a binary
# gap.

# For example, given N = 1041 the function should return 5, because N has binary 
# representation 10000010001 and so its longest binary gap is of length 5. Given
# N = 32 the function should return 0, because N has binary representation
# '100000' and thus no binary gaps.

#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [1..2,147,483,647].

## ------ version 1 ----------
def count_gap(x):
    """
        Perform Find the longest sequence of zeros between ones "gap" in binary representation of an integer

        Parameters
        ----------
        x : int
            input integer value

        Returns
        ----------
        max_gap : int
            the maximum gap length

    """
    try:
        # Convert int to binary
        b = "{0:b}".format(x)
        # Iterate from right to lift 
        # Start detecting gaps after fist "one"
        for i,j in enumerate(b[::-1]):
            if int(j) == 1:
                max_gap = max([len(i) for i in b[::-1][i:].split('1') if i])
                break
    except ValueError:
        print("Oops! no gap found")
        max_gap = 0
    return max_gap