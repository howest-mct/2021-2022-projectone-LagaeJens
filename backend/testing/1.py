from classen.bcd_classe import BCD
import time

test=BCD()

try:
    test.setup()
    while True:
       test.main()
       time.sleep(1)
        
        
except Exception as e:
    print(e)
    
    
finally:
    print("finally")