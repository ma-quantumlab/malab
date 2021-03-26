# from .instruments import InstrumentManager, LocalInstruments, keysight
from .datamanagement import SlabFile, h5File, AttrDict
from .dataanalysis import *
from .experiment import Experiment

# #
# # try:
# #     from plotting import ScriptPlotter
# # except:
# #     "Warning could not import ScriptPlotter"
#
# from .dsfit import argselectdomain, selectdomain, zipsort, fitgeneral, fitexp, fitgauss, fithanger, \
#     fithangertilt, fitlor, fitdecaysin, fithanger_new, hangerfunc_new, fit_SNT