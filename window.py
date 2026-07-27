from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLineEdit
from game_card import GameCard
from steam import games


class MainWindow(QWidget):

    def __init__(self, games):
        super().__init__()

        self.games = games

        self.search = QLineEdit()

        self.search.setPlaceholderText("Search Games...")

        self.search.textChanged.connect(self.filter_games)

        self.setWindowTitle("Crazy Launcher")

        self.resize(1200,900)

        self.grid_layout = QGridLayout()

        main_layout = QVBoxLayout()

        self.grid_layout.setSpacing(10)

        row = 0
        column = 0

        self.columns = max(1, self.width() // 240)

        self.cards = []

        for game in games:
            card = GameCard(game)

            self.cards.append(card)

            self.grid_layout.addWidget(
                card,
                row,
                column
            )

            column += 1

            if column == self.columns:
                column = 0
                row += 1



        main_layout.addWidget(self.search)
        main_layout.addLayout(self.grid_layout)
        self.setLayout(main_layout)

    def filter_games(self):
        search_text = self.search.text().lower()

        row = 0
        column = 0

        for card in self.cards:
            self.grid_layout.removeWidget(card)
            card.hide()

        for card in self.cards:
            if search_text in card.game["name"].lower():
                self.grid_layout.addWidget(card, row, column)
                card.show()

                column += 1

                if column == self.columns:
                    column = 0
                    row += 1