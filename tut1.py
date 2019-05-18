import eel

eel.init('web', allowed_extensions=['.js', '.html'])
eel.init('static_web_folder')
eel.start('SCPI.html')