"""
FOX Asset Studio
Exceptions
"""


class FoxError(Exception):
    """Base FOX exception."""
    pass


class InvalidFoxJson(FoxError):
    """JSON file is invalid."""
    pass


class UnsupportedVersion(FoxError):
    """Unsupported FOX version."""
    pass


class MissingTemplate(FoxError):
    """Template missing."""
    pass


class MissingMaterial(FoxError):
    """Material missing."""
    pass


class MissingTexture(FoxError):
    """Texture missing."""
    pass


class MissingModel(FoxError):
    """Model missing."""
    pass


class ParserError(FoxError):
    """General parser error."""
    pass
