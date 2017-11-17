import struct
import itertools

polys = [
          [ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
          [ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
          [ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ],
        ]

def write_polys(filename, polys):
    # Determine bounding box    
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)
    
    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi', 
                            0x1234, 
                            min_x, min_y, 
                            max_x, max_y, 
                            len(polys)))

        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size+4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))

# Call it with our polygon data
write_polys('polys.bin', polys)
