# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'def_helper_ui_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddonWindow(object):
    def setupUi(self, AddonWindow):
        AddonWindow.setObjectName("AddonWindow")
        AddonWindow.resize(375, 710)
        AddonWindow.setMinimumSize(QtCore.QSize(375, 710))
        AddonWindow.setMaximumSize(QtCore.QSize(375, 710))
        self.centralwidget = QtWidgets.QWidget(AddonWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dict_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.dict_tabs.setGeometry(QtCore.QRect(1, 178, 373, 523))
        self.dict_tabs.setObjectName("dict_tabs")
        self.res_tab_1 = QtWidgets.QWidget()
        self.res_tab_1.setObjectName("res_tab_1")
        self.dict_1_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_1)
        self.dict_1_tab_scroll_area.setGeometry(QtCore.QRect(0, 0, 367, 497))
        self.dict_1_tab_scroll_area.setWidgetResizable(True)
        self.dict_1_tab_scroll_area.setObjectName("dict_1_tab_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 365, 495))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dict_1_tab_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.dict_tabs.addTab(self.res_tab_1, "")
        self.res_tab_2 = QtWidgets.QWidget()
        self.res_tab_2.setObjectName("res_tab_2")
        self.dict_2_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_2)
        self.dict_2_tab_scroll_area.setGeometry(QtCore.QRect(0, 0, 367, 497))
        self.dict_2_tab_scroll_area.setWidgetResizable(True)
        self.dict_2_tab_scroll_area.setObjectName("dict_2_tab_scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 365, 495))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dict_2_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.dict_tabs.addTab(self.res_tab_2, "")
        self.res_tab_3 = QtWidgets.QWidget()
        self.res_tab_3.setObjectName("res_tab_3")
        self.dict_3_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_3)
        self.dict_3_tab_scroll_area.setGeometry(QtCore.QRect(0, 0, 367, 497))
        self.dict_3_tab_scroll_area.setWidgetResizable(True)
        self.dict_3_tab_scroll_area.setObjectName("dict_3_tab_scroll_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 365, 495))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dict_3_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_3)
        self.dict_tabs.addTab(self.res_tab_3, "")
        self.res_tab_4 = QtWidgets.QWidget()
        self.res_tab_4.setObjectName("res_tab_4")
        self.dict_4_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_4)
        self.dict_4_tab_scroll_area.setGeometry(QtCore.QRect(0, 0, 367, 497))
        self.dict_4_tab_scroll_area.setWidgetResizable(True)
        self.dict_4_tab_scroll_area.setObjectName("dict_4_tab_scroll_area")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 365, 495))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.dict_4_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_5)
        self.dict_tabs.addTab(self.res_tab_4, "")
        self.res_tab_5 = QtWidgets.QWidget()
        self.res_tab_5.setObjectName("res_tab_5")
        self.dict_5_tab_scroll_area = QtWidgets.QScrollArea(self.res_tab_5)
        self.dict_5_tab_scroll_area.setGeometry(QtCore.QRect(0, 0, 367, 497))
        self.dict_5_tab_scroll_area.setWidgetResizable(True)
        self.dict_5_tab_scroll_area.setObjectName("dict_5_tab_scroll_area")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 365, 495))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dict_5_tab_scroll_area.setWidget(self.scrollAreaWidgetContents_6)
        self.dict_tabs.addTab(self.res_tab_5, "")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_re_options = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_re_options.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_re_options.setObjectName("horizontalLayout_re_options")
        self.checkBox_re_sentences = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_re_sentences.setChecked(True)
        self.checkBox_re_sentences.setObjectName("checkBox_re_sentences")
        self.horizontalLayout_re_options.addWidget(self.checkBox_re_sentences)
        self.checkBox_re_parenthesis_jp = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_re_parenthesis_jp.setChecked(True)
        self.checkBox_re_parenthesis_jp.setObjectName("checkBox_re_parenthesis_jp")
        self.horizontalLayout_re_options.addWidget(self.checkBox_re_parenthesis_jp)
        self.checkBox_re_parenthesis_std = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_re_parenthesis_std.setObjectName("checkBox_re_parenthesis_std")
        self.horizontalLayout_re_options.addWidget(self.checkBox_re_parenthesis_std)
        self.checkBox_re_custom = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_re_custom.setObjectName("checkBox_re_custom")
        self.horizontalLayout_re_options.addWidget(self.checkBox_re_custom)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 90, 361, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_over_add = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_over_add.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_over_add.setObjectName("horizontalLayout_over_add")
        self.radioButton_Overwrite = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_Overwrite.setChecked(True)
        self.radioButton_Overwrite.setObjectName("radioButton_Overwrite")
        self.horizontalLayout_over_add.addWidget(self.radioButton_Overwrite)
        self.radioButton_add = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_add.setObjectName("radioButton_add")
        self.horizontalLayout_over_add.addWidget(self.radioButton_add)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 361, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_re_custom = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_re_custom.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_re_custom.setObjectName("horizontalLayout_re_custom")
        self.label_re_find = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_re_find.setObjectName("label_re_find")
        self.horizontalLayout_re_custom.addWidget(self.label_re_find)
        self.lineEdit_re_find = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_re_find.setObjectName("lineEdit_re_find")
        self.horizontalLayout_re_custom.addWidget(self.lineEdit_re_find)
        self.label_re_replace = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_re_replace.setObjectName("label_re_replace")
        self.horizontalLayout_re_custom.addWidget(self.label_re_replace)
        self.lineEdit_re_replace = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_re_replace.setObjectName("lineEdit_re_replace")
        self.horizontalLayout_re_custom.addWidget(self.lineEdit_re_replace)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 150, 361, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_custom_reading = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_custom_reading.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_custom_reading.setObjectName("horizontalLayout_custom_reading")
        self.label_custom_reading = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_custom_reading.setObjectName("label_custom_reading")
        self.horizontalLayout_custom_reading.addWidget(self.label_custom_reading)
        self.lineEdit_custom_reading = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_custom_reading.setObjectName("lineEdit_custom_reading")
        self.horizontalLayout_custom_reading.addWidget(self.lineEdit_custom_reading)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label.setObjectName("label")
        self.horizontalLayout_custom_reading.addWidget(self.label)
        self.lineEdit_custom_pitch = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_custom_pitch.setObjectName("lineEdit_custom_pitch")
        self.horizontalLayout_custom_reading.addWidget(self.lineEdit_custom_pitch)
        self.pushButton_custom_pa_reading = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_custom_pa_reading.setObjectName("pushButton_custom_pa_reading")
        self.horizontalLayout_custom_reading.addWidget(self.pushButton_custom_pa_reading)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_check_mode = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_check_mode.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_check_mode.setObjectName("horizontalLayout_check_mode")
        self.radioButton_Current = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Current.setChecked(True)
        self.radioButton_Current.setObjectName("radioButton_Current")
        self.horizontalLayout_check_mode.addWidget(self.radioButton_Current)
        self.radioButton_last_added = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_last_added.setObjectName("radioButton_last_added")
        self.horizontalLayout_check_mode.addWidget(self.radioButton_last_added)
        self.lineEdit_read_note = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_read_note.setReadOnly(True)
        self.lineEdit_read_note.setObjectName("lineEdit_read_note")
        self.horizontalLayout_check_mode.addWidget(self.lineEdit_read_note)
        self.pushButton_get_note = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_get_note.setObjectName("pushButton_get_note")
        self.horizontalLayout_check_mode.addWidget(self.pushButton_get_note)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 120, 361, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_rtk_keywords = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_rtk_keywords.setChecked(False)
        self.pushButton_rtk_keywords.setObjectName("pushButton_rtk_keywords")
        self.horizontalLayout.addWidget(self.pushButton_rtk_keywords)
        self.pushButton_pos = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_pos.setEnabled(False)
        self.pushButton_pos.setCheckable(True)
        self.pushButton_pos.setObjectName("pushButton_pos")
        self.horizontalLayout.addWidget(self.pushButton_pos)
        AddonWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddonWindow)
        self.dict_tabs.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(AddonWindow)

    def retranslateUi(self, AddonWindow):
        _translate = QtCore.QCoreApplication.translate
        AddonWindow.setWindowTitle(_translate("AddonWindow", "MainWindow"))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_1), _translate("AddonWindow", "Dict 1"))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_2), _translate("AddonWindow", "Dict 2"))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_3), _translate("AddonWindow", "Dict 3"))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_4), _translate("AddonWindow", "Dict 4"))
        self.dict_tabs.setTabText(self.dict_tabs.indexOf(self.res_tab_5), _translate("AddonWindow", "Pitch Accent"))
        self.checkBox_re_sentences.setText(_translate("AddonWindow", "Remove 「　」"))
        self.checkBox_re_parenthesis_jp.setText(_translate("AddonWindow", "Remove （　）"))
        self.checkBox_re_parenthesis_std.setText(_translate("AddonWindow", "Remove ( )"))
        self.checkBox_re_custom.setText(_translate("AddonWindow", "Custom"))
        self.radioButton_Overwrite.setText(_translate("AddonWindow", "Overwrite"))
        self.radioButton_add.setText(_translate("AddonWindow", "Add"))
        self.label_re_find.setText(_translate("AddonWindow", "Find"))
        self.label_re_replace.setText(_translate("AddonWindow", "Replace"))
        self.label_custom_reading.setText(_translate("AddonWindow", "Reading"))
        self.label.setText(_translate("AddonWindow", "Pitch Accent"))
        self.pushButton_custom_pa_reading.setText(_translate("AddonWindow", "Add Custom"))
        self.radioButton_Current.setText(_translate("AddonWindow", "Current"))
        self.radioButton_last_added.setText(_translate("AddonWindow", "Last Added"))
        self.lineEdit_read_note.setText(_translate("AddonWindow", "Focus Field"))
        self.pushButton_get_note.setText(_translate("AddonWindow", "Get Note"))
        self.pushButton_rtk_keywords.setText(_translate("AddonWindow", "RTK Keywords"))
        self.pushButton_pos.setText(_translate("AddonWindow", "Part Of Speech"))