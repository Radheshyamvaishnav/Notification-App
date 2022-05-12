import time
from plyer import notification

if __name__ == '__main__':
 	while True:
         
         notification.notify(
 			title = "Please Drink Water Now !!",
 			message ="Success !!",
			app_icon = r'icon.ico',
            timeout= 7,
			app_name = "Time to get hyderated !!",
            )
         time.sleep(60*45)
		#pyinstaller -F -w  --onefile --windowed --icon=icon.ico Time_To_Get_Hyderated.py --hidden-import plyer.platforms.win.notification