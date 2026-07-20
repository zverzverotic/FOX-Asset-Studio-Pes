"""
FOX Asset Studio
parser.py
"""

import json
from pathlib import Path

from .asset import (
    FoxAsset,
    FoxTemplate,
    FoxElement,
    FoxVertex,
)


class FoxParser:

    def load(self, filename):

        filename = Path(filename)

        with open(filename, "r", encoding="utf-8") as f:
            raw = json.load(f)

        asset = FoxAsset()

        asset.filename = filename.name
        asset.version = raw.get("version", 0)

        # --------------------------
        # Textures
        # --------------------------

        for texture in raw.get("textures", []):

            asset.add_texture(texture)

        # --------------------------
        # Templates
        # --------------------------

        template_dict = raw.get("templates", {})

        for template_name, objects in template_dict.items():

            template = FoxTemplate(name=template_name)

            for obj in objects:

                element = FoxElement(
                    material=obj["material"],
                    texture_index=obj["texture"]
                )

                for vertex in obj["vertices"]:

                    element.vertices.append(

                        FoxVertex(
                            x=vertex[0],
                            y=vertex[1],
                            z=vertex[2],
                            u=vertex[3],
                            v=vertex[4]
                        )

                    )

                template.elements.append(element)

            asset.add_template(template)

        # --------------------------
        # Unknown Fields
        # --------------------------

        for key, value in raw.items():

            if key not in (
                "version",
                "textures",
                "templates"
            ):
                asset.unknown_fields[key] = value

        return asset
