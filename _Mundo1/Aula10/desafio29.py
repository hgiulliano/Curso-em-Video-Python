speed = float(input('How fast you were going?: '))
if speed > 80:
    value = (speed-80)*7
    print(f'You got a traffic ticket, because you were driving above 80km/h, the money you need to pay is : {value:.2f} ')
else:
    print('Good bro, continue driving safely')