# Definition-Helper-Anki-Addon
An addon that I made for helping me with my japanese cards

It was designed around my own personal cards, so adjustments will most likely be needed if you want to use it.

In the __init__.py file, you'll find these variables:

focus_field = 'Focus'  (this is the field the addon will read to use as base for the search)

target_jp_field = 'Def Jp'  (this is the field in which the addon will write the japanese definition into)

target_en_field = 'Def En'  (this is the field in which the addon will write the english definition into)

You can set them to fit your own cards. Remember to let the field name inside the single quotation makrs

There are four areas in the addon. Fetch Options, Current, Results.

In Fetch Options, you'll type a search filter (def. is "added:1" which will list all the new notes added today). When you press the button "Run" it will get the list of cards for that filter and get the last one in the list (which should be the newst added, with default settings). Then it will search the dictionaries and plot the results for you to click and it will add it to the card. 

In Current, you'll choose if you wish to overwrite the Target field or just add to whatever's already there. When you click "Get", the addon will get the info from the card that you are CURRENTLY viewing in the reviewer, and plot the definitions. Once you choose one, it'll recalculate the reviewer. Note that sometimes it will come back into a different card, but the changes will be applied correctly.

In regex you can choose to apply regular expression to the text from the definition when adding it to a card. The first field is for what you want to replace, and the second one for the replacement. The default settings searches for everything inside 「 」and removes it (replaces it with nothing). The reason for that is that personally I usually prefer not to have the sentence examples from the japanese dictionaries, since I already have example sentences in my cards.
Remember if you want to use regex somethign else, you have to remember to use '\' before special characters like '('.

In Results, you see three tabs in which the results for each dictionary will be ploted.

NOTE: The Dictionary files are NOT provided, you'll have to set them manually. (As of 12/06/2020, added support to the JMEdict)

To set up the dictionaries, you'll need to provide the path for the folder in which the dictionaries will be on in the variable "dict_folder_path" (ex. dict_folder_path = "D:\\Japanese\\Dictionaries\\"  *with two slashes* )

Inside that folder you'll need to create a new folder for each dictionary and put all the json files in there. 

Update each variable in __init__.py with the name of each dictionary. (ex. dict_1 = "大辞林", dict_2 = "広辞苑", dict_3 = "新明解", dict_4 = "jmdict_english")

You should than be good to go.

When in anki, go to TOOLS, and there should be a new option "Definition Updater". Just click it and the window will open.

Note that it is basically a personal project, by someone who is not particularly good at coding. It can give some errors if you missuse the addon (like using a non valid filter in the Fetch setting) but it shouldn't cause any harm in your anki. Don't expect consistent (if any) updates or proper support. I'll try to help if you find any problems or any suggestions if I have the time.

If you actually want to use it, remember it is provided "As is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

To install, copy the Definition folder into your anki2\addons21 folder (you can go in anki -> tools -> add-ons -> view files), make necessary changes in __init.py__ with any text editor and restart anki.
