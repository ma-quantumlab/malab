
from .instrumentmanager import InstrumentManager
from .instrumenttypes import Instrument, VisaInstrument, TelnetInstrument, SocketInstrument, SerialInstrument, \
    WebInstrument

try: from .InstrumentManagerWindow import InstrumentManagerWindow
except: print("Could not load InstrumentManagerWindow")

from .spectrumanalyzer import E4440
from .PNAX import N5242A
from .rfgenerators import N5183B,E8257D,BNC845
from .multimeter import Keithley199

try: from .bkpowersupply import BKPowerSupply
except: print("Could not load BKPowerSupply")
try: from .bkpowersupply import BKPowerSupplynew
except: print("Could not load BKPowerSupply")
try: from .bkpowersupply import BKPowerSupply2
except: print("Could not load BKPowerSupply")
try: from .voltsource import SRS900
except: print("Could not load SRS900")
try: from .voltsource import YokogawaGS200
except: print("Could not load YokogawaGS200")
try: from .function_generator import BiasDriver,FilamentDriver,BNCAWG
except: print("Could not load BNC AWG classes")
try: from .multimeter import Keithley199, HP34401A
except: print("Could not load Keithley199/HP34401A multimeter classes")
try: from .spectrumanalyzer import E4440
except: print("Could not load E4440 Spectrum Analyzer")