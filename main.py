from PyQt6.QtWidgets import QApplication, QWidget
import sys

# в скобках sys.argv если используем командную строку
app = QApplication(sys.argv)

window = QWidget()
window.show()

sys.exit(app.exec())