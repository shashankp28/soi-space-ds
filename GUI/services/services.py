def check_format(df):
    # correct = True
    error_msg = ""
    required_columns = {'kepid' : 0, 'tce_plnt_num' : 0, 'tce_rogue_flag' : 0, 'tce_period' : 0,
       'tce_period_err' : 0, 'tce_time0bk' : 0, 'tce_time0bk_err' : 0, 'tce_impact' : 0,
       'tce_impact_err' : 0, 'tce_duration' : 0, 'tce_duration_err' : 0, 'tce_depth' : 0,
       'tce_depth_err' : 0, 'tce_model_snr' : 0, 'tce_prad' : 0, 'tce_prad_err' : 0, 'tce_eqt' : 0,
       'tce_eqt_err' : 0, 'tce_insol' : 0, 'tce_insol_err' : 0, 'tce_steff' : 0,
       'tce_steff_err' : 0, 'tce_slogg' : 0, 'tce_slogg_err' : 0, 'tce_sradius' : 0,
       'tce_sradius_err' : 0}
    
    columns = df.columns

    for i in columns:
        if(i not in required_columns.keys()):
            df.drop(i, inplace=True, axis=1)
        
        else:
            if(required_columns[i] == 0):
                required_columns[i] = 1
            else:
                df.drop(i, inplace=True, axis=1)  

    for i in required_columns:
        if(required_columns[i] == 0):
            error_msg = i + " column is missing"
            return False, error_msg
    
    types = df.dtypes
    for i in required_columns:
        if(types[i] != 'float' and types[i] != 'int'):
            error_msg = "Data type of " + str(i) + " should be int or float " 
            return  False, error_msg

    return True, error_msg


def predict(df):
    # prediction coloumn
    # new df extra coloumn
    pass
