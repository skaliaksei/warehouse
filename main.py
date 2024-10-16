from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt6.QtGui import QIcon
import sys

# в скобках sys.argv если используем командную строку
app = QApplication(sys.argv)

window = QWidget()
# window.setGeometry(100, 100, 800, 600)
window.setWindowTitle('Фортива - Склад')
window.setWindowIcon(QIcon('./img/favicon.ico'))
window.setFixedSize(800, 600)
window.setStyleSheet('background-color: #3c3f41')
# window.setWindowOpacity(0.6)

window.show()

sys.exit(app.exec())