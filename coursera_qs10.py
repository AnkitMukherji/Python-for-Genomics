import random
def create_dna(n,alphabet='acgt'):
    print(''.join([random.choice(alphabet) for i in range(n)]))
dna=create_dna(10)