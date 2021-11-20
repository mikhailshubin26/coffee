import sys, sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.result = self.cur.execute("""SELECT * FROM coffee""").fetchall()
        self.sp = []
        for el in self.result:
            elem = el[1]
            self.sp.append(elem)
        self.comboBox.addItems(self.sp)

    def run(self):
        # print(self.result)
        g = (self.comboBox.currentText())
        print(g)
        output = ''
        for element in self.result:
            if element[1] == g:
                output += f'Название: {element[1]}\n'
                output += f'Степень обжарки: {element[2]}\n'
                if element[3] == 'beens':
                    output += f'Вид: В зёрнах\n'
                elif element[3] == 'ground':
                    output += f'Вид: Молотый\n'
                output += f'Описание: {element[4]}\n'
                output += f'Цена: {element[5]}\n'
                output += f'Объём: {element[6]}\n'
            else:
                continue
        self.plainTextEdit.setPlainText(output)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())