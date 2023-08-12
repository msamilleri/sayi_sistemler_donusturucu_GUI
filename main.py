from main_page_python import Ui_MainWindow
import PyQt5
from sayisal_donusum import binary2decimal, decimal2binary, decimalToHexadecimal, HexadecimalTodecimal, hex2Bin, bin2hex
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene,QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap


class SayiDonustucuAPP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cevir_btn.pressed.connect(self.pintItem)


    def pintItem(self):
        try:
            content = self.ui.ceviri_cmbx.currentText()
            if self.ui.girilen_sayi_lne.text() =='':
                print("ERROR")

            match content:
                case 'Binary -> Dec':
                   res = binary2decimal(self.ui.girilen_sayi_lne.text())
                   res = str(res)
                   self.ui.decimal_lne.setText(res)
                   print(res)

                case 'Dec -> Binary':
                  res = decimal2binary(self.ui.girilen_sayi_lne.text())
                  res = str(res)
                  self.ui.binary_lne.setText(res)
                  print(res)

                case 'Hex -> Dec':
                  res = HexadecimalTodecimal(self.ui.girilen_sayi_lne.text())
                  res = str(res)
                  self.ui.decimal_lne.setText(res)

                case 'Dec -> Hex':
                     res = decimalToHexadecimal(self.ui.girilen_sayi_lne.text())
                     res = str(res)
                     self.ui.hexadecimal_lne.setText(res)
                     print(res)

                case 'Hex -> Binary':
                    res = hex2Bin(self.ui.girilen_sayi_lne.text())
                    res = str(res)
                    self.ui.binary_lne.setText(res)
                    print(res)

                case 'Binary -> Hex':
                    res = bin2hex(self.ui.girilen_sayi_lne.text())
                    res = str(res)
                    self.ui.hexadecimal_lne.setText(res)
                    print(res)

                case '_':
                    print("Error")
        except Exception:
            print("ERROR")
            QMessageBox.about(self, "Uyarı", "Sayi girilen alan boş bırakılmaz")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SayiDonustucuAPP()
    window.show()
    sys.exit(app.exec_())
