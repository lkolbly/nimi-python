# This file was generated

import platform

from niscope import errors
from niscope import library


_instance = None


def _get_library_name():
    try:
        return {'Linux': {'64bit': {'name': 'libscope.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'niscope_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'niscope_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['name']
    except KeyError:  # pragma: no cover
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return {'Linux': {'64bit': {'name': 'libscope.so', 'type': 'cdll'}},
                'Windows': {'32bit': {'name': 'niscope_32.dll', 'type': 'windll'},
                            '64bit': {'name': 'niscope_64.dll', 'type': 'cdll'}}}[platform.system()][platform.architecture()[0]]['type']
    except KeyError:  # pragma: no cover
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for niscope.
    '''
    global _instance
    if _instance is None:
        try:
            _instance = library.Library(_get_library_name(), _get_library_type())
        except OSError:  # pragma: no cover
            raise errors.DriverNotInstalledError()
    return _instance
