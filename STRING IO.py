# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import io
import sys
from itertools import groupby
from chroma import *


for k, g in groupby(sorted(nots),
                    key=nots.get):
    print('{}: {}'.format(list(g)[-1], k))



old_stdout = sys.stdout
sys.stdout = mystdout = io.StringIO()



sys.stdout = old_stdout

