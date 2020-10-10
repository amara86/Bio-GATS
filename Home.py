# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
from PyQt5 import Qt, QtCore, QtGui, QtWidgets

from BrowseTemplate import Ui_BrowseTemplates
from SSDcalculate import Ui_SsdCalculator
from SearchTemplate import Ui_SearchTemplate
from helper import Helper

df_targ = pd.read_excel('gpcr_data.xlsx', sheet_name="Targets")


class Ui_HomeWindow(object):
    def __init__(self, HomeWindow):
        self.home_window = HomeWindow

    def setup_ui(self):
        self.home_window.setObjectName("home_window")
        self.home_window.resize(859, 706)
        self.centralwidget = QtWidgets.QWidget(self.home_window)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(12)

        self.radio_button_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_button_1.setGeometry(QtCore.QRect(130, 260, 401, 31))
        self.radio_button_1.setObjectName("radio_button_1")
        self.radio_button_1.input_type = 'sequence'
        self.radio_button_1.setChecked(True)
        self.radio_button_1.toggled.connect(self.on_clicked)

        self.input_path = QtWidgets.QLabel(self.centralwidget)
        self.input_path.setGeometry(QtCore.QRect(130, 460, 321, 51))
        self.input_path.setObjectName("input_path")
        self.input_path.setDisabled(True)

        self.radio_button_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_button_2.setGeometry(QtCore.QRect(130, 430, 401, 31))
        self.radio_button_2.setObjectName('radio_button_2')
        self.radio_button_2.input_type = 'file'
        self.radio_button_2.toggled.connect(self.on_clicked)

        self.choose_input_file = QtWidgets.QPushButton(self.centralwidget)
        self.choose_input_file.setGeometry(QtCore.QRect(490, 460, 151, 51))
        self.choose_input_file.setFont(font)
        self.choose_input_file.setObjectName("choose_input_file")
        self.choose_input_file.clicked.connect(self.chose_file)
        self.choose_input_file.setDisabled(True)

        self.browse_template = QtWidgets.QPushButton(self.centralwidget)
        self.browse_template.setGeometry(QtCore.QRect(470, 580, 261, 61))
        self.browse_template.setFont(font)
        self.browse_template.setObjectName("browse_template")
        self.browse_template.clicked.connect(self.browse)
        self.browse_template.setDisabled(True)

        self.search_template = QtWidgets.QPushButton(self.centralwidget)
        self.search_template.setGeometry(QtCore.QRect(190, 580, 261, 61))
        self.search_template.clicked.connect(self.search)
        self.search_template.setFont(font)
        self.search_template.setObjectName("search_template")
        self.search_template.setDisabled(True)

        self.clear_form = QtWidgets.QPushButton(self.centralwidget)
        self.clear_form.setGeometry(QtCore.QRect(130, 520, 131, 31))
        self.clear_form.setObjectName("clear_form")
        self.clear_form.clicked.connect(self.clear)
        self.clear_form.setDisabled(True)

        self.example_input = QtWidgets.QPushButton(self.centralwidget)
        self.example_input.setGeometry(QtCore.QRect(520, 260, 115, 25))
        self.example_input.setObjectName("example_input")
        self.example_input.clicked.connect(self.example)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 10, 641, 241))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap('logo.jpg'))
        self.label_4.setObjectName("label_4")

        fixed_width_font = QtGui.QFont()
        fixed_width_font.setPointSize(10)
        fixed_width_font.setFamily('Courier New')

        self.target_sequence = QtWidgets.QTextEdit(self.centralwidget)
        self.target_sequence.setGeometry(QtCore.QRect(130, 290, 641, 141))
        self.target_sequence.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.target_sequence.setFont(fixed_width_font)
        self.target_sequence.setObjectName("target_sequence")
        self.target_sequence.textChanged.connect(self.on_text_changed)

        self.custom_tm = QtWidgets.QPushButton(self.centralwidget)
        self.custom_tm.setGeometry(QtCore.QRect(650, 260, 115, 25))
        self.custom_tm.setObjectName("custom_tm")
        self.custom_tm.clicked.connect(self.custom_tm_click_handler)

        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(780, 10, 80, 30))
        self.help_button.setObjectName("help_button")
        self.help_button.clicked.connect(self.help_button_click_handler)

        self.menubar = QtWidgets.QMenuBar(self.home_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 20))
        self.menubar.setObjectName("menubar")
        self.home_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self.home_window)
        self.statusbar.setObjectName("statusbar")
        self.home_window.setStatusBar(self.statusbar)

        self.home_window.setCentralWidget(self.centralwidget)
        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.home_window)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.home_window.setWindowTitle(_translate("home_window", "home_window"))
        self.radio_button_1.setText(_translate("home_window", "Paste protein sequence in FASTA format"))
        self.radio_button_2.setText(_translate("home_window", "Upload the protein sequence from your computer"))
        self.choose_input_file.setText(_translate("home_window", "Choose File"))
        self.browse_template.setToolTip(_translate("home_window", "Browse from available list of GPCRs templates"))
        self.browse_template.setText(_translate("home_window", "Browse Template"))
        self.search_template.setToolTip(_translate("home_window", "Automated template selection"))
        self.search_template.setText(_translate("home_window", "Search Template"))
        self.clear_form.setText(_translate("home_window", "Clear form"))
        self.example_input.setText(_translate("home_window", "Example input"))
        self.custom_tm.setText(_translate("home_window", "SSD calculator"))
        self.help_button.setText(_translate("home_window", "Help"))

    def on_text_changed(self):
        is_disabled = self.target_sequence.toPlainText().strip() == '' and self.input_path.text().strip() == ''
        self.browse_template.setDisabled(is_disabled)
        self.search_template.setDisabled(is_disabled)

        has_content = self.target_sequence.toPlainText().strip() != '' or self.input_path.text().strip() != ''
        self.clear_form.setDisabled(not has_content)

    def on_clicked(self):
        if self.radio_button_1.isChecked():
            self.target_sequence.setDisabled(False)
            self.input_path.setDisabled(True)
            self.choose_input_file.setDisabled(True)
        elif self.radio_button_2.isChecked():
            self.target_sequence.setDisabled(True)
            self.input_path.setDisabled(False)
            self.choose_input_file.setDisabled(False)

    def help_button_click_handler(self):
        # TODO: replace with GitHub wiki url
        url = Qt.QUrl('https://www.google.com')
        Qt.QDesktopServices.openUrl(url)

    def example(self):
        self.target_sequence.setText(
            ">OR1A2\n"
            "MKKENQSFNLDFILLGVTSQQEQNNVFFVIFLCIYPITLTGNLLIILAICADIRLHNPMY\n"
            "FLLANLSLVDIIFSSVTIPKVLANHLLGSKFISFGGCLMQMYFMIALAKADSYTLAAMAY\n"
            "DRAVAISCPLHYTTIMSPRSCILLIAGSWVIGNTSALPHTLLTASLSFCGNQEVANFYCD\n"
            "IMPLLKLSCSDVHFNVKMMYLGVGVFSLPLLCIIVSYVQVFSTVFQVPSTKSLFKAFCTC\n"
            "GSHLTVVFLYYGTTMGMYFRPLTSYSPKDAVITVMYVAVTPALNPFIYSLRNWDMKAALQ\n"
            "KLFSKRISS")

    def clear(self):
        self.target_sequence.setText('')
        self.input_path.setText('')

    def custom_tm_click_handler(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SsdCalculator(self.window)
        self.ui.setup_ui()
        self.home_window.hide()
        self.window.setWindowTitle('SSD Calculator - Bio-GATS')
        self.window.show()

    def chose_file(self):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(caption='Select .fasta file containing GPCR sequence', filter='*.fasta')
        self.input_path.setText(filename)

        if not filename:
            QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), "Warning", "Please select a valid .fasta file")
            return

        with open(filename, 'r') as f:
            sequence = f.read()
            self.target_sequence.setText(sequence)

    def browse(self):
        seq_id = self.preprocess_input()
        if not seq_id:
            return

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BrowseTemplates(self.window, seq_id)
        self.ui.setup_ui()
        self.home_window.hide()
        self.window.setWindowTitle('Browse Template - Bio-GATS')
        self.window.show()

    def search(self):
        seq_id = self.preprocess_input()
        if not seq_id:
            return

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SearchTemplate(self.window, seq_id)
        self.ui.setup_ui()
        self.home_window.hide()
        self.window.setWindowTitle('Search Template - Bio-GATS')
        self.window.show()

    def preprocess_input(self):
        # read input from text editor
        sequence = self.target_sequence.toPlainText().strip()
        sequence = Helper.sanitize_input(sequence)

        # check if protein sequence is valid
        if not Helper.validate_input(sequence):
            QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), "Warning", "Please enter a valid GPCR sequence")
            return False

        # get unitprod_id of protein sequence
        seq_id = Helper.get_unitprot_id(sequence)
        if not seq_id:
            QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), "Warning", "Sequence not found in target file")
            return False

        return seq_id

    def helix_numbers(self, tup, df):
        name = tup[0]
        helix = []
        BW = []
        for i in range(1, 8):
            beg = 'TM' + str(i) + ' start'
            end = 'TM' + str(i) + ' end'
            bw = 'BW' + str(i) + '.50'
            tupbeg = df.loc[df['Uniprot_ID'] == name, beg].iloc[0]
            tupend = df.loc[df['Uniprot_ID'] == name, end].iloc[0]
            bw1 = df.loc[df['Uniprot_ID'] == name, bw].iloc[0]
            BW.append(int(bw1[1:]))
            helix.append((tupbeg, tupend))
            return (BW, helix)

    def split_helix(self, id, type, numbers):
        if type == 'template':
            ref = 'PDBID'
        elif type == 'target':
            ref = 'Uniprot_ID'
        prot = [[None for x in range(7)], [None for y in range(7)]]
        numb = [[None for x in range(7)], [None for y in range(7)]]
        seq = df_targ.loc[df_targ['Uniprot_ID'] == id, 'Sequence'].iloc[0]
        for i in range(1, 8):
            beg = int(df_targ.loc[df_targ['Uniprot_ID'] == id, 'TM' + str(i) + ' start'].iloc[0])
            end = int(df_targ.loc[df_targ['Uniprot_ID'] == id, 'TM' + str(i) + ' end'].iloc[0])
            numb[0][i - 1] = [beg, end]
            prot[0][i - 1] = seq[(int(beg) - 1):int(end)]
            bw = (df_targ.loc[df_targ['Uniprot_ID'] == id, 'BW' + str(i) + '.50'].iloc[0])
            numb[1][i - 1] = int(bw[1:])
            prot[1][i - 1] = int(bw[1:]) - int(beg)

        TM1 = prot[0][0]
        TM2 = prot[0][1]
        TM3 = prot[0][2]
        TM4 = prot[0][3]
        TM5 = prot[0][4]
        TM6 = prot[0][5]
        TM7 = prot[0][6]

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BrowseTemplates(self.window, TM1, TM2, TM3, TM4, TM5, TM6, TM7, id)
        self.ui.setup_ui()
        self.home_window.hide()
        self.home_window.setWindowTitle('Browse Template - Bio-GATS')
        self.window.show()
