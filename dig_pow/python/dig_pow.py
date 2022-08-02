# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    num = str(n)
    s = sum([pow(int(num[i]), p + i) for i in range(len(num))])
    k, rem = divmod(s, n)
    if rem == 0:
        return k
    else:
        return -1
