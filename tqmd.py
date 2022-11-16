
from tqdm import tnrange, tqdm_notebook
from time import sleep

for i in tnrange(4, desc='1st loop'):
    for j in tnrange(100, desc='2nd loop'):
        sleep(0.2)