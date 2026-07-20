"""
FOX Asset Studio
Asset data model

Author:
FOX Asset Studio Project

Target:
PES 2021 FOX Engine
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ---------------------------------------------------------
# TEXTURE
# ---------------------------------------------------------

@dataclass
class FoxTexture:

    name: str = ""
    path: str = ""
    texture_type: str = ""
    width: int = 0
    height: int = 0

    metadata: Dict = field(default_factory=dict)


# ---------------------------------------------------------
# MATERIAL
# ---------------------------------------------------------

@dataclass
class FoxMaterial:

    name: str = ""

    shader: str = ""

    textures: List[FoxTexture] = field(default_factory=list)

    metadata: Dict = field(default_factory=dict)


# ---------------------------------------------------------
# MODEL
# ---------------------------------------------------------

@dataclass
class FoxModel:

    name: str = ""

    file: str = ""

    metadata: Dict = field(default_factory=dict)


# ---------------------------------------------------------
# TEMPLATE
# ---------------------------------------------------------

@dataclass
class FoxTemplate:

    name: str = ""

    materials: List[FoxMaterial] = field(default_factory=list)

    models: List[FoxModel] = field(default_factory=list)

    metadata: Dict = field(default_factory=dict)


# ---------------------------------------------------------
# ASSET
# ---------------------------------------------------------

@dataclass
class FoxAsset:

    filename: str = ""

    version: int = 0

    asset_type: str = "UNKNOWN"

    templates: List[FoxTemplate] = field(default_factory=list)

    textures: List[FoxTexture] = field(default_factory=list)

    materials: List[FoxMaterial] = field(default_factory=list)

    models: List[FoxModel] = field(default_factory=list)

    metadata: Dict = field(default_factory=dict)

    unknown_fields: Dict = field(default_factory=dict)

    # -----------------------------------------------------

    def add_texture(self, texture: FoxTexture):

        self.textures.append(texture)

    # -----------------------------------------------------

    def add_material(self, material: FoxMaterial):

        self.materials.append(material)

    # -----------------------------------------------------

    def add_model(self, model: FoxModel):

        self.models.append(model)

    # -----------------------------------------------------

    def add_template(self, template: FoxTemplate):

        self.templates.append(template)

    # -----------------------------------------------------

    def clear(self):

        self.templates.clear()

        self.materials.clear()

        self.models.clear()

        self.textures.clear()

        self.metadata.clear()

        self.unknown_fields.clear()

    # -----------------------------------------------------

    @property
    def texture_count(self):

        return len(self.textures)

    # -----------------------------------------------------

    @property
    def material_count(self):

        return len(self.materials)

    # -----------------------------------------------------

    @property
    def model_count(self):

        return len(self.models)

    # -----------------------------------------------------

    @property
    def template_count(self):

        return len(self.templates)

    # -----------------------------------------------------

    def info(self):

        return {

            "filename": self.filename,

            "version": self.version,

            "asset_type": self.asset_type,

            "templates": self.template_count,

            "materials": self.material_count,

            "models": self.model_count,

            "textures": self.texture_count

        }

    # -----------------------------------------------------

    def __repr__(self):

        return (

            f"<FoxAsset "

            f"type={self.asset_type} "

            f"templates={self.template_count} "

            f"materials={self.material_count} "

            f"models={self.model_count} "

            f"textures={self.texture_count}>"

        )
