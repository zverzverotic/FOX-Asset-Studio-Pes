"""
FOX Asset Studio
exporter.py

Exports FoxAsset back to PES TV JSON
"""

import json
from pathlib import Path

from .asset import FoxAsset


class FoxExporter:

    def export(self, asset: FoxAsset, filename):

        output = {
            "templates": {},
            "textures": list(asset.textures),
            "version": asset.version
        }

        #
        # Templates
        #

        for template_name, template in asset.templates.items():

            template_items = []

            for element in template.elements:

                item = {

                    "material": element.material,

                    "texture": element.texture_index,

                    "vertices": []

                }

                for vertex in element.vertices:

                    item["vertices"].append([
                        float(vertex.x),
                        float(vertex.y),
                        float(vertex.z),
                        float(vertex.u),
                        float(vertex.v)
                    ])

                template_items.append(item)

            output["templates"][template_name] = template_items

        #
        # Preserve unknown root fields
        #

        for key, value in asset.unknown_fields.items():

            if key not in output:
                output[key] = value

        filename = Path(filename)

        with open(filename, "w", encoding="utf-8") as fp:

            json.dump(
                output,
                fp,
                indent=4
            )
