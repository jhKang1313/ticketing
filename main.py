import requests as requests
import Message as Message
#1
request_url = "https://www.eticketing.co.uk/tottenhamhotspur/EDP/Seats/AvailableRegular"

param = {
  "AreSeatsTogether" : "true",
  "EventId" : "9377",
  "MaximumPrice" : 10000000,
  "MinimumPrice" : 0,
  "Quantity" : 1
}

# Header 에 Queueit-Session-tottenhamhotspur, ASP.NET_SessionId 가 필수로 필요함
header = {
  "Cookie" : "Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3D2b29087e-9464-4c77-9401-79bc8a7e3b0d%26Expires%3D1710338792%26Hash%3D32f47cd11cdee6ba22d41a3f6c2b68444b73baa1ee0bfd1dff6763d7a56db634; ASP.NET_SessionId=p0rdwmdf4ylikw2ipiegwsmz; ",
  "X-Requested-With" : "XMLHttpRequest",
  "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"
}

response = requests.get(request_url, data = param, headers= header)

print(response.text)

if response.text == "[]":
  Message.send_slack_notification("자리없음")
else :
  Message.send_slack_notification("자리있다!!!!!")
