# $language = "Python"
# $interface = "1.0"


def TextTest1():
    crt.CommandWindow.Text = "ls -l \r\npwd\r\n whoami"  

def SendToAllSessionsTest1():
    crt.CommandWindow.Text = "ls -l \r\npwd\r\n whoami"
    crt.CommandWindow.SendToAllSessions = True


def SendCharactersImmediatelyTest1():
    crt.CommandWindow.SendCharactersImmediately = True

def SendTest1():
    crt.CommandWindow.Text = "ls -l \r\npwd\r\n whoami"
    crt.CommandWindow.Send()



SendCharactersImmediatelyTest1()
