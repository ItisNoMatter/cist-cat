import requests
import os
import pdfminer
import urllib.parse

from pdfminer.high_level import extract_text

class PdfManager:

  # 日付・学期・年度を可変にする必要あり
  url = "https://www.chitose.ac.jp/uploads/files/R４年度シャトルバス時刻表秋学期_0306-0331.pdf"
  file_name = "R４年度シャトルバス時刻表秋学期_0306-0331.pdf"
  
  # パーセントエンコーディングされたURLをデコードする方法
  # tmp = "R%EF%BC%94%E5%B9%B4%E5%BA%A6%E3%82%B7%E3%83%A3%E3%83%88%E3%83%AB%E3%83%90%E3%82%B9%E6%99%82%E5%88%BB%E8%A1%A8%E7%A7%8B%E5%AD%A6%E6%9C%9F"
  # quote = urllib.parse.unquote(tmp)
  # url = "https://www.chitose.ac.jp/uploads/files/"+quote+"_0306-0331.pdf"
  
  # ファイルの保存先のディレクトリ
  file_dir = ""
  
  response = requests.get(url, verify=False)

  def get_pdf_from_web(self):
      print(self.response.status_code)
      print(self.url)
      
      
      # 新規ファイル作成
      file = open(os.path.join(self.file_dir,os.path.basename(self.url)),"wb")
      
      # ファイルをローカルに書き込む
      for chunk in self.response.iter_content(100000):
          file.write(chunk)
          
      # ファイル保存完了
      file.close()
      print("ダウンロード・ファイル保存完了")
      
      self.analyze_pdf()
      
      return    

  def analyze_pdf(self):
      FILE_PATH = self.file_name
      
      text = extract_text(FILE_PATH)
      print(text)
      
      # 抽出したテキストを保存するロジックが必要
