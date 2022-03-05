import json
import sys

import requests

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QImage, QIcon, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skin Finder")

        icon = QIcon("logo.jpg")

        self.setWindowIcon(icon)

        self.image_label = QLabel(self)
        self.setup_ui()

    def setup_ui(self):
        self.setFixedSize(QSize(400, 300))

        self.image_label.setGeometry(100, 75, 200, 200)

        textbox = QLineEdit(self)
        textbox.resize(280, 40)

        button = QPushButton("Find Skin", self)
        button.clicked.connect(lambda: self.get_n_set(textbox.text()))

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(textbox)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def get_n_set(self, username): # Gotta love this nesting, LOL. I rlly cba to fix this its 3:00 and im hungry AFAF
        try:
            if username != "":
                print("Searching for " + username)

                UUID_URL = "https://api.minetools.eu/uuid/"
                SKIN_URL = "https://crafatar.com/renders/head/"

                r = requests.get(url=UUID_URL + username)

                data = r.json()
                
                uuid = data["id"]
                
                if uuid != None:
                    print(uuid)
                
                    image = QImage()
                    image.loadFromData(requests.get(SKIN_URL + uuid).content)
                    
                    self.image_label.setPixmap(QPixmap(image))
                else:
                    print("Unable to find user")
            else:
                print("Unable to search user")
        except:
            print("Unable to search")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
