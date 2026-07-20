"""
FOX Asset Studio
parser.py

Parser for PES 2021 FOX TV template JSON
"""

from pathlib import Path
import json

from .asset import (
    FoxAsset,
    FoxTemplate,
    FoxElement,
    FoxVertex,
)


class FoxParser:

    def load(self, filename):

        filename = Path(filename)

        if not filename.exists():
            raise FileNotFoundError(filename)

        with open(filename, "r", encoding="utf-8") as fp:
            data = json.load(fp)

        asset = FoxAsset()

        asset.filename = filename.name
        asset.version = data.get("version", 0)

        #
        # TEXTURES
        #

        textures = data.get("textures", [])

        for texture in textures:
            asset.add_texture(texture)

        #
        # TEMPLATES
        #

        template_root = data.get("templates", {})

        for template_name, template_items in template_root.items():

            template = FoxTemplate(name=template_name)

            for item in template_items:

                material = item.get("material", "")

                texture_index = item.get("texture", -1)

                element = FoxElement(
                    material=material,
                    texture_index=texture_index
                )

                vertices = item.get("vertices", [])

                for vertex in vertices:

                    #
                    # Vertex format:
                    # [x,y,z,u,v]
                    #

                    if len(vertex) < 5:
                        continue

                    element.vertices.append(

                        FoxVertex(
                            x=float(vertex[0]),
                            y=float(vertex[1]),
                            z=float(vertex[2]),
                            u=float(vertex[3]),
                            v=float(vertex[4])
                        )

                    )

                template.elements.append(element)

            asset.add_template(template)

        #
        # UNKNOWN ROOT FIELDS
        #

        for key, value in data.items():

            if key not in (
                "version",
                "templates",
                "textures",
            ):

                asset.unknown_fields[key] = value

        return asset

    # -------------------------------------------------

    def get_texture_path(self, asset, texture_index):

        if texture_index < 0:
            return None

        if texture_index >= len(asset.textures):
            return None

        return asset.textures[texture_index]

    # -------------------------------------------------

    def print_summary(self, asset):

        print("=" * 40)

        print("FOX TV ASSET")

        print("=" * 40)

        print("File:", asset.filename)

        print("Version:", asset.version)

        print("Templates:", asset.template_count)

        print("Textures:", asset.texture_count)

        print()

        for template in asset.templates.values():

            print(template.name)

            print(" Elements:", len(template.elements))

            for element in template.elements:

                texture = self.get_texture_path(
                    asset,
                    element.texture_index
                )

                print(
                    "   Material:",
                    element.material
                )

                print(
                    "   Texture:",
                    texture
                )

                print(
                    "   Vertices:",
                    len(element.vertices)
                )

            print()
