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
            fp, pathname, description = imp.find_module('_opcuatypes', [dirname(__file__)])
        except ImportError:
            import _opcuatypes
            return _opcuatypes
        if fp is not None:
            try:
                _mod = imp.load_module('_opcuatypes', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _opcuatypes = swig_import_helper()
    del swig_import_helper
else:
    import _opcuatypes
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


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _opcuatypes.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _opcuatypes.SwigPyIterator_value(self)
    def incr(self, n=1): return _opcuatypes.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _opcuatypes.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _opcuatypes.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _opcuatypes.SwigPyIterator_equal(self, *args)
    def copy(self): return _opcuatypes.SwigPyIterator_copy(self)
    def next(self): return _opcuatypes.SwigPyIterator_next(self)
    def __next__(self): return _opcuatypes.SwigPyIterator___next__(self)
    def previous(self): return _opcuatypes.SwigPyIterator_previous(self)
    def advance(self, *args): return _opcuatypes.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _opcuatypes.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _opcuatypes.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _opcuatypes.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _opcuatypes.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _opcuatypes.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _opcuatypes.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _opcuatypes.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

Null = _opcuatypes.Null
Boolean = _opcuatypes.Boolean
SByte = _opcuatypes.SByte
Byte = _opcuatypes.Byte
Int16 = _opcuatypes.Int16
UInt16 = _opcuatypes.UInt16
Int32 = _opcuatypes.Int32
UInt32 = _opcuatypes.UInt32
Int64 = _opcuatypes.Int64
UInt64 = _opcuatypes.UInt64
Float = _opcuatypes.Float
Double = _opcuatypes.Double
String = _opcuatypes.String
DateTime = _opcuatypes.DateTime
Guid = _opcuatypes.Guid
ByteString = _opcuatypes.ByteString
XmlElement = _opcuatypes.XmlElement
NodeId = _opcuatypes.NodeId
ExpandedNodeId = _opcuatypes.ExpandedNodeId
StatusCode = _opcuatypes.StatusCode
QualifiedName = _opcuatypes.QualifiedName
LocalizedText = _opcuatypes.LocalizedText
ExtensionObject = _opcuatypes.ExtensionObject
DataValue = _opcuatypes.DataValue
Variant = _opcuatypes.Variant
DiagnosticInfo = _opcuatypes.DiagnosticInfo

def toString(*args):
  return _opcuatypes.toString(*args)
toString = _opcuatypes.toString
# This file is compatible with both classic and new-style classes.


