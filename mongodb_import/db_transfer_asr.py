from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://jkp:phd2024@172.16.134.8:27017/')
db = client.dep6_gtb

test_list = db.list_collection_names()
test_list_eis = sorted([t for t in test_list if t.endswith('EIS')])

t = 1

for test in test_list_eis:
    print(str(test)[:-3])
    if str(test)[:-3] + '_ASR' in db.list_collection_names():
        print('collection already exists!')
        continue
    else:
        collection = db[test]
        measurements = collection.distinct('source_file')
        print(measurements)

        asr_collection_name = str(test)[:-3] + 'ASR'
        print(str(asr_collection_name))

        asr_collection = db[asr_collection_name]
        print('Collection: ' + str(collection))

        for measurement in measurements:
            print(measurement)
            query = {'source_file':measurement}
            projection = {'datetime': 1, 's':1, 'Hz':1, 'z_real': 1, 'z_imag': 1}

            documents = list(collection.find(query, projection))
            print('query data...')

            eis_df = pd.json_normalize(documents)

            # hfr_dfs = {}
            #
            # hfr_counter = 1
            # char = 1
            amp_last = 5
            # asr_data = []

            for document in documents:

                amp = document['ac_amp']

                datetime = document['datetime']

                if amp < amp_last:
                    document['char'] = char
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