import pandas as pd
import os

tests = [t for t in os.listdir(r'C:\Users\j.kapp\PycharmProjects\AST-Analysis\rawdata')]

for t in tests:

    dir_source = r'C:\Users\j.kapp\PycharmProjects\AST-Analysis\rawdata' + '\\' + t +  '\\' + 'gamry\eis'
    dir_target = r'C:\Users\j.kapp\PycharmProjects\AST-Analysis\data' + '\\' + t

    csv_files = [f for f in os.listdir(dir_source)]

    eis5a_dfs = {}
    eis25a_dfs = {}
    eis50a_dfs = {}
    eis75a_dfs = {}
    eis100a_dfs = {}
    hfr_dfs = {}

    columns_of_interest = ['s', 'Hz', 'ohm', 'ohm.1', '°']

    eis5a_counter = 1
    eis25a_counter = 1
    eis50a_counter = 1
    eis75a_counter = 1
    eis100a_counter = 1
    hfr_counter = 1

    char = 1
    amp_last = 5

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

        len(df_file)

        df_file['amp'] = amp
        df_file['date'] = date
        df_file['time'] = time

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

        df_file['asr'] = asr

        if amp < amp_last:
            df_file['char'] = char
            amp_last = amp
        elif amp == amp_last:
            continue
        else:
            char += 1
            df_file['char'] = char
            amp_last = amp

        # if len(df_file) < 40:
        print('HFR-Data Files ' + str(hfr_counter) + ' ' + str(char))
        df_file['#'] = hfr_counter
        hfr_dfs[file] = df_file
        hfr_counter += 1



        if amp == 0.25 and freq_final == 0.1:
            print('EIS-Data (5A) Files ' + str(eis5a_counter))
            df_file['#'] = eis5a_counter
            eis5a_dfs[file] = df_file
            eis5a_counter += 1

        if amp == 1.25 and freq_final == 0.1:
            print('EIS-Data (25A) Files ' + str(eis25a_counter))
            df_file['#'] = eis25a_counter
            eis25a_dfs[file] = df_file
            eis25a_counter += 1

        if amp == 2.5 and freq_final == 0.1:
            print('EIS-Data (50A) Files ' + str(eis50a_counter))
            df_file['#'] = eis50a_counter
            eis50a_dfs[file] = df_file
            eis50a_counter += 1

        if amp == 3.75 and freq_final == 0.1:
            print('EIS-Data (75A) Files ' + str(eis75a_counter))
            df_file['#'] = eis75a_counter
            eis75a_dfs[file] = df_file
            eis75a_counter += 1

        if amp == 5.00 and freq_final == 0.1:
            print('EIS-Data (100A) Files ' + str(eis100a_counter))
            df_file['#'] = eis100a_counter
            eis100a_dfs[file] = df_file
            eis100a_counter += 1


    try:
        hfr_df = pd.concat(hfr_dfs.values(), ignore_index=True)
    except:
        print('No HFR-Data')
    try:
        eis5a_df = pd.concat(eis5a_dfs.values(), ignore_index=True)
    except:
        print('No EIS-Data for 5A Current')
    try:
        eis25a_df = pd.concat(eis25a_dfs.values(), ignore_index=True)
    except:
        print('No EIS-Data for 25A Current')
    try:
        eis50a_df = pd.concat(eis50a_dfs.values(), ignore_index=True)
    except:
        print('No EIS-Data for 50A Current')
    try:
        eis75a_df = pd.concat(eis75a_dfs.values(), ignore_index=True)
    except:
        print('No EIS-Data for 75A Current')
    try:
        eis100a_df = pd.concat(eis100a_dfs.values(), ignore_index=True)
    except:
        print('No EIS-Data for 100A Current')

    try:
        hfr_df.to_csv(dir_target + '\hfr.csv', index=False)
    except:
        pass
    try:
        eis5a_df.to_csv(dir_target + '\eis_5a.csv', index=False)
    except:
        pass
    try:
        eis25a_df.to_csv(dir_target + '\eis_25a.csv', index=False)
    except:
        pass
    try:
        eis50a_df.to_csv(dir_target + '\eis_50a.csv', index=False)
    except:
        pass
    try:
        eis75a_df.to_csv(dir_target + '\eis_75a.csv', index=False)
    except:
        pass
    try:
        eis100a_df.to_csv(dir_target + '\eis_100a.csv', index=False)
    except:
        pass







