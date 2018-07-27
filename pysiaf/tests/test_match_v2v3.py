from pysiaf import iando
from pysiaf.utils import tools
from pysiaf.utils import tools2

print('\n\n ************************************* BEGIN TEST **************************')
instrument = 'NIRCam'
apName_1 = 'NRCA1_FULL'
apName_2 = 'NRCA5_FULL'
location = '/itar/jwst/tel/share/SIAF_WG/Instruments/NIRCam/NIRCam_SIAF_2018-07-23.xml'
siaf = iando.read.read_jwst_siaf(instrument=instrument, filename=location)
aperture_1 = siaf[apName_1]
aperture_2 = siaf[apName_2]

tools2.match_v2v3(aperture_1, aperture_2, verbose=True)
finish = input('Show plot until return is hit')
