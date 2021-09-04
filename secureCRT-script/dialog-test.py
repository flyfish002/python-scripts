# $language = "Python"
# $interface = "1.0"

def MessageBoxTest1():
    crt.Dialog.MessageBox("this is messagebox test")              

#*******************************************************************************************************
def MessageBoxTest2():
    result = crt.Dialog.MessageBox("Login Failed, Retry?", "Error", ICON_QUESTION | BUTTON_YESNO | DEFBUTTON2 )     
    if result == IDNO:
       return  

#图标类型
"""
ICON_STOP = 16                 # display the ERROR/STOP icon.
ICON_QUESTION = 32             # display the '?' icon
ICON_WARN = 48                 # display a '!' icon.
ICON_INFO= 64                  # displays "info" icon.
"""
#按钮类型
"""
BUTTON_OK = 0                  # OK button only
BUTTON_CANCEL = 1              # OK and Cancel buttons
BUTTON_ABORTRETRYIGNORE = 2    # Abort, Retry, and Ignore buttons
BUTTON_YESNOCANCEL = 3         # Yes, No, and Cancel buttons
BUTTON_YESNO = 4               # Yes and No buttons
BUTTON_RETRYCANCEL = 5         # Retry and Cancel buttons
"""
#选中默认值
"""
DEFBUTTON1 = 0        # First button is default
DEFBUTTON2 = 256      # Second button is default
DEFBUTTON3 = 512      # Third button is default
"""
#返回值类型
"""
IDOK = 1              # OK button clicked
IDCANCEL = 2          # Cancel button clicked
IDABORT = 3           # Abort button clicked
IDRETRY = 4           # Retry button clicked
IDIGNORE = 5          # Ignore button clicked
IDYES = 6             # Yes button clicked
IDNO = 7              # No button clicked
"""

#************************************************************************************************************
def PromptTest1():
    password = crt.Dialog.Prompt("Enter your password:", "Logon Script", "", True)
    crt.Dialog.MessageBox( password )

#********************************************************************************************************
def FileOpenDialogTest1():
    AbsPathFile1 = crt.Dialog.FileOpenDialog( title="Please selcet a file")
    crt.Dialog.MessageBox( AbsPathFile1 ) 

def FileOpenDialogTest2():
    AbsPathFile2 = crt.Dialog.FileOpenDialog(title="Please selcet a text file", filter="Text Files (*.txt)|*.txt||" )



FileOpenDialogTest2()