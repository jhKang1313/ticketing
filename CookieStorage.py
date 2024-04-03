
class CookieStorage:
  def __init__(self):
    with open("cookies", "r") as file:
      self.cookieLine = [line for line in file.readlines()]
  def popCookie(self):
    return self.cookieLine[len(self.cookieLine) - 1]
  def getAllCookies(self):
    return self.cookieLine

  def getOneCookies(self):
    return self.cookieLine[0:3]

resultDic = {}
if __name__ == "__main__" :
  cookies = CookieStorage()
  print(f" total len : {len(cookies.getAllCookies())}")
  for cookie_str in cookies.getAllCookies():
    dic = {key: value for key, value in (
        cookie.split('=', 1) for cookie in cookie_str.replace(" ", "").split(';')
      ) if value.strip()
    }

    for key in dic.keys():
      resultDic[key] = [] if resultDic.get(key) is None else resultDic[key]
      resultDic[key].append(dic.get(key))

  for key in resultDic.keys():
    resultDic[key] = set(resultDic[key])

  for key in resultDic.keys():
    if len(resultDic[key]) > 1:
      print(f"{key} ({len(resultDic[key])}): {resultDic[key]}")
  #print(list(resultDic[key] for key in resultDic.keys() if len(resultDic[key]) > 1))





