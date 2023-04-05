import datetime
import pandas as pd
import glob
import tabula

class JsonManager:

    # json形式に整形する関数
    def new_json(self):
        dicts = []
        for df in self.toDataFrame():
            key_list = ["bus stations"]
            contents_list = [list(df.columns)]

            for i in range(len(df)):
                key_list.append(f"bus{i}")
                contents_list.append(df.iloc[i].tolist())

            dicts.append(dict(zip(key_list, contents_list)))
        
        json_dict = {"to cist": dicts[0], "to chitose station": dicts[1], "created at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
        return json_dict
    
    # downloadフォルダ直下にあるPDFファイルの時刻表データを読み取る関数
    def toDataFrame(self):

        file = glob.glob("/download/*")
        #downloadフォルダの0番目のpdfをparseします
        dfs = tabula.read_pdf(f"{file[0]}", lattice=True, pages='all')[:2] #必要な部分のみ
        
        for i in range(2):
            dfs[i] = dfs[i].dropna(axis = 1)
            dfs[i] = pd.DataFrame(dfs[i])

        return dfs
