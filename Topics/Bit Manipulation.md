- [Bit Manipulation for python](https://weikaiwei.com/python/python-bitwise/)
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
```

![[Pasted image 20240429122716.png]]