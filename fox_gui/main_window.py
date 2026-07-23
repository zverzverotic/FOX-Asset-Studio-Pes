from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QListWidget,
    QLabel,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
)

from fox_core.parser import FoxParser
from pathlib import Path
from fox_core.exporter import FoxExporter

from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.parser = FoxParser()
        self.exporter = FoxExporter()

self.current_file = None
        self.asset = None
        self.current_template = None
self.texture_folder = None

        self.setWindowTitle("FOX Asset Studio")
        self.resize(1200, 700)

        self.create_ui()

    def create_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        #
        # Left panel
        #

        left = QVBoxLayout()

        self.openButton = QPushButton("Open JSON")
        self.saveButton = QPushButton("Save JSON")

        self.templateList = QListWidget()

       left.addWidget(self.openButton)
left.addWidget(self.saveButton)
left.addWidget(self.templateList)

        #
        # Right panel
        #

        right = QVBoxLayout()

        from uv_preview import UVPreview

self.preview = UVPreview()

        self.preview.setMinimumSize(700, 500)

        self.info = QLabel("No asset loaded")

        right.addWidget(self.preview)
        right.addWidget(self.info)

        layout.addLayout(left, 1)

        layout.addLayout(right, 3)

        #
        # Signals
        #

        self.openButton.clicked.connect(
            self.open_json
        )

        self.templateList.currentTextChanged.connect(
            self.template_changed
        )
self.saveButton.clicked.connect(
    self.save_json
)

    def open_json(self):

        filename, _ = QFileDialog.getOpenFileName(

            self,

            "Open TV JSON",

            "",

            "JSON (*.json)"

        )

        if not filename:
            return

        self.asset = self.parser.load(filename)
        self.current_file = filename
        folder = QFileDialog.getExistingDirectory(

    self,

    "Select Texture Folder"

)

if folder:

    self.texture_folder = folder

        self.templateList.clear()

        for name in self.asset.templates.keys():

            self.templateList.addItem(name)

    def template_changed(self, name):

    if self.asset is None:
        return

    self.current_template = self.asset.templates[name]

    element = self.current_template.elements[0]

    texture_path = self.asset.textures[element.texture_index]

    texture_name = Path(texture_path).stem

    self.info.setText(

f"""Template

{name}

Material:
{element.material}

Texture Index:
{element.texture_index}

Texture:
{texture_name}

Vertices:
{len(element.vertices)}
"""
    )

    #
    # Preview PNG ako postoji
    #

    if self.texture_folder is None:
        return

    png = Path(self.texture_folder) / (texture_name + ".png")

    if png.exists():

      self.preview.set_preview(
    str(png),
    element.vertices
)

        

    else:

        self.preview.setText(

            "Preview not found"
        )
