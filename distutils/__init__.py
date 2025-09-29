# Shim to provide distutils module on Python versions where it's removed from stdlib
# This file simply re-exports setuptools' distutils compatibility package if available.
try:
    # setuptools provides a vendored distutils package on newer Pythons
    from setuptools import _distutils as distutils
    # Expose submodules to mimic the stdlib distutils package
    import importlib
    import types
    module = types.ModuleType('distutils')
    for attr in dir(distutils):
        try:
            setattr(module, attr, getattr(distutils, attr))
        except Exception:
            pass
    # Make the module available under name 'distutils'
    import sys
    sys.modules['distutils'] = module
except Exception:
    # Fallback: try importing real distutils (if present) or raise the original import error
    try:
        import distutils  # type: ignore
    except Exception:
        raise
