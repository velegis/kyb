#!/bin/python
from pwn import *

p = process("/challenge/run")
p.recvuntil(b"p = 0x")
modulus = int(p.recvline().strip().decode(), 16)

g = 2

p.recvuntil(b"A = 0x")
num_A = int(p.recvline().strip().decode(), 16)

b = int("7FFFFFFF", 16)

num_B = pow(g, b, modulus)
p.sendlineafter(b"B? ", hex(num_B).encode())
s = pow(num_A, b, modulus)
p.sendlineafter(b"s? ", hex(s).encode())

print(p.readline().decode())
print(p.readline().decode())
