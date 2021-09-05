# $language = "Python"
# $interface = "1.0"
import SecureCRT


def LocalAddressTest1():
#    config = crt.Session.Config
    address = crt.Session.LocalAddress
    crt.Dialog.MessageBox( address )
    
def PathTest1():
#    config = crt.Session.Config
    filenamepath = crt.Session.Path
    crt.Dialog.MessageBox( filenamepath )

def ConnectTest1():
    errcode = 0
    try:
       crt.Session.Connect("/SSH2 /PASSWORD Test123455  root@10.10.0.1", True)
    except ScriptError:
       errcode = crt.GetLastError()
    if errcode != 0:
       crt.Dialog.MessageBox("Connection Failed")
    else:
       crt.Dialog.MessageBox("Connection Successful")
   

PathTest1()