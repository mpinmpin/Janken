import sys
import random
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QGridLayout)


class Janken(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.labels()
        self.buttons()

    def initUI(self):
        self.setFixedSize(400, 250)
        self.center()
        self.setWindowTitle('Janken')

        self.winpoints = 0
        self.drawpoints = 0
        self.losepoints = 0

    def buttons(self):
        rock = 'Rock'
        paper = 'Paper'
        scissors = 'Scissors'

        rockbtn = QPushButton(rock, self)
        rockbtn.setFixedSize(80, 30)
        rockbtn.move(50, 50)
        rockbtn.clicked.connect(self.pickrock)
        rockbtn.clicked.connect(self.roundupdate)

        paperbtn = QPushButton(paper, self)
        paperbtn.setFixedSize(80, 30)
        paperbtn.move(50, 100)
        paperbtn.clicked.connect(self.pickpaper)
        paperbtn.clicked.connect(self.roundupdate)

        scibtn = QPushButton(scissors, self)
        scibtn.setFixedSize(80, 30)
        scibtn.move(50, 150)
        scibtn.clicked.connect(self.pickscissors)
        scibtn.clicked.connect(self.roundupdate)

    def labels(self):
        self.roundcnt = 0
        self.roundlbl = QLabel(f'Round: {self.roundcnt}', self)
        self.roundlbl.move(200, 60)
        self.roundlbl.resize(150, 15)

        self.youlbl = QLabel(f'You chose:', self)
        self.youlbl.move(200, 85)
        self.youlbl.resize(150, 15)

        self.comlbl = QLabel(f'COM chose :', self)
        self.comlbl.move(200, 100)
        self.comlbl.resize(150, 15)

        self.thisroundlbl = QLabel('', self)
        self.thisroundlbl.move(200, 115)
        self.thisroundlbl.resize(150, 15)

        self.resultlbl = QLabel(f'Results : \n'
                                f'You: {self.winpoints} '
                                f'Draw: {self.drawpoints} '
                                f'Opponent: {self.losepoints} ', self)
        self.resultlbl.move(200, 150)
        self.resultlbl.resize(250, 35)

    def pickrock(self):
        self.yourpick = 'Rock'
        self.opp_choose = self.opp_pick()

    def pickpaper(self):
        self.yourpick = 'Paper'
        self.opp_choose = self.opp_pick()

    def pickscissors(self):
        self.yourpick = 'Scissors'
        self.opp_choose = self.opp_pick()

    def opp_pick(self):
        ranlist = ['Rock', 'Paper', 'Scissors']
        rand = random.choice(ranlist)
        return rand

    def roundresult(self):
        if self.yourpick == self.opp_choose:
            self.drawpoints += 1
            return 'draw'
        elif self.yourpick == 'Rock'and self.opp_choose == 'Scissors':
            self.winpoints += 1
            return 'win'
        elif self.yourpick == 'Paper' and self.opp_choose == 'Rock':
            self.winpoints += 1
            return 'win'
        elif self.yourpick == 'Scissors' and self.opp_choose == 'Paper':
            self.winpoints += 1
            return 'win'
        else:
            self.losepoints +=1
            return 'lose'

    def roundupdate(self):
        self.roundcnt += 1
        self.youlbl.setText(f'You chose: {self.yourpick}')
        self.roundlbl.setText(f'Round: {self.roundcnt}')
        self.comlbl.setText(f'COM chose: {self.opp_choose}')
        self.thisroundlbl.setText(f'You {self.roundresult()} this round.')
        self.resultlbl.setText(f'Results : \n'
                               f'You: {self.winpoints} '
                               f'Draw: {self.drawpoints} '
                               f'Opponent: {self.losepoints} ')

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    jan = Janken()
    jan.show()
    sys.exit(app.exec())
