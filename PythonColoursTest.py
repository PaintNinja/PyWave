VerFloat = str(0.10) # We need to convert it to a string here otherwise Python will not allow us to use this float with strings in a print command
Version = 'Pre-Alpha v' + VerFloat
Title = 'PyWave ' + Version

print(Title)
print('''
Notice: This is a highly experimental, stipped down version of Wave made from scratch in Python. Expect a lot of bugs and missing features.
''')

from colorama import init
init(autoreset=True)
# Those two lines of code are required for console colours to work multi-platform, however the IDLE IDE still does not support colours
# The autoreset=True within the init is so that the colours don't persist in following prints, so that I don't need to manually reset the colours back to normal after printing a warning line in yellow for example

from colorama import Fore # Needed to change foreground colours of the console
print(Fore.GREEN + 'Success!') # The colour name must be fully capitalised in order to work

from colorama import Back # Needed to change background colours
print(Fore.WHITE + Back.RED + 'DANGER!')

# Colorama's 'style' feature doesn't work on Windows and is therefore not documented here
