import time
from plyer import notification

if __name__ == "__main__" :

   
        notification.notify(

            title = " Drink Water Now !",
            message =   """ Engineering, and Medicine determined that an adequate daily 
                        fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for
                        men. About 11.5 cups (2.7 liters) of fluids a day for women """,
            app_icon = "D:\Python Practice\Drinkingwater_reminder\water.ico",
            timeout = 10 ## it run for ten sec and then disappear

        )
        time.sleep(60) ## Notification will be reappear after every 60 seconds
