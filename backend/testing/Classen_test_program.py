from classen.bcd_classe import BCD
from classen.dungeons import dungeons
from time import sleep

test=BCD()
dungeon = dungeons()
try:
    test.setup()
    while True:
        dungeon.dungeons_main()
        # test.main()
        sleep(1)
        
        
        
except Exception as e:
    print(e)
    
    
finally:
    print("finally")