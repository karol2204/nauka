import sys

evenNumberGenerator = (element
                       for element in range(100)
                       if (element % 2 == 0)
                       )
print(sum(evenNumberGenerator))
