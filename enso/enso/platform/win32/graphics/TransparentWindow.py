# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TransparentWindow', [dirname(__file__)])
        except ImportError:
            import _TransparentWindow
            return _TransparentWindow
        if fp is not None:
            try:
                _mod = imp.load_module('_TransparentWindow', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _TransparentWindow = swig_import_helper()
    del swig_import_helper
else:
    import _TransparentWindow
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
    if (not static) or hasattr(self,name):
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


BITS_PER_PIXEL = _TransparentWindow.BITS_PER_PIXEL
BYTES_PER_PIXEL = _TransparentWindow.BYTES_PER_PIXEL
MAX_OPACITY = _TransparentWindow.MAX_OPACITY
class TransparentWindowError(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TransparentWindowError, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TransparentWindowError, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _TransparentWindow.new_TransparentWindowError(*args)
        try: self.this.append(this)
        except: self.this = this
    def what(self): return _TransparentWindow.TransparentWindowError_what(self)
    __swig_destroy__ = _TransparentWindow.delete_TransparentWindowError
    __del__ = lambda self : None;
TransparentWindowError_swigregister = _TransparentWindow.TransparentWindowError_swigregister
TransparentWindowError_swigregister(TransparentWindowError)

class FatalError(TransparentWindowError):
    __swig_setmethods__ = {}
    for _s in [TransparentWindowError]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FatalError, name, value)
    __swig_getmethods__ = {}
    for _s in [TransparentWindowError]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, FatalError, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _TransparentWindow.new_FatalError(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TransparentWindow.delete_FatalError
    __del__ = lambda self : None;
FatalError_swigregister = _TransparentWindow.FatalError_swigregister
FatalError_swigregister(FatalError)

class RangeError(TransparentWindowError):
    __swig_setmethods__ = {}
    for _s in [TransparentWindowError]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RangeError, name, value)
    __swig_getmethods__ = {}
    for _s in [TransparentWindowError]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, RangeError, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _TransparentWindow.new_RangeError(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TransparentWindow.delete_RangeError
    __del__ = lambda self : None;
RangeError_swigregister = _TransparentWindow.RangeError_swigregister
RangeError_swigregister(RangeError)

class TransparentWindow(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TransparentWindow, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TransparentWindow, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _TransparentWindow.new_TransparentWindow(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TransparentWindow.delete_TransparentWindow
    __del__ = lambda self : None;
    def update(self): return _TransparentWindow.TransparentWindow_update(self)
    def setOpacity(self, *args): return _TransparentWindow.TransparentWindow_setOpacity(self, *args)
    def getOpacity(self): return _TransparentWindow.TransparentWindow_getOpacity(self)
    def setPosition(self, *args): return _TransparentWindow.TransparentWindow_setPosition(self, *args)
    def getX(self): return _TransparentWindow.TransparentWindow_getX(self)
    def getY(self): return _TransparentWindow.TransparentWindow_getY(self)
    def setSize(self, *args): return _TransparentWindow.TransparentWindow_setSize(self, *args)
    def getWidth(self): return _TransparentWindow.TransparentWindow_getWidth(self)
    def getHeight(self): return _TransparentWindow.TransparentWindow_getHeight(self)
    def getMaxWidth(self): return _TransparentWindow.TransparentWindow_getMaxWidth(self)
    def getMaxHeight(self): return _TransparentWindow.TransparentWindow_getMaxHeight(self)
    def makeCairoSurface(self, *args): return _TransparentWindow.TransparentWindow_makeCairoSurface(self, *args)
TransparentWindow_swigregister = _TransparentWindow.TransparentWindow_swigregister
TransparentWindow_swigregister(TransparentWindow)


def _getDesktopSize():
  return _TransparentWindow._getDesktopSize()
_getDesktopSize = _TransparentWindow._getDesktopSize

def _getDesktopOffset(*args):
  return _TransparentWindow._getDesktopOffset(*args)
_getDesktopOffset = _TransparentWindow._getDesktopOffset

