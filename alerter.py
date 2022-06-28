import alerter_stub

alert_failure_count = 0

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = alerter_stub.network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1

alert_in_celcius(100.0)
assert(alert_failure_count == 0)
alert_in_celcius(400.5)
alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')
#Test to find error in counting when result in Not ok
assert(alert_failure_count != 0)
print('All is well (maybe!)')
