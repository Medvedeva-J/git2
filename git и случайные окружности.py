import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_mw


class Example(QMainWindow, Ui_mw):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        y = self.size().height()
        x = self.size().width()
        for k in range(7):
            qp.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            x = random.randint(0, 300)
            y = random.randint(0, 300)
            a = random.randint(10, 250)
            qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())