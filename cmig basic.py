/challenge/cimg
vim test.py

cat /challenge/cimg

    header = file.read1(17)
    assert len(header) == 17, "ERROR: Failed to read header!"
    assert header[:4] == b"cIMG", "ERROR: Invalid magic number!"
    assert int.from_bytes(header[4:5], "little") == 2, "ERROR: Invalid version!"
    width = int.from_bytes(header[5:13], "little")
    assert width == 30, "ERROR: Incorrect width!"
    height = int.from_bytes(header[13:17], "little")
    assert height == 20, "ERROR: Incorrect height!"
    data = file.read1(width * height * 4)
    assert len(data) == width * height * 4, "ERROR: Failed to read data!"

nonspace_count == 819
ASU maroon: RGB(0x8C, 0x1D, 0x40)

#!/bin/python

with open("example.cimg", "wb") as file:
    file.write(b"cIMG") 
    file.write((2).to_bytes(1, "little"))
    
    file.write((30).to_bytes(8, "little")) 
    file.write((20).to_bytes(4, "little")) 
    
    asu_maroon_r = 0x8C
    asu_maroon_g = 0x1D
    asu_maroon_b = 0x40
    
    for _ in range(30 * 20):
        file.write(bytes([asu_maroon_r, asu_maroon_g, asu_maroon_b, ord('X')]))

chmod +x test.py
./test.py
cat example.cimg
/challenge/cimg example.cimg
