Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c myscript.bat"
oShell.Run strArgs, 0, false