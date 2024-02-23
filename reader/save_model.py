from reader.models import *


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
    time_data.time_bazar_open = time_bazar_op_time
    time_data.time_bazar_close = time_bazar_cl_time
    time_data.madhur_day_open = madhur_day_op_time
    time_data.madhur_day_close = madhur_day_cl_time
    time_data.milan_day_open =  milan_day_op_time
    time_data.milan_day_close = milan_day_cl_time
    time_data.rajdhani_day_open = rajdhani_day_op_time
    time_data.rajdhani_day_close = rajdhani_day_cl_time
    time_data.superem_day_open = supreme_day_op_time
    time_data.superem_day_close = supreme_day_cl_time
    time_data.kalyan_day_open = kalyan_day_op_time
    time_data.kalyan_day_close = kalyan_day_cl_time
    
    time_data.sridevi_night_open = sridevi_nigh_op_time
    time_data.sridevi_night_close = sridevi_nigh_cl_time
    time_data.madhur_night_open = madhur_nigh_op_time
    time_data.madhur_night_close = madhur_nigh_cl_time
    time_data.superem_night_open = supreme_nigh_op_time
    time_data.superem_night_close = supreme_nigh_cl_time
    time_data.milan_night_open = milan_nigh_op_time
    time_data.milan_night_close = milan_nigh_cl_time
    time_data.kalyan_night_open = kalyan_nigh_op_time
    time_data.kalyan_night_close = kalyan_nigh_cl_time
    time_data.rajdhani_night_open = rajdhani_nigh_op_time
    time_data.rajdhani_night_close = rajdhani_nigh_cl_time
    time_data.main_bazar_open = main_bazar_op_time
    time_data.main_bazar_close = main_bazar_cl_time
    
    time_data.save()
    