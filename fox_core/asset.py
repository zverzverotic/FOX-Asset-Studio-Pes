"""
FOX Asset Studio
asset.py
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class FoxVertex:
    x: float
    y: float
    z: float
    u: float
    v: float


@dataclass
class FoxElement:
    material: str
    texture_index: int
    vertices: List[FoxVertex] = field(default_factory=list)


@dataclass
class FoxTemplate:
    name: str
    elements: List[FoxElement] = field(default_factory=list)


@dataclass
class FoxAsset:
    filename: str = ""
    version: int = 0

    textures: List[str] = field(default_factory=list)

    templates: Dict[str, FoxTemplate] = field(default_factory=dict)

    unknown_fields: Dict = field(default_factory=dict)

    def add_texture(self, path: str):
        self.textures.append(path)

    def add_template(self, template: FoxTemplate):
        self.templates[template.name] = template

    @property
    def texture_count(self):
        return len(self.textures)

    @property
    def template_count(self):
        return len(self.templates)
