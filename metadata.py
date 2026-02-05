#!/bin/python
import struct

with open("example.cimg","wb") as file:
        file.write(b"<:MG")
        file.write((1).to_bytes(2,"little"))
        file.write((50).to_bytes(1, "little"))
        file.write((11).to_bytes(8,"little"))
        file.write((50*11)*b"q")
