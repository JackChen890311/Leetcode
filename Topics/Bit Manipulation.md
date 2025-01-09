- [Bitwise operation for python](https://weikaiwei.com/python/python-bitwise/)
- [Python的位元運算 - HackMD](https://hackmd.io/@apcser/H14FONT4n?utm_source=preview-mode&utm_medium=rec)
```python=
>>> bin(13)
'0b1101'
>>> bin(200)
'0b11001000'
>>> int(bin(200),2)
200
>>> int(bin(200)[2:],2)
200
>>> 1 << 3 # 2 ^ 3
8
>>> '1011'.zfill(8)
'00001011'
>>> x = 5  # 101
>>> x.bit_length()
>>> 3
```

![[Pasted image 20240429122716.png]]