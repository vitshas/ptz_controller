from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.13.51', 80, 'admin', 'Supervisor', '/Applications/Python 2.7/onvif/wsdl')

imaging_ptz = mycam.create_imaging_service()
media = mycam.create_media_service()

profiles = media.GetProfile()[0]

from imaging import Imaging

ptz = Imaging (imaging_ptz, profiles)
ptz.setFocus("Manual")
