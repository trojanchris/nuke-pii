# nuke-pii
Easy one click tool so our employees can remove downloaded customer pii

Mini GUI application written in python, using the WxPython library to create visual elements and pyinstaller for packaging into an executable.

Provides checkboxes to clear the following locations:
* Documents
* Pictures
* Desktop
* Downloads
* Temp

Removes all files and folders in selected directories **_except for_** those files/directories beginning with an underscore. The intention is that they will mark files they want to be persistent (hopefully not more PII) with the underscore and remove the rest.
