import struct

class StructField:
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r =  struct.unpack_from(self.format, 
                                    instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

if __name__ == '__main__':

    class PolyHeader(Structure):
        file_code = StructField('<i', 0)
        min_x = StructField('<d', 4)
        min_y = StructField('<d', 12)
        max_x = StructField('<d', 20)
        max_y = StructField('<d', 28)
        num_polys = StructField('<i', 36)

    f = open('polys.bin','rb')
    data = f.read()
    
    phead = PolyHeader(data)
    print(phead.file_code == 0x1234)
    print('min_x=', phead.min_x)
    print('max_x=', phead.max_x)
    print('min_y=', phead.min_y)
    print('max_y=', phead.max_y)
    print('num_polys=', phead.num_polys)
