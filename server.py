import eel

# initial and Start project
eel.init('web')



@eel.expose
def testFunc(Name):
    print(Name)

eel.start('main.html', size=(400, 400))

