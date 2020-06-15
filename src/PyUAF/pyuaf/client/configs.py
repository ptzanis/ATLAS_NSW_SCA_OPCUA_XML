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
            fp, pathname, description = imp.find_module('_configs', [dirname(__file__)])
        except ImportError:
            import _configs
            return _configs
        if fp is not None:
            try:
                _mod = imp.load_module('_configs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _configs = swig_import_helper()
    del swig_import_helper
else:
    import _configs
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
    __swig_destroy__ = _configs.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _configs.SwigPyIterator_value(self)
    def incr(self, n=1): return _configs.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _configs.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _configs.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _configs.SwigPyIterator_equal(self, *args)
    def copy(self): return _configs.SwigPyIterator_copy(self)
    def next(self): return _configs.SwigPyIterator_next(self)
    def __next__(self): return _configs.SwigPyIterator___next__(self)
    def previous(self): return _configs.SwigPyIterator_previous(self)
    def advance(self, *args): return _configs.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _configs.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _configs.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _configs.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _configs.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _configs.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _configs.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _configs.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import pyuaf.util.attributeids
import pyuaf.util.monitoringmodes
import pyuaf.util.primitives
import pyuaf.util.browsedirections
import pyuaf.util.nodeclasses
import pyuaf.util.timestampstoreturn
import pyuaf.util
import settings
import pyuaf.util.messagesecuritymodes
import pyuaf.util.usertokentypes
import pyuaf.util.loglevels
import pyuaf.util.applicationtypes
import pyuaf.util.constants
import pyuaf.util.nodeididentifiertypes
import pyuaf.util.statuscodes
import pyuaf.util.opcuatypes
import pyuaf.util.opcuaidentifiers
import pyuaf.util.securitypolicies
import pyuaf.util.__unittesthelper__
class SessionConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SessionConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SessionConfig, name)
    def __init__(self, *args): 
        this = _configs.new_SessionConfig(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["defaultSessionSettings"] = _configs.SessionConfig_defaultSessionSettings_set
    __swig_getmethods__["defaultSessionSettings"] = _configs.SessionConfig_defaultSessionSettings_get
    if _newclass:defaultSessionSettings = _swig_property(_configs.SessionConfig_defaultSessionSettings_get, _configs.SessionConfig_defaultSessionSettings_set)
    __swig_setmethods__["specificSessionSettings"] = _configs.SessionConfig_specificSessionSettings_set
    __swig_getmethods__["specificSessionSettings"] = _configs.SessionConfig_specificSessionSettings_get
    if _newclass:specificSessionSettings = _swig_property(_configs.SessionConfig_specificSessionSettings_get, _configs.SessionConfig_specificSessionSettings_set)
    __swig_setmethods__["useOnlySpecificSettings"] = _configs.SessionConfig_useOnlySpecificSettings_set
    __swig_getmethods__["useOnlySpecificSettings"] = _configs.SessionConfig_useOnlySpecificSettings_get
    if _newclass:useOnlySpecificSettings = _swig_property(_configs.SessionConfig_useOnlySpecificSettings_get, _configs.SessionConfig_useOnlySpecificSettings_set)
    def __str__(self, indent="", colon=40): return _configs.SessionConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.SessionConfig___repr__(self)
    __swig_destroy__ = _configs.delete_SessionConfig
    __del__ = lambda self : None;
SessionConfig_swigregister = _configs.SessionConfig_swigregister
SessionConfig_swigregister(SessionConfig)

class SubscriptionConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubscriptionConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SubscriptionConfig, name)
    def __init__(self, *args): 
        this = _configs.new_SubscriptionConfig(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["defaultSubscriptionSettings"] = _configs.SubscriptionConfig_defaultSubscriptionSettings_set
    __swig_getmethods__["defaultSubscriptionSettings"] = _configs.SubscriptionConfig_defaultSubscriptionSettings_get
    if _newclass:defaultSubscriptionSettings = _swig_property(_configs.SubscriptionConfig_defaultSubscriptionSettings_get, _configs.SubscriptionConfig_defaultSubscriptionSettings_set)
    __swig_setmethods__["specificSubscriptionSettings"] = _configs.SubscriptionConfig_specificSubscriptionSettings_set
    __swig_getmethods__["specificSubscriptionSettings"] = _configs.SubscriptionConfig_specificSubscriptionSettings_get
    if _newclass:specificSubscriptionSettings = _swig_property(_configs.SubscriptionConfig_specificSubscriptionSettings_get, _configs.SubscriptionConfig_specificSubscriptionSettings_set)
    def __str__(self, indent="", colon=33): return _configs.SubscriptionConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.SubscriptionConfig___repr__(self)
    __swig_destroy__ = _configs.delete_SubscriptionConfig
    __del__ = lambda self : None;
SubscriptionConfig_swigregister = _configs.SubscriptionConfig_swigregister
SubscriptionConfig_swigregister(SubscriptionConfig)

class ReadConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ReadConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ReadConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.ReadConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.ReadConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.ReadConfig_serviceSettings_get, _configs.ReadConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.ReadConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.ReadConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.ReadConfig_translationSettings_get, _configs.ReadConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.ReadConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.ReadConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_ReadConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_ReadConfig
    __del__ = lambda self : None;
ReadConfig_swigregister = _configs.ReadConfig_swigregister
ReadConfig_swigregister(ReadConfig)

class WriteConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WriteConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WriteConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.WriteConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.WriteConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.WriteConfig_serviceSettings_get, _configs.WriteConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.WriteConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.WriteConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.WriteConfig_translationSettings_get, _configs.WriteConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.WriteConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.WriteConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_WriteConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_WriteConfig
    __del__ = lambda self : None;
WriteConfig_swigregister = _configs.WriteConfig_swigregister
WriteConfig_swigregister(WriteConfig)

class MethodCallConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MethodCallConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MethodCallConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.MethodCallConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.MethodCallConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.MethodCallConfig_serviceSettings_get, _configs.MethodCallConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.MethodCallConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.MethodCallConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.MethodCallConfig_translationSettings_get, _configs.MethodCallConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.MethodCallConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.MethodCallConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_MethodCallConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_MethodCallConfig
    __del__ = lambda self : None;
MethodCallConfig_swigregister = _configs.MethodCallConfig_swigregister
MethodCallConfig_swigregister(MethodCallConfig)

class TranslateBrowsePathsToNodeIdsConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TranslateBrowsePathsToNodeIdsConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TranslateBrowsePathsToNodeIdsConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.TranslateBrowsePathsToNodeIdsConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.TranslateBrowsePathsToNodeIdsConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.TranslateBrowsePathsToNodeIdsConfig_serviceSettings_get, _configs.TranslateBrowsePathsToNodeIdsConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.TranslateBrowsePathsToNodeIdsConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.TranslateBrowsePathsToNodeIdsConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.TranslateBrowsePathsToNodeIdsConfig_translationSettings_get, _configs.TranslateBrowsePathsToNodeIdsConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.TranslateBrowsePathsToNodeIdsConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.TranslateBrowsePathsToNodeIdsConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_TranslateBrowsePathsToNodeIdsConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_TranslateBrowsePathsToNodeIdsConfig
    __del__ = lambda self : None;
TranslateBrowsePathsToNodeIdsConfig_swigregister = _configs.TranslateBrowsePathsToNodeIdsConfig_swigregister
TranslateBrowsePathsToNodeIdsConfig_swigregister(TranslateBrowsePathsToNodeIdsConfig)

class BrowseConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BrowseConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BrowseConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.BrowseConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.BrowseConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.BrowseConfig_serviceSettings_get, _configs.BrowseConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.BrowseConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.BrowseConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.BrowseConfig_translationSettings_get, _configs.BrowseConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.BrowseConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.BrowseConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_BrowseConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_BrowseConfig
    __del__ = lambda self : None;
BrowseConfig_swigregister = _configs.BrowseConfig_swigregister
BrowseConfig_swigregister(BrowseConfig)

class BrowseNextConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BrowseNextConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BrowseNextConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.BrowseNextConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.BrowseNextConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.BrowseNextConfig_serviceSettings_get, _configs.BrowseNextConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.BrowseNextConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.BrowseNextConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.BrowseNextConfig_translationSettings_get, _configs.BrowseNextConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.BrowseNextConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.BrowseNextConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_BrowseNextConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_BrowseNextConfig
    __del__ = lambda self : None;
BrowseNextConfig_swigregister = _configs.BrowseNextConfig_swigregister
BrowseNextConfig_swigregister(BrowseNextConfig)

class HistoryReadRawModifiedConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HistoryReadRawModifiedConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HistoryReadRawModifiedConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.HistoryReadRawModifiedConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.HistoryReadRawModifiedConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.HistoryReadRawModifiedConfig_serviceSettings_get, _configs.HistoryReadRawModifiedConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.HistoryReadRawModifiedConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.HistoryReadRawModifiedConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.HistoryReadRawModifiedConfig_translationSettings_get, _configs.HistoryReadRawModifiedConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.HistoryReadRawModifiedConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.HistoryReadRawModifiedConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_HistoryReadRawModifiedConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_HistoryReadRawModifiedConfig
    __del__ = lambda self : None;
HistoryReadRawModifiedConfig_swigregister = _configs.HistoryReadRawModifiedConfig_swigregister
HistoryReadRawModifiedConfig_swigregister(HistoryReadRawModifiedConfig)

class CreateMonitoredDataConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CreateMonitoredDataConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CreateMonitoredDataConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.CreateMonitoredDataConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.CreateMonitoredDataConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.CreateMonitoredDataConfig_serviceSettings_get, _configs.CreateMonitoredDataConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.CreateMonitoredDataConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.CreateMonitoredDataConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.CreateMonitoredDataConfig_translationSettings_get, _configs.CreateMonitoredDataConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.CreateMonitoredDataConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.CreateMonitoredDataConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_CreateMonitoredDataConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_CreateMonitoredDataConfig
    __del__ = lambda self : None;
CreateMonitoredDataConfig_swigregister = _configs.CreateMonitoredDataConfig_swigregister
CreateMonitoredDataConfig_swigregister(CreateMonitoredDataConfig)

class CreateMonitoredEventsConfig(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CreateMonitoredEventsConfig, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CreateMonitoredEventsConfig, name)
    __swig_setmethods__["serviceSettings"] = _configs.CreateMonitoredEventsConfig_serviceSettings_set
    __swig_getmethods__["serviceSettings"] = _configs.CreateMonitoredEventsConfig_serviceSettings_get
    if _newclass:serviceSettings = _swig_property(_configs.CreateMonitoredEventsConfig_serviceSettings_get, _configs.CreateMonitoredEventsConfig_serviceSettings_set)
    __swig_setmethods__["translationSettings"] = _configs.CreateMonitoredEventsConfig_translationSettings_set
    __swig_getmethods__["translationSettings"] = _configs.CreateMonitoredEventsConfig_translationSettings_get
    if _newclass:translationSettings = _swig_property(_configs.CreateMonitoredEventsConfig_translationSettings_get, _configs.CreateMonitoredEventsConfig_translationSettings_set)
    def __str__(self, indent="", colon=40): return _configs.CreateMonitoredEventsConfig___str__(self, indent, colon)
    def __repr__(self): return _configs.CreateMonitoredEventsConfig___repr__(self)
    def __init__(self): 
        this = _configs.new_CreateMonitoredEventsConfig()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _configs.delete_CreateMonitoredEventsConfig
    __del__ = lambda self : None;
CreateMonitoredEventsConfig_swigregister = _configs.CreateMonitoredEventsConfig_swigregister
CreateMonitoredEventsConfig_swigregister(CreateMonitoredEventsConfig)

# This file is compatible with both classic and new-style classes.


