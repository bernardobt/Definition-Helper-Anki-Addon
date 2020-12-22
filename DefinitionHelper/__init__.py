# -*- coding: utf-8 -*-

from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import json
import re
from textwrap import wrap
from PyQt5 import QtCore, QtWidgets
from aqt.main import ResetReason

from . import Pyperclip

from . import mecab_wrapper



class Ui_AddonWindow(QDialog):
    # Config Setup
    focus_field = 'Focus'
    target_jp_field = 'Def Jp'
    target_en_field = 'Def En'
    target_deck = "6 - Mining deck"

    results_font_jp = "Meiryo"
    font_size_jp = 10
    set_wrap_jp = 21

    results_font_en = "Meiryo"
    font_size_en = 10
    set_wrap_en = 40

    dict_1 = "大辞林"
    dict_2 = "広辞苑"
    dict_3 = "新明解"
    dict_4 = "jmdict_english"

    dict_folder_path = "D:\\Python\\MineHelper\\Dictionaries\\"
    dict_path = [dict_folder_path + dict_1,
                 dict_folder_path + dict_2,
                 dict_folder_path + dict_3,
                 dict_folder_path + dict_4]

    monitor_state = False

    # stop_signal = pyqtSignal()


    def setupUi(self, AddonWindow):

        AddonWindow.setObjectName("AddonWindow")
        AddonWindow.resize(375, 720)
        AddonWindow.setMinimumSize(QtCore.QSize(375, 720))

        self.dictionaries_list = self.load_multi_dict(self.dict_path)

        self.centralwidget = QtWidgets.QWidget(AddonWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget_menu = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_menu.setEnabled(True)
        self.tabWidget_menu.setGeometry(QtCore.QRect(5, 10, 360, 230))
        self.tabWidget_menu.setObjectName("tabWidget_menu")


        # Current Tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
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
        self.tabWidget_menu.addTab(self.tab, "")

        self.curr_dis_button.clicked.connect(lambda: self.get_current_gui(self.dictionaries_list))

        # Fetch Recent
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 330, 30))
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

        self.fb_btn_run.clicked.connect(
            lambda: self.run_clicked(self.fb_rbtn_last.isChecked(), self.fb_le_query.text()))

        # Regex
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 330, 30))
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

        # Parser
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 330, 30))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.parser_chkbtn_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_6)
        self.parser_chkbtn_2.setObjectName("parser_chkbtn_2")
        self.parser_chkbtn_2.toggled.connect(self.on_check_cb_funtion_toggled)

        self.horizontalLayout_4.addWidget(self.parser_chkbtn_2)
        self.parser_text_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.parser_text_2.setObjectName("parser_text_2")
        self.horizontalLayout_4.addWidget(self.parser_text_2)
        self.parser_pushbutton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.parser_pushbutton_2.setObjectName("parser_pushbutton_2")
        self.horizontalLayout_4.addWidget(self.parser_pushbutton_2)
        self.parser_pushbutton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.parser_pushbutton_3.setObjectName("parser_pushbutton_3")
        self.horizontalLayout_4.addWidget(self.parser_pushbutton_3)

        self.parser_tab_scroll_area_2 = QtWidgets.QScrollArea(self.tab_2)
        self.parser_tab_scroll_area_2.setGeometry(QtCore.QRect(5, 40, 350, 160))
        self.parser_tab_scroll_area_2.setWidgetResizable(True)
        self.parser_tab_scroll_area_2.setObjectName("parser_tab_scroll_area_2")

        self.scrollAreaWidgetContents_parser = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_parser.setGeometry(QtCore.QRect(1, 1, 348, 158))
        self.scrollAreaWidgetContents_parser.setObjectName("scrollAreaWidgetContents_parser")

        self.verticalLayout_parser = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_parser)
        self.verticalLayout_parser.setObjectName("verticalLayoutWidget_4")
        self.parser_tab_scroll_area_2.setWidget(self.scrollAreaWidgetContents_parser)

        self.tabWidget_menu.addTab(self.tab_2, "")

        self.parser_pushbutton_2.clicked.connect(lambda: self.mecab_parse(self.parser_text_2.text()))
        self.parser_pushbutton_3.clicked.connect(lambda: self.copy_clipboard())

        # Clipboard
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 359, 202))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.plainTextEdit.setFont(QFont(self.results_font_jp, self.font_size_jp))
        
        self.tabWidget_menu.addTab(self.tab_3, "")

        # tab 4
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        # self.tabWidget_menu.addTab(self.tab_4, "")


        # Settings
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        # self.tabWidget_menu.addTab(self.tab_5, "")

        # Results Box
        self.results_box = QtWidgets.QGroupBox(self.centralwidget)
        self.results_box.setGeometry(QtCore.QRect(10, 250, 360, 450))
        self.results_box.setObjectName("results_box")
        self.dict_tabs = QtWidgets.QTabWidget(self.results_box)
        self.dict_tabs.setGeometry(QtCore.QRect(10, 20, 340, 420))
        self.dict_tabs.setObjectName("dict_tabs")

        # tab dict 1
        self.res_tab_1 = QtWidgets.QWidget()
        self.res_tab_1.setObjectName("res_tab_1")
        self.dict_1_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_1)
        self.dict_1_tab_scroll_area.setGeometry(QtCore.QRect(5, 5, 325, 380))
        self.dict_1_tab_scroll_area.setWidgetResizable(True)
        self.dict_1_tab_scroll_area.setObjectName("dict_1_tab_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(1, 1, 323, 378))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dict_1_tab_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.dict_tabs.addTab(self.res_tab_1, "")

        # tab dict 2
        self.res_tab_2 = QtWidgets.QWidget()
        self.res_tab_2.setObjectName("res_tab_2")
        self.dict_2_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_2)
        self.dict_2_tab_scroll_area.setGeometry(QtCore.QRect(5, 5, 325, 380))
        self.dict_2_tab_scroll_area.setWidgetResizable(True)
        self.dict_2_tab_scroll_area.setObjectName("dict_2_tab_scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(1, 1, 323, 378))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dict_2_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.dict_tabs.addTab(self.res_tab_2, "")

        # tab dict 3
        self.res_tab_3 = QtWidgets.QWidget()
        self.res_tab_3.setObjectName("res_tab_3")
        self.dict_3_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_3)
        self.dict_3_tab_scroll_area.setGeometry(QtCore.QRect(5, 5, 325, 380))
        self.dict_3_tab_scroll_area.setWidgetResizable(True)
        self.dict_3_tab_scroll_area.setObjectName("dict_3_tab_scroll_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(1, 1, 323, 378))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dict_3_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_3)
        self.dict_tabs.addTab(self.res_tab_3, "")

        # tab dict 4
        self.res_tab_4 = QtWidgets.QWidget()
        self.res_tab_4.setObjectName("res_tab_4")
        self.dict_4_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_4)
        self.dict_4_tab_scroll_area.setGeometry(QtCore.QRect(5, 5, 325, 380))
        self.dict_4_tab_scroll_area.setWidgetResizable(True)
        self.dict_4_tab_scroll_area.setObjectName("dict_4_tab_scroll_area")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(1, 1, 323, 378))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dict_4_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_4)
        self.dict_tabs.addTab(self.res_tab_4, "")

        AddonWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddonWindow)
        self.tabWidget_menu.setCurrentIndex(0)
        self.dict_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AddonWindow)

    def retranslateUi(self, AddonWindow):
        _translate = QtCore.QCoreApplication.translate
        AddonWindow.setWindowTitle(_translate("AddonWindow", "Definition Aid"))

        # Current
        self.tabWidget_menu.setTabText(self.tabWidget_menu.indexOf(self.tab), _translate("AddonWindow", "Current"))
        self.curr_dis_textbox.setText(_translate("AddonWindow", "current note"))
        self.curr_disp_overwrite.setText(_translate("AddonWindow", "Overwrite"))
        self.curr_disp_add.setText(_translate("AddonWindow", "Add"))
        self.curr_dis_button.setText(_translate("AddonWindow", "Get"))
        self.results_box.setTitle(_translate("AddonWindow", "Results"))

        # Fetch last
        self.fb_rbtn_last.setText(_translate("AddonWindow", "Last"))
        self.fb_le_query.setText(_translate("AddonWindow", "added:1"))
        self.fb_btn_run.setText(_translate("AddonWindow", "Run"))

        # Regex
        self.regex_apply_rbtn.setText(_translate("AddonWindow", "Apply"))
        self.regex_ignore_rbtn.setText(_translate("AddonWindow", "Ignore"))
        self.regex_text.setText(_translate("AddonWindow", "regex"))
        self.regex_apply_rbtn.setText(_translate("MainWindow", "Apply"))
        self.regex_ignore_rbtn.setText(_translate("MainWindow", "Ignore"))
        self.regex_text.setText(_translate("MainWindow", "(?:(BEGIN:)|(\「)).*?(?(1):END)(?(2)\」)"))
        self.regex_text_replace.setText(_translate("MainWindow", ""))

        # Parser
        self.parser_chkbtn_2.setText(_translate("AddonWindow", "Monitor"))
        self.parser_pushbutton_2.setText(_translate("AddonWindow", "Parse"))
        self.parser_pushbutton_3.setText(_translate("AddonWindow", "Get Clipboard"))
        self.tabWidget_menu.setTabText(self.tabWidget_menu.indexOf(self.tab_2), _translate("AddonWindow", "Parser"))
        self.parser_text_2.setText("")

        # Clipboard
        self.tabWidget_menu.setTabText(self.tabWidget_menu.indexOf(self.tab_3), _translate("AddonWindow", "Clipboard"))

        # Settings
        self.tabWidget_menu.setTabText(self.tabWidget_menu.indexOf(self.tab_5), _translate("AddonWindow", "Settings"))

        # Results Box
        self.results_box.setTitle(_translate("AddonWindow", "Results"))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_1), _translate("AddonWindow", self.dict_1))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_2), _translate("AddonWindow", self.dict_2))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_3), _translate("AddonWindow", self.dict_3))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_4), _translate("AddonWindow", self.dict_4))


    def run_clicked(self, chk, qry_txt):
        if chk:
            self.get_query_last(qry_txt, self.dictionaries_list)
        else:
            showInfo(f"Extra is selected\nQuery: '{qry_txt}'\n\nNo function yet :(")

    def get_current_gui(self, dict_list):
        tab = [self.verticalLayout, self.verticalLayout_2, self.verticalLayout_3, self.verticalLayout_4]
        scroll_area = [self.scrollAreaWidgetContents, self.scrollAreaWidgetContents_2, self.scrollAreaWidgetContents_3,
                       self.scrollAreaWidgetContents_4]
        rev = mw.reviewer.card
        nid = rev.nid
        note = mw.col.getNote(nid)
        self.curr_dis_textbox.setText(f"{note[self.focus_field]}")
        for i, dict in enumerate(dict_list):
            if i != 3:
                result = self.query_dict(dict, note[self.focus_field])
                self.plot_results_gui(result, note, scroll_area[i], tab[i], self.results_font_jp, self.font_size_jp,
                                      self.set_wrap_jp, self.target_jp_field)
            else:
                result = self.jmedict_query_dict(dict, note[self.focus_field])
                self.plot_results_gui(result, note, scroll_area[i], tab[i], self.results_font_en, self.font_size_en,
                                      self.set_wrap_en, self.target_en_field)

    def get_query_last(self, query_filter, dict_list):
        tab = [self.verticalLayout, self.verticalLayout_2, self.verticalLayout_3, self.verticalLayout_4]
        scroll_area = [self.scrollAreaWidgetContents, self.scrollAreaWidgetContents_2, self.scrollAreaWidgetContents_3,
                       self.scrollAreaWidgetContents_4]
        ids = mw.col.find_notes(query_filter)
        note = mw.col.getNote(ids[-1])
        for i, dict in enumerate(dict_list):
            if i != 3:
                result = self.query_dict(dict, note[self.focus_field])
                self.plot_results(result, note, scroll_area[i], tab[i], self.results_font_jp, self.font_size_jp,
                                  self.set_wrap_jp, self.target_jp_field)
            else:
                result = self.jmedict_query_dict(dict, note[self.focus_field])
                self.plot_results(result, note, scroll_area[i], tab[i], self.results_font_en, self.font_size_en,
                                  self.set_wrap_en, self.target_en_field)

    def jmedict_query_dict(self, list_entries, query):
        result = []
        for bank in list_entries:
            for entry in bank:
                if entry[0] == query:
                    temp = []
                    query_id = f"[{entry[0]}] [{entry[1]}]"
                    temp.append(query_id)
                    tag_str = entry[2].split(' ')
                    new_tag = self.jmedict_tag_handler(tag_str, list_entries[1])
                    temp.append(new_tag)

                    def_str = ', '.join(entry[5])
                    temp.append(def_str)
                    if entry[7] != "":
                        sp_tag_str = entry[7].split(' ')
                        new_sp_tags = self.jmedict_tag_handler(sp_tag_str, list_entries[1])
                        temp.append(new_sp_tags)

                    result.append(temp)
                elif entry[1] == query:
                    temp = []
                    query_id = f"[{entry[0]}] [{entry[1]}]"
                    temp.append(query_id)
                    tag_str = entry[2].split(' ')
                    new_tag = self.jmedict_tag_handler(tag_str, list_entries[1])
                    temp.append(new_tag)

                    def_str = ', '.join(entry[5])
                    temp.append(def_str)
                    if entry[7] != "":
                        sp_tag_str = entry[7].split(' ')
                        new_sp_tags = self.jmedict_tag_handler(sp_tag_str, list_entries[1])
                        temp.append(new_sp_tags)

                    result.append(temp)

        return result

    def jmedict_tag_handler(self, to_handle_list, tag_bank):
        fixed_tags = []
        for tag in to_handle_list:
            for listed_tag in tag_bank:
                if tag == listed_tag[0]:
                    fixed_tags.append(listed_tag[3])
        tags_in_list = '; '.join(fixed_tags)
        return tags_in_list

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
                    result.append(def_list)
                elif entry[1] == query:
                    def_str = ' '.join(map(str, entry[5]))
                    def_list = def_str.split('\n')
                    def_list += def_list.pop()
                    result.append(def_list)
        return result

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def plot_results(self, results_list, note, which_scroll, which_tab, results_font, font_size, set_wrap,
                     target_field):
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
                    self.tab_res_button.setFont(QFont(results_font, font_size))
                    new_ele = wrap(element, set_wrap)
                    wraped_ele = "\n".join(new_ele)
                    self.tab_res_button.setText(f"{wraped_ele}")
                    which_tab.addWidget(self.tab_res_button)
                    self.tab_res_button.clicked.connect(
                        lambda ch, element=element: self.update_note(note, element, target_field))
        else:
            self.tab_res_label = QtWidgets.QLabel(which_scroll)
            self.tab_res_label.setObjectName("label")
            self.tab_res_label.setText(f"No Results found!")
            which_tab.addWidget(self.tab_res_label)

    def plot_results_gui(self, results_list, note, which_scroll, which_tab, results_font, font_size, set_wrap,
                         target_field):
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
                    self.tab_res_button.setFont(QFont(results_font, font_size))
                    new_ele = wrap(element, set_wrap)
                    wraped_ele = "\n".join(new_ele)
                    self.tab_res_button.setText(f"{wraped_ele}")
                    which_tab.addWidget(self.tab_res_button)
                    self.tab_res_button.clicked.connect(
                        lambda ch, element=element: self.update_note_gui(note, element, target_field))
        else:
            self.tab_res_label = QtWidgets.QLabel(which_scroll)
            self.tab_res_label.setObjectName("label")
            self.tab_res_label.setText(f"No Results found!")
            which_tab.addWidget(self.tab_res_label)

    def update_note(self, note_id, content, target_field):
        if self.curr_disp_overwrite.isChecked():
            if self.regex_apply_rbtn.isChecked():
                regex_content = re.sub(f"{self.regex_text.text()}", f"{self.regex_text_replace.text()}", content)
                note_id[target_field] = regex_content
                note_id.flush()
            else:
                note_id[self.target_jp_field] = content
                note_id.flush()
        else:
            if self.regex_apply_rbtn.isChecked():
                regex_content = re.sub(f"{self.regex_text.text()}", f"{self.regex_text_replace.text()}", content)
                note_id[target_field] += f"<br>{regex_content}"
                note_id.flush()
            else:
                note_id[target_field] += f"<br>{content}"
                note_id.flush()

    def update_note_gui(self, note_id, content, target_field):
        if self.curr_disp_overwrite.isChecked():
            if self.regex_apply_rbtn.isChecked():
                regex_content = re.sub(f"{self.regex_text.text()}", f"{self.regex_text_replace.text()}", content)
                note_id[target_field] = regex_content
                note_id.flush()
            else:
                note_id[target_field] = content
                note_id.flush()
        else:
            if self.regex_apply_rbtn.isChecked():
                regex_content = re.sub(f"{self.regex_text.text()}", f"{self.regex_text_replace.text()}", content)
                note_id[target_field] += f"<br>{regex_content}"
                note_id.flush()
            else:
                note_id[target_field] += f"<br>{content}"
                note_id.flush()
        mw.requireReset(reason=ResetReason.EditCurrentInit, context=self)
        mw.delayedMaybeReset()

    def mecab_parse(self, sentence):
        parsed = mecab_wrapper.getMorphemesMecab(sentence)
        self.plot_parsed(parsed, self.scrollAreaWidgetContents_parser , self.verticalLayout_parser, self.results_font_jp,
                         self.font_size_jp)
        return parsed

    def find_duplicates(self, text):
        ids = mw.col.find_notes(f'"deck:{self.target_deck}"')
        for id in ids:
            note = mw.col.getNote(id)
            if note[self.focus_field] == text:
                return True

    def plot_parsed(self, data, which_scroll, which_layout,  results_font, font_size):
        self.clearLayout(which_layout)
        if data:
            for morpheme in data:
                self.parse_res_button = QtWidgets.QPushButton(which_scroll)
                self.parse_res_button.setObjectName("pushButton")
                self.parse_res_button.setFont(QFont(results_font, font_size))
                dupe = self.find_duplicates(morpheme.base)
                if dupe:
                    self.parse_res_button.setText(f"{morpheme.inflected} ({morpheme.base}) (Duplicate)")
                else:
                    self.parse_res_button.setText(f"{morpheme.inflected} ({morpheme.base})")
                which_layout.addWidget(self.parse_res_button)
                self.parse_res_button.clicked.connect(
                    lambda ch, morpheme=morpheme: self.create_new_card(morpheme.base))
        pass

    def create_new_card(self, morph):
        deck_id = mw.col.decks.id_for_name(self.target_deck)
        new_note = mw.col.newNote()
        mw.col.add_note(new_note, deck_id)
        new_note['Focus'] = morph
        new_note.flush()
        self.run_clicked(self.fb_rbtn_last.isChecked(), self.fb_le_query.text())
        mw.requireReset(reason=ResetReason.EditCurrentInit, context=self)
        mw.delayedMaybeReset()

    def copy_clipboard(self):
        cilp_text = Pyperclip.paste()
        self.parser_text_2.setText(cilp_text)

    def monitor_clipboard(self):
        self.cb_monitor = clip_monitor()
        self.cb_monitor.start()
        self.cb_monitor.update_clipboard.connect(self.cb_mon_update_progress)


    def cb_mon_update_progress(self, val):
        self.plainTextEdit.appendPlainText(f"{val}")

    def on_check_cb_funtion_toggled(self):
        if self.parser_chkbtn_2.isChecked():
            self.monitor_clipboard()
        else:
            pass

class clip_monitor(QThread):
    continue_run = True
    update_clipboard = pyqtSignal(str)

    finished = pyqtSignal()

    def run(self):
        while self.continue_run:
            new_text = Pyperclip.waitForNewPaste()
            self.update_clipboard.emit(new_text)
        self.finished.emit()

    def stop(self):
        self.continue_run = False


def window():
    mw.myWidget = AddonWindow = QtWidgets.QMainWindow()
    AddonWindow.setObjectName("Definition Updater")
    ui = Ui_AddonWindow()
    ui.setupUi(AddonWindow)
    AddonWindow.show()


action = QAction("Definition Updater", mw)
action.triggered.connect(window)
mw.form.menuTools.addAction(action)
