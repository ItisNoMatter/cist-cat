import requests
import os
from bs4 import BeautifulSoup

from pdfminer.high_level import extract_text

class PdfManager:

  # bs4でクラス名がelement_grp_linkの要素の一つ目のファイルを取得する
  load_url = "https://www.chitose.ac.jp/info/access"
  html = requests.get(load_url, verify=False)
  soup = BeautifulSoup(html.content, "html.parser")
  tag_list = soup.select('a[href*="/uploads/files/"]')
  file_name = tag_list[0].get('href')
  
  # ファイルの保存先のディレクトリ
  file_dir = "download"
  # ファイルを取得するURL
  file_url = "https://www.chitose.ac.jp"+file_name
  
  response = requests.get(file_url, verify=False)

  def get_pdf_from_web(self):
      print(self.response.status_code)
      print(self.load_url)
            
      # フォルダ内にPDFファイルが一つしか存在しないように確認した上でファイルを保存する
      file_path = os.path.join(self.file_dir, os.path.basename(self.file_url))
      if not os.path.exists(self.file_dir):
          os.makedirs(self.file_dir)
      file = open(file_path, "wb")
      
      # ファイルをローカルに書き込む
      for chunk in self.response.iter_content(100000):
          file.write(chunk)
          
      # ファイル保存完了
      file.close()
      print("ダウンロード・ファイル保存完了")
      
      return    