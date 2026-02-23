#!/bin/python

with open("example.cimg", "wb") as file:
    file.write(b"cIMG")  
    file.write((1).to_bytes(8, "little"))  
    
    width = 25
    height = 11
    file.write(width.to_bytes(2, "little"))  
    file.write(height.to_bytes(2, "little"))  
    file.write((width * height) * b"X")
