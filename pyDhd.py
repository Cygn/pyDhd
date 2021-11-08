# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyDhd', [dirname(__file__)])
        except ImportError:
            import _pyDhd
            return _pyDhd
        if fp is not None:
            try:
                _mod = imp.load_module('_pyDhd', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyDhd = swig_import_helper()
    del swig_import_helper
else:
    import _pyDhd
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def dhdGetDeviceAngleRad(*args):
  return _pyDhd.dhdGetDeviceAngleRad(*args)
dhdGetDeviceAngleRad = _pyDhd.dhdGetDeviceAngleRad

def dhdGetDeviceAngleDeg(*args):
  return _pyDhd.dhdGetDeviceAngleDeg(*args)
dhdGetDeviceAngleDeg = _pyDhd.dhdGetDeviceAngleDeg

def dhdGetEffectorMass(*args):
  return _pyDhd.dhdGetEffectorMass(*args)
dhdGetEffectorMass = _pyDhd.dhdGetEffectorMass

def dhdGetPosition(*args):
  return _pyDhd.dhdGetPosition(*args)
dhdGetPosition = _pyDhd.dhdGetPosition

def dhdGetForce(*args):
  return _pyDhd.dhdGetForce(*args)
dhdGetForce = _pyDhd.dhdGetForce

def dhdGetOrientationRad(*args):
  return _pyDhd.dhdGetOrientationRad(*args)
dhdGetOrientationRad = _pyDhd.dhdGetOrientationRad

def dhdGetOrientationDeg(*args):
  return _pyDhd.dhdGetOrientationDeg(*args)
dhdGetOrientationDeg = _pyDhd.dhdGetOrientationDeg

def dhdGetPositionAndOrientationRad(*args):
  return _pyDhd.dhdGetPositionAndOrientationRad(*args)
dhdGetPositionAndOrientationRad = _pyDhd.dhdGetPositionAndOrientationRad

def dhdGetPositionAndOrientationDeg(*args):
  return _pyDhd.dhdGetPositionAndOrientationDeg(*args)
dhdGetPositionAndOrientationDeg = _pyDhd.dhdGetPositionAndOrientationDeg

def dhdGetPositionAndOrientationFrame(*args):
  return _pyDhd.dhdGetPositionAndOrientationFrame(*args)
dhdGetPositionAndOrientationFrame = _pyDhd.dhdGetPositionAndOrientationFrame

def dhdGetForceAndTorque(*args):
  return _pyDhd.dhdGetForceAndTorque(*args)
dhdGetForceAndTorque = _pyDhd.dhdGetForceAndTorque

def dhdGetGripperAngleDeg(*args):
  return _pyDhd.dhdGetGripperAngleDeg(*args)
dhdGetGripperAngleDeg = _pyDhd.dhdGetGripperAngleDeg

def dhdGetGripperAngleRad(*args):
  return _pyDhd.dhdGetGripperAngleRad(*args)
dhdGetGripperAngleRad = _pyDhd.dhdGetGripperAngleRad

def dhdGetGripperGap(*args):
  return _pyDhd.dhdGetGripperGap(*args)
dhdGetGripperGap = _pyDhd.dhdGetGripperGap

def dhdGetGripperThumbPos(*args):
  return _pyDhd.dhdGetGripperThumbPos(*args)
dhdGetGripperThumbPos = _pyDhd.dhdGetGripperThumbPos

def dhdGetGripperFingerPos(*args):
  return _pyDhd.dhdGetGripperFingerPos(*args)
dhdGetGripperFingerPos = _pyDhd.dhdGetGripperFingerPos

def dhdGetForceAndTorqueAndGripperForce(*args):
  return _pyDhd.dhdGetForceAndTorqueAndGripperForce(*args)
dhdGetForceAndTorqueAndGripperForce = _pyDhd.dhdGetForceAndTorqueAndGripperForce

def dhdGetLinearVelocity(*args):
  return _pyDhd.dhdGetLinearVelocity(*args)
dhdGetLinearVelocity = _pyDhd.dhdGetLinearVelocity

def dhdGetAngularVelocityRad(*args):
  return _pyDhd.dhdGetAngularVelocityRad(*args)
dhdGetAngularVelocityRad = _pyDhd.dhdGetAngularVelocityRad

def dhdGetAngularVelocityDeg(*args):
  return _pyDhd.dhdGetAngularVelocityDeg(*args)
dhdGetAngularVelocityDeg = _pyDhd.dhdGetAngularVelocityDeg

def dhdGetGripperLinearVelocity(*args):
  return _pyDhd.dhdGetGripperLinearVelocity(*args)
dhdGetGripperLinearVelocity = _pyDhd.dhdGetGripperLinearVelocity

def dhdGetGripperAngularVelocityRad(*args):
  return _pyDhd.dhdGetGripperAngularVelocityRad(*args)
dhdGetGripperAngularVelocityRad = _pyDhd.dhdGetGripperAngularVelocityRad

def dhdGetGripperAngularVelocityDeg(*args):
  return _pyDhd.dhdGetGripperAngularVelocityDeg(*args)
dhdGetGripperAngularVelocityDeg = _pyDhd.dhdGetGripperAngularVelocityDeg

def dhdGetBaseAngleXRad(*args):
  return _pyDhd.dhdGetBaseAngleXRad(*args)
dhdGetBaseAngleXRad = _pyDhd.dhdGetBaseAngleXRad

def dhdGetBaseAngleXDeg(*args):
  return _pyDhd.dhdGetBaseAngleXDeg(*args)
dhdGetBaseAngleXDeg = _pyDhd.dhdGetBaseAngleXDeg

def dhdGetBaseAngleZRad(*args):
  return _pyDhd.dhdGetBaseAngleZRad(*args)
dhdGetBaseAngleZRad = _pyDhd.dhdGetBaseAngleZRad

def dhdGetBaseAngleZDeg(*args):
  return _pyDhd.dhdGetBaseAngleZDeg(*args)
dhdGetBaseAngleZDeg = _pyDhd.dhdGetBaseAngleZDeg

def dhdGetDeviceCount():
  return _pyDhd.dhdGetDeviceCount()
dhdGetDeviceCount = _pyDhd.dhdGetDeviceCount

def dhdGetAvailableCount():
  return _pyDhd.dhdGetAvailableCount()
dhdGetAvailableCount = _pyDhd.dhdGetAvailableCount

def dhdSetDevice(*args):
  return _pyDhd.dhdSetDevice(*args)
dhdSetDevice = _pyDhd.dhdSetDevice

def dhdGetDeviceID():
  return _pyDhd.dhdGetDeviceID()
dhdGetDeviceID = _pyDhd.dhdGetDeviceID

def dhdGetSerialNumber(*args):
  return _pyDhd.dhdGetSerialNumber(*args)
dhdGetSerialNumber = _pyDhd.dhdGetSerialNumber

def dhdOpen():
  return _pyDhd.dhdOpen()
dhdOpen = _pyDhd.dhdOpen

def dhdOpenType(*args):
  return _pyDhd.dhdOpenType(*args)
dhdOpenType = _pyDhd.dhdOpenType

def dhdOpenSerial(*args):
  return _pyDhd.dhdOpenSerial(*args)
dhdOpenSerial = _pyDhd.dhdOpenSerial

def dhdOpenID(*args):
  return _pyDhd.dhdOpenID(*args)
dhdOpenID = _pyDhd.dhdOpenID

def dhdClose(*args):
  return _pyDhd.dhdClose(*args)
dhdClose = _pyDhd.dhdClose

def dhdStop(*args):
  return _pyDhd.dhdStop(*args)
dhdStop = _pyDhd.dhdStop

def dhdGetComMode(*args):
  return _pyDhd.dhdGetComMode(*args)
dhdGetComMode = _pyDhd.dhdGetComMode

def dhdEnableForce(*args):
  return _pyDhd.dhdEnableForce(*args)
dhdEnableForce = _pyDhd.dhdEnableForce

def dhdGetSystemType(*args):
  return _pyDhd.dhdGetSystemType(*args)
dhdGetSystemType = _pyDhd.dhdGetSystemType

def dhdGetSystemName(*args):
  return _pyDhd.dhdGetSystemName(*args)
dhdGetSystemName = _pyDhd.dhdGetSystemName

def dhdGetVersion(*args):
  return _pyDhd.dhdGetVersion(*args)
dhdGetVersion = _pyDhd.dhdGetVersion

def dhdGetSDKVersion(*args):
  return _pyDhd.dhdGetSDKVersion(*args)
dhdGetSDKVersion = _pyDhd.dhdGetSDKVersion

def dhdGetSystemCounter():
  return _pyDhd.dhdGetSystemCounter()
dhdGetSystemCounter = _pyDhd.dhdGetSystemCounter

def dhdGetButton(*args):
  return _pyDhd.dhdGetButton(*args)
dhdGetButton = _pyDhd.dhdGetButton

def dhdGetButtonMask(*args):
  return _pyDhd.dhdGetButtonMask(*args)
dhdGetButtonMask = _pyDhd.dhdGetButtonMask

def dhdSetOutput(*args):
  return _pyDhd.dhdSetOutput(*args)
dhdSetOutput = _pyDhd.dhdSetOutput

def dhdIsLeftHanded(*args):
  return _pyDhd.dhdIsLeftHanded(*args)
dhdIsLeftHanded = _pyDhd.dhdIsLeftHanded

def dhdHasWrist(*args):
  return _pyDhd.dhdHasWrist(*args)
dhdHasWrist = _pyDhd.dhdHasWrist

def dhdHasActiveWrist(*args):
  return _pyDhd.dhdHasActiveWrist(*args)
dhdHasActiveWrist = _pyDhd.dhdHasActiveWrist

def dhdHasGripper(*args):
  return _pyDhd.dhdHasGripper(*args)
dhdHasGripper = _pyDhd.dhdHasGripper

def dhdReset(*args):
  return _pyDhd.dhdReset(*args)
dhdReset = _pyDhd.dhdReset

def dhdResetWrist(*args):
  return _pyDhd.dhdResetWrist(*args)
dhdResetWrist = _pyDhd.dhdResetWrist

def dhdWaitForReset(*args):
  return _pyDhd.dhdWaitForReset(*args)
dhdWaitForReset = _pyDhd.dhdWaitForReset

def dhdSetStandardGravity(*args):
  return _pyDhd.dhdSetStandardGravity(*args)
dhdSetStandardGravity = _pyDhd.dhdSetStandardGravity

def dhdSetGravityCompensation(*args):
  return _pyDhd.dhdSetGravityCompensation(*args)
dhdSetGravityCompensation = _pyDhd.dhdSetGravityCompensation

def dhdSetBrakes(*args):
  return _pyDhd.dhdSetBrakes(*args)
dhdSetBrakes = _pyDhd.dhdSetBrakes

def dhdSetDeviceAngleRad(*args):
  return _pyDhd.dhdSetDeviceAngleRad(*args)
dhdSetDeviceAngleRad = _pyDhd.dhdSetDeviceAngleRad

def dhdSetDeviceAngleDeg(*args):
  return _pyDhd.dhdSetDeviceAngleDeg(*args)
dhdSetDeviceAngleDeg = _pyDhd.dhdSetDeviceAngleDeg

def dhdSetEffectorMass(*args):
  return _pyDhd.dhdSetEffectorMass(*args)
dhdSetEffectorMass = _pyDhd.dhdSetEffectorMass

def dhdSetForce(*args):
  return _pyDhd.dhdSetForce(*args)
dhdSetForce = _pyDhd.dhdSetForce

def dhdSetForceAndTorque(*args):
  return _pyDhd.dhdSetForceAndTorque(*args)
dhdSetForceAndTorque = _pyDhd.dhdSetForceAndTorque

def dhdGetComFreq(*args):
  return _pyDhd.dhdGetComFreq(*args)
dhdGetComFreq = _pyDhd.dhdGetComFreq

def dhdSetForceAndGripperForce(*args):
  return _pyDhd.dhdSetForceAndGripperForce(*args)
dhdSetForceAndGripperForce = _pyDhd.dhdSetForceAndGripperForce

def dhdSetForceAndTorqueAndGripperForce(*args):
  return _pyDhd.dhdSetForceAndTorqueAndGripperForce(*args)
dhdSetForceAndTorqueAndGripperForce = _pyDhd.dhdSetForceAndTorqueAndGripperForce

def dhdConfigLinearVelocity(*args):
  return _pyDhd.dhdConfigLinearVelocity(*args)
dhdConfigLinearVelocity = _pyDhd.dhdConfigLinearVelocity

def dhdConfigAngularVelocity(*args):
  return _pyDhd.dhdConfigAngularVelocity(*args)
dhdConfigAngularVelocity = _pyDhd.dhdConfigAngularVelocity

def dhdConfigGripperVelocity(*args):
  return _pyDhd.dhdConfigGripperVelocity(*args)
dhdConfigGripperVelocity = _pyDhd.dhdConfigGripperVelocity

def dhdEmulateButton(*args):
  return _pyDhd.dhdEmulateButton(*args)
dhdEmulateButton = _pyDhd.dhdEmulateButton

def dhdSetBaseAngleXRad(*args):
  return _pyDhd.dhdSetBaseAngleXRad(*args)
dhdSetBaseAngleXRad = _pyDhd.dhdSetBaseAngleXRad

def dhdSetBaseAngleXDeg(*args):
  return _pyDhd.dhdSetBaseAngleXDeg(*args)
dhdSetBaseAngleXDeg = _pyDhd.dhdSetBaseAngleXDeg

def dhdSetBaseAngleZRad(*args):
  return _pyDhd.dhdSetBaseAngleZRad(*args)
dhdSetBaseAngleZRad = _pyDhd.dhdSetBaseAngleZRad

def dhdSetBaseAngleZDeg(*args):
  return _pyDhd.dhdSetBaseAngleZDeg(*args)
dhdSetBaseAngleZDeg = _pyDhd.dhdSetBaseAngleZDeg
DHD_ON = _pyDhd.DHD_ON
DHD_OFF = _pyDhd.DHD_OFF
# This file is compatible with both classic and new-style classes.


