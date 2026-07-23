"""
FOX Asset Studio
texture_manager.py

Manages TV textures referenced by FOX JSON.
"""

from pathlib import Path
import shutil


class TextureManager:

    def __init__(self, asset):

        self.asset = asset

    # -----------------------------------------------------

    def texture_path(self, texture_index):

        if texture_index < 0:
            return None

        if texture_index >= len(self.asset.textures):
            return None

        return self.asset.textures[texture_index]

    # -----------------------------------------------------

    def texture_name(self, texture_index):

        path = self.texture_path(texture_index)

        if path is None:
            return None

        return Path(path).stem

    # -----------------------------------------------------

    def dds_filename(self, texture_index):

        name = self.texture_name(texture_index)

        if name is None:
            return None

        return name + ".dds"

    # -----------------------------------------------------

    def png_filename(self, texture_index):

        name = self.texture_name(texture_index)

        if name is None:
            return None

        return name + ".png"

    # -----------------------------------------------------

    def locate(self, texture_index, search_folder):

        search_folder = Path(search_folder)

        dds = search_folder / self.dds_filename(texture_index)

        if dds.exists():
            return dds

        png = search_folder / self.png_filename(texture_index)

        if png.exists():
            return png

        return None

    # -----------------------------------------------------

    def backup(self, texture_file):

        texture_file = Path(texture_file)

        backup = texture_file.with_suffix(
            texture_file.suffix + ".bak"
        )

        shutil.copy2(texture_file, backup)

        return backup

    # -----------------------------------------------------

    def replace(self, destination, new_texture):

        destination = Path(destination)

        new_texture = Path(new_texture)

        if not destination.exists():
            raise FileNotFoundError(destination)

        if not new_texture.exists():
            raise FileNotFoundError(new_texture)

        self.backup(destination)

        shutil.copy2(new_texture, destination)

        return destination

    # -----------------------------------------------------

    def print_summary(self):

        print("=" * 40)

        print("FOX Texture Manager")

        print("=" * 40)

        for i, path in enumerate(self.asset.textures):

            print(f"[{i}] {Path(path).name}")
