
sridevi_day = ''
sridevi_day_op_time = ''
sridevi_day_cl_time = ''

time_bazar = ''
time_bazar_op_time = ''
time_bazar_cl_time = ''

madhur_day = ''
madhur_day_op_time = ''
madhur_day_cl_time = ''

milan_day = ''
milan_day_op_time = ''
milan_day_cl_time = ''

raj_day = ''
raj_day_op_time = ''
raj_day_cl_time = ''

suprem_day = ''
suprem_day_op_time = ''
suprem_day_cl_time = ''

kalyan_day = ''
kalyan_day_op_time = ''
kalyan_day_cl_time = ''

sridevi_night = ''
sridevi_night_op_time = ''
sridevi_night_cl_time = ''

madhur_night = ''
madhur_night_op_time = ''
madhur_night_cl_time = ''

suprem_night = ''
suprem_night_op_time = ''
suprem_night_cl_time = ''

milan_night = ''
milan_night_op_time = ''
milan_night_cl_time = ''

raj_night = ''
raj_night_op_time = ''
raj_night_cl_time = ''

kalyan_night = ''
kalyan_night_op_time = ''
kalyan_night_cl_time = ''

main_bazar = ''
main_bazar_op_time = ''
main_bazar_cl_time = ''

def update_date():
    global sridevi_day_op_time 
    global sridevi_day_cl_time
    global time_bazar_op_time
    global time_bazar_cl_time
    global madhur_day_op_time
    global madhur_day_cl_time 
    global milan_day_op_time
    global milan_day_cl_time
    global raj_day_op_time
    global raj_day_cl_time
    global suprem_day_op_time
    global suprem_day_cl_time
    global kalyan_day_op_time
    global kalyan_day_cl_time
    global sridevi_night_op_time
    global sridevi_night_cl_time
    global madhur_night_op_time
    global madhur_night_cl_time
    global suprem_night_op_time
    global suprem_night_cl_time
    global milan_night_op_time
    global milan_night_cl_time
    global raj_night_op_time
    global raj_night_cl_time
    global kalyan_night_op_time
    global kalyan_night_cl_time
    global main_bazar_op_time
    global main_bazar_cl_time
    
    sridevi_day_op_time = '11:50 AM'
    sridevi_day_cl_time = '12:50 PM'
    time_bazar_op_time = '01:00 PM'
    time_bazar_cl_time = '03:15 PM'
    madhur_day_op_time = '01:30 PM'
    madhur_day_cl_time = '02:30 PM'
    milan_day_op_time = '02:15 PM'
    milan_day_cl_time = '04:15 PM'
    raj_day_op_time = '03:15 PM'
    raj_day_cl_time = '05:15 PM'
    suprem_day_op_time = '03:40 PM'
    suprem_day_cl_time = '05:40 PM'
    kalyan_day_op_time = '04:55 PM'
    kalyan_day_cl_time = '06:55 PM'
    sridevi_night_op_time = '07:10 PM'
    sridevi_night_cl_time = '08:10 PM'
    madhur_night_op_time = '08:40 PM'
    madhur_night_cl_time = '10:40 PM'
    suprem_night_op_time = '08:50 PM'
    suprem_night_cl_time = '10:50 PM'
    milan_night_op_time = '09:00 PM'
    milan_night_cl_time = '11:00 PM'
    raj_night_op_time = '09:35 PM'
    raj_night_cl_time = '11:45 PM'
    kalyan_night_op_time = '09:45 PM'
    kalyan_night_cl_time = '11:45 PM'
    main_bazar_op_time = '09:48 PM'
    main_bazar_cl_time = '12:10 AM'
    
def update_result():
    global sridevi_day
    global time_bazar
    global madhur_day
    global milan_day
    global raj_day
    global suprem_day
    global kalyan_day
    global sridevi_night
    global madhur_night
    global suprem_night
    global milan_night
    global raj_night
    global kalyan_night
    global main_bazar

    sridevi_day = '128-12-200'
    time_bazar = '158-46-178'
    madhur_day = '569-01-100'
    milan_day = '235-02-237'
    raj_day = '179-70-479'
    suprem_day = '347-48-260'
    kalyan_day = '249-54-789'
    sridevi_night = '470-18-350'
    madhur_night = '367-63-148'
    suprem_night = '689-31-560'
    milan_night = '112-43-490'
    raj_night = '225-96-457'
    kalyan_night = '114-60-668'
    main_bazar = '366-51-245'


def update_data():
    update_date()
    update_result()
    data = {
        'sridevi_day' : sridevi_day,
        'sridevi_day_op_time': sridevi_day_op_time,
        'sridevi_day_cl_time' : sridevi_day_cl_time,
        'time_bazar': time_bazar,
        'time_bazar_op_time': time_bazar_op_time,
        'time_bazar_cl_time': time_bazar_cl_time,
        'madhur_day': madhur_day,
        'madhur_day_op_time': madhur_day_op_time,
        'madhur_day_cl_time': madhur_day_cl_time,
        'milan_day': milan_day,
        'milan_day_op_time': milan_day_op_time,
        'milan_day_cl_time': milan_day_cl_time,
        'raj_day': raj_day,
        'raj_day_op_time': raj_day_op_time,
        'raj_day_cl_time': raj_day_cl_time,
        'suprem_day': suprem_day,
        'suprem_day_op_time': suprem_day_op_time,
        'suprem_day_cl_time': suprem_day_cl_time,
        'kalyan_day': kalyan_day,
        'kalyan_day_op_time': kalyan_day_op_time,
        'kalyan_day_cl_time': kalyan_day_cl_time,
        'sridevi_night': sridevi_night,
        'sridevi_night_op_time': sridevi_night_op_time,
        'sridevi_night_cl_time': sridevi_night_cl_time,
        'madhur_night': madhur_night,
        'madhur_night_op_time': madhur_night_op_time,
        'madhur_night_cl_time': madhur_night_cl_time,
        'suprem_night': suprem_night,
        'suprem_night_op_time': suprem_night_op_time,
        'suprem_night_cl_time': suprem_night_cl_time,
        'milan_night': milan_night,
        'milan_night_op_time': milan_night_op_time,
        'milan_night_cl_time': milan_night_cl_time,
        'raj_night': raj_night,
        'raj_night_op_time': raj_night_op_time,
        'raj_night_cl_time': raj_night_cl_time,
        'kalyan_night': kalyan_night,
        'kalyan_night_op_time': kalyan_night_op_time,
        'kalyan_night_cl_time': kalyan_night_cl_time,
        'main_bazar': main_bazar,
        'main_bazar_op_time': main_bazar_op_time,
        'main_bazar_cl_time': main_bazar_cl_time,
    }
    return data