# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrowseTemplates.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets

from Alignment import Ui_Alignment
from aPdb import Ui_aPdb
from helper import Helper


class Ui_BrowseTemplates(object):
    def __init__(self, BrowseTemplates, seq_id):
        self.browse_templates = BrowseTemplates
        self.targ_id = seq_id
        self.hotspot_residue_positions = Helper.non_olfactory_hotspot_residue_positions
        self.receptors = Helper.df_template[Helper.df_template['Receptor'].str.contains('_')]['Receptor'].values.tolist()
        self.receptors_size = len(self.receptors)

        self.template_list_size = 0
        self.template = []
        self.target = []
        self.report_data = []
        self.template_id = ''
        self.target_id = ''
        self.template_receptor = ''
        self.target_receptor = ''
        self.template_sequence = ''
        self.target_sequence = ''
        self.target_number = []  # list of tuples like ('TM1 start', 'TM1 end'), ('TM2 start', 'TM2 end'), ...
        self.template_number = []  # list of tuples like ('TM1 start', 'TM1 end'), ('TM2 start', 'TM2 end'), ...
        self.alignment = []

        self.ress = []
        self.hydrh = []
        self.summ = [0] * 7
        self.value = [0] * 7
        self.name = ''

    def setup_ui(self):
        self.browse_templates.setObjectName("browse_templates")
        self.browse_templates.resize(844, 499)
        self.central_widget = QtWidgets.QWidget(self.browse_templates)
        self.central_widget.setObjectName("central_widget")

        font = QtGui.QFont()

        font.setPointSize(14)
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 251, 41))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.home_button = QtWidgets.QPushButton(self.central_widget)
        self.home_button.setGeometry(QtCore.QRect(750, 10, 80, 23))
        self.home_button.setObjectName("home_button")
        self.home_button.clicked.connect(self.back_home)

        self.show_alignment_button = QtWidgets.QPushButton(self.central_widget)
        self.show_alignment_button.setGeometry(QtCore.QRect(650, 90, 180, 31))
        self.show_alignment_button.setObjectName("show_alignment_button")
        self.show_alignment_button.clicked.connect(self.show_alignment_click_handler)
        self.show_alignment_button.setDisabled(True)

        self.show_hydrophobicity_plot_button = QtWidgets.QPushButton(self.central_widget)
        self.show_hydrophobicity_plot_button.setGeometry(QtCore.QRect(650, 130, 180, 31))
        self.show_hydrophobicity_plot_button.setObjectName("show_hydrophobicity_plot_button")
        self.show_hydrophobicity_plot_button.clicked.connect(self.show_hydrophobicity_plot)
        self.show_hydrophobicity_plot_button.setDisabled(True)

        self.show_helical_plot_button = QtWidgets.QPushButton(self.central_widget)
        self.show_helical_plot_button.setGeometry(QtCore.QRect(650, 170, 180, 31))
        self.show_helical_plot_button.setObjectName("download_helical_plot_button")
        self.show_helical_plot_button.clicked.connect(self.show_helical_plot)
        self.show_helical_plot_button.setDisabled(True)

        self.download_result_summary_button = QtWidgets.QPushButton(self.central_widget)
        self.download_result_summary_button.setGeometry(QtCore.QRect(650, 210, 180, 31))
        self.download_result_summary_button.setObjectName("download_result_summary_button")
        self.download_result_summary_button.clicked.connect(self.download_result_summary)
        self.download_result_summary_button.setDisabled(True)

        self.available_pdb_files_button = QtWidgets.QPushButton(self.central_widget)
        self.available_pdb_files_button.setGeometry(QtCore.QRect(310, 430, 241, 31))
        self.available_pdb_files_button.setObjectName("available_pdb_files_button")
        self.available_pdb_files_button.clicked.connect(self.available_pdb_files)
        self.available_pdb_files_button.setDisabled(True)

        self.template_list = QtWidgets.QListWidget(self.central_widget)
        self.template_list.setGeometry(QtCore.QRect(15, 91, 251, 341))
        self.template_list.setObjectName("template_list")

        for i in range(self.receptors_size):
            item = QtWidgets.QListWidgetItem("Item %i" % i)
            self.template_list.addItem(item)
        self.template_list.clicked.connect(self.template_list_clicked_handler)

        self.browse_templates.setCentralWidget(self.central_widget)

        self.ssd_table = QtWidgets.QTableWidget(self.central_widget)
        self.ssd_table.setGeometry(QtCore.QRect(310, 171, 244, 242))
        self.ssd_table.setObjectName("ssd_table")
        self.ssd_table.setRowCount(7)
        self.ssd_table.setColumnCount(2)
        self.ssd_table.setDisabled(True)
        for i in range(7):
            self.ssd_table.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for i in range(2):
            self.ssd_table.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.similarity_score_text_label = QtWidgets.QLabel(self.central_widget)
        self.similarity_score_text_label.setGeometry(QtCore.QRect(310, 90, 150, 25))
        self.similarity_score_text_label.setObjectName("similarity_score_text_label")

        self.similarity_score_field = QtWidgets.QTextEdit(self.central_widget)
        self.similarity_score_field.setGeometry(QtCore.QRect(470, 90, 60, 25))
        self.similarity_score_field.setObjectName("similarity_score_field")
        self.similarity_score_field.setDisabled(True)

        self.sequence_identity_text_label = QtWidgets.QLabel(self.central_widget)
        self.sequence_identity_text_label.setGeometry(QtCore.QRect(310, 130, 150, 25))
        self.sequence_identity_text_label.setObjectName("sequence_identity_text_label")

        self.sequence_identity_field = QtWidgets.QTextEdit(self.central_widget)
        self.sequence_identity_field.setGeometry(QtCore.QRect(470, 130, 60, 25))
        self.sequence_identity_field.setObjectName("sequence_identity_field")
        self.sequence_identity_field.setDisabled(True)

        self.sequence_identity_percent_label = QtWidgets.QLabel(self.central_widget)
        self.sequence_identity_percent_label.setGeometry(QtCore.QRect(540, 130, 59, 25))
        self.sequence_identity_percent_label.setObjectName("sequence_identity_percent_label")

        self.browse_templates.setCentralWidget(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(self.browse_templates)
        self.status_bar.setObjectName("status_bar")
        self.browse_templates.setStatusBar(self.status_bar)

        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.browse_templates)

    def translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.browse_templates.setWindowTitle(_translate("browse_templates", "MainWindow"))
        self.label.setText(_translate("browse_templates", '<html><head/><body><p><span style="font-weight:600;">Available templates</span></p></body></html>'))
        self.home_button.setText(_translate("browse_templates", "Home"))

        self.show_alignment_button.setToolTip(_translate("browse_templates", "Show TM wise alignment between target sequence and selected template"))
        self.show_alignment_button.setText(_translate("browse_templates", "Alignment"))

        self.show_hydrophobicity_plot_button.setToolTip(_translate("browse_templates", "Show hydrophobicity plot"))
        self.show_hydrophobicity_plot_button.setText(_translate("browse_templates", "Hydrophobicity plot"))

        self.show_helical_plot_button.setToolTip(_translate("browse_templates", "Show helical plot"))
        self.show_helical_plot_button.setText(_translate("browse_templates", "Helical plot"))

        self.download_result_summary_button.setToolTip(_translate("browse_templates", "Download result summary"))
        self.download_result_summary_button.setText(_translate("browse_templates", "Result summary"))

        self.available_pdb_files_button.setToolTip(_translate("browse_templates", "Show available PDBs for selected GPCR"))
        self.available_pdb_files_button.setText(_translate("browse_templates", "Available PDB files"))

        item = self.ssd_table.verticalHeaderItem(0)
        item.setText(_translate("browse_templates", "TM1"))
        item = self.ssd_table.verticalHeaderItem(1)
        item.setText(_translate("browse_templates", "TM2"))
        item = self.ssd_table.verticalHeaderItem(2)
        item.setText(_translate("browse_templates", "TM3"))
        item = self.ssd_table.verticalHeaderItem(3)
        item.setText(_translate("browse_templates", "TM4"))
        item = self.ssd_table.verticalHeaderItem(4)
        item.setText(_translate("browse_templates", "TM5"))
        item = self.ssd_table.verticalHeaderItem(5)
        item.setText(_translate("browse_templates", "TM6"))
        item = self.ssd_table.verticalHeaderItem(6)
        item.setText(_translate("browse_templates", "TM7"))
        item = self.ssd_table.horizontalHeaderItem(0)
        item.setText(_translate("browse_templates", "SSD"))
        item = self.ssd_table.horizontalHeaderItem(1)
        item.setText(_translate("browse_templates", "Identity (%)"))

        self.similarity_score_text_label.setText(_translate("browse_templates", "Hotspot Residue Similarity:"))
        self.sequence_identity_text_label.setText(_translate("browse_templates", "Sequence Identity:"))
        self.sequence_identity_percent_label.setText(_translate("browse_templates", "%"))

        __sortingEnabled = self.template_list.isSortingEnabled()
        self.template_list.setSortingEnabled(False)

        for i in range(self.receptors_size):
            item = self.template_list.item(i)
            item.setText(_translate("BrowseTemplates", self.receptors[i]))

        self.template_list.setSortingEnabled(__sortingEnabled)

    def template_list_clicked_handler(self, i):
        current_item_text = self.template_list.itemFromIndex(i).text()

        self.calculate(current_item_text)
        self.alignment = self.align()

        target_id, target_receptor, target_sequence, target_number, template_id, template_receptor, template_sequence, template_number = Helper.calculate_alignment(self.targ_id, current_item_text)

        self.target_id = target_id
        self.target_receptor = target_receptor
        self.target_sequence = target_sequence
        self.target_number = target_number
        self.template_id = template_id
        self.template_receptor = template_receptor
        self.template_sequence = template_sequence
        self.template_number = template_number

        self.show_alignment_button.setDisabled(False)
        self.show_hydrophobicity_plot_button.setDisabled(False)
        self.show_helical_plot_button.setDisabled(False)
        self.download_result_summary_button.setDisabled(False)
        self.available_pdb_files_button.setDisabled(False)

    def calculate(self, current_item_text):
        df4 = Helper.df_target.apply(lambda row: row.astype(str).str.contains(self.targ_id).any(), axis=1)  # searching entered sequence in target database
        df5, = df4[df4 == True].index  # getting row number of target sequence
        self.target_id = Helper.df_target.loc[df5, "Uniprot_ID"]  # getting uniprot_id of template name
        targ_seq = Helper.df_target.loc[df5, "Sequence"]  # getting target sequence
        self.target_receptor = Helper.df_target.loc[df5, 'Receptor']  # getting target receptor

        df2 = Helper.df_template.apply(lambda row: row.astype(str).str.contains(current_item_text).any(), axis=1)  # searching clicked name in template database
        df3, = df2[df2 == True].index  # getting row number of template name
        self.template_id = Helper.df_template.loc[df3, "PDBID"]  # getting pdbid of template name
        temp_seq = Helper.df_template.loc[df3, "Sequence"]  # getting template sequence
        self.template_receptor = Helper.df_template.loc[df3, 'Receptor']  # getting template receptor
        self.split_helix(self.template_id, type='template', numbers=True)

        self.target_sequence = targ_seq
        self.template_sequence = temp_seq

        sum_value = 0
        for hotspot_residue_position in self.hotspot_residue_positions:
            sum_value += Helper.calculate_hotspot_residue_similarity(targ_seq, temp_seq, hotspot_residue_position)
        self.similarity_score_field.setText(str(sum_value))

        self.align()
        ssd_tm = self.ssd()
        tm1 = str(ssd_tm[0])  # storing SSD for TM1 and converting into string
        tm2 = str(ssd_tm[1])
        tm3 = str(ssd_tm[2])
        tm4 = str(ssd_tm[3])
        tm5 = str(ssd_tm[4])
        tm6 = str(ssd_tm[5])
        tm7 = str(ssd_tm[6])

        self.ssd_table.setItem(0, 0, QtWidgets.QTableWidgetItem(tm1))
        self.ssd_table.setItem(1, 0, QtWidgets.QTableWidgetItem(tm2))
        self.ssd_table.setItem(2, 0, QtWidgets.QTableWidgetItem(tm3))
        self.ssd_table.setItem(3, 0, QtWidgets.QTableWidgetItem(tm4))
        self.ssd_table.setItem(4, 0, QtWidgets.QTableWidgetItem(tm5))
        self.ssd_table.setItem(5, 0, QtWidgets.QTableWidgetItem(tm6))
        self.ssd_table.setItem(6, 0, QtWidgets.QTableWidgetItem(tm7))

        ident = Helper.identity_for_whole_sequence(temp_seq, targ_seq)
        self.sequence_identity_field.setText(str(ident))

        self.report_data.append({
            'receptor': current_item_text,
            'ssd_tm1': tm1,
            'ssd_tm2': tm2,
            'ssd_tm3': tm3,
            'ssd_tm4': tm4,
            'ssd_tm5': tm5,
            'ssd_tm6': tm6,
            'ssd_tm7': tm7,
            'sequence_identity': ident
        })

    def back_home(self):
        from Home import Ui_HomeWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeWindow(self.window)
        self.ui.setup_ui()
        self.browse_templates.hide()
        self.window.setWindowTitle('Bio-GATS')
        self.window.show()

    def split_helix(self, id, type, numbers):
        df, ref = '', ''
        if type == 'template':
            ref = 'PDBID'
            df = Helper.df_template
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
        if numbers == False:
            return (prot)
        if numbers == True:
            return (numb)

    def align(self):
        self.template = self.split_helix(self.template_id, 'template', False)
        self.target = self.split_helix(self.target_id, 'target', False)

        for i in range(7):
            ident = Helper.identity_for_sequence_chunks(self.template[0][i], self.target[0][i])
            self.ssd_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(ident)))

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

        return align

    def ssd(self):
        template = Helper.df_template.loc[Helper.df_template['PDBID'] == self.template_id, 'Sequence'].iloc[0]
        target = Helper.df_target.loc[Helper.df_target['Uniprot_ID'] == self.target_id, 'Sequence'].iloc[0]
        windowl = 11
        hyd = [None, None]
        hyd[0] = [Helper.hydscale[res] for res in template]
        hyd[1] = [Helper.hydscale[res] for res in target]
        lens = [len(template), len(target)]
        hydr = [[1] * int(windowl / 2) for i in range(2)]
        for k in range(2):
            for i in range(int(windowl / 2), lens[k] - int(windowl / 2)):
                sumb = 0
                for j in range(-int(windowl / 2), int(windowl / 2) + 1):
                    sumb += hyd[k][i + j]
                avg = sumb / windowl
                hydr[k].append(avg)
        for i in range(2):
            hydr[i] += [1] * int(windowl / 2)
        templist = list(template)
        targlist = list(target)
        length = len(templist)
        targalign = ['-'] * (length)
        tempalign = templist
        tempvals = self.split_helix(self.template_id, type='template', numbers=True)
        targvals = self.split_helix(self.target_id, type='target', numbers=True)
        temphelix = tempvals[0]
        targhelix = targvals[0]
        tempBW = tempvals[1]
        targBW = targvals[1]
        self.name = self.template_id + ',' + self.target_id
        hydiff = []
        self.hydrh = [[[] for x in range(2)] for y in range(7)]
        self.ress = [[] for y in range(7)]
        perresssd = []
        for i in range(7):
            self.summ = [0] * 7
            for j in range(int(targhelix[i][0]) - 1, int(targhelix[i][1])):
                targalign[j + tempBW[i] - targBW[i]] = targlist[j]
            for j in range(int(temphelix[i][0]) - 1, int(temphelix[i][1])):
                self.hydrh[i][0].append(hydr[0][j])
                self.hydrh[i][1].append(hydr[1][targBW[i] - tempBW[i] + j])
                self.summ[i] += ((hydr[1][targBW[i] - tempBW[i] + j]) - (hydr[0][j])) ** 2
            resno = (tempBW[i] - targBW[i] + targhelix[i][0]) - temphelix[i][0]
            self.ress[i] = [x for x in range(int(temphelix[i][0]), int(temphelix[i][1] + 1))]
            self.value[i] = self.summ[i] / (temphelix[i][1] - temphelix[i][0] + 1)
            hydiff.append(round(self.summ[i], 3))
            perresssd.append(round(self.value[i], 3))

        return (perresssd)

    def show_alignment_click_handler(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Alignment(self.window, self.alignment, self.template_receptor, self.target_receptor, self.template_sequence, self.target_sequence, self.template_number, self.target_number)
        self.ui.setup_ui()
        self.window.setWindowTitle('Alignment - Bio-GATS')
        self.window.show()

    def available_pdb_files(self):
        itemd = self.template_list.currentItem()
        df4 = None
        for i in range(69):
            if itemd == self.template_list.item(i):
                item1 = self.template_list.item(i).text()
                df2 = Helper.df_template.apply(lambda row: row.astype(str).str.contains(item1).any(), axis=1)  # searching clicked name in template database
                df3, = df2[df2 == True].index  # getting row number of template name
                seq = Helper.df_template.loc[df3, 'Sequence']
                df4 = Helper.df_template[Helper.df_template['Sequence'] == seq]

        if df4 is None:
            QtWidgets.QMessageBox.about(QtWidgets.QMessageBox(), "Information", "Please select a template first")
            return

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aPdb(self.window, df4)
        self.ui.setup_ui()
        self.window.setWindowTitle('Available PDBs - Bio-GATS')
        self.window.show()

    def show_hydrophobicity_plot(self):
        Helper.show_hydrophobicity_plot(self.ress, self.hydrh, self.summ, self.value, self.template_receptor, self.target_receptor, self.name, download=False)

    def show_helical_plot(self):
        Helper.show_helical_plot(self.template, self.target, self.template_receptor, self.target_receptor, self.name, download=False)

    def download_result_summary(self):
        hydrophobicity_plot_filenames = Helper.show_hydrophobicity_plot(self.ress, self.hydrh, self.summ, self.value, self.template_receptor, self.target_receptor, self.name, download=True)
        helical_plot_filenames = Helper.show_helical_plot(self.template, self.target, self.template_receptor, self.target_receptor, self.name, download=True)
        Helper.generate_result_summary(self.alignment, self.template_receptor, self.target_receptor, self.template_sequence, self.target_sequence, self.template_number, self.target_number, hydrophobicity_plot_filenames, helical_plot_filenames)
