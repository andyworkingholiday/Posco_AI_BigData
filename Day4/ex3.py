import sys
import os

args = sys.argv[1:]
input_name = args[0] 
output_name = args[1]

rf = open(input_name, 'r')
wf = open(output_name, 'w')

for read_line in rf:
    wf.write(read_line)
    
rf.close()
wf.close()
