__author__ = 'Habeeb'

import sys
from PyQt4 import QtGui,QtCore

class CgpaCalc(QtGui.QWidget):

    def __init__(self):
        super(CgpaCalc, self).__init__()

        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        space1 = QtGui.QLabel("")

        # Labels

        title = QtGui.QLabel("Enter the course unit and scores in the spaces provided below")
        title.setIndent(50)

        title2 = QtGui.QLabel("Click Next to Start")
        title2.setIndent(60)

        name = QtGui.QLabel("Name")
        regno = QtGui.QLabel("Reg. No")
        dept = QtGui.QLabel("GPA")

        courses = QtGui.QLabel("Courses")
        units = QtGui.QLabel("Units")
        scores = QtGui.QLabel("Scores")
        grades = QtGui.QLabel("Grades")

        # Line edits --->> Text boxes

        nm1 = QtGui.QLineEdit(self)
        rg = QtGui.QLineEdit(self)
        dpt = QtGui.QLineEdit(self)

        course1 = QtGui.QLineEdit(self)
        course2 = QtGui.QLineEdit(self)
        course3 = QtGui.QLineEdit(self)
        course4 = QtGui.QLineEdit(self)
        course5 = QtGui.QLineEdit(self)
        course6 = QtGui.QLineEdit(self)

        unit1 = QtGui.QLineEdit(self)
        unit2 = QtGui.QLineEdit(self)
        unit3 = QtGui.QLineEdit(self)
        unit4 = QtGui.QLineEdit(self)
        unit5 = QtGui.QLineEdit(self)
        unit6 = QtGui.QLineEdit(self)

        score1 = QtGui.QLineEdit(self)
        score2 = QtGui.QLineEdit(self)
        score3 = QtGui.QLineEdit(self)
        score4 = QtGui.QLineEdit(self)
        score5 = QtGui.QLineEdit(self)
        score6 = QtGui.QLineEdit(self)

        grade1 = QtGui.QLineEdit(self)
        grade2 = QtGui.QLineEdit(self)
        grade3 = QtGui.QLineEdit(self)
        grade4 = QtGui.QLineEdit(self)
        grade5 = QtGui.QLineEdit(self)
        grade6 = QtGui.QLineEdit(self)

        # Buttons

        calcBtn = QtGui.QPushButton("Calculate CGPA", self)
        rstBtn = QtGui.QPushButton("Reset",self)
        prevBtn = QtGui.QPushButton("Previous",self)
        nxtBtn = QtGui.QPushButton("Next", self)
        extBtn = QtGui.QPushButton("Exit", self)


        grid.addWidget(title, 0, 0, 1, 6)
        grid.addWidget(title2, 1, 0, 1, 6)

        # ADDING COURSES LABELS AND LINE EDITS

        grid.addWidget(courses, 2, 3)
        grid.addWidget(course1, 3, 3)
        grid.addWidget(course2, 4, 3)
        grid.addWidget(course3, 5, 3)
        grid.addWidget(course4, 6, 3)
        grid.addWidget(course5, 7, 3)
        grid.addWidget(course6, 8, 3)

        # ADDING UNITS AND LINE EDITS

        grid.addWidget(units, 2, 4)
        grid.addWidget(unit1, 3, 4)
        grid.addWidget(unit2, 4, 4)
        grid.addWidget(unit3, 5, 4)
        grid.addWidget(unit4, 6, 4)
        grid.addWidget(unit5, 7, 4)
        grid.addWidget(unit6, 8, 4)

        # ADDING SCORES LABEL AND SCORES EDIT

        grid.addWidget(scores, 2, 5)
        grid.addWidget(score1, 3, 5)
        grid.addWidget(score2, 4, 5)
        grid.addWidget(score3, 5, 5)
        grid.addWidget(score4, 6, 5)
        grid.addWidget(score5, 7, 5)
        grid.addWidget(score6, 8, 5)

        # ADDING GRADE LABEL AND GRADE EDITS

        grid.addWidget(grades, 2, 6)
        grid.addWidget(grade1, 3, 6)
        grid.addWidget(grade2, 4, 6)
        grid.addWidget(grade3, 5, 6)
        grid.addWidget(grade4, 6, 6)
        grid.addWidget(grade5, 7, 6)
        grid.addWidget(grade6, 8, 6)

        # ADDING STUDENT INFO LABEL AND LINE EDIT

        grid.addWidget(name, 3, 0)
        grid.addWidget(nm1, 3, 1)
        grid.addWidget(regno, 4, 0)
        grid.addWidget(rg, 4, 1)
        grid.addWidget(dept, 5, 0)
        grid.addWidget(dpt, 5, 1)
        grid.addWidget(space1, 6, 0)
        grid.addWidget(calcBtn, 7, 0, 1, 2)
        grid.addWidget(rstBtn, 10, 2)
        grid.addWidget(prevBtn, 10, 3)
        grid.addWidget(nxtBtn, 10, 4)
        grid.addWidget(extBtn, 10, 5)


        self.setLayout(grid)
        self.setGeometry(300,150,400,290)
        self.setWindowTitle('CGPA Calculator')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    calc = CgpaCalc()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()