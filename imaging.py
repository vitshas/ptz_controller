from copy import copy

class Imaging:
    def __init__(self, imaging, profile):
        self.imaging = imaging
        self.profile = copy(profile)
        
    def brightness(self, brightness = 58.0):
        return self.applySettings( dict(Brightness = brightness) )
    
    def colorSaturation(self, colorSaturation  = 52.0):
        return self.applySettings( dict(ColorSaturation  = colorSaturation) )
    
    def contrast(self, contrast  = 55.0):
        return self.applySettings( dict(Contrast  = contrast) )
    
    def sharpness(self, sharpness = 41.0):
        return self.applySettings( dict(Sharpness  = sharpness) )
         
    
    def setExposure(self, Mode = 'AUTO', Priority = None, Window = None, MinExposureTime = 33.0,
                    MaxExposureTime = 40000.0, MinGain = 0.0, MaxGain = 0.0, MinIris = -22.0,
                    MaxIris = 0.0, ExposureTime = None, Gain = None, Iris = None):
        exposure = {}
        exposure['Mode'] = Mode
        exposure['Priority'] = Priority
        exposure['Window'] = Window
        exposure['MinExposureTime'] = MinExposureTime
        exposure['MaxExposureTime'] = MaxExposureTime
        exposure['MinGain'] = MinGain
        exposure['MaxGain'] = MaxGain
        exposure['MinIris'] = MinIris
        exposure['MaxIris'] = MaxIris
        exposure['ExposureTime'] = ExposureTime
        exposure['Gain'] = Gain
        exposure['Iris'] = Iris
        return self.applySettings( dict(Exposure = exposure) )
    
    def setFocus(self, AutoFocusMode = 'AUTO', DefaultSpeed = None,
                  NearLimit = 300.0, FarLimit = 0.0, Extension = None):
        focus = {}
        focus['AutoFocusMode'] = AutoFocusMode
        focus['DefaultSpeed'] = DefaultSpeed
        focus['NearLimit'] = NearLimit
        focus['FarLimit'] = FarLimit
        focus['Extension'] = Extension
        return self.applySettings( dict(Focus  = focus) )
    
    def applySettings(self, attribute):
        request = self.imaging.create_type('SetImagingSettings')
        request.VideoSourceToken = self.profile.VideoSourceConfiguration.SourceToken
        request.ImagingSettings = attribute
        self.imaging.SetImagingSettings(request)