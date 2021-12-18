import darkdetect

darkdetect.theme()
'Dark'
if darkdetect.isDark():
	print('THE SYSTEM IS IN DARK MODE')
elif darkdetect.isLight():
	print('THE SYSTEM IS IN LIGHT MODE')
