from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import cv2

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,150,350,500)
        self.setWindowTitle("Instagram effects")
        self.ui()

    def ui(self):
        main_layout = QVBoxLayout()
        # main_layout.addStretch(1)

        effect_list = ['none', 'b/w', 'blur', 'negative']
        grid = QGridLayout()
        k=0
        for i in range(2):
            for j in range(2): # range(len(effect_list)/2)
                # b.clicked.connect(lambda: self.applyEffect(b.text))
                grid.addWidget(QPushButton(effect_list[k]), i, j)
                k=k+1

    # def applyEffect(self, v):
        # print(v)

        '''
        # for video processing >>>
        image_label = QLabel(self)
        org_pic = cv2.imread('perspective_image.png')
        height, width, bpc = org_pic.shape
        image = QImage(org_pic.data, width, height, bpc*width, QImage.Format_RGB888)
        pixMap = QPixmap(image)
        image_label.setPixmap(pixMap)
        # end video processing <<<
        '''

        
        # for image processing >>>
        image_label = QLabel(self)
        pixmap = QPixmap('perspective_image.png')
        image_label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        # end image processing <<<

        main_layout.addWidget(image_label)
        main_layout.addLayout(grid)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())