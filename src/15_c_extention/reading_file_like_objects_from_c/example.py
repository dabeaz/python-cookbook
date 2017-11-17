f = open('sample.c')
import sample
sample.consume_file(f)
f.close()

print('**** DONE')
