## Description:

[Digital root](https://en.wikipedia.org/wiki/Digital_root) is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

## Examples

```
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
```

## Solution:

1\. If 'n' is less than 10, add each digit.  
2\. Repeat until a single digit appears.  
3. When a single digit is returned, it is returned.

```
def digital_root(n):    
    return (digital_root(sum([int(i) for i in str(n)])) if n >= 10 else n)
```