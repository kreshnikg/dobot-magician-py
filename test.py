from Dobot import Dobot
import time

dbt = Dobot(220, 0, -6.5)

dbt.moveXY(120, 20)

dbt.toggleSuction()
time.sleep(2)
dbt.toggleSuction()
