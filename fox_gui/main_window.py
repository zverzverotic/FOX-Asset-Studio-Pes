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


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.parser = FoxParser()
        self.asset = None

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

        self.templateList = QListWidget()

        left.addWidget(self.openButton)
        left.addWidget(self.templateList)

        #
        # Right panel
        #

        right = QVBoxLayout()

        self.preview = QLabel("Texture Preview")

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

        self.templateList.clear()

        for name in self.asset.templates.keys():

            self.templateList.addItem(name)

    def template_changed(self, name):

        if self.asset is None:
            return

        template = self.asset.templates[name]

        self.info.setText(

            f"""
Template:

{name}

Elements:

{len(template.elements)}
"""
        )
