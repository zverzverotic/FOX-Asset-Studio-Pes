"""
FOX Asset Studio
validator.py
"""

from pathlib import Path

from .exceptions import (
    InvalidFoxJson,
    MissingMaterial,
    MissingModel,
    MissingTemplate,
    MissingTexture,
)


class FoxValidator:

    REQUIRED_ROOT_KEYS = (
        "version",
        "templates",
        "textures",
    )

    def validate_root(self, data: dict):

        if not isinstance(data, dict):
            raise InvalidFoxJson("Root element must be dictionary.")

        for key in self.REQUIRED_ROOT_KEYS:

            if key not in data:
                raise InvalidFoxJson(
                    f"Missing root key '{key}'"
                )

        return True

    # ----------------------------------------

    def validate_templates(self, asset):

        if len(asset.templates) == 0:
            raise MissingTemplate(
                "Asset contains no templates."
            )

        return True

    # ----------------------------------------

    def validate_materials(self, asset):

        if len(asset.materials) == 0:
            raise MissingMaterial(
                "Asset contains no materials."
            )

        return True

    # ----------------------------------------

    def validate_models(self, asset):

        if len(asset.models) == 0:
            raise MissingModel(
                "Asset contains no models."
            )

        return True

    # ----------------------------------------

    def validate_textures(self, asset):

        if len(asset.textures) == 0:
            raise MissingTexture(
                "Asset contains no textures."
            )

        return True

    # ----------------------------------------

    def validate_file_exists(self, path):

        return Path(path).exists()

    # ----------------------------------------

    def validate_asset(self, asset):

        self.validate_templates(asset)

        self.validate_materials(asset)

        self.validate_models(asset)

        self.validate_textures(asset)

        return True
