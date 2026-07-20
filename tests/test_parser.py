import unittest
from pathlib import Path

from fox_core.parser import FoxParser


class TestFoxParser(unittest.TestCase):

    def setUp(self):
        self.parser = FoxParser()

        # Promeni ovu putanju na svoj JSON
        self.sample = Path("samples/tv_template_st081_basic.json")

    def test_load(self):

        asset = self.parser.load(self.sample)

        self.assertGreaterEqual(asset.version, 1)

    def test_has_templates(self):

        asset = self.parser.load(self.sample)

        self.assertGreater(asset.template_count, 0)

    def test_has_textures(self):

        asset = self.parser.load(self.sample)

        self.assertGreater(asset.texture_count, 0)

    def test_texture_indexes(self):

        asset = self.parser.load(self.sample)

        texture_count = asset.texture_count

        for template in asset.templates.values():

            for element in template.elements:

                self.assertGreaterEqual(
                    element.texture_index,
                    0
                )

                self.assertLess(
                    element.texture_index,
                    texture_count
                )


if __name__ == "__main__":
    unittest.main()
