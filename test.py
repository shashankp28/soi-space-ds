import pickle
import pandas as pd


def predict(df):

    delete = ["kepid", "tce_plnt_num", "tce_rogue_flag", "tce_insol", "tce_impact", "tce_insol_err", "tce_period_err", "tce_time0bk_err", "tce_impact_err",
              "tce_duration_err", "tce_depth_err", "tce_prad_err", "tce_eqt_err", "tce_eqt_err", "tce_steff_err", "tce_slogg_err", "tce_sradius_err"]
    data_new = df.drop(delete, axis=1)
    data_new.dropna(subset=['tce_period', 'tce_time0bk', 'tce_duration', 'tce_depth', 'tce_model_snr',
                    'tce_prad', 'tce_eqt', 'tce_steff', 'tce_slogg', 'tce_sradius'], inplace=True)

    mean = {
        'tce_period': 2.93291512e+01,
        'tce_time0bk': 1.43612343e+02,
        'tce_duration': 4.80776600e+00,
        'tce_depth': 1.27949972e+04,
        'tce_model_snr': 1.90403268e+02,
        'tce_prad': 8.15391768e+00,
        'tce_eqt': 1.86699887e+03,
        'tce_steff': 6.33844191e+03,
        'tce_slogg': 4.19125150e+00,
        'tce_sradius': 2.43331856e+00
    }

    std_dev = {
        'tce_period': 9.24820052e+01,
        'tce_time0bk': 3.97876643e+01,
        'tce_duration': 4.24394720e+00,
        'tce_depth': 6.92931174e+04,
        'tce_model_snr': 1.06404264e+03,
        'tce_prad': 4.78599773e+01,
        'tce_eqt': 1.28271642e+03,
        'tce_steff': 1.15825662e+03,
        'tce_slogg': 4.87043496e-01,
        'tce_sradius': 8.97215415e+00
    }
    for i in mean:
        data_new[i] -= mean[i]
        data_new[i] /= std_dev[i]
    print("setup")
    model = pickle.load(open('./ML/model_rfc.pkl', "rb"))
    model_type = "rfc"
    print("load")

    # prediction coloumn
    prediction = model.predict(data_new)
    print("predict")

    # new df extra coloumn
    df['predicted'] = prediction

    print("Added")

    return df, model_type


df = pd.read_csv("ML/test.csv")
print(predict(df))
