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

        self.points = []

        self.offset_x = 0
        self.offset_y = 0

        self.scale_w = 1
        self.scale_h = 1

        self.selected = -1

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

        self.scale_w = scaled.width()
        self.scale_h = scaled.height()

        self.offset_x = (self.width() - scaled.width()) / 2
        self.offset_y = (self.height() - scaled.height()) / 2

        painter.drawPixmap(
            int(self.offset_x),
            int(self.offset_y),
            scaled
        )

        pen = QPen(QColor(255, 0, 0))
        pen.setWidth(2)

        painter.setPen(pen)

        self.points.clear()

        for v in self.vertices:

            x = self.offset_x + v.u * self.scale_w
            y = self.offset_y + v.v * self.scale_h

            self.points.append(QPointF(x, y))

        if len(self.points) > 1:

            for i in range(len(self.points)):

                a = self.points[i]
                b = self.points[(i + 1) % len(self.points)]

                painter.drawLine(a, b)

        for i, p in enumerate(self.points):

            if i == self.selected:
                painter.setBrush(QColor(255, 255, 0))
            else:
                painter.setBrush(QColor(0, 255, 0))

            painter.drawEllipse(p, 5, 5)

    def mousePressEvent(self, event):

        self.selected = -1

        for i, p in enumerate(self.points):

            if abs(event.position().x() - p.x()) < 8 and \
               abs(event.position().y() - p.y()) < 8:

                self.selected = i
                break

        self.update()

    def mouseMoveEvent(self, event):

        if self.selected == -1:
            return

        x = event.position().x()
        y = event.position().y()

        u = (x - self.offset_x) / self.scale_w
        v = (y - self.offset_y) / self.scale_h

        u = max(0.0, min(1.0, u))
        v = max(0.0, min(1.0, v))

        self.vertices[self.selected].u = u
        self.vertices[self.selected].v = v

        self.update()

    def mouseReleaseEvent(self, event):

        self.selected = -1

        self.update()
