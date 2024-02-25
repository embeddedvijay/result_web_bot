from reader.models import *
from datetime import datetime
    
def time_covert_12hr_to_24hr_format(time_string_12hr,format):
    # Example 12-hour time string
    time_string_12hr = time_string_12hr + ' '+ format
    
    # Specify the format of the 12-hour time string
    time_format_12hr = "%I:%M %p"

    # Convert 12-hour time string to a datetime object
    time_object_12hr = datetime.strptime(time_string_12hr, time_format_12hr)

    # Format the datetime object as a 24-hour time string
    time_string_24hr = time_object_12hr.strftime("%H:%M")
    print('what is time is here--->',time_string_24hr)
    return time_string_24hr
    
def save_market_time(sridevi_day_op_time,sridevi_day_cl_time,
                     time_bazar_op_time,time_bazar_cl_time,
                     madhur_day_op_time,madhur_day_cl_time,
                     milan_day_op_time,milan_day_cl_time,
                     rajdhani_day_op_time,rajdhani_day_cl_time,
                     supreme_day_op_time,supreme_day_cl_time,
                     kalyan_day_op_time,kalyan_day_cl_time,
                     sridevi_nigh_op_time,sridevi_nigh_cl_time,
                     main_bazar_op_time,main_bazar_cl_time,
                     madhur_nigh_op_time,madhur_nigh_cl_time,
                     milan_nigh_op_time,milan_nigh_cl_time,
                     rajdhani_nigh_op_time,rajdhani_nigh_cl_time,
                     supreme_nigh_op_time,supreme_nigh_cl_time,
                     kalyan_nigh_op_time,kalyan_nigh_cl_time):
    
    time_data = market_time_update()
    
    time_data.sridevi_day_open = sridevi_day_op_time
    time_data.sridevi_day_close = sridevi_day_cl_time
    time_data.time_bazar_open = time_covert_12hr_to_24hr_format(time_bazar_op_time,'PM')
    time_data.time_bazar_close = time_covert_12hr_to_24hr_format(time_bazar_cl_time,'PM')
    time_data.madhur_day_open = time_covert_12hr_to_24hr_format(madhur_day_op_time,'PM')
    time_data.madhur_day_close = time_covert_12hr_to_24hr_format(madhur_day_cl_time,'PM')
    time_data.milan_day_open =  time_covert_12hr_to_24hr_format(milan_day_op_time,'PM')
    time_data.milan_day_close = time_covert_12hr_to_24hr_format(milan_day_cl_time,'PM')
    time_data.rajdhani_day_open = time_covert_12hr_to_24hr_format(rajdhani_day_op_time,'PM')
    time_data.rajdhani_day_close = time_covert_12hr_to_24hr_format(rajdhani_day_cl_time,'PM')
    time_data.superem_day_open = time_covert_12hr_to_24hr_format(supreme_day_op_time,'PM')
    time_data.superem_day_close = time_covert_12hr_to_24hr_format(supreme_day_cl_time,'PM')
    time_data.kalyan_day_open = time_covert_12hr_to_24hr_format(kalyan_day_op_time,'PM')
    time_data.kalyan_day_close = time_covert_12hr_to_24hr_format(kalyan_day_cl_time,'PM')
    
    time_data.sridevi_night_open = time_covert_12hr_to_24hr_format(sridevi_nigh_op_time,'PM')
    time_data.sridevi_night_close = time_covert_12hr_to_24hr_format(sridevi_nigh_cl_time,'PM')
    time_data.madhur_night_open = time_covert_12hr_to_24hr_format(madhur_nigh_op_time,'PM')
    time_data.madhur_night_close = time_covert_12hr_to_24hr_format(madhur_nigh_cl_time,'PM')
    time_data.superem_night_open = time_covert_12hr_to_24hr_format(supreme_nigh_op_time,'PM')
    time_data.superem_night_close = time_covert_12hr_to_24hr_format(supreme_nigh_cl_time,'PM')
    time_data.milan_night_open = time_covert_12hr_to_24hr_format(milan_nigh_op_time,'PM')
    time_data.milan_night_close = time_covert_12hr_to_24hr_format(milan_nigh_cl_time,'PM')
    time_data.kalyan_night_open = time_covert_12hr_to_24hr_format(kalyan_nigh_op_time,'PM')
    time_data.kalyan_night_close = time_covert_12hr_to_24hr_format(kalyan_nigh_cl_time,'PM')
    time_data.rajdhani_night_open = time_covert_12hr_to_24hr_format(rajdhani_nigh_op_time,'PM')
    time_data.rajdhani_night_close = time_covert_12hr_to_24hr_format(rajdhani_nigh_cl_time,'PM')
    time_data.main_bazar_open = time_covert_12hr_to_24hr_format(main_bazar_op_time,'PM')
    time_data.main_bazar_close = time_covert_12hr_to_24hr_format(main_bazar_cl_time,'PM')
    
    time_data.save()
    
