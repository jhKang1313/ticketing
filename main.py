import time as time
import random as random
import SlackWebHook as msg
import SeatAvailable as seat
import subprocess
import CookieStorage as cookie

QUANTITY = "2"
# cookie 가 15 분 정도는 가는 것 같음 -> 새창으로 열어야 capture 화면 나
cookieStorage = cookie.CookieStorage()
regularSeat = seat.SeatAvailable(cookieStorage.popCookie(), QUANTITY)
resaleSeat = seat.ResaleSeatAvailable(cookieStorage.popCookie(), QUANTITY)
exitResult = ('identify', 'captcha', 'error')
result = ""
while result not in exitResult:
  for seat in [resaleSeat, regularSeat]:
    if result in exitResult: 
      break
    seat.request()
    if seat.getStatus() == 200:
      if seat.response.text.startswith("<!DOCTYPE html>"):
        result = 'captcha'
        msg.send_slack_notification(f"Required Capture Code  : {seat.captureUrl}")
        subprocess.Popen(['open', '-na', 'Safari', seat.captureUrl])

      elif seat.response.text != '[]':
        result = seat.getJsonReponse()
        msg.send_slack_notification("Available Seat!!!")
      
    else:
      result = seat.getJsonReponse()['response']
      if result == 'identify':
        msg.send_slack_notification(f"Required Login : {seat.ticketUrl}")
        subprocess.Popen(['open', '-na', 'Safari', seat.captureUrl])
      elif result == 'captcha':
        msg.send_slack_notification(f"Required Capture Code  : {seat.captureUrl}")
        subprocess.Popen(['open', '-na', 'Safari', seat.captureUrl])
      else:
        result = 'error'
        msg.send_slack_notification(f"Occur Error : {seat.ticketUrl}")
    time.sleep(2)
  time.sleep(random.randint(55, 65))

print("exit")

