import datetime
import pandas as pd
import glob
import tabula
# import pdfplumber

class JsonManager:

    # json形式に整形する関数
    def new_json(self):
        outbound_list = []
        inbound_list = []
        station_list = ["chitose","minami-chitose","lab","main",]

        for df in self.toDataFrame():
            timeschedule_list = [list(df.columns)]

            for i in range(len(df)):
                row = df.iloc[i].tolist()  # dfのi番目の行をリスト化

                timeschedule_list.append(row)  # timeschedule_listに行を追加          
                
                if len(row) == 4:   # 往路の時
            # 5bit表記に変換
                    remark_bits = "0b"
            # 本部棟に発着しない
                    remark_bits += "1" if row[3] == "-" else "0"
             # 研究棟に発着しない
                    remark_bits += "1" if row[2] == "-" else "0"
            # 南千歳駅に発着しない
                    remark_bits += "1" if row[1] == "-" else "0"
            # 千歳駅に発着しない
                    remark_bits += "1" if row[0] == "-" else "0"
            # 往路のため必ず"0"を入れる
                    remark_bits += "0"

                    row.append(remark_bits)
                    direction = 0

                else:   # 復路の時
             # 5bit表記に変換
                    remark_bits = "0b"
            # 本部棟に発着しない
                    remark_bits += "1" if row[0] == "-" else "0"
            # 研究棟に発着しない
                    remark_bits += "1" if row[1] == "-" else "0"
            # 南千歳駅に発着しない
                    remark_bits += "1" if row[2] == "-" else "0"
            # 千歳駅に発着しない
                    remark_bits += "1" if row[3] == "-" else "0"
            # 復路のバス乗り場
                    remark_bits += "0" if row[-1] == 1 else "1"

                    row[-1] = remark_bits
                    direction = 1

                if direction == 0:      # 往路の時
                    outbound_list.append(dict(zip(station_list + ["remark"], row)))
                if direction == 1:      #復路の時
                    inbound_list.append(dict(zip(station_list[::-1] + ["remark"], row)))

        
        json_dict = {"sheet":{
             "created at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
             "timetable":{
                 "outbound": outbound_list,
                 "inbound": inbound_list
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
