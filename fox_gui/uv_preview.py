from PySide6.QtWidgets import QLabel
from PySide6.QtGui import (
    QPixmap,
    QPainter,
    QPen,
    QColor,
)
from PySide6.QtCore import Qt, QPointF


class UVPreview(QLabel):

    def __init__(self):

        super().__init__()

        self.setMinimumSize(700, 500)

        self.pix = None
        self.vertices = []

    def set_preview(self, image, vertices):

        self.pix = QPixmap(image)
        self.vertices = vertices

        self.update()

    def paintEvent(self, event):

        super().paintEvent(event)

        if self.pix is None:
            return

        painter = QPainter(self)

        scaled = self.pix.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        x = (self.width() - scaled.width()) / 2
        y = (self.height() - scaled.height()) / 2

        painter.drawPixmap(int(x), int(y), scaled)

        if len(self.vertices) < 2:
            return

        pen = QPen(QColor(255, 0, 0))
        pen.setWidth(2)

        painter.setPen(pen)

        points = []

        for v in self.vertices:

            px = x + v.u * scaled.width()
            py = y + v.v * scaled.height()

            points.append(QPointF(px, py))

        for i in range(len(points)):

            a = points[i]
            b = points[(i + 1) % len(points)]

            painter.drawLine(a, b)

        painter.setBrush(QColor(0, 255, 0))

        for p in points:

            painter.drawEllipse(p, 4, 4)
