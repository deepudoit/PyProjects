import webbrowser, sys, pyperclip

mos_url = 'https://support.us.oracle.com/oip/faces/secure/srm/srview/SRTechnical.jspx?srNumber='
if len(sys.argv) > 1:
    sr = sys.argv[1]
else:
    sr = pyperclip.paste()

webbrowser.open(mos_url + sr)
