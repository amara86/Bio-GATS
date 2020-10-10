# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import matplotlib.pyplot as plt
import pandas as pd
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
from PyQt5 import QtCore, QtGui, QtWidgets

from Alignment import Ui_Alignment
from helper import Helper


class Ui_SearchTemplate(object):
    def __init__(self, SearchTemplate, seq_id):
        self.search_template = SearchTemplate
        self.targ_id = seq_id
        self.hotspot_residue_positions = Helper.non_olfactory_hotspot_residue_positions

        self.template = []
        self.target = []

        self.ress = []
        self.hydrh = []
        self.summ = [0] * 7
        self.value = [0] * 7
        self.plot_data = {}
        self.current_df = ''

        self.index_temp1 = 0
        self.index_temp2 = 0
        self.index_temp3 = 0
        self.state_selected_index = 0
        self.identities = []

        self.temp_df = pd.DataFrame()

    def setup_ui(self):
        self.search_template.setObjectName("search_template")
        self.search_template.resize(900, 870)

        self.central_widget = QtWidgets.QWidget(self.search_template)
        self.central_widget.setObjectName("central_widget")

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 51))
        self.label.setObjectName("label")

        self.template_1 = QtWidgets.QLabel(self.central_widget)
        self.template_1.setGeometry(QtCore.QRect(20, 90, 150, 40))
        self.template_1.setObjectName("template_1")

        self.table_template_1 = QtWidgets.QTableWidget(self.central_widget)
        self.table_template_1.setGeometry(QtCore.QRect(80, 120, 775, 102))
        self.table_template_1.setObjectName("table_template_1")
        self.table_template_1.setRowCount(2)
        self.table_template_1.setColumnCount(7)
        for i in range(2):
            self.table_template_1.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for i in range(7):
            self.table_template_1.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.table_template_1_res = QtWidgets.QTableWidget(self.central_widget)
        self.table_template_1_res.setGeometry(QtCore.QRect(370, 230, 235, 125))
        self.table_template_1_res.setObjectName("table_template_1_res")
        self.table_template_1_res.setRowCount(4)
        self.table_template_1_res.setColumnCount(1)
        self.table_template_1_res.horizontalHeader().hide()
        for i in range(4):
            self.table_template_1_res.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for i in range(1):
            self.table_template_1_res.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        font = QtGui.QFont()
        font.setPointSize(12)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.table_template_1_res.setItem(0, 0, item)

        self.template_2 = QtWidgets.QLabel(self.central_widget)
        self.template_2.setGeometry(QtCore.QRect(20, 334, 150, 40))
        self.template_2.setObjectName("template_2")

        self.table_template_2 = QtWidgets.QTableWidget(self.central_widget)
        self.table_template_2.setGeometry(QtCore.QRect(80, 364, 775, 102))
        self.table_template_2.setObjectName("table_template_2")
        self.table_template_2.setRowCount(2)
        self.table_template_2.setColumnCount(7)
        for i in range(2):
            self.table_template_2.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for i in range(7):
            self.table_template_2.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.table_template_2_res = QtWidgets.QTableWidget(self.central_widget)
        self.table_template_2_res.setGeometry(QtCore.QRect(370, 474, 235, 125))
        self.table_template_2_res.setObjectName("table_template_2_res")
        self.table_template_2_res.setRowCount(4)
        self.table_template_2_res.setColumnCount(1)
        self.table_template_2_res.horizontalHeader().hide()
        for i in range(4):
            self.table_template_2_res.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for i in range(1):
            self.table_template_2_res.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        font = QtGui.QFont()
        font.setPointSize(12)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.table_template_2_res.setItem(0, 0, item)

        self.template_3 = QtWidgets.QLabel(self.central_widget)
        self.template_3.setGeometry(QtCore.QRect(20, 578, 150, 40))
        self.template_3.setObjectName("template_3")

        self.table_template_3 = QtWidgets.QTableWidget(self.central_widget)
        self.table_template_3.setGeometry(QtCore.QRect(80, 608, 775, 102))
        self.table_template_3.setObjectName("table_template_3")
        self.table_template_3.setRowCount(2)
        self.table_template_3.setColumnCount(7)
        for i in range(2):
            self.table_template_3.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for i in range(7):
            self.table_template_3.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.table_template_3_res = QtWidgets.QTableWidget(self.central_widget)
        self.table_template_3_res.setGeometry(QtCore.QRect(370, 718, 235, 125))
        self.table_template_3_res.setObjectName("table_template_3_res")
        self.table_template_3_res.setRowCount(4)
        self.table_template_3_res.setColumnCount(1)
        self.table_template_3_res.horizontalHeader().hide()
        for i in range(4):
            self.table_template_3_res.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for i in range(1):
            self.table_template_3_res.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        font = QtGui.QFont()
        font.setPointSize(12)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.table_template_3_res.setItem(0, 0, item)

        self.show_alignment_button_1 = QtWidgets.QPushButton(self.central_widget)
        self.show_alignment_button_1.setGeometry(QtCore.QRect(80, 230, 180, 23))
        self.show_alignment_button_1.setObjectName("show_alignment_button_1")
        self.show_alignment_button_1.clicked.connect(lambda: self.show_alignment(self.current_df, self.index_temp1))

        self.show_alignment_button_2 = QtWidgets.QPushButton(self.central_widget)
        self.show_alignment_button_2.setGeometry(QtCore.QRect(80, 474, 180, 23))
        self.show_alignment_button_2.setObjectName("show_alignment_button_2")
        self.show_alignment_button_2.clicked.connect(lambda: self.show_alignment(self.current_df, self.index_temp2))

        self.show_alignment_button_3 = QtWidgets.QPushButton(self.central_widget)
        self.show_alignment_button_3.setGeometry(QtCore.QRect(80, 718, 180, 23))
        self.show_alignment_button_3.setObjectName("show_alignment_button_3")
        self.show_alignment_button_3.clicked.connect(lambda: self.show_alignment(self.current_df, self.index_temp3))

        self.home_button = QtWidgets.QPushButton(self.central_widget)
        self.home_button.setGeometry(QtCore.QRect(800, 40, 80, 23))
        self.home_button.setObjectName("home_button")
        self.home_button.clicked.connect(self.back_home)

        self.download_report_button = QtWidgets.QPushButton(self.central_widget)
        self.download_report_button.setGeometry(QtCore.QRect(750, 73, 130, 23))
        self.download_report_button.setObjectName("download_report_button")
        self.download_report_button.clicked.connect(self.download_report)

        self.show_hydrophobicity_plot_button_1 = QtWidgets.QPushButton(self.central_widget)
        self.show_hydrophobicity_plot_button_1.setGeometry(QtCore.QRect(80, 260, 180, 23))
        self.show_hydrophobicity_plot_button_1.setObjectName("show_hydrophobicity_plot_button_1")
        self.show_hydrophobicity_plot_button_1.clicked.connect(lambda: self.show_hydrophobicity_plot(self.template_1.text()))

        self.show_hydrophobicity_plot_button_2 = QtWidgets.QPushButton(self.central_widget)
        self.show_hydrophobicity_plot_button_2.setGeometry(QtCore.QRect(80, 504, 180, 23))
        self.show_hydrophobicity_plot_button_2.setObjectName("show_hydrophobicity_plot_button_2")
        self.show_hydrophobicity_plot_button_2.clicked.connect(lambda: self.show_hydrophobicity_plot(self.template_2.text()))

        self.show_hydrophobicity_plot_button_3 = QtWidgets.QPushButton(self.central_widget)
        self.show_hydrophobicity_plot_button_3.setGeometry(QtCore.QRect(80, 748, 180, 23))
        self.show_hydrophobicity_plot_button_3.setObjectName("show_hydrophobicity_plot_button_3")
        self.show_hydrophobicity_plot_button_3.clicked.connect(lambda: self.show_hydrophobicity_plot(self.template_3.text()))

        self.show_helical_plot_button_1 = QtWidgets.QPushButton(self.central_widget)
        self.show_helical_plot_button_1.setGeometry(QtCore.QRect(80, 290, 180, 23))
        self.show_helical_plot_button_1.setObjectName("show_helical_plot_button_1")
        self.show_helical_plot_button_1.clicked.connect(lambda: self.show_helical_plot(self.template_1.text()))

        self.show_helical_plot_button_2 = QtWidgets.QPushButton(self.central_widget)
        self.show_helical_plot_button_2.setGeometry(QtCore.QRect(80, 534, 180, 23))
        self.show_helical_plot_button_2.setObjectName("show_helical_plot_button_2")
        self.show_helical_plot_button_2.clicked.connect(lambda: self.show_helical_plot(self.template_2.text()))

        self.show_helical_plot_button_3 = QtWidgets.QPushButton(self.central_widget)
        self.show_helical_plot_button_3.setGeometry(QtCore.QRect(80, 778, 180, 23))
        self.show_helical_plot_button_3.setObjectName("show_helical_plot_button_3")
        self.show_helical_plot_button_3.clicked.connect(lambda: self.show_helical_plot(self.template_3.text()))

        self.download_result_summary_button_1 = QtWidgets.QPushButton(self.central_widget)
        self.download_result_summary_button_1.setGeometry(QtCore.QRect(80, 320, 180, 23))
        self.download_result_summary_button_1.setObjectName("download_result_summary_button_1")
        self.download_result_summary_button_1.clicked.connect(lambda: self.download_result_summary(self.index_temp1))

        self.download_result_summary_button_2 = QtWidgets.QPushButton(self.central_widget)
        self.download_result_summary_button_2.setGeometry(QtCore.QRect(80, 564, 180, 23))
        self.download_result_summary_button_2.setObjectName("download_result_summary_button_2")
        self.download_result_summary_button_2.clicked.connect(lambda: self.download_result_summary(self.index_temp2))

        self.download_result_summary_button_3 = QtWidgets.QPushButton(self.central_widget)
        self.download_result_summary_button_3.setGeometry(QtCore.QRect(80, 807, 180, 23))
        self.download_result_summary_button_3.setObjectName("download_result_summary_button_3")
        self.download_result_summary_button_3.clicked.connect(lambda: self.download_result_summary(self.index_temp3))

        self.label_state = QtWidgets.QLabel(self.central_widget)
        self.label_state.setGeometry(QtCore.QRect(80, 50, 70, 23))
        self.label_state.setObjectName("label_state")

        self.combobox_state = QtWidgets.QComboBox(self.central_widget)
        self.combobox_state.setGeometry(QtCore.QRect(80, 73, 100, 23))
        self.combobox_state.setObjectName("combobox_state")
        self.combobox_state.addItem("")
        self.combobox_state.addItem("")
        self.combobox_state.addItem("")
        self.combobox_state.addItem("")
        self.combobox_state.currentIndexChanged.connect(self.state_changed_handler)

        self.label_resolution = QtWidgets.QLabel(self.central_widget)
        self.label_resolution.setGeometry(QtCore.QRect(200, 50, 90, 23))
        self.label_resolution.setObjectName("label_resolution")

        self.combobox_resolution = QtWidgets.QComboBox(self.central_widget)
        self.combobox_resolution.setGeometry(QtCore.QRect(200, 73, 160, 23))
        self.combobox_resolution.setObjectName("combobox_resolution")
        self.combobox_resolution.addItem("")
        self.combobox_resolution.addItem("")
        self.combobox_resolution.currentIndexChanged.connect(self.resolution_changed_handler)

        self.search_template.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(self.search_template)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 909, 20))
        self.menu_bar.setObjectName("menubar")
        self.search_template.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(self.search_template)
        self.status_bar.setObjectName("statusbar")
        self.search_template.setStatusBar(self.status_bar)

        self.translate_ui()
        self.reset_ui()
        QtCore.QMetaObject.connectSlotsByName(self.search_template)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.search_template.setWindowTitle(_translate("SearchTemplate", "MainWindow"))
        self.label.setText(_translate("SearchTemplate", '<html><head/><body><p><span style="font-size:12pt; font-weight:600;">Top 3 templates</span></p></body></html>'))

        item = self.table_template_1.verticalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "SSD"))
        item = self.table_template_1.verticalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "Identity (%)"))
        item = self.table_template_1.horizontalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "TM1"))
        item = self.table_template_1.horizontalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "TM2"))
        item = self.table_template_1.horizontalHeaderItem(2)
        item.setText(_translate("SearchTemplate", "TM3"))
        item = self.table_template_1.horizontalHeaderItem(3)
        item.setText(_translate("SearchTemplate", "TM4"))
        item = self.table_template_1.horizontalHeaderItem(4)
        item.setText(_translate("SearchTemplate", "TM5"))
        item = self.table_template_1.horizontalHeaderItem(5)
        item.setText(_translate("SearchTemplate", "TM6"))
        item = self.table_template_1.horizontalHeaderItem(6)
        item.setText(_translate("SearchTemplate", "TM7"))
        self.template_1.setText(_translate("SearchTemplate", "TextLabel"))
        item = self.table_template_1_res.verticalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "Resolution (Å)"))
        item = self.table_template_1_res.verticalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "Sequence identity (%)"))
        item = self.table_template_1_res.verticalHeaderItem(2)
        item.setText(_translate("SearchTemplate", "Position"))
        item = self.table_template_1_res.verticalHeaderItem(3)
        item.setText(_translate("SearchTemplate", "BRS Score"))
        __sortingEnabled = self.table_template_1_res.isSortingEnabled()
        self.table_template_1_res.setSortingEnabled(False)
        self.table_template_1_res.setSortingEnabled(__sortingEnabled)

        self.template_2.setText(_translate("SearchTemplate", "TextLabel"))
        item = self.table_template_2.verticalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "SSD"))
        item = self.table_template_2.verticalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "Identity (%)"))
        item = self.table_template_2.horizontalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "TM1"))
        item = self.table_template_2.horizontalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "TM2"))
        item = self.table_template_2.horizontalHeaderItem(2)
        item.setText(_translate("SearchTemplate", "TM3"))
        item = self.table_template_2.horizontalHeaderItem(3)
        item.setText(_translate("SearchTemplate", "TM4"))
        item = self.table_template_2.horizontalHeaderItem(4)
        item.setText(_translate("SearchTemplate", "TM5"))
        item = self.table_template_2.horizontalHeaderItem(5)
        item.setText(_translate("SearchTemplate", "TM6"))
        item = self.table_template_2.horizontalHeaderItem(6)
        item.setText(_translate("SearchTemplate", "TM7"))
        item = self.table_template_2_res.verticalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "Resolution (Å)"))
        item = self.table_template_2_res.verticalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "Sequence identity (%)"))
        item = self.table_template_2_res.verticalHeaderItem(2)
        item.setText(_translate("SearchTemplate", "Position"))
        item = self.table_template_2_res.verticalHeaderItem(3)
        item.setText(_translate("SearchTemplate", "BRS Score"))
        __sortingEnabled = self.table_template_2_res.isSortingEnabled()
        self.table_template_2_res.setSortingEnabled(False)
        self.table_template_2_res.setSortingEnabled(__sortingEnabled)

        self.template_3.setText(_translate("SearchTemplate", "TextLabel"))
        item = self.table_template_3.verticalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "SSD"))
        item = self.table_template_3.verticalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "Identity (%)"))
        item = self.table_template_3.horizontalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "TM1"))
        item = self.table_template_3.horizontalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "TM2"))
        item = self.table_template_3.horizontalHeaderItem(2)
        item.setText(_translate("SearchTemplate", "TM3"))
        item = self.table_template_3.horizontalHeaderItem(3)
        item.setText(_translate("SearchTemplate", "TM4"))
        item = self.table_template_3.horizontalHeaderItem(4)
        item.setText(_translate("SearchTemplate", "TM5"))
        item = self.table_template_3.horizontalHeaderItem(5)
        item.setText(_translate("SearchTemplate", "TM6"))
        item = self.table_template_3.horizontalHeaderItem(6)
        item.setText(_translate("SearchTemplate", "TM7"))
        item = self.table_template_3_res.verticalHeaderItem(0)
        item.setText(_translate("SearchTemplate", "Resolution (Å)"))
        item = self.table_template_3_res.verticalHeaderItem(1)
        item.setText(_translate("SearchTemplate", "Sequence identity (%)"))
        item = self.table_template_3_res.verticalHeaderItem(2)
        item.setText(_translate("SearchTemplate", "Position"))
        item = self.table_template_3_res.verticalHeaderItem(3)
        item.setText(_translate("SearchTemplate", "BRS Score"))
        __sortingEnabled = self.table_template_3_res.isSortingEnabled()
        self.table_template_3_res.setSortingEnabled(False)
        self.table_template_3_res.setSortingEnabled(__sortingEnabled)

        self.home_button.setText(_translate("SearchTemplate", "Home"))
        self.download_report_button.setText(_translate("SearchTemplate", "Download Report"))

        self.show_alignment_button_1.setToolTip(_translate("SearchTemplate", "Show TM wise alignment between target sequence and selected template"))
        self.show_alignment_button_1.setText(_translate("SearchTemplate", "Alignment"))
        self.show_alignment_button_2.setToolTip(_translate("SearchTemplate", "Show TM wise alignment between target sequence and selected template"))
        self.show_alignment_button_2.setText(_translate("SearchTemplate", "Alignment"))
        self.show_alignment_button_3.setToolTip(_translate("SearchTemplate", "Show TM wise alignment between target sequence and selected template"))
        self.show_alignment_button_3.setText(_translate("SearchTemplate", "Alignment"))

        self.show_hydrophobicity_plot_button_1.setToolTip(_translate("SearchTemplate", "Show hydrophobicity plot"))
        self.show_hydrophobicity_plot_button_1.setText(_translate("SearchTemplate", "Hydrophobicity plot"))
        self.show_hydrophobicity_plot_button_2.setToolTip(_translate("SearchTemplate", "Show hydrophobicity plot"))
        self.show_hydrophobicity_plot_button_2.setText(_translate("SearchTemplate", "Hydrophobicity plot"))
        self.show_hydrophobicity_plot_button_3.setToolTip(_translate("SearchTemplate", "Show hydrophobicity plot"))
        self.show_hydrophobicity_plot_button_3.setText(_translate("SearchTemplate", "Hydrophobicity plot"))

        self.show_helical_plot_button_1.setToolTip(_translate("SearchTemplate", "Show helical plot"))
        self.show_helical_plot_button_1.setText(_translate("SearchTemplate", "Helical plot"))
        self.show_helical_plot_button_2.setToolTip(_translate("SearchTemplate", "Show helical plot"))
        self.show_helical_plot_button_2.setText(_translate("SearchTemplate", "Helical plot"))
        self.show_helical_plot_button_3.setToolTip(_translate("SearchTemplate", "Show helical plot"))
        self.show_helical_plot_button_3.setText(_translate("SearchTemplate", "Helical plot"))

        self.download_result_summary_button_1.setToolTip(_translate("SearchTemplate", "Download result summary"))
        self.download_result_summary_button_1.setText(_translate("SearchTemplate", "Result summary"))
        self.download_result_summary_button_2.setToolTip(_translate("SearchTemplate", "Download result summary"))
        self.download_result_summary_button_2.setText(_translate("SearchTemplate", "Result summary"))
        self.download_result_summary_button_3.setToolTip(_translate("SearchTemplate", "Download result summary"))
        self.download_result_summary_button_3.setText(_translate("SearchTemplate", "Result summary"))

        self.label_state.setText(_translate("SearchTemplate", "Select state"))
        self.combobox_state.setItemText(0, _translate("SearchTemplate", "None"))
        self.combobox_state.setItemText(1, _translate("SearchTemplate", "Active"))
        self.combobox_state.setItemText(2, _translate("SearchTemplate", "Inactive"))
        self.combobox_state.setItemText(3, _translate("SearchTemplate", "Intermediate"))

        self.label_resolution.setText(_translate("SearchTemplate", "Select resolution"))
        self.combobox_resolution.setItemText(0, _translate("SearchTemplate", "All"))
        self.combobox_resolution.setItemText(1, _translate("SearchTemplate", "Less than or equal to 2.5 Å"))

    def back_home(self):
        from Home import Ui_HomeWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeWindow(self.window)
        self.ui.setup_ui()
        self.search_template.hide()
        self.window.setWindowTitle('Bio-GATS')
        self.window.show()

    def state_changed_handler(self):
        self.reset_ui()
        self.scoring_scheme()

    def scoring_scheme(self):
        df4 = Helper.df_target.apply(lambda row: row.astype(str).str.contains(self.targ_id).any(), axis=1)  # searching entered sequence in target database
        df5, = df4[df4 == True].index  # getting row number of target sequence
        targ_seq = Helper.df_target.loc[df5, "Sequence"]  # getting target sequence

        current_identity = []
        current_resolution = []

        if self.combobox_state.currentIndex() == 0:
            self.reset_ui()
            return
        elif self.combobox_state.currentIndex() == 1:
            self.current_df = Helper.df_active
        elif self.combobox_state.currentIndex() == 2:
            self.current_df = Helper.df_inactive
        elif self.combobox_state.currentIndex() == 3:
            self.current_df = Helper.df_intermediate

        # select resolution with values less than or equal to 2.5
        resolution_index = self.combobox_resolution.currentIndex()
        if resolution_index == 1:
            self.current_df = self.current_df[self.current_df['Resolution'] <= 2.5]

        # get number of rows in excel sheet (depending on selected value in dropdown i.e. active, inactive, or intermediate)
        number_of_rows_in_sheet = len(self.current_df.axes[0])
        tm1 = [None] * number_of_rows_in_sheet
        tm2 = [None] * number_of_rows_in_sheet
        tm3 = [None] * number_of_rows_in_sheet
        tm4 = [None] * number_of_rows_in_sheet
        tm5 = [None] * number_of_rows_in_sheet
        tm6 = [None] * number_of_rows_in_sheet
        tm7 = [None] * number_of_rows_in_sheet

        self.identities = [None] * number_of_rows_in_sheet
        tm_score_aggregate = [None] * number_of_rows_in_sheet

        similarity_scores = []

        for j in range(number_of_rows_in_sheet):
            current_pdbid = self.current_df['PDBID'][j]
            self.split_helix(self.current_df, current_pdbid, type='template', numbers=True)
            _, self.identities[j] = self.align(self.current_df, current_pdbid, self.targ_id)
            ssd_tm = self.ssd(self.current_df, current_pdbid, self.targ_id)

            tm1[j], tm2[j], tm3[j], tm4[j], tm5[j], tm6[j], tm7[j] = ssd_tm
            iden = Helper.identity_for_whole_sequence(self.current_df['Sequence'][j], targ_seq)

            current_identity.append(iden)
            current_resolution.append(self.current_df['Resolution'][j])

            # similarity score
            sum_value = 0
            for hotspot_residue_position in self.hotspot_residue_positions:
                sum_value += Helper.calculate_hotspot_residue_similarity(targ_seq, self.current_df['Sequence'][j], hotspot_residue_position)
            similarity_scores.append(sum_value)

        # calculate SSD score
        self.temp_df = pd.DataFrame()
        self.temp_df['PDBID'] = self.current_df['PDBID']
        self.temp_df['Receptor'] = self.current_df['Receptor']
        self.temp_df['Sequence'] = self.current_df['Sequence']

        for i in range(1, 8):
            self.temp_df[f'TM{i} start'] = self.current_df[f'TM{i} start']
            self.temp_df[f'TM{i} end'] = self.current_df[f'TM{i} end']
            self.temp_df[f'BW{i}.50'] = self.current_df[f'BW{i}.50']

        self.temp_df['TM1_score'] = self.calculate_score(number_of_rows_in_sheet, tm1, 1)
        self.temp_df['TM2_score'] = self.calculate_score(number_of_rows_in_sheet, tm2, 2)
        self.temp_df['TM3_score'] = self.calculate_score(number_of_rows_in_sheet, tm3, 2)
        self.temp_df['TM4_score'] = self.calculate_score(number_of_rows_in_sheet, tm4, 2)
        self.temp_df['TM5_score'] = self.calculate_score(number_of_rows_in_sheet, tm5, 2)
        self.temp_df['TM6_score'] = self.calculate_score(number_of_rows_in_sheet, tm6, 2)
        self.temp_df['TM7_score'] = self.calculate_score(number_of_rows_in_sheet, tm7, 2)

        # calculate normalized value of all TM#_score
        tm_columns = ['TM1_score', 'TM2_score', 'TM3_score', 'TM4_score', 'TM5_score', 'TM6_score', 'TM7_score']
        self.temp_df['tm_score_aggregate'] = self.temp_df[tm_columns].sum(axis=1)
        self.temp_df['tm_score_normalized'] = (self.temp_df['tm_score_aggregate'] - self.temp_df['tm_score_aggregate'].min()) / (self.temp_df['tm_score_aggregate'].max() - self.temp_df['tm_score_aggregate'].min())

        # calculate identity score
        # self.temp_df['identity_score'] = self.calculate_score(number_of_rows_in_sheet, current_identity, reverse=True)

        # calculate resolution score
        self.temp_df['resolution'] = current_resolution
        self.temp_df['resolution_score'] = self.calculate_resolution_score(number_of_rows_in_sheet, current_resolution)

        # calculate similarity score
        self.temp_df['similarity_score'] = similarity_scores
        similarity_scores_df = pd.DataFrame(similarity_scores)
        self.temp_df['similarity_score_normalized'] = (similarity_scores_df - similarity_scores_df.min()) / (similarity_scores_df.max() - similarity_scores_df.min())

        # calculate normalized score (normalized_score score = tm_score_normalized + similarity_score_normalized + resolution_score)
        columns_to_aggregate = ['tm_score_normalized', 'similarity_score_normalized', 'resolution_score']
        self.temp_df['normalized_score'] = self.temp_df[columns_to_aggregate].sum(axis=1)

        # arrange aggregate scores in descending order
        aggregate_score_sorted_indexes = sorted(range(len(self.temp_df['normalized_score'])), key=lambda k: self.temp_df['normalized_score'][k], reverse=True)

        # TODO: comment in production
        # print(self.temp_df)
        # print(aggregate_score_sorted_indexes)  # use first three index values ONLY

        # Printing resolution, position and identity of top 3 templates
        if len(aggregate_score_sorted_indexes) > 0:
            self.index_temp1 = aggregate_score_sorted_indexes[0]  # getting the index of best template

            for i in range(7):
                self.table_template_1.setItem(1, i, QtWidgets.QTableWidgetItem(str(self.identities[self.index_temp1][i])))

            res1 = self.current_df['Resolution'].iloc[self.index_temp1]  # getting resolution of the best template
            self.table_template_1_res.setDisabled(False)
            self.table_template_1_res.setItem(0, 0, QtWidgets.QTableWidgetItem(str(res1)))

            ident1 = current_identity[self.index_temp1]  # getting identity of the best template
            self.table_template_1_res.setItem(1, 0, QtWidgets.QTableWidgetItem(str(ident1)))

            pos1 = self.current_df['Position'].iloc[self.index_temp1]  # getting position of the best template
            self.table_template_1_res.setItem(2, 0, QtWidgets.QTableWidgetItem(str(pos1)))

            sim1 = self.temp_df['similarity_score'].iloc[self.index_temp1]  # getting similarity score of the best template
            self.table_template_1_res.setItem(3, 0, QtWidgets.QTableWidgetItem(str(sim1)))

            temp1_id = self.current_df['PDBID'].iloc[self.index_temp1]  # getting pdbid of the top template
            temp1_name = self.current_df['Receptor'].iloc[self.index_temp1]
            self.template_1.setText(temp1_name + " " + "(PDBID" + ":" + temp1_id + ")")  # displaying PDBID

        if len(aggregate_score_sorted_indexes) > 1:
            self.index_temp2 = aggregate_score_sorted_indexes[1]  # getting the index of 2nd best template

            for i in range(7):
                self.table_template_2.setItem(1, i, QtWidgets.QTableWidgetItem(str(self.identities[self.index_temp2][i])))

            res2 = self.current_df['Resolution'].iloc[self.index_temp2]  # getting resolution of the 2nd best template
            self.table_template_2_res.setDisabled(False)
            self.table_template_2_res.setItem(0, 0, QtWidgets.QTableWidgetItem(str(res2)))

            ident2 = current_identity[self.index_temp2]  # getting identity of the 2nd best template
            self.table_template_2_res.setItem(1, 0, QtWidgets.QTableWidgetItem(str(ident2)))

            pos2 = self.current_df['Position'].iloc[self.index_temp2]  # getting position of the 2nd best template
            self.table_template_2_res.setItem(2, 0, QtWidgets.QTableWidgetItem(str(pos2)))

            sim2 = self.temp_df['similarity_score'].iloc[self.index_temp2]  # getting similarity score of the best template
            self.table_template_2_res.setItem(3, 0, QtWidgets.QTableWidgetItem(str(sim2)))

            temp2_id = self.current_df['PDBID'].iloc[self.index_temp2]  # getting pdbid of the top template
            temp2_name = self.current_df['Receptor'].iloc[self.index_temp2]
            self.template_2.setText(temp2_name + " " + "(PDBID" + ":" + temp2_id + ")")  # displaying PDBID

        if len(aggregate_score_sorted_indexes) > 2:
            self.index_temp3 = aggregate_score_sorted_indexes[2]  # getting the index of best template

            for i in range(7):
                self.table_template_3.setItem(1, i, QtWidgets.QTableWidgetItem(str(self.identities[self.index_temp3][i])))

            res3 = self.current_df['Resolution'].iloc[self.index_temp3]  # getting resolution of the best template
            self.table_template_3_res.setDisabled(False)
            self.table_template_3_res.setItem(0, 0, QtWidgets.QTableWidgetItem(str(res3)))

            ident3 = current_identity[self.index_temp3]  # getting identity of the best template
            self.table_template_3_res.setItem(1, 0, QtWidgets.QTableWidgetItem(str(ident3)))

            pos3 = self.current_df['Position'].iloc[self.index_temp3]  # getting position of the 3rd best template
            self.table_template_3_res.setItem(2, 0, QtWidgets.QTableWidgetItem(str(pos3)))

            sim3 = self.temp_df['similarity_score'].iloc[self.index_temp3]  # getting similarity score of the best template
            self.table_template_3_res.setItem(3, 0, QtWidgets.QTableWidgetItem(str(sim3)))

            temp3_id = self.current_df['PDBID'].iloc[self.index_temp3]  # getting pdbid of the top template
            temp3_name = self.current_df['Receptor'].iloc[self.index_temp3]
            self.template_3.setText(temp3_name + " " + "(PDBID" + ":" + temp3_id + ")")  # displaying PDBID

        for idx, current_index in enumerate(aggregate_score_sorted_indexes[:3]):
            if idx == 0:  # first best template
                self.table_template_1.setItem(0, 0, QtWidgets.QTableWidgetItem(str(tm1[current_index])))
                self.table_template_1.setItem(0, 1, QtWidgets.QTableWidgetItem(str(tm2[current_index])))
                self.table_template_1.setItem(0, 2, QtWidgets.QTableWidgetItem(str(tm3[current_index])))
                self.table_template_1.setItem(0, 3, QtWidgets.QTableWidgetItem(str(tm4[current_index])))
                self.table_template_1.setItem(0, 4, QtWidgets.QTableWidgetItem(str(tm5[current_index])))
                self.table_template_1.setItem(0, 5, QtWidgets.QTableWidgetItem(str(tm6[current_index])))
                self.table_template_1.setItem(0, 6, QtWidgets.QTableWidgetItem(str(tm7[current_index])))
                self.table_template_1.setDisabled(False)
                self.show_alignment_button_1.setDisabled(False)
                self.show_hydrophobicity_plot_button_1.setDisabled(False)
                self.show_helical_plot_button_1.setDisabled(False)
            elif idx == 1:  # second best template
                self.table_template_2.setItem(0, 0, QtWidgets.QTableWidgetItem(str(tm1[current_index])))
                self.table_template_2.setItem(0, 1, QtWidgets.QTableWidgetItem(str(tm2[current_index])))
                self.table_template_2.setItem(0, 2, QtWidgets.QTableWidgetItem(str(tm3[current_index])))
                self.table_template_2.setItem(0, 3, QtWidgets.QTableWidgetItem(str(tm4[current_index])))
                self.table_template_2.setItem(0, 4, QtWidgets.QTableWidgetItem(str(tm5[current_index])))
                self.table_template_2.setItem(0, 5, QtWidgets.QTableWidgetItem(str(tm6[current_index])))
                self.table_template_2.setItem(0, 6, QtWidgets.QTableWidgetItem(str(tm7[current_index])))
                self.table_template_2.setDisabled(False)
                self.show_alignment_button_2.setDisabled(False)
                self.show_hydrophobicity_plot_button_2.setDisabled(False)
                self.show_helical_plot_button_2.setDisabled(False)
            elif idx == 2:  # third best template:
                self.table_template_3.setItem(0, 0, QtWidgets.QTableWidgetItem(str(tm1[current_index])))
                self.table_template_3.setItem(0, 1, QtWidgets.QTableWidgetItem(str(tm2[current_index])))
                self.table_template_3.setItem(0, 2, QtWidgets.QTableWidgetItem(str(tm3[current_index])))
                self.table_template_3.setItem(0, 3, QtWidgets.QTableWidgetItem(str(tm4[current_index])))
                self.table_template_3.setItem(0, 4, QtWidgets.QTableWidgetItem(str(tm5[current_index])))
                self.table_template_3.setItem(0, 5, QtWidgets.QTableWidgetItem(str(tm6[current_index])))
                self.table_template_3.setItem(0, 6, QtWidgets.QTableWidgetItem(str(tm7[current_index])))
                self.table_template_3.setDisabled(False)
                self.show_alignment_button_3.setDisabled(False)
                self.show_hydrophobicity_plot_button_3.setDisabled(False)
                self.show_helical_plot_button_3.setDisabled(False)

        self.download_report_button.setDisabled(False)
        self.combobox_resolution.setDisabled(False)

        self.download_result_summary_button_1.setDisabled(False)
        self.download_result_summary_button_2.setDisabled(False)
        self.download_result_summary_button_3.setDisabled(False)

    def split_helix(self, current_df, id, type, numbers):
        ref = ''
        df = pd.DataFrame()
        if type == 'template':
            ref = 'PDBID'
            df = current_df
        elif type == 'target':
            ref = 'Uniprot_ID'
            df = Helper.df_target

        prot = [[None for x in range(7)], [None for y in range(7)]]
        numb = [[None for x in range(7)], [None for y in range(7)]]
        seq = df.loc[df[ref] == id, 'Sequence'].iloc[0]

        for i in range(1, 8):
            beg = int(df.loc[df[ref] == id, 'TM' + str(i) + ' start'].iloc[0])
            end = int(df.loc[df[ref] == id, 'TM' + str(i) + ' end'].iloc[0])
            numb[0][i - 1] = [beg, end]
            prot[0][i - 1] = seq[(int(beg) - 1):int(end)]
            bw = (df.loc[df[ref] == id, 'BW' + str(i) + '.50'].iloc[0])
            numb[1][i - 1] = int(bw[1:])
            prot[1][i - 1] = int(bw[1:]) - int(beg)

        return (numb) if numbers else (prot)

    def align(self, df, template_id, target_id):
        self.template = self.split_helix(df, template_id, type='template', numbers=False)
        self.target = self.split_helix(Helper.df_target, target_id, type='target', numbers=False)

        identities = []
        for i in range(7):
            ident = Helper.identity_for_sequence_chunks(self.template[0][i], self.target[0][i])
            identities.append(ident)

        align = [[None for x in range(7)], [None for y in range(7)]]

        for i in range(7):
            if self.template[1][i] > self.target[1][i]:
                align[0][i] = self.template[0][i]
                align[1][i] = ''.join(['-'] * (self.template[1][i] - self.target[1][i])) + self.target[0][i]
            elif self.template[1][i] < self.target[1][i]:
                align[0][i] = ''.join(['-'] * (self.target[1][i] - self.template[1][i])) + self.template[0][i]
                align[1][i] = self.target[0][i]
            else:
                align[0][i] = self.template[0][i]
                align[1][i] = self.target[0][i]

            if len(align[0][i]) > len(align[1][i]):
                align[1][i] = align[1][i] + ''.join(['-'] * (len(align[0][i]) - len(align[1][i])))
            elif len(align[1][i]) > len(align[0][i]):
                align[0][i] = align[0][i] + ''.join(['-'] * (len(align[1][i]) - len(align[0][i])))

        return align, identities

    def ssd(self, current_df, template_id, target_id):
        template_sequence = current_df.loc[current_df['PDBID'] == template_id, 'Sequence'].iloc[0]
        template_receptor = current_df.loc[current_df['PDBID'] == template_id, 'Receptor'].iloc[0]
        target_sequence = Helper.df_target.loc[Helper.df_target['Uniprot_ID'] == target_id, 'Sequence'].iloc[0]
        target_receptor = Helper.df_target.loc[Helper.df_target['Uniprot_ID'] == target_id, 'Receptor'].iloc[0]

        window_size = 11
        hyd = [None, None]
        hyd[0] = [Helper.hydscale[res] for res in template_sequence]
        hyd[1] = [Helper.hydscale[res] for res in target_sequence]
        lens = [len(template_sequence), len(target_sequence)]
        hydr = [[1] * int(window_size / 2) for i in range(2)]
        for k in range(2):
            for i in range(int(window_size / 2), lens[k] - int(window_size / 2)):
                sumb = 0
                for j in range(-int(window_size / 2), int(window_size / 2) + 1):
                    sumb += hyd[k][i + j]
                avg = sumb / window_size
                hydr[k].append(avg)
        for i in range(2):
            hydr[i] += [1] * int(window_size / 2)
        temp_list = list(template_sequence)
        targ_list = list(target_sequence)
        length = len(temp_list)
        targ_align = ['-'] * length
        temp_align = temp_list
        temp_vals = self.split_helix(current_df, template_id, type='template', numbers=True)
        targ_vals = self.split_helix(Helper.df_target, target_id, type='target', numbers=True)
        temp_helix = temp_vals[0]
        targ_helix = targ_vals[0]
        temp_bw = temp_vals[1]
        targ_bw = targ_vals[1]
        name = template_id + ',' + target_id
        hydiff = []
        self.hydrh = [[[] for x in range(2)] for y in range(7)]
        self.ress = [[] for y in range(7)]
        per_res_ssd = []
        for i in range(7):
            self.summ = [0] * 7
            for j in range(int(targ_helix[i][0]) - 1, int(targ_helix[i][1])):
                targ_align[j + temp_bw[i] - targ_bw[i]] = targ_list[j]
            for j in range(int(temp_helix[i][0]) - 1, int(temp_helix[i][1])):
                self.hydrh[i][0].append(hydr[0][j])
                self.hydrh[i][1].append(hydr[1][targ_bw[i] - temp_bw[i] + j])
                self.summ[i] += ((hydr[1][targ_bw[i] - temp_bw[i] + j]) - (hydr[0][j])) ** 2
            resno = (temp_bw[i] - targ_bw[i] + targ_helix[i][0]) - temp_helix[i][0]
            self.ress[i] = [x for x in range(int(temp_helix[i][0]), int(temp_helix[i][1] + 1))]
            self.value[i] = self.summ[i] / (temp_helix[i][1] - temp_helix[i][0] + 1)
            hydiff.append(round(self.summ[i], 3))
            per_res_ssd.append(round(self.value[i], 3))

            temp_pdbid = current_df.loc[current_df['PDBID'] == template_id, 'PDBID'].iloc[0]
            self.plot_data[temp_pdbid] = {
                'current_df': current_df,
                'name': name,
                'ress': self.ress,
                'hydrh': self.hydrh,
                'summ': self.summ,
                'value': self.value,
                'template_receptor': template_receptor,
                'target_receptor': target_receptor,
            }

        return per_res_ssd

    def show_alignment(self, current_df, index):
        df4 = Helper.df_target.apply(lambda row: row.astype(str).str.contains(self.targ_id).any(), axis=1)  # searching entered sequence in target database
        df5, = df4[df4 == True].index  # getting row number of target sequence
        seq_id = Helper.df_target.loc[df5, "Uniprot_ID"]
        target_receptor = Helper.df_target.loc[df5, 'Receptor']
        target_sequence = Helper.df_target.loc[df5, 'Sequence']

        pdb_id = current_df['PDBID'].iloc[index]  # getting pdbid of template name
        template_receptor = current_df['Receptor'].iloc[index]
        template_sequence = current_df['Sequence'].iloc[index]

        target_number = []  # list of tuples like ('TM1 start', 'TM1 end'), ('TM2 start', 'TM2 end'), ...
        template_number = []  # list of tuples like ('TM1 start', 'TM1 end'), ('TM2 start', 'TM2 end'), ...

        for i in range(1, 8):
            target_number.append((Helper.df_target.loc[df5, f'TM{i} start'], Helper.df_target.loc[df5, f'TM{i} end']))
            template_number.append((current_df[f'TM{i} start'].iloc[index], current_df[f'TM{i} end'].iloc[index]))

        alignment, _ = self.align(current_df, pdb_id, seq_id)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Alignment(self.window, alignment, template_receptor, target_receptor, template_sequence, target_sequence, template_number, target_number)
        self.ui.setup_ui()
        self.window.setWindowTitle('Alignment - Bio-GATS')
        self.window.show()

    def identity(self, template_seq, target_seq):
        matrix = matlist.blosum62
        for a in pairwise2.align.globaldx(template_seq, target_seq, matrix):
            align_temp = a[0]
            align_targ = a[1]
            seq_len = len(align_temp)
            matches = [align_temp[i] == align_targ[i] for i in range(seq_len)]
            iden = (100 * sum(matches)) / seq_len
            return round(iden, 2)
        return None

    def calculate_score(self, number_of_rows_in_sheet, current_list, add_value=1, reverse=False):
        score = [0] * number_of_rows_in_sheet

        for index, value in enumerate(current_list):
            if value > 2.5:
                score[index] = 0
            else:
                score[index] = 1

            if 0 <= value < 0.1:
                score[index] = 2
            elif value >= 0.1:
                score[index] = -1

        return score

    def calculate_resolution_score(self, number_of_rows_in_sheet, current_list):
        score = [0] * number_of_rows_in_sheet

        for index, value in enumerate(current_list):
            if value > 2.5:
                score[index] = 0
            else:
                score[index] = 1

        return score

    def show_hydrophobicity_plot(self, template_text):
        pdbid = template_text.rstrip(')').split(':')[1]
        current_plot_data = self.plot_data[pdbid]

        Helper.show_hydrophobicity_plot(current_plot_data['ress'], current_plot_data['hydrh'], current_plot_data['summ'], current_plot_data['value'], current_plot_data['template_receptor'], current_plot_data['target_receptor'], current_plot_data['name'], download=False)

    def show_helical_plot(self, template_text):
        pdbid = template_text.rstrip(')').split(':')[1]
        current_plot_data = self.plot_data[pdbid]
        current_df = self.plot_data[pdbid]['current_df']

        template_receptor = current_plot_data['template_receptor']
        target_receptor = current_plot_data['target_receptor']

        template = self.split_helix(current_df, pdbid, type='template', numbers=False)
        target = self.split_helix(Helper.df_target, self.targ_id, type='target', numbers=False)

        Helper.show_helical_plot(template, target, template_receptor, target_receptor, current_plot_data['name'], download=False)

    def download_report(self):
        combo_selected_text = self.combobox_state.currentText().lower()
        filename = 'report_{}.csv'.format(combo_selected_text)
        try:
            self.temp_df.to_csv(filename, header=True, index=False)
        except PermissionError:
            msg = QtWidgets.QMessageBox()
            QtWidgets.QMessageBox.about(msg, 'Error', 'File already in use. Close file and try again.')

        msg = QtWidgets.QMessageBox()
        QtWidgets.QMessageBox.about(msg, 'Information', 'Report file ({}) downloaded to project folder'.format(filename))

    def resolution_changed_handler(self):
        self.reset_ui()
        self.scoring_scheme()

    def reset_ui(self):
        self.plot_data = {}
        self.current_df = ''

        self.download_report_button.setDisabled(True)

        if self.combobox_state.currentIndex() == 0:
            self.combobox_resolution.setCurrentIndex(0)

        self.combobox_resolution.setDisabled(True)

        self.show_alignment_button_1.setDisabled(True)
        self.show_alignment_button_2.setDisabled(True)
        self.show_alignment_button_3.setDisabled(True)

        self.show_hydrophobicity_plot_button_1.setDisabled(True)
        self.show_hydrophobicity_plot_button_2.setDisabled(True)
        self.show_hydrophobicity_plot_button_3.setDisabled(True)

        self.show_helical_plot_button_1.setDisabled(True)
        self.show_helical_plot_button_2.setDisabled(True)
        self.show_helical_plot_button_3.setDisabled(True)

        self.download_result_summary_button_1.setDisabled(True)
        self.download_result_summary_button_2.setDisabled(True)
        self.download_result_summary_button_3.setDisabled(True)

        self.template_1.setText('')
        self.template_2.setText('')
        self.template_3.setText('')

        self.table_template_1.setDisabled(True)
        self.table_template_2.setDisabled(True)
        self.table_template_3.setDisabled(True)

        for i in range(7):
            self.table_template_1.setItem(0, i, QtWidgets.QTableWidgetItem(''))
            self.table_template_2.setItem(0, i, QtWidgets.QTableWidgetItem(''))
            self.table_template_3.setItem(0, i, QtWidgets.QTableWidgetItem(''))

        self.table_template_1_res.setDisabled(True)
        self.table_template_2_res.setDisabled(True)
        self.table_template_3_res.setDisabled(True)

        for i in range(3):
            self.table_template_1_res.setItem(i, 0, QtWidgets.QTableWidgetItem(''))
            self.table_template_2_res.setItem(i, 0, QtWidgets.QTableWidgetItem(''))
            self.table_template_3_res.setItem(i, 0, QtWidgets.QTableWidgetItem(''))

    def download_result_summary(self, current_index):
        current_item_text = self.temp_df['PDBID'].iloc[current_index]  # getting PDBID of the top 3 templates
        target_id, target_receptor, target_sequence, target_number, template_id, template_receptor, template_sequence, template_number = Helper.calculate_alignment(self.targ_id, current_item_text)

        name = template_id + ',' + target_id
        alignment, _ = self.align(self.temp_df, template_id, target_id)

        hydrophobicity_plot_filenames = Helper.show_hydrophobicity_plot(self.ress, self.hydrh, self.summ, self.value, template_receptor, target_receptor, name, download=True)
        helical_plot_filenames = Helper.show_helical_plot(self.template, self.target, template_receptor, target_receptor, name, download=True)
        Helper.generate_result_summary(alignment, template_receptor, target_receptor, template_sequence, target_sequence, template_number, target_number, hydrophobicity_plot_filenames, helical_plot_filenames)
