#%%
import webbrowser
import subprocess
from wilty import mainfunc

# %%
for x in range(1, 10):
    mainfunc(12, x, 101+x)
    strURL = f"https://wilty.fandom.com/wiki/Series_12,_Episode_{x}?action=edit"
    webbrowser.open(strURL, new=0)
    subprocess.call(["C:/Users/Ayoola_PC/Documents/PythonScripts/other/webactions.exe", "webactions.ahk"])

 
# %%
