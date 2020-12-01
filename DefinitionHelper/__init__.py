# -*- coding: utf-8 -*-
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import json
import re
from textwrap import wrap
from PyQt5 import QtCore, QtWidgets
from aqt.main import ResetReason


class Def_Updater(object):
    focus_field = 'Focus'
    target_jp_field = 'Def Jp'

    results_font = "Meiryo"
    font_size = 10
    set_wrap = 21

    dict_1 = "大辞林"
    dict_2 = "広辞苑"
    dict_3 = "新明解"
    
    dict_folder_path = "D:\\Python\\MineHelper\\Dictionaries\\"
    dict_path = [dict_folder_path + dict_1,
                 dict_folder_path + dict_2,
                 dict_folder_path + dict_3]

    def setupUi(self, AddonWindow):
        AddonWindow.setObjectName("Definition Updater")
        AddonWindow.resize(366, 680)
        AddonWindow.setMinimumSize(366, 680)

        #Fetch options
        self.dictionaries_list = self.load_multi_dict(self.dict_path)
        self.centralwidget = QtWidgets.QWidget(AddonWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fetch_options_box = QtWidgets.QGroupBox(self.centralwidget)
        self.fetch_options_box.setGeometry(QtCore.QRect(10, 10, 350, 60))
        self.fetch_options_box.setObjectName("fetch_options_box")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.fetch_options_box)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 330, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.fetch_box_h_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.fetch_box_h_layout.setContentsMargins(0, 0, 0, 0)
        self.fetch_box_h_layout.setObjectName("fetch_box_h_layout")
        self.fb_rbtn_last = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.fb_rbtn_last.setChecked(True)
        self.fb_rbtn_last.setObjectName("fb_rbtn_last")
        self.fetch_box_h_layout.addWidget(self.fb_rbtn_last)
        # self.fb_rbtn_loop = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        # self.fb_rbtn_loop.setObjectName("fb_rbtn_loop")
        # self.fetch_box_h_layout.addWidget(self.fb_rbtn_loop)
        self.fb_le_query = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.fb_le_query.setObjectName("fb_le_query")
        self.fetch_box_h_layout.addWidget(self.fb_le_query)
        self.fb_btn_run = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fb_btn_run.setObjectName("fb_btn_run")
        self.fetch_box_h_layout.addWidget(self.fb_btn_run)

        # Get current
        self.current_display_box = QtWidgets.QGroupBox(self.centralwidget)
        self.current_display_box.setGeometry(QtCore.QRect(10, 80, 350, 60))
        self.current_display_box.setObjectName("current_display_box")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.current_display_box)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 330, 30))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.current_box_h_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.current_box_h_layout.setContentsMargins(0, 0, 0, 0)
        self.current_box_h_layout.setObjectName("current_box_h_layout")
        self.curr_disp_overwrite = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.curr_disp_overwrite.setChecked(True)
        self.curr_disp_overwrite.setObjectName("curr_disp_overwrite")
        self.current_box_h_layout.addWidget(self.curr_disp_overwrite)
        self.curr_disp_add = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.curr_disp_add.setObjectName("curr_disp_add")
        self.current_box_h_layout.addWidget(self.curr_disp_add)
        self.curr_dis_textbox = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.curr_dis_textbox.setObjectName("curr_dis_textbox")
        self.current_box_h_layout.addWidget(self.curr_dis_textbox)
        self.curr_dis_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.curr_dis_button.setObjectName("curr_dis_button")
        self.current_box_h_layout.addWidget(self.curr_dis_button)

        #regex stuff
        self.regex_options_box = QtWidgets.QGroupBox(self.centralwidget)
        self.regex_options_box.setGeometry(QtCore.QRect(10, 150, 350, 60))
        self.regex_options_box.setObjectName("regex_options_box")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.regex_options_box)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 330, 30))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.regex_box_h_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.regex_box_h_layout.setContentsMargins(0, 0, 0, 0)
        self.regex_box_h_layout.setObjectName("regex_box_h_layout")
        self.regex_apply_rbtn = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.regex_apply_rbtn.setChecked(True)
        self.regex_apply_rbtn.setObjectName("regex_apply_rbtn")
        self.regex_box_h_layout.addWidget(self.regex_apply_rbtn)
        self.regex_ignore_rbtn = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.regex_ignore_rbtn.setObjectName("regex_ignore_rbtn")
        self.regex_box_h_layout.addWidget(self.regex_ignore_rbtn)
        self.regex_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.regex_text.setObjectName("regex_text")
        self.regex_box_h_layout.addWidget(self.regex_text)
        self.regex_text_replace = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.regex_text_replace.setObjectName("regex_text_replace")
        self.regex_box_h_layout.addWidget(self.regex_text_replace)

        #Results box
        self.results_box = QtWidgets.QGroupBox(self.centralwidget)
        self.results_box.setGeometry(QtCore.QRect(10, 220, 350, 430))
        self.results_box.setObjectName("results_box")
        self.dict_tabs = QtWidgets.QTabWidget(self.results_box)
        self.dict_tabs.setGeometry(QtCore.QRect(10, 20, 330, 400))
        self.dict_tabs.setObjectName("dict_tabs")
        self.res_tab_1 = QtWidgets.QWidget()
        self.res_tab_1.setObjectName("res_tab_1")
        self.dict_1_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_1)
        self.dict_1_tab_scroll_area.setGeometry(QtCore.QRect(5, 5, 315, 360))
        self.dict_1_tab_scroll_area.setWidgetResizable(True)
        self.dict_1_tab_scroll_area.setObjectName("dict_1_tab_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(1, 1, 313, 368))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dict_1_tab_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.dict_tabs.addTab(self.res_tab_1, "")
        self.res_tab_2 = QtWidgets.QWidget()
        self.res_tab_2.setObjectName("res_tab_2")
        self.dict_2_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_2)
        self.dict_2_tab_scroll_area.setGeometry(QtCore.QRect(5, 5, 315, 360))
        self.dict_2_tab_scroll_area.setWidgetResizable(True)
        self.dict_2_tab_scroll_area.setObjectName("dict_2_tab_scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(1, 1, 313, 368))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dict_2_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.dict_tabs.addTab(self.res_tab_2, "")
        self.res_tab_3 = QtWidgets.QWidget()
        self.res_tab_3.setObjectName("res_tab_3")
        self.dict_3_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_3)
        self.dict_3_tab_scroll_area.setGeometry(QtCore.QRect(5, 5, 315, 360))
        self.dict_3_tab_scroll_area.setWidgetResizable(True)
        self.dict_3_tab_scroll_area.setObjectName("dict_3_tab_scroll_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(1, 1, 313, 368))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dict_3_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_3)
        self.dict_tabs.addTab(self.res_tab_3, "")
        AddonWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddonWindow)
        self.statusbar.setObjectName("statusbar")
        AddonWindow.setStatusBar(self.statusbar)

        self.curr_dis_button.clicked.connect(lambda: self.get_current_gui(self.dictionaries_list))
        self.fb_btn_run.clicked.connect(lambda: self.run_clicked(self.fb_rbtn_last.isChecked(), self.fb_le_query.text()))

        self.retranslateUi(AddonWindow)
        self.dict_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AddonWindow)

    def retranslateUi(self, AddonWindow):
        _translate = QtCore.QCoreApplication.translate
        AddonWindow.setWindowTitle(_translate("AddonWindow", "Definition Helper"))
        self.fetch_options_box.setTitle(_translate("AddonWindow", "Fetch Options"))
        self.fb_rbtn_last.setText(_translate("AddonWindow", "Last"))
        # self.fb_rbtn_loop.setText(_translate("AddonWindow", "Extra"))
        self.fb_le_query.setText(_translate("AddonWindow", "added:1"))
        self.fb_btn_run.setText(_translate("AddonWindow", "Run"))
        self.current_display_box.setTitle(_translate("AddonWindow", "Current"))
        self.curr_dis_textbox.setText(_translate("AddonWindow", "current note"))
        self.curr_disp_overwrite.setText(_translate("AddonWindow", "Overwrite"))
        self.curr_disp_add.setText(_translate("AddonWindow", "Add"))
        self.curr_dis_button.setText(_translate("AddonWindow", "Get"))
        self.results_box.setTitle(_translate("AddonWindow", "Results"))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_1), _translate("AddonWindow", self.dict_1))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_2), _translate("AddonWindow", self.dict_2))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_3), _translate("AddonWindow", self.dict_3))
        self.regex_options_box.setTitle(_translate("MainWindow", "Regex"))
        self.regex_apply_rbtn.setText(_translate("MainWindow", "Apply"))
        self.regex_ignore_rbtn.setText(_translate("MainWindow", "Ignore"))
        self.regex_text.setText(_translate("MainWindow", "(?:(BEGIN:)|(\「)).*?(?(1):END)(?(2)\」)"))
        self.regex_text_replace.setText(_translate("MainWindow", ""))


    def run_clicked(self, chk, qry_txt):
        if chk:
            # showInfo(f"Last added is selected\nQuery: '{qry_txt}'")
            self.get_query_last(qry_txt, self.dictionaries_list)
        else:
            showInfo(f"Extra is selected\nQuery: '{qry_txt}'\n\nNo function yet :(")


    def get_current_gui(self, dict_list):
        tab = [self.verticalLayout, self.verticalLayout_2, self.verticalLayout_3]
        scroll_area = [self.scrollAreaWidgetContents, self.scrollAreaWidgetContents_2, self.scrollAreaWidgetContents_3]
        rev = mw.reviewer.card
        nid = rev.nid
        note = mw.col.getNote(nid)
        self.curr_dis_textbox.setText(f"{note[self.focus_field]}")
        for i, dict in enumerate(dict_list):
            result = self.query_dict(dict, note[self.focus_field])
            self.plot_results_gui(result, note, scroll_area[i], tab[i])

    def get_query_last(self, query_filter, dict_list):
        tab = [self.verticalLayout, self.verticalLayout_2, self.verticalLayout_3]
        scroll_area = [self.scrollAreaWidgetContents, self.scrollAreaWidgetContents_2, self.scrollAreaWidgetContents_3]
        ids = mw.col.find_notes(query_filter)
        note = mw.col.getNote(ids[-1])
        # showInfo(f"Search: {note[self.focus_field]}")
        for i, dict in enumerate(dict_list):
            result = self.query_dict(dict, note[self.focus_field])
            self.plot_results_gui(result, note, scroll_area[i], tab[i])

    def get_query_loop(self, query_filter):
        ids = mw.col.find_notes(query_filter)
        # showInfo(f"Cards found: {len(ids)}")
        for id in ids:
            note = mw.col.getNote(id)
            result = self.query_dict(self.term_bank_file_list, note[self.focus_field])
            # showInfo(f"Search: {note[self.focus_field]}")
            self.plot_results(result, note, self.verticalLayout)

    def get_file_list(self, path):
        arr = os.listdir(path)
        return arr

    def load_multi_dict(self, path_list):
        all_dict_jsons = []
        for path in path_list:
            list_of_files = self.get_file_list(path)
            all_jsons = []
            for i, file in enumerate(list_of_files):
                with open(f"{path}\\{list_of_files[i]}", encoding="utf-8") as file:
                    data = json.load(file)
                    all_jsons.append(data)
            all_dict_jsons.append(all_jsons)
        return all_dict_jsons

    def query_dict(self, list_entries, query):
        result = []
        for bank in list_entries:
            for entry in bank:
                if entry[0] == query:
                    def_str = ' '.join(map(str, entry[5]))
                    def_list = def_str.split('\n')
                    def_list += def_list.pop()
                    ## if you wan to add the term and reading in the results
                    # def_list.insert(0,f"{entry[0]} ")
                    # def_list.insert(1, f"{entry[1]}")
                    result.append(def_list)
        return result

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def plot_results(self, results_list, note, which_tab, which_scroll):
        self.clearLayout(which_tab)
        if results_list:
            for dindex, result in enumerate(results_list):
                self.tab_res_label = QtWidgets.QLabel(which_scroll)
                self.tab_res_label.setObjectName("label")
                self.tab_res_label.setText(f"Definition {dindex + 1}")
                which_tab.addWidget(self.tab_res_label)
                for lindex, element in enumerate(result):
                    self.tab_res_button = QtWidgets.QPushButton(which_scroll)
                    self.tab_res_button.setObjectName("pushButton")
                    self.tab_res_button.setFont(QFont(self.results_font, self.font_size))
                    new_ele = wrap(element, self.set_wrap)
                    wraped_ele = "\n".join(new_ele)
                    self.tab_res_button.setText(f"{wraped_ele}")
                    which_tab.addWidget(self.tab_res_button)
                    self.tab_res_button.clicked.connect(lambda ch, element=element: self.update_note(note, element))
        else:
            # showInfo("No Results found!")
            self.tab_res_label = QtWidgets.QLabel(which_scroll)
            self.tab_res_label.setObjectName("label")
            self.tab_res_label.setText(f"No Results found!")
            which_tab.addWidget(self.tab_res_label)

    def plot_results_gui(self, results_list, note, which_scroll, which_tab):
        self.clearLayout(which_tab)
        if results_list:
            for dindex, result in enumerate(results_list):
                self.tab_res_label = QtWidgets.QLabel(which_scroll)
                self.tab_res_label.setObjectName("label")
                self.tab_res_label.setText(f"Definition {dindex + 1}")
                which_tab.addWidget(self.tab_res_label)
                for lindex, element in enumerate(result):
                    self.tab_res_button = QtWidgets.QPushButton(which_scroll)
                    self.tab_res_button.setObjectName("pushButton")
                    self.tab_res_button.setFont(QFont(self.results_font, self.font_size))
                    new_ele = wrap(element, self.set_wrap)
                    wraped_ele = "\n".join(new_ele)
                    self.tab_res_button.setText(f"{wraped_ele}")
                    which_tab.addWidget(self.tab_res_button)
                    self.tab_res_button.clicked.connect(lambda ch, element=element: self.update_note_gui(note, element))
        else:
            # showInfo("No Results found!")
            self.tab_res_label = QtWidgets.QLabel(which_scroll)
            self.tab_res_label.setObjectName("label")
            self.tab_res_label.setText(f"No Results found!")
            which_tab.addWidget(self.tab_res_label)

    def update_note(self, note_id, content):
        if self.curr_disp_overwrite.isChecked():
            if self.regex_apply_rbtn.isChecked():
                regex_content = re.sub(f"{self.regex_text.text()}", f"{self.regex_text_replace}", content)
                note_id[self.target_jp_field] = regex_content
                note_id.flush()
            else:
                note_id[self.target_jp_field] = content
                note_id.flush()
        else:
            if self.regex_apply_rbtn.isChecked():
                regex_content = re.sub(f"{self.regex_text.text()}", f"{self.regex_text_replace}", content)
                note_id[self.target_jp_field] += regex_content
                note_id.flush()
            else:
                note_id[self.target_jp_field] += content
                note_id.flush()

    def update_note_gui(self, note_id, content):
        if self.curr_disp_overwrite.isChecked():
            if self.regex_apply_rbtn.isChecked():
                regex_content = re.sub(f"{self.regex_text.text()}", f"{self.regex_text_replace.text()}", content)
                note_id[self.target_jp_field] = regex_content
                note_id.flush()
            else:
                note_id[self.target_jp_field] = content
                note_id.flush()
        else:
            if self.regex_apply_rbtn.isChecked():
                regex_content = re.sub(f"{self.regex_text.text()}", f"{self.regex_text_replace.text()}", content)
                note_id[self.target_jp_field] = regex_content
                note_id.flush()
            else:
                note_id[self.target_jp_field] += f"<br>{content}"
                note_id.flush()
        mw.requireReset(reason=ResetReason.EditCurrentInit, context=self)
        mw.delayedMaybeReset()


def window():
    mw.myWidget = AddonWindow = QtWidgets.QMainWindow()
    AddonWindow.setObjectName("Definition Updater")
    ui = Def_Updater()
    ui.setupUi(AddonWindow)
    AddonWindow.show()


action = QAction("Definition Updater", mw)
action.triggered.connect(window)
mw.form.menuTools.addAction(action)
