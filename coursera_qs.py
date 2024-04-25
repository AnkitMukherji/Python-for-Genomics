seq='ACG'
for i in range(len(seq)) :     
    for j in range(i) :        
        print(seq[j:i])
"""
The conditions possible are:
    i   j   Result
    0   0   Empty
    1   0   A
    1   1   Empty
    2   0   AC
    2   1   C
    2   2   Empty
"""