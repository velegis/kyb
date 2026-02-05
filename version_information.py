#!/bin/python

with open ("example.cimg","wb") as file:
        header_magic=b"[lMg"
        version=(225).to_bytes(2, "little")
        file.write(header_magic+version)
