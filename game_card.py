from PySide6.QtWidgets import *
import os
from PySide6.QtCore import Qt



class GameCard(QWidget):

    def __init__(self, game):
        super().__init__()

        self.game = game
        self.setFixedWidth(240)
        self.setObjectName("GameCard")

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 10)
        layout.setSpacing(10)

        header = QWidget()
        header.setObjectName("CardHeader")
        header.setFixedHeight(12)

        name = QLabel(game["name"])
        name.setObjectName("GameName")
        name.setContentsMargins(5,5,5,5)
        name.setWordWrap(True)
        name.setAlignment(Qt.AlignCenter)

        button = QPushButton("Starten")
        button.setObjectName("StartButton")
        button.clicked.connect(self.start_game)

        layout.addWidget(header)
        layout.addWidget(name)
        layout.addWidget(button)
        layout.addStretch()
        self.setLayout(layout)

    def start_game(self):
        os.startfile(
            f"steam://rungameid/{self.game['appid']}"
        )