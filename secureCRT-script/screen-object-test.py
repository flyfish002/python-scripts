# $language = "Python"
# $interface = "1.0"

def WaitForStringTest1():
    result = crt.Screen.WaitForStrings(["foo", "bar", "quux", "gee"], 10)
    crt.Dialog.MessageBox( str(result) )
    if (result == 3):
       crt.Dialog.MessageBox("Got quux!")
    if (result == 0):
       crt.Dialog.MessageBox("Timed out!")

def ReadStringTest1():
    char = crt.Screen.ReadString()
    crt.Dialog.MessageBox( char )     
    
def ReadStringTest2():
    str = crt.Screen.ReadString("home", 10)
    crt.Dialog.MessageBox( str ) 


ReadStringTest2( )