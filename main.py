from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.13.51', 80, 'admin', 'Supervisor', '/Applications/Python 2.7/onvif/wsdl')

imaging = mycam.create_imaging_service()
media = mycam.create_media_service()

profiles = media.GetProfiles()[0]

from imaging import Imaging

ptz = Imaging(imaging,profiles)

ptz.setFocus()
