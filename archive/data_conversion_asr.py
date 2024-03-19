
import pandas as pd
import os

tests = [t for t in os.listdir(r'../rawdata')]

for t in tests:

    dir_source = r'C:\Users\j.kapp\PycharmProjects\AST-Analysis\rawdata' + '\\' + t +  '\\' + 'gamry\eis'
    dir_target = r'C:\Users\j.kapp\PycharmProjects\AST-Analysis\data' + '\\' + t

    csv_files = [f for f in os.listdir(dir_source)]


    columns_of_interest = ['s', 'Hz', 'ohm', 'ohm.1', '°']

    hfr_dfs = {}

    hfr_counter = 1
    char = 1
    amp_last = 5
    asr_data = []

    for file in csv_files:
        df_file = pd.read_csv(os.path.join(dir_source, file), encoding='cp1252',
                              skiprows=54, sep='\t', usecols=columns_of_interest,
                              low_memory=False)

        df_info = pd.read_csv(os.path.join(dir_source, file), encoding='cp1252',
                              nrows=12, sep='\t', low_memory=False)

        amp = float(df_info.iloc[11, 2])
        freq_final = float(df_info.iloc[9, 2])

        date = df_info.iloc[2, 2]
        time = df_info.iloc[3, 2]

        # df_file['amp'] = amp
        # df_file['date'] = date
        # df_file['time'] = time

        if amp < amp_last:
            df_file['char'] = char
            amp_last = amp
        else:
            char += 1
            df_file['char'] = char
            amp_last = amp

        # Smallest value below zero in each column
        imag_sub = df_file[df_file['ohm.1'] < 0]['ohm.1'].min()
        real_sub = df_file[df_file['ohm.1'] == imag_sub]['ohm'].min()

        # Smallest value above zero in each column
        imag_up = df_file[df_file['ohm.1'] > 0]['ohm.1'].min()
        real_up = df_file[df_file['ohm.1'] == imag_up]['ohm'].min()

        x = [real_sub, real_up]
        y = [imag_sub, imag_up]

        m = (y[1] - y[0]) / (x[1] - x[0])  # slope formula: (y2 - y1) / (x2 - x1)
        b = y[0] - m * x[0]  # y-intercept formula: y1 - m * x1
        x_line = [x[0], x[1]]
        y_line = [m * xi + b for xi in x_line]

        asr = round((-b / m) * 1000 * 25, 2)


        dict_meas = {'date': date, 'time':time, 'sample' : t, '#': hfr_counter, 'AC Amp [A]': amp, 'ASR [mOhm*cm2]':asr}

        # if len(df_file) < 40:
        df_file['#'] = hfr_counter
        hfr_dfs[file] = df_file
        hfr_counter += 1

        asr_data.append(dict_meas)

    df = pd.DataFrame(asr_data)
    df.to_csv(dir_target + '\\' + 'asr.csv', index=False)












