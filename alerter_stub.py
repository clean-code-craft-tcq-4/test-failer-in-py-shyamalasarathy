Threshold_Celcius = 150

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius <= Threshold_Celcius:
        return 200  #Return 200 for OK
    elif celcius > Threshold_Celcius:
        return 500  #Return 500 for NOT-OK
