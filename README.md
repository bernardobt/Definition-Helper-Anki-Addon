# Definition-Helper-Anki-Addon
An addon that I made for helping me with my japanese cards

It was designed around my own personal cards, so adjustments will most likely be needed if you want to use it.

In the __init__.py file, you'll find these variables:

focus_field = 'Focus'  (this is the field the addon will read to use as base for the search)

target_jp_field = 'Def Jp'  (this is the field in which the addon will write into)

You can set them to fit your own cards. Remember to let the field name inside the single quotation makrs (ex. 'YOUR_FIELD' )

There are three areas in the addon. Fetch Options, Current, Results.

In Fetch Options, you'll type a search filter (def. is "added:1" which will list all the new notes added today). When you press the button "Run" it will get the list of cards for that filter and get the last one in the list (which should be the newst added, with default settings). Then it will search the dictionaries and plot the results for you to click and it will add it to the card. 

In Current, you'll choose if you wish to overwrite the Target field or jsut add to waht whatever's already there. When you click "Get", the addon will get the info form the card that you are CURRENTLY viewing in the reviewer, and plot the definitions. Once you choose one, it'll recalculate the reviewer. Note that sometimes it will come back into a different card, but the changes will be applied correctly.

In Results, you see three tabs in which the results for each dictionary will be ploted.

NOTE: The Dictionary files ARE NOT provided, you'll have to set them manually and currently it DOES NOT WORK with Jmdict_English. It was designed with Japanese dictionaries in mind. The files are the same are Yomichan uses.

To set up the dictionaries, you'll need to provide the path for the folder in which the dictionaries will be on in the variable "dict_folder_path" (ex. dict_folder_path = "D:\\Japanese\\Dictionaries\\" )

Inside that folder you'll need to create a new folder for each dictionary and put all the json files in there. 

Update each variable in __init__.py with the name of each dictionary. (ex. dict_1 = "大辞林", dict_2 = "広辞苑", dict_3 = "新明解")

You should than be good to go.

When in anki, go to TOOLS, and there should be a new option "Definition Updater". Just click it and the window will open.

Note that it is basically a personal project, by someone who is not particularly good at coding. It can give some errors if you missuse the addon (like using a non valid filter in the Fetch setting) but it shouldn't cause any harm in your anki. Don't expect consistent (if any) updates or proper support. I'll try to help if you find any problems or any suggestions if I have the time.

If you actually want to use it, remember it is provided "As is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
