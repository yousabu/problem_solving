from time import time

class Debugger(object):
  attribute_acceses = []
  method_calls = []

class Meta(type):
  def __new__(cls, name, bases, atts):
    for k,v in atts.items():
      if callable(v): atts[k] = wrapped_method(cls, v)
    atts['__getattribute__'] = wrapped_getattribute(cls)
    atts['__setattr__'] = wrapped_setattr(cls)
    return type.__new__(cls, name, bases, atts)

def wrapped_method(c, f):
  def w(*args, **kwargs):
    a = time()
    r = f(*args, **kwargs)
    b = time()
    Debugger.method_calls.append({'class':c,'mehod':f.__name__,'args':args,'kwargs':kwargs,'time':b-a})
  return w

def wrapped_setattr(c):
  def s(self, k, v):
    object.__setattr__(self, k, v)
    Debugger.attribute_acceses.append({'action':'set','class':c,'attribute':k,'value':v})
  return s

def wrapped_getattribute(c):
  def g(self, k):
    v = object.__getattribute__(self, k)
    Debugger.attribute_acceses.append({'action':'get','class':c,'attribute':k,'value':v})
    return v
  return g