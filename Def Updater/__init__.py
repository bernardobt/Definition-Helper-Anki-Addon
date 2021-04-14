import re, json, csv
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from .main_ui import *
from textwrap import wrap
from aqt.main import ResetReason


class def_helper_2(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_AddonWindow()
        self.ui.setupUi(self)

        config = mw.addonManager.getConfig(__name__)

        # Config Setup
        self.focus_field = config['focus_field']
        self.target_jp_field = config['target_jp_field']
        self.target_en_field = config['target_en_field']
        self.target_deck = config['target_deck']
        self.target_pitch_field = config['target_pitch_field']
        self.target_rtk_field = config['target_rtk_field']
        self.target_readingfocus_field = config['target_readingfocus_field']
        self.parts_of_speech_field = config['parts_of_speech_field']

        self.results_font_jp = "Meiryo"
        self.font_size_jp = 11
        self.set_wrap_jp = 21

        self.results_font_en = "Meiryo"
        self.font_size_en = 11
        self.set_wrap_en = 42

        dict_1 = config['dict_1']
        dict_2 = config['dict_2']
        dict_3 = config['dict_3']
        dict_4 = config['dict_4']

        # Dictionaries folder location
        dict_folder_path = config['dict_folder_path']
        dict_path = [dict_folder_path + dict_1,
                     dict_folder_path + dict_2,
                     dict_folder_path + dict_3,
                     dict_folder_path + dict_4]

        self.ui.dict_tabs.setTabText(0, dict_1)
        self.ui.dict_tabs.setTabText(1, dict_2)
        self.ui.dict_tabs.setTabText(2, dict_3)
        self.ui.dict_tabs.setTabText(3, dict_4)


        self.dictionaries_list = self.load_multi_dict(dict_path)

        # Pitch accent data location
        self.accent_list_tsv = config['accent_list_tsv']

        # RTK Keyword list
        self.rtk_list_csv = config['rtk_list_csv']

        #Get Note Button Config
        self.ui.pushButton_get_note.clicked.connect(self.check_get_note_push_button)

        # Get Note Button Config
        self.ui.pushButton_rtk_keywords.clicked.connect(self.rtk_keywords)

    def check_get_note_push_button(self):
        if self.ui.radioButton_Current.isChecked():
            self.get_current_gui(self.dictionaries_list)
        elif self.ui.radioButton_last_added.isChecked():
            self.run_clicked("added:1")

    def run_clicked(self, qry_txt):
        self.get_query_last(qry_txt, self.dictionaries_list)

    def get_current_gui(self, dict_list):
        tab = [self.ui.verticalLayout_2, self.ui.verticalLayout_3, self.ui.verticalLayout_4, self.ui.verticalLayout_5,
               self.ui.verticalLayout_6]
        scroll_area = [self.ui.dict_1_tab_scroll_area, self.ui.dict_2_tab_scroll_area, self.ui.dict_3_tab_scroll_area,
                       self.ui.dict_4_tab_scroll_area, self.ui.dict_5_tab_scroll_area]
        rev = mw.reviewer.card
        try:
            noteid = rev.nid
        except:
            showInfo("You must open the reviewer")
            return
        try:
            note = mw.col.getNote(noteid)
        except:
            showInfo("Couldn't find Note Info")
            return

        if note[self.focus_field]:
            self.ui.lineEdit_read_note.setText(f"{note[self.focus_field]}")
            # Plots the dictionary tabs
            for i, dict in enumerate(dict_list):
                if i == 3:
                    result = self.jmedict_query_dict(dict, note[self.focus_field])
                    self.plot_results_gui(result, note, scroll_area[i], tab[i], self.results_font_en, self.font_size_en,
                                          self.set_wrap_en, self.target_en_field)
                else:
                    result = self.query_dict(dict, note[self.focus_field])
                    self.plot_results_gui(result, note, scroll_area[i], tab[i], self.results_font_jp, self.font_size_jp,
                                          self.set_wrap_jp, self.target_jp_field)
            # Plot the utils tab
            self.plot_utils(self.ui.dict_5_tab_scroll_area, self.ui.verticalLayout_6, self.results_font_jp,
                             self.font_size_jp, noteid)
        else:
            showInfo(f"Nothing in the {self.focus_field} field")

    def get_query_last(self, query_filter, dict_list):
        tab = [self.ui.verticalLayout_2, self.ui.verticalLayout_3, self.ui.verticalLayout_4, self.ui.verticalLayout_5,
               self.ui.verticalLayout_6]
        scroll_area = [self.ui.dict_1_tab_scroll_area, self.ui.dict_2_tab_scroll_area, self.ui.dict_3_tab_scroll_area,
                       self.ui.dict_4_tab_scroll_area, self.ui.dict_5_tab_scroll_area]
        ids = mw.col.find_notes(query_filter)
        note = mw.col.getNote(ids[-1])
        self.ui.lineEdit_read_note.setText(f"{note[self.focus_field]}")
        for i, dict in enumerate(dict_list):
            if i == 3:
                result = self.jmedict_query_dict(dict, note[self.focus_field])
                self.plot_results(result, note, scroll_area[i], tab[i], self.results_font_en, self.font_size_en,
                                  self.set_wrap_en, self.target_en_field)
            else:
                result = self.query_dict(dict, note[self.focus_field])
                self.plot_results(result, note, scroll_area[i], tab[i], self.results_font_jp, self.font_size_jp,
                                  self.set_wrap_jp, self.target_jp_field)
        # Plot the utils tab
        self.plot_utils(self.ui.dict_5_tab_scroll_area, self.ui.verticalLayout_6, self.results_font_jp,
                        self.font_size_jp, ids[-1])

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
        regex_content = content
        if self.ui.checkBox_re_sentences.isChecked():
            regex_content = re.sub("(?:(BEGIN:)|(\「)).*?(?(1):END)(?(2)\」)", "", regex_content)
        if self.ui.checkBox_re_parenthesis_jp.isChecked():
            regex_content = re.sub("(?:(BEGIN:)|(\（)).*?(?(1):END)(?(2)\）)", "", regex_content)
        if self.ui.checkBox_re_parenthesis_std.isChecked():
            regex_content = re.sub("(?:(BEGIN:)|(\()).*?(?(1):END)(?(2)\))", "", regex_content)
        if self.ui.checkBox_re_custom.isChecked():
            regex_content = re.sub(f"{self.ui.lineEdit_re_find.text()}", f"{self.ui.lineEdit_re_replace.text()}", regex_content)
        if self.ui.radioButton_Overwrite.isChecked():
            note_id[target_field] = regex_content
            note_id.flush()
        elif self.ui.radioButton_add.isChecked():
            note_id[target_field] += f"<br>{regex_content}"
            note_id.flush()

    def update_note_gui(self, note_id, content, target_field):
        regex_content = content
        if self.ui.checkBox_re_sentences.isChecked():
            regex_content = re.sub("(?:(BEGIN:)|(\「)).*?(?(1):END)(?(2)\」)", "", regex_content)
        if self.ui.checkBox_re_parenthesis_jp.isChecked():
            regex_content = re.sub("(?:(BEGIN:)|(\（)).*?(?(1):END)(?(2)\）)", "", regex_content)
        if self.ui.checkBox_re_parenthesis_std.isChecked():
            regex_content = re.sub("(?:(BEGIN:)|(\()).*?(?(1):END)(?(2)\))", "", regex_content)
        if self.ui.checkBox_re_custom.isChecked():
            regex_content = re.sub(f"{self.ui.lineEdit_re_find.text()}", f"{self.ui.lineEdit_re_replace.text()}", regex_content)
        if self.ui.radioButton_Overwrite.isChecked():
            note_id[target_field] = regex_content
            note_id.flush()
        elif self.ui.radioButton_add.isChecked():
            note_id[target_field] += f"<br>{regex_content}"
            note_id.flush()
        mw.requireReset(reason=ResetReason.EditCurrentInit, context=self)
        mw.delayedMaybeReset()

    def update_utils_gui(self, nid, reading, pitch, target_reading, target_pitch, pitch_number):
        note = mw.col.getNote(nid)
        if self.ui.radioButton_Overwrite.isChecked():
            note[target_reading] = reading
            note[target_pitch] = f"{pitch} ({pitch_number})"
            note.flush()
        mw.requireReset(reason=ResetReason.EditCurrentInit, context=self)
        mw.delayedMaybeReset()

    def rtk_keywords(self):
        rev = mw.reviewer.card
        try:
            noteid = rev.nid
        except:
            showInfo("You must open the reviewer")
            return
        try:
            note = mw.col.getNote(noteid)
        except:
            showInfo("Couldn't find Note Info")
            return
        if note[self.focus_field]:
            keywords_res = self.query_rtk_list(note[self.focus_field])
            note[self.target_rtk_field] = keywords_res
            note.flush()
            mw.requireReset(reason=ResetReason.EditCurrentInit, context=self)
            mw.delayedMaybeReset()
        else:
            showInfo(f"Nothing in the {self.focus_field} field")

    def plot_utils(self, which_scroll, which_layout, results_font, font_size, note_id):
        self.clearLayout(which_layout)
        note = mw.col.getNote(note_id)
        pitch_res = ""

        word_list = self.find_words(note[self.focus_field])  # Find matches in the accent list
        pitch_res = self.search_pitch(word_list)
        if pitch_res != "":
            for result in pitch_res:
                pitch_string = "・".join(result[3])
                pitch_number_string = "・".join(result[2])
                self.parse_res_button = QtWidgets.QPushButton(which_scroll)
                self.parse_res_button.setObjectName("pushButton")
                self.parse_res_button.setFont(QFont(results_font, font_size))
                self.parse_res_button.setText(f"{result[0]}\n"
                                              f"Reading: {result[1]}\n"
                                              f"Pitch Accent: {pitch_number_string}")
                which_layout.addWidget(self.parse_res_button)
                self.parse_res_button.clicked.connect(
                    lambda ch, result=result, pitch_string=pitch_string, pitch_number_string=pitch_number_string  : self.update_utils_gui(note_id, result[1], pitch_string,
                                                                        self.target_readingfocus_field,
                                                                        self.target_pitch_field, pitch_number_string))



    # # thanks to http://olsgaard.dk/hiragana-katakana-transliteration-in-4-lines-of-python.html
    # def kana_convert(self, text):
    #     katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
    #     hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
    #     # hir2kat = str.maketrans(hiragana_chart, katakana_chart)
    #     kat2hir = str.maketrans(katakana_chart, hiragana_chart)
    #     return text.translate(kat2hir)


    def find_words(self, query):
        with open(self.accent_list_tsv, "r", encoding="utf-8") as f:
            next(f)
            reader = csv.reader(f, delimiter="\t")
            words_list = []
            for line in reader:
                if line[0] == query:
                    line[2] = re.sub("\(.\)", "", line[2])
                    words_list.append(line)
            return words_list

    def search_pitch(self, entry_list):
        return_final_results = []
        for line in entry_list:
            final_results = []
            pitch_list = line[2].split(",")
            small_table = ['ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ',
                           'ゃ', 'ゅ', 'ょ',
                           'ァ', 'ィ', 'ゥ', 'ェ', 'ォ',
                           'ャ', 'ュ', 'ョ']
            if line[1]:
                kana_list = list(line[1])
                for i, char in enumerate(kana_list):
                    if char in small_table:
                        kana_list[i - 1] += char
                        del kana_list[i]
            else:
                kana_list = list(line[0])
                for i, char in enumerate(kana_list):
                    if char in small_table:
                        kana_list[i - 1] += char
                        del kana_list[i]
            pitch_result_list = []
            for i, pitch in enumerate(pitch_list):
                pitch_css_list = []
                if pitch == "0":
                    result = []
                    result_string = ""
                    for kana in kana_list:
                        formated = f'<span class = "H">{kana}</span>'
                        result.append(formated)
                    result[0] = f'<span class = "LH">{kana_list[0]}</span>'
                    result_string += "".join(result)
                    pitch_css_list = result_string
                elif pitch == "1":
                    result = []
                    result_string = ""
                    for kana in kana_list:
                        formated = f'<span class = "L">{kana}</span>'
                        result.append(formated)
                    result[0] = f'<span class = "HL">{kana_list[0]}</span>'
                    result_string += "".join(result)
                    pitch_css_list = result_string
                elif pitch == "2":
                    result = []
                    result_string = ""
                    for kana in kana_list:
                        formated = f'<span class = "L">{kana}</span>'
                        result.append(formated)
                    result[0] = f'<span class = "LH">{kana_list[0]}</span>'
                    result[1] = f'<span class = "HL">{kana_list[1]}</span>'
                    result_string += "".join(result)
                    pitch_css_list = result_string
                elif pitch == "3":
                    result = []
                    result_string = ""
                    for kana in kana_list:
                        formated = f'<span class = "L">{kana}</span>'
                        result.append(formated)
                    result[0] = f'<span class = "LH">{kana_list[0]}</span>'
                    result[1] = f'<span class = "H">{kana_list[1]}</span>'
                    result[2] = f'<span class = "HL">{kana_list[2]}</span>'
                    result_string += "".join(result)
                    pitch_css_list = result_string
                elif pitch == "4":
                    result = []
                    result_string = ""
                    for kana in kana_list:
                        formated = f'<span class = "L">{kana}</span>'
                        result.append(formated)
                    result[0] = f'<span class = "LH">{kana_list[0]}</span>'
                    result[1] = f'<span class = "H">{kana_list[1]}</span>'
                    result[2] = f'<span class = "H">{kana_list[2]}</span>'
                    result[3] = f'<span class = "HL">{kana_list[3]}</span>'
                    result_string += "".join(result)
                    pitch_css_list = result_string
                elif pitch == "5":
                    result = []
                    result_string = ""
                    for kana in kana_list:
                        formated = f'<span class = "L">{kana}</span>'
                        result.append(formated)
                    result[0] = f'<span class = "LH">{kana_list[0]}</span>'
                    result[1] = f'<span class = "H">{kana_list[1]}</span>'
                    result[2] = f'<span class = "H">{kana_list[2]}</span>'
                    result[3] = f'<span class = "H">{kana_list[3]}</span>'
                    result[4] = f'<span class = "HL">{kana_list[4]}</span>'
                    result_string += "".join(result)
                    pitch_css_list = result_string
                elif pitch == "6":
                    result = []
                    result_string = ""
                    for kana in kana_list:
                        formated = f'<span class = "L">{kana}</span>'
                        result.append(formated)
                    result[0] = f'<span class = "LH">{kana_list[0]}</span>'
                    result[1] = f'<span class = "H">{kana_list[1]}</span>'
                    result[2] = f'<span class = "H">{kana_list[2]}</span>'
                    result[3] = f'<span class = "H">{kana_list[3]}</span>'
                    result[4] = f'<span class = "H">{kana_list[4]}</span>'
                    result[5] = f'<span class = "HL">{kana_list[5]}</span>'
                    result_string += "".join(result)
                    pitch_css_list = result_string
                pitch_result_list.append(pitch_css_list)
            final_results.append(line[0])
            final_results.append(line[1])
            final_results.append(pitch_list)
            final_results.append(pitch_result_list)
            return_final_results.append(final_results)
        return return_final_results


    def query_rtk_list(self, word):
        word_list = list(word)
        result = []
        furigana_output = ""
        for char in word_list:
            res = self.search_rtk_kanji(char)
            result.append(res)
            furigana_output += f"<ruby><rb>{char}<rt>{res}</ruby> "
        return furigana_output

    def search_rtk_kanji(self, get_query):
        with open(self.rtk_list_csv, "r", encoding="utf-8") as f:
            next(f)
            reader = csv.reader(f)
            for line in reader:
                if line[0] == get_query:
                    return line[4].capitalize()
            else:
                return " "

def setup_ui():
    mw.myWidget = AddonWindow = QtWidgets.QMainWindow()
    AddonWindow.setObjectName("Jp Def Addon")
    widget = def_helper_2(AddonWindow)
    widget.show()


# create a new menu item, "test"
action = QAction("Jp Def Addon", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(setup_ui)
# and add it to the tools menu
mw.form.menuTools.addAction(action)