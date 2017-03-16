from hello import Hello
import sys
sys.path.append('G:\\eclipse mares programs\\Database Tests\\PE Resources Management\\UIs')#import from other directory
from PyQt5.QtWidgets import QApplication
from windowTesting import MyWindow
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    dlg = Hello()
    dlg.show()
    sys.exit(app.exec_())