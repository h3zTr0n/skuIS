# ------------------------------------------------------------------------------
# Appy is a framework for building applications in the Python language.
 
# ------------------------------------------------------------------------------
class AppyError(Exception):
    '''Root Appy exception class.'''
    pass

class ValidationError(AppyError):
    '''Represents an error that occurs on data sent to the Appy server.'''
    pass

class InternalError(AppyError):
    '''Represents a programming error: something that should never occur.'''
    pass
# ------------------------------------------------------------------------------
