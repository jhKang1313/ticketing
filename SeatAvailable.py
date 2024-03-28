import requests as requests
from datetime import datetime
import logging as log
import sys as sys

log.basicConfig(stream=sys.stdout, level=log.INFO)

class SeatAvailable:
  def __init__(self, cookies):
    self.request_url = 'https://www.eticketing.co.uk/tottenhamhotspur/EDP/Seats/AvailableRegular'
    self.param = {
      "AreSeatsTogether" : "true",
      "EventId" : "9377",
      "MaximumPrice" : 10000000,
      "MinimumPrice" : 0,
      "Quantity" : 1
    }
    #"https: //www.eticketing.co.uk/tottenhamhotspur/EDP/Seats/AvailableResale?AreSeatsTogether=false&EventId=9377&MarketType=1&MaximumPrice=10000000&MinimumPrice=0&Quantity=1"
    self.captureUrl = 'https://www.eticketing.co.uk/tottenhamhotspur/EDP/Event/Index/9377?edpState=BestAvailable'
    self.ticketUrl = 'https://www.eticketing.co.uk/tottenhamhotspur/EDP/Event/Index/9377?edpState=BestAvailable'
    self.cookie_session = cookies
    self.header = {
      "Cookie" : f"{self.cookie_session}",
      "X-Requested-With" : "XMLHttpRequest",
      "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"
    }
    self.response = None
  def request(self):
    self.response = requests.get(self.request_url, data=self.param, headers=self.header)
    log.info(f"[{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')}] request ==> result : {self.response.status_code}, {self.response.text}")

  def getStatus(self):
    return self.response.status_code if self.response is not None else "response is none"
  def getJsonReponse(self):
    return self.response.json()
