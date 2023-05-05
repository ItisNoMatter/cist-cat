import datetime
import pandas as pd
import glob
import tabula
# import pdfplumber

class JsonManager:

    # json形式に整形する関数
    def new_json(self):
        dicts = []
        content_list =[]
        station_list = ["chitose","minami-chitose","lab","main","remark",]

        for df in self.toDataFrame():
            key_list = ["bus stations"] #busに番号を振ってる
            timeschedule_list = [list(df.columns)]

            for i in range(len(df)):
                key_list.append(f"bus{i}")
                timeschedule_list.append(df.iloc[i].tolist()) #iloc[]の中に時刻が入ってる
                
                content_list.append(dict(zip(station_list, timeschedule_list[i] + ["任意の値"])))

            dicts.append(dict(zip(key_list, content_list)))
        
        json_dict = {"sheet":{
             "created at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
             "timetable":{
                 "outbound": [dicts[0]],
                 "inbound": [dicts[1]]
                }
            }
        }

        return json_dict
    
    # downloadフォルダ直下にあるPDFファイルの時刻表データを読み取る関数
    def toDataFrame(self):

        file = glob.glob("./download/*")
        print(file[0])
        #downloadフォルダの0番目のpdfをparseします
        dfs = tabula.read_pdf(f"{file[0]}", lattice=True, pages='all')[:2] #必要な部分のみ
        
        for i in range(2):
            dfs[i] = dfs[i].dropna(axis = 1)
            dfs[i] = pd.DataFrame(dfs[i])

        return dfs
