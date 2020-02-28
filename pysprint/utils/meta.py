from collections.abc import Mapping
from collections import OrderedDict

__all__ = ['MetaData']

class MetaData:
    """
    A class to store additional meta property.
    This can be set to any valid ~collections.abc.Mapping.
    Shamefully borrowed from astropy, all the credits to them.

    Parameters
    ----------
    doc : `str`, optional
        Documentation for the attribute of the class.
        Default is ``""``.

    copy : `bool`, optional
        If ``True`` the the value is deepcopied before setting, otherwise it
        is saved as reference.
        Default is ``True``.

    """

    def __init__(self, doc="", copy=True):
        self.__doc__ = doc
        self.copy = copy

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if not hasattr(instance, '_meta'):
            instance._meta = OrderedDict()
        return instance._meta

    def __set__(self, instance, value):
        if value is None:
            instance._meta = OrderedDict()
        else:
            if isinstance(value, Mapping):
                if self.copy:
                    instance._meta = deepcopy(value)
                else:
                    instance._meta = value
            else:
                raise TypeError("meta attribute must be dict-like")