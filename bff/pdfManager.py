import requests
import urllib.parse

class PdfManager:

  # 日付・学期・年度を可変にする必要あり
  url = "https://www.chitose.ac.jp/uploads/files/R４年度シャトルバス時刻表秋学期_0306-0331.pdf"
  
  # パーセントエンコーディングされたURLをデコードする方法
  # tmp = "R%EF%BC%94%E5%B9%B4%E5%BA%A6%E3%82%B7%E3%83%A3%E3%83%88%E3%83%AB%E3%83%90%E3%82%B9%E6%99%82%E5%88%BB%E8%A1%A8%E7%A7%8B%E5%AD%A6%E6%9C%9F"
  # quote = urllib.parse.unquote(tmp)
  # url = "https://www.chitose.ac.jp/uploads/files/"+quote+"_0306-0331.pdf"
  
  response = requests.get(url, verify=False)

  def get_pdf_from_web(self):
      print(self.response.status_code)
      print(self.url)
      return "ok"
    
