#!/usr/bin/env python
# coding: utf-8

# # bit_IO: Input and output of single bits

# In[13]:


import struct

class Bit_IO():
    
    def __init__(self):
        self.bit_to_read = 256
        self.bit_to_write = 1
        self.get_counter = 0
        self.output_byte = 0
        
    def read(self, file):
        # I return ~0 or 0.
        if self.bit_to_read == 256:
            read_byte = file.read(1)
            self.input_byte = struct.unpack("B", read_byte)[0]
            self.bit_to_read = 1
        bit = self.input_byte & self.bit_to_read
        self.bit_to_read <<= 1
        return bit
    
    def write(self, bit, file):
        # bit can be 0 or ~0.
        if self.bit_to_write == 256:
            #print(self.output_byte, end=' ')
            file.write(struct.pack("B", self.output_byte))
            self.bit_to_write = 1
            self.output_byte = 0
        if bit:
            self.output_byte |= self.bit_to_write
        self.bit_to_write <<= 1
            
    def flush(self, file):
        if self.bit_to_write != 0:
            file.write(struct.pack("B", self.output_byte))


# In[15]:


if __name__ == "__main__":
    f = open("/tmp/bitio", "wb")
    bitio = Bit_IO()
    bitio.write(1, f)
    bitio.write(0, f)
    bitio.write(2, f) # Same that bitio.write(1, f)
    bitio.write(1, f)
    
    bitio.write(1, f)
    bitio.write(0, f)
    bitio.write(1, f)
    bitio.write(1, f)
    
    bitio.write(1, f)
    bitio.flush(f)
    f.close() 
    get_ipython().system('hexdump -C /tmp/bitio')
    f = open("/tmp/bitio", "rb")
    print(bitio.read(f))
    print(bitio.read(f))
    print(bitio.read(f))
    print(bitio.read(f))
    
    print(bitio.read(f))
    print(bitio.read(f))
    print(bitio.read(f))
    print(bitio.read(f))
    
    print(bitio.read(f))


# In[ ]:





# In[ ]:





# In[ ]:




