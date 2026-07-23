import unittest
from pathlib import Path

from fox_core.parser import FoxParser


class ParserTests(unittest.TestCase):

    def setUp(self):

        self.parser = FoxParser()

        self.sample = Path(
            "samples/tv_template_st081_basic.json"
        )

    def test_load(self):

        asset = self.parser.load(self.sample)

        self.assertEqual(
            asset.version,
            2
        )

    def test_templates_exist(self):

        asset = self.parser.load(self.sample)

        expected = {

            "match_score_small",

            "score_large",

            "match_score_large",

            "match_small",

            "score_small",

            "match_large",

        }

        self.assertEqual(
            set(asset.templates.keys()),
            expected
        )

    def test_textures(self):

        asset = self.parser.load(self.sample)

        self.assertEqual(
            asset.texture_count,
            3
        )

    def test_texture_indexes(self):

        asset = self.parser.load(self.sample)

        for template in asset.templates.values():

            for element in template.elements:

                self.assertGreaterEqual(
                    element.texture_index,
                    0
                )

                self.assertLess(
                    element.texture_index,
                    asset.texture_count
                )


if __name__ == "__main__":
    unittest.main()
