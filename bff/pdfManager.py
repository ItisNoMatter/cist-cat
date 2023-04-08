import requests
import os
from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text
import shutil

class PdfManager:

  def __init__(self):
    self.load_url = "https://www.chitose.ac.jp/info/access"
    self.html = requests.get(self.load_url, verify=False)
    self.soup = BeautifulSoup(self.html.content, "html.parser")
    self.tag_list = self.soup.select('a[href*="/uploads/files/"]')
    self.file_name = self.tag_list[0].get('href')
    self.file_dir = "download"
    self.file_path = os.path.join(self.file_dir, self.get_file_name())

  def get_file_name(self):
      JST = timezone(timedelta(hours=+9), 'JST')
      now = datetime.now(JST).strftime("%Y_%m_%d")
      return now + ".pdf"

  def file_exists(self):
      return os.path.isfile(self.file_path)
    
  # def rename_file(self):
  #     os.remove(self.file_path)
  #     self.file_path = os.path.join(self.file_dir, self.get_file_name())

  def download_file(self):
      file_url = "https://www.chitose.ac.jp" + self.file_name
      response = requests.get(file_url, verify=False)
      with open(self.file_path, "wb") as file:
          for chunk in response.iter_content(100000):
              file.write(chunk)
      print("ダウンロード・ファイル保存完了")

  def get_pdf_from_web(self):
    if os.path.isdir(self.file_dir):
      shutil.rmtree(self.file_dir)
      os.makedirs(self.file_dir)
      if not self.file_exists():
        self.download_file()
      else:
        print("ファイルが既に存在します")
        current_file_name = os.path.basename(self.file_path)
        expected_file_name = self.get_file_name()
        if current_file_name != expected_file_name:
          os.remove(self.file_path)
          self.file_path = os.path.join(self.file_dir, expected_file_name)
          self.download_file()

  # # bs4でクラス名がelement_grp_linkの要素の一つ目のファイルを取得する
  # load_url = "https://www.chitose.ac.jp/info/access"
  # html = requests.get(load_url, verify=False)
  # soup = BeautifulSoup(html.content, "html.parser")
  # tag_list = soup.select('a[href*="/uploads/files/"]')
  # file_name = tag_list[0].get('href')
  
  # # ファイルの保存先のディレクトリ
  # file_dir = "download"
  # # ファイルを取得するURL
  # file_url = "https://www.chitose.ac.jp"+file_name
  
  # response = requests.get(file_url, verify=False)

  # def get_pdf_from_web(self):
  #     print(self.response.status_code)
  #     print(self.load_url)
            
  #     # フォルダ内にPDFファイルが一つしか存在しないように確認した上でファイルを保存する
  #     file_path = os.path.join(self.file_dir, os.path.basename(self.file_url))
  #     if not os.path.exists(self.file_dir):
  #         os.makedirs(self.file_dir)
  #     file = open(file_path, "wb")
      
  #     # ファイルをローカルに書き込む
  #     for chunk in self.response.iter_content(100000):
  #         file.write(chunk)
          
  #     # ファイル保存完了
  #     file.close()
  #     print("ダウンロード・ファイル保存完了")
      
  #     return    