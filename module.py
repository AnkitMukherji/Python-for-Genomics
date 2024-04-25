#Three ways to import functions from modules
"""
import dnautil
dnautil.gc("ATACGCAGACGG")
"""
"""
from dnautil import*
gc("ATACGCAGACGG")
"""
from dnautil import gc
gc("ATACGCAGACGG")