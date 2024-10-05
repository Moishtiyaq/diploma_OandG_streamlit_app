import numpy as np
import pandas as pd

mw = float(input("enter the mud weight value (ppg): "))
apl = float(input("enter the annular pressure loss value(psi): "))
tvd = float(input("enter the true vertical depth (ft): "))
ecd = ((apl/(0.052*tvd))+mw)
print(f"the equivalent density on this tvd {tvd}ft is {ecd}")