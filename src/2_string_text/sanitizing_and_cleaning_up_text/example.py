# example.py
#
# Example of some tricky sanitization problems

# A tricky string
s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)

# (a) Remapping whitespace
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None      # Deleted
}

a = s.translate(remap)
print('whitespace remapped:', a)

# (b) Remove all combining characters/marks
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
c = b.translate(cmb_chrs)
print('accents removed:', c)

# (c) Accent removal using I/O decoding
d = b.encode('ascii','ignore').decode('ascii')
print('accents removed via I/O:', d)
