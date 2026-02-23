/challenge/cimg
vim test.py

cat /challenge/cimg
    
    header = file.read1(16)
    assert len(header) == 16, "ERROR: Failed to read header!"
    assert header[:4] == b"cIMG", "ERROR: Invalid magic number!"
    assert int.from_bytes(header[4:6], "little") == 1, "ERROR: Invalid version!"
    width = int.from_bytes(header[6:14], "little")
    assert width == 64, "ERROR: Incorrect width!"
    height = int.from_bytes(header[14:16], "little")
    assert height == 12, "ERROR: Incorrect height!"
    data = file.read1(width * height)
    assert len(data) == width * height, "ERROR: Failed to read data!"

#!/bin/python

with open("example.cimg", "wb") as file:
    file.write(b"cIMG")
    file.write((1).to_bytes(2, "little"))
    file.write((64).to_bytes(8, "little"))
    file.write((12).to_bytes(2, "little"))
    file.write((64*12)*b"x")

chmod +x test.py
./test.py
cat example.cimg
/challenge/cimg example.cimg
