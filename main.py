import time as time
import random as random
import requests as requests
import Message as Message
import SeatAvailable as sa
import webbrowser as webbrowser
import subprocess


#1
# cookie 가 15 분 정도는 가는 것 같음 -> 새창으로 열어야 capture 화면 나
cookie_session = \
    "OptanonConsent=isGpcEnabled=0&datestamp=Fri+Mar+29+2024+00%3A05%3A30+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; reese84=3:fWuhKzqNK1D6k//7xN2RbQ==:+FvwsUx4gmTsMZPQa1tKvZy0XfaFj811PsqjajVu7GqsIsm4vde558Gf2jlc7sksrup/t8ScoywhX6kbFupaOO/w9TmqSWc+N+GUXBVXCkDBcXFFwUGeCGZ0jQUCFzjkrEN6XxW8zsb5uhlSnrCY/fMcyxIT2Vm3rfw0MeA5TzDzWgRQOpvYTCCFQ4T3FJhGvrZoyc85CQNhZRzQjSewX/d6ZiKzSVyO5BpZaOylaQJenwS0b51aROmsLV8wihqYvsXKlA0T2AMyBFwFb5iPcyi+OnlULyWRpp46GdMGtB/n7uCPHeu/CXmA+kF68ChSgIKqXuTjCqjloMxMDxxcXx6flcICQwodo6Ybm1epimTXhdR+/vh0kGGXqaZG9UPsnjyKQu4DmMzXiqvI7DZQaHEghW1MxoS8+53zcBICP8/iFaOD2e5x58LdnHy1yJeWtOB5YdyWwVrfuKE5KMZuM4E7h3YBo6bhddOP+PoxhFBBDwNfhO9Pr84hAPyR/nHxTNhCr1rYbmsyNUr7CW1s0A==:jZJ/B2FqmnaMr6laVMmPKcNoGfmr951hahu5EuGuu0Q=; selectedCulture=en-GB; www.eticketing.co.uk/tottenhamhotspur=E013CD2369A4A667DA3C00604F9F935209BF14021D7A0357FB651EF5B43AE79774690ADB1330B4BC53DF31A6CD44B3F178C6A64A917ED5F609FE64CC0F10251B170C897B5149CFA323AB53DC5500ED93EFAF85B5; www.eticketing.co.uk/tottenhamhotspur_E=95D81158E6F72B3CD78301B68FE276A6413CE05A58BF8837576B371018C3739306E354147DE0418012D86F676D408588B41F2F6EA9BE1424CA8C7AC3588E839F2E9C2BA6A5F60FCA92F7445E24463B2FE0D7F6CCFC7721BE96EF8F8A94A3B3231D3337D19733EBB52232DB2C4D4119BCC8FADA0147841CE7A7383440D8EA0FEA16EDDBC988A367EFF9B810EFCD0DC1AFF098098D77776EBB226B657F68C366D71D29F5968726EBA85E8DC7FBA91469DB66F80D4D86A3C804CFDC58E1DCDA3EF860E3A5B014726408909C2CD3B0B0A9890E1A2561BA20AAC4C8F4082DFDD7F8EBC0A12A7D0A8C76A2DB48CD9490E3E79611C6E1D8213EA43755C92768A0BB20B0A338DA3078EAD477C0C39DC47366394C475619E5BD64463AB54CE626DF09FBB3F3807AF7B1A3A8338C02DF83EF22BA921263672C15098904CC85261A950FBDF525CCA92CD07AE44FB0A8D60B6B1BC20739A5DCB845F0685795B57251CFB4971EB1ED6047; Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3D71c2b626-5d8b-4586-a3a2-80f5cc776bf3%26Expires%3D1711640126%26Hash%3Dd746e42c9600d6d1c3c9d1d47ba13fd54a79ea87639d21b73d6dffeab70d27a9; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711638310.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711638310.0.0.0; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711638310.60.0.0; _sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; _sc_cspv=; _scid_r=; _screload=; _ga=GA1.1.24637876.1709650705; _gid=GA1.3.1638996738.1711623560; ASP.NET_SessionId=cjnmswmfcexaragfei0xnlxw; uniqueid=cjnmswmfcexaragfei0xnlxw; NSC_JOoilvjmbv3hpnkb35fzrxc5ykb2ocv=ffffffff0943ed3d45525d5f4f58455e445a4a423660; eps_sid=892af8bd04df944c78ba79d3581780e019e68525; _sctr=1%7C1711119600000; referrer=; session=1; NSC_JOydqodicsnriladjes2uzco3apr2dv=ffffffffc3a06e0145525d5f4f58455e445a4a423660; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
#    "OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+23%3A31%3A41+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; reese84=3:RymCAWC91Ls1/foToOw5xw==:axRDi1+S83UxyRPw0U8ZAusXGMaKcHeKWL6MCK4lUyrhBOiuX+73Ms5gbZdj9T2yx6M0tMKSmF57xQ00+rWjqQ801xTDwGN4EYp2PE8bBVvpCl4m6OqcxvV/16f1xH2UFojrMt2JAwR+4zGg2Aw4S3mzuJeoOn2dPq3CZOSmxPFWXqJI+I4eB1wwIAVshQ/0/pgHw6Rc+ZuJMqz+4EmTZkZkUhwWRZE9gRw48E+6qHuIra1tpo0ICi+Qu8YSbyrJmfO8iaUxwnntyXRC/RsNQciBbfO7x5C0iAOGmD6trHcrwcaugpWHyZpQ7RBIBv7w9gXwVVVnMOFh9qvE5vcv+O+ibjgpej2cdWGH/p6KASQxXwk3b5LwOt+bm3X/EvcBaDmH10Ix+5KtjbtECIuzok4/jRAfenYlUE8SohMxmEr9FvmKPc8KXXAUq3gSjIDxPii2miG/8Jeg4oNf+CSonNIBWf3uMOm1hkDj1fEDnjE7yXu0ODj2IBgm7JXJICl7:Hcc6NbVltp8aCkn3PNqHAXWGfDtIEnsxVq0kpYm7FSY=; selectedCulture=en-GB; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711636288.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711636288.0.0.0; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711636288.60.0.0; _sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; _sc_cspv=; _scid_r=; _screload=; _ga=GA1.3.24637876.1709650705; _gid=GA1.3.1638996738.1711623560; Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3D4936b807-015e-42c5-a617-dfa1ecbd0f13%26Expires%3D1711638020%26Hash%3De2255361188a781f2e92f62420ee53b3841808b911bdeafe982f3cae458a6def; www.eticketing.co.uk/tottenhamhotspur=FF6DD24D8343BECC940126885886FCAC278F56D116D62C4FFED52A0C3389FC984DB22F651A24D4A9A5D4EC1632956D8540E68C9641A0CB6C685E3450C0AF1F5750773C2818E0026B44541B46C30D0535E108B2B4; www.eticketing.co.uk/tottenhamhotspur_E=F9EAF1C588B6217BED5DA4E6C08FC0940769FAD64734B07F7A39CE1A95FC088BC2337BA6F202F027A23A93EDD95E6ABE6774675D2D65EE1F6981B8C3A50330D611986E3A8B8970C66E1949D085AC389885EA08107572A6CB9A44E2C6D45C31C86DB5A13F065DBDB2D986F7D41AF8627106FD4FC93C4C35209FEA7203689118AF8A6845C435E0FDEC2DFC65E79F569F64DF3752F30B8E3AE308B0A34721DC6AC9673903030D4537ACED6371A1B2B602DA005C87B23D370FEE7BA6582ED75745CC3B58D4D311A0F10698B3DF54A0CB6CB041A9862332237F6E679E4E2E85E90F20A25FE6DDBA024157C8225A7F81A379F1735286385F262811CBC42B6C1D8C69C68C796B1F3FE1BA5A6C1F4C25DE789FEDB5628295D134C92C991F3355CAD37B6A8A225717669AA01D58DC34C7A998988F0318D649377779B76FCBF0F10F47B124DFB5286C8E9915FFDD808D46364B01CDA0255D05BCD4FDB612E94F73D7A36214E92061B4; ASP.NET_SessionId=cjnmswmfcexaragfei0xnlxw; uniqueid=cjnmswmfcexaragfei0xnlxw; NSC_JOoilvjmbv3hpnkb35fzrxc5ykb2ocv=ffffffff0943ed3d45525d5f4f58455e445a4a423660; eps_sid=892af8bd04df944c78ba79d3581780e019e68525; _sctr=1%7C1711119600000; referrer=; session=1; NSC_JOydqodicsnriladjes2uzco3apr2dv=ffffffffc3a06e0145525d5f4f58455e445a4a423660; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
#   "selectedCulture=en-GB; _ga=GA1.1.24637876.1709650705; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711635519.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711635519.0.0.0; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711635518.45.0.0; reese84=3:eUGl+YEctPXBq0L9PrbUpg==:Q0EGp9cL1Q6tba/4SD3RT+3kutbPzJ72KLcCBKGIXcaEmw3IR037jCMw+vHzz9Ep6Se3PL/+i70MrutWo9ofCd3dsQA9ni7GB1wvGbpKwfTjwip2bGmi4un3qoMeMm+cQKw1uWQhpWy79Xleaq7+daJviW6OVMxHVlfJeMnQ8vTGqIuDRs9rTyDfMwLbjAEHCVzQ2MIRQUEVU1UqwfkjeaJzD1g7z5FQDdyv27KBdYknAROXGoRelRNv4Z3mxkDj3bJ3NFhpMKpaFfp4fJPXfyLXujbr1D97oiOrNOGqE2HT/20BYP8/wZSH5YmkWJBopD4NOdMIHIPvyGsytzL9Lho2+cmng6AwsVfijFWLjAQpNSG82XyJlq/Lqy23yzP33Hxssb4N1JF7hJGchZ60D02qOa3zsSIhuoVejvhJlAv+oRbttFdCfQVLOq3BxGbTOPhQR3NA+jQdIrOIFXpmRVPJAKv9WQI558QiDH8QyvNCsR8fu5mF1G/KJrHlTVqi+CvYsccKI7mlzHE5H+wD9w==:0ob7dUhojmTff3alyUcLBZfcPoo76azOJ9G1NbOj9rs=; _gid=GA1.3.1638996738.1711623560; _sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; _sc_cspv=; _scid_r=; _screload=; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+23%3A18%3A33+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; _gat_UA-24386340-2=1; _gat_gtag_UA_137194665_26=1; _gat_gtag_UA_5723713_13=1; _gat_gtag_UA_7935519_2=1; www.eticketing.co.uk/tottenhamhotspur=FF6DD24D8343BECC940126885886FCAC278F56D116D62C4FFED52A0C3389FC984DB22F651A24D4A9A5D4EC1632956D8540E68C9641A0CB6C685E3450C0AF1F5750773C2818E0026B44541B46C30D0535E108B2B4; www.eticketing.co.uk/tottenhamhotspur_E=F9EAF1C588B6217BED5DA4E6C08FC0940769FAD64734B07F7A39CE1A95FC088BC2337BA6F202F027A23A93EDD95E6ABE6774675D2D65EE1F6981B8C3A50330D611986E3A8B8970C66E1949D085AC389885EA08107572A6CB9A44E2C6D45C31C86DB5A13F065DBDB2D986F7D41AF8627106FD4FC93C4C35209FEA7203689118AF8A6845C435E0FDEC2DFC65E79F569F64DF3752F30B8E3AE308B0A34721DC6AC9673903030D4537ACED6371A1B2B602DA005C87B23D370FEE7BA6582ED75745CC3B58D4D311A0F10698B3DF54A0CB6CB041A9862332237F6E679E4E2E85E90F20A25FE6DDBA024157C8225A7F81A379F1735286385F262811CBC42B6C1D8C69C68C796B1F3FE1BA5A6C1F4C25DE789FEDB5628295D134C92C991F3355CAD37B6A8A225717669AA01D58DC34C7A998988F0318D649377779B76FCBF0F10F47B124DFB5286C8E9915FFDD808D46364B01CDA0255D05BCD4FDB612E94F73D7A36214E92061B4; Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3Ddb6c7e8a-e9b2-42c5-a2a7-88cdf0c5b84a%26Expires%3D1711635950%26Hash%3Dd4cee37752303b29884214c0ebf9fae4a6fcbd009000c09bcd395561497f2a32; ASP.NET_SessionId=cjnmswmfcexaragfei0xnlxw; uniqueid=cjnmswmfcexaragfei0xnlxw; NSC_JOoilvjmbv3hpnkb35fzrxc5ykb2ocv=ffffffff0943ed3d45525d5f4f58455e445a4a423660; eps_sid=892af8bd04df944c78ba79d3581780e019e68525; _sctr=1%7C1711119600000; referrer=; session=1; NSC_JOydqodicsnriladjes2uzco3apr2dv=ffffffffc3a06e0145525d5f4f58455e445a4a423660; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
#   "_sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; selectedCulture=en-GB; _ga=GA1.3.24637876.1709650705; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711634502.48.0.0; _gid=GA1.3.1638996738.1711623560; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; _sc_cspv=; _scid_r=; _screload=; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+23%3A01%3A41+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711634501.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711634501.0.0.0; reese84=3:V2uEcg3jc4YS8P7eLrzBvQ==:9SDH9nCONzikF6B0VAgrahwutjOaogfSmeoxMJmVzBc+AQxwG8lvZ/kZPpmkAJFUycwWJlNGPGOG0Joquw/a7k/FSwSwOMR085OtIl9DwvC9AyAjzglm6qTbJ1IewEl2nTb0GHT7BfHKLwr+q0/cMYFyynhuQ3EDjGI/7FN6xmKo7bgfTJcm09H7plF56Qa2Iznmc0UX/bf3YBa6mAZLEsE/sJbRmF1l+6ppjM7IrTiAvomUUFTN8FnZg7QL4NuamVzn4AgjN4smkNWBJ3c8VohaC6YACLfxKJM0cicPWF7oPvAMC+EaAOCtbLM5arzQW9o9EakSLcK03xeDcYgn2Dtqld8RcQ19vJYt3Ai+g1I42wlEghO840dSQMW7cX3JIrWVzlQUKl2EbB5YE+w14VAE9TJDVdllcip1zbeySB1PIueFxdvZanAJL6J5mIjkly7Y2fnUF39GqAr9CKs/Tp1cRzZB8gOoWxDBJNgXIPDS+8AT0kzupt23QpsnsoNNyKUEeMo+WWHZlLp2EevINQ==:jxiPklQEwTXw2eJzngKZhiG7e97xKyHhZbiZ8EOAYYc=; _gat_UA-24386340-2=1; _gat_gtag_UA_137194665_26=1; _gat_gtag_UA_5723713_13=1; _gat_gtag_UA_7935519_2=1; www.eticketing.co.uk/tottenhamhotspur_E=A82D68446808A09000D195EADDE10C9F47FB6D4D2C47D5A01421263D0CC61F894229B1CEEA4C35E42F6CD43F9EE61E327412C63B1866B9CE2E261CDF855DCC9D4411A4AFE809E776D6DEB9496EE5EA52B6D9D5218406BE19C8087823D242517F3322D9C31E689581CCDAA96190ACA6ECFDEB97EA1A6310AB4208D47598DA8728188C64BF37F88330FD80A85D0A9942C33BC02524EC471B742B1F7A01BB55B2A5D02DC857D324DEEDA58C5520ABD4F572FCD8434088C56A51350157A6BD0EEB8BA3E178B459943E057C9D9C9FF6D5A3410DE519CE50690E075C145C237882D0942CEF5969013808452B9D38C4D3FDE2739EDD937B677606E7FE09B41BE161BE15067CA49D1DC43F8C38A94920A901658312ABCF4CDFBB6BD63C2831292952D08705910440FA6A4C59F63F6D09FCFE87E0EAD01ACD835B6BF991FDA06E0D6A32D8EDDF2CF9C33781AD70D80960119E2AC49EB8041AB733F092D96C269E0DCBDAC209AC5FE3; www.eticketing.co.uk/tottenhamhotspur=94116317474F0D58D74061081C683A712BF2A034A28F85415AC977EFC9729C3494953C9A1237FD944463F20814670AEA1CAECEE8AD71C5290F7CB9C8C1A8C7F3833C1DA9DEC403271B228272C72EDCCAA2E5D6B5; Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3Ddb6c7e8a-e9b2-42c5-a2a7-88cdf0c5b84a%26Expires%3D1711635950%26Hash%3Dd4cee37752303b29884214c0ebf9fae4a6fcbd009000c09bcd395561497f2a32; ASP.NET_SessionId=cjnmswmfcexaragfei0xnlxw; uniqueid=cjnmswmfcexaragfei0xnlxw; NSC_JOoilvjmbv3hpnkb35fzrxc5ykb2ocv=ffffffff0943ed3d45525d5f4f58455e445a4a423660; eps_sid=892af8bd04df944c78ba79d3581780e019e68525; _sctr=1%7C1711119600000; referrer=; session=1; NSC_JOydqodicsnriladjes2uzco3apr2dv=ffffffffc3a06e0145525d5f4f58455e445a4a423660; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
#   "selectedCulture=en-GB; _ga=GA1.1.24637876.1709650705; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711632718.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711632718.0.0.0; _sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; _screload=; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; _sc_cspv=; _scid_r=; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711632717.39.0.0; reese84=3:umQrT9yL+O8nPyQUvOwQGA==:iYQNAPmrUAF2MqLE3fluFWp5mmVXvb9TFomUHUb+IOGV2BLe3jDJTzsqbKvOcbSU2sSaH4vo/Kg/CJ5Kx6wXZ1SSxWsd50scU7tJ0krMMm1Kz+0oWbh+vrsH8dGdR+KTo8gfChdf956tptbXcGstAuwvdaxLd5QSvzuRCadytNvvfR+Tuk1qzfhgxbaMyBFFRWwYXXzixxX26uCTfw3xNDqZsFQWTIX8dPcg2VPujJZV703ihZbhVQoiAhqzWk7YQZTMOp/s1tjpoec+2q5xkhExDla61VmLudBE3wUxHYvS+fS8naqRfY4Sr62Bi8cnrK6oE6s7JE/PDYOiiOnSrw5pvnfrb+V15r755Ef0zOvdcmf6wI/GrxD/5AKgL06R+0UnNkXtUoghFnNEelTMU5+kSVP8Gu4xkwu23cVAsXcdSAtMbYl3R7SdizVZpJqPoYoP9eWaN6k3f+TxjQ4bV333+jAMCUtwzIIIVbxBwJZ9gWgaB5xUXPGOiduHYrsDPnEWoMBvypf6VXp61up95A==:Y8ZKbHKKlmpy57OQnZ+ElHJPRO2hplg5qEyC+oWD2n0=; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+22%3A31%3A42+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; _gid=GA1.3.1638996738.1711623560; _gat_UA-24386340-2=1; _gat_gtag_UA_137194665_26=1; _gat_gtag_UA_5723713_13=1; _gat_gtag_UA_7935519_2=1; www.eticketing.co.uk/tottenhamhotspur=A3F5691176DF780D7224DC2105E7696224614AEB51E90F797B6638385C652F8551A19E0B66FFA62FD2B28259BF7CAC043A2CC06B37FC13C7D4D3A1BF60BFE448F3673C621A51FE8EC78547670976B0D5786A32BF; www.eticketing.co.uk/tottenhamhotspur_E=22CDC0445253BE07DC930AB73F02CBB709991BFC7399E60027AE41AC58F32A8E7DBEAE0952B37FA02A313B8BE4FFF231FE76AF4D148BA21CE353721010EBD942D346D7993F29F2527A58C8D7F3763D0191BAB39A38CFF3928E8B687C61546DA11C3802E60322E70EB8EB084268A1BC19026827DF36D085B2B9D8613F06A1DA6F40F4A5515A5A61997C16DDC4744784739F75FC41DADFC69E2A8F5C96A7DB4A1C27DF8316E0AE8D7C1A100E6AD06A20C10892B1A2B970909E6F70FF2BEB7CBBAB520C2CF1B986E1B39CC1D09C0859852694C8C519A48A297869DA1C2E9603202AA8D65C8ECA9C036CA613CC5FA16034A59024D9A6EA16099993B019D0E35F05C5E8DDDFD72589927208EFEF81ECC8BFFFAF394088E9582FED7C28E0BB0118F4C8C0672A00BA408521C58B82FC3CB67DBB171D195EBFE5C660F31238891951347F050D9F5372F141D440CFC7E8DE18720B90DC8E19085753A4B9CC5E762627053BADC7B81E; Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3D9b827548-5d54-426b-946a-52a179e49c6e%26Expires%3D1711633921%26Hash%3Dc6db2b17ed8d89e799c6cdc8fda6a232c7ac479d0cfc535e69577c88ca5bd0e3; ASP.NET_SessionId=cjnmswmfcexaragfei0xnlxw; uniqueid=cjnmswmfcexaragfei0xnlxw; NSC_JOoilvjmbv3hpnkb35fzrxc5ykb2ocv=ffffffff0943ed3d45525d5f4f58455e445a4a423660; eps_sid=892af8bd04df944c78ba79d3581780e019e68525; _sctr=1%7C1711119600000; referrer=; session=1; NSC_JOydqodicsnriladjes2uzco3apr2dv=ffffffffc3a06e0145525d5f4f58455e445a4a423660; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
#   "_ga=GA1.1.24637876.1709650705; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711632176.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711632176.0.0.0; _sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; _screload=; selectedCulture=en-GB; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; reese84=3:LxENoWh7GTCJKuDIfUBcoA==:gUm/0iwOGoDASEf5BRx3ScSA7SFX8225NUMWeCIlStnVaT/Aee7tGMfV6We3gU5apKOkWcZlBiSxHPeaZIIanX4tAIxV9aOMO1w56UScGbz5OUF68pA3Z18yxCnnUCXWFvU/CmNekBAzRlD5EAqwytNer+bmW61wKwAZxrPWvZGgFIQZ48fdXBrLRvHZ8eIzR4bS0HtnJ6pH+qgpSkuYW+ITgx79p+qA0vgTj+Q/Q8JMsolZQ2YNwXOoT906D6sqojnOh2c/4DdURGyXC7Ow8PXEuXnoidLYpFAns3tBGT9ipNVQk6Dkh6NCYwCchPQnhslFFxpcrZTD8sLSEFUeEorKV/VAbWqin5utOlYOij9bE0PRSL7OH9sKgZIvEBXbTjqoHCi3/zdGhNBq57WU9o/ppsfbFZnfvcD9pcjhJGpnTKVPmlV+b1J7Aq0Rj3LIkkua3RXKWTaHD2xlaU8mMBiNWZAKzktIXHW/6SFgyq5W7S9ak0Oi2x76lM+nIjX7:7kt6w3YZ75uAbetd98s2wFKqMgcxRVh9dXfXD2eezqo=; _sc_cspv=; _scid_r=; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711632175.34.0.0; _gid=GA1.3.1638996738.1711623560; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+22%3A22%3A36+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; _gat_UA-24386340-2=1; _gat_gtag_UA_137194665_26=1; _gat_gtag_UA_5723713_13=1; _gat_gtag_UA_7935519_2=1; Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3D9b827548-5d54-426b-946a-52a179e49c6e%26Expires%3D1711633921%26Hash%3Dc6db2b17ed8d89e799c6cdc8fda6a232c7ac479d0cfc535e69577c88ca5bd0e3; www.eticketing.co.uk/tottenhamhotspur=09A6DD72339730C5A7412C44F4C7EB0D70087C7C742D84A72A8EB7DBA444318F6585C02CB136375032709D0160D9CD3B309D08468D1B43FDB2901F84987E47E0A15FC0409EEE2565D01A9EC110347A431855A80D; www.eticketing.co.uk/tottenhamhotspur_E=9C9BB40743560EF0ECFE5A6EDE7D70CB086C44E2A5249BAADF133B779F675DBF751570FE161026E65FB10703F327F9A85913733E64D2FB2163255AC068118A2D7585B0466BC395158E5A256C752CCB46A6E2E82A28B6DE94A046E3EEE0E653497602092143E19AFC8C69CB7713344A2126480D3D5C538BBD9BEBCBDF172137C5752247936090E680E3D8E7EF47C970922F7D2CD2E5FFEBAD99566ACB9FC5523DB1509E72E0C4A31748709AA0BF95AE5CF624042F24CB462E95E819BF220F6B35BBC785BEC66FE3E2B57FE70B9B7460AFE81C96596BD23A9FCC5AFEC27C0FD72BD24FD61FC218A5B3BE542D3A0ADD3F240583B3C5FB30C111CE1CB5D1A1313CA29891716AADC851F117CF66C37D67A9BD0FC333794D357FD7B21173F253AA94F0D47CD537CE187DCFD917872F2C9572E7BD0E0C548E18E170B126B17DF4C67BEAE6CF2A75A05D29BB64D81C75D50B7AB7CC08953EB2FD811006F31AE722A85661E9F18E65; ASP.NET_SessionId=cjnmswmfcexaragfei0xnlxw; uniqueid=cjnmswmfcexaragfei0xnlxw; NSC_JOoilvjmbv3hpnkb35fzrxc5ykb2ocv=ffffffff0943ed3d45525d5f4f58455e445a4a423660; eps_sid=892af8bd04df944c78ba79d3581780e019e68525; _sctr=1%7C1711119600000; referrer=; session=1; NSC_JOydqodicsnriladjes2uzco3apr2dv=ffffffffc3a06e0145525d5f4f58455e445a4a423660; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
#   "OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+22%3A12%3A52+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; selectedCulture=en-GB; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711631571.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711631571.0.0.0; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711631571.52.0.0; reese84=3:HGha+R7gz41NOWvkDaJZew==:IOGiS/41ia0DI0OoXgdRemLqBfRobgQMjJTCl7VmIHT+5oMnOTx+G5I5lhQyz9iDI9hDVCEuNhaxcX3Kowd9xriopyb3MuAhJSIqZeCZFA7tFUsIJC6KdReAFtVWBGUSho6DqVKot07sA6EsF5BPJ78TofMC8lKVJvs6pttIMAf2feDG7kQJASY0zy3HP+CcyUas54EMOKL2yyL1T+RVudjrI27L9DQil4jmQOutteOgKy4Mn+tQPmOw7vdzgabU7P8YoPWVruAYC7g+4pgP5gcrQrlMa75ZiCJ6GfnSntjbPu8g4kE5cXmtgc7rWstU+NRn+qVBZk+v+jyzGEUR5vsYUlQFoA4uqg9Q6eJ/7DWlTrMGkgyHlw1S16MdcD6VcfgrLOta4t6IFfD1ml79lRboEr0BzynSab2OWp29Tz6g4/TfK8eEtjdYGB0vOmG1+6xDh8oXSzRKeAt+IuPMAYA45e5sxwN2f0FB4IIjgLC0AMIxnPTJ4jkeEwnvvAbk1FX2xl9jrALt7ZKWrWeeNw==:3P3YSUMDGSwoX1dRS0Mnu5LghjdQ/4uv8QXTzUzh7xc=; _ga=GA1.3.24637876.1709650705; _gat_UA-24386340-2=1; _gat_gtag_UA_137194665_26=1; _gat_gtag_UA_5723713_13=1; _gat_gtag_UA_7935519_2=1; _gid=GA1.3.1638996738.1711623560; _sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; _sc_cspv=; _scid_r=; _screload=; www.eticketing.co.uk/tottenhamhotspur=09A6DD72339730C5A7412C44F4C7EB0D70087C7C742D84A72A8EB7DBA444318F6585C02CB136375032709D0160D9CD3B309D08468D1B43FDB2901F84987E47E0A15FC0409EEE2565D01A9EC110347A431855A80D; www.eticketing.co.uk/tottenhamhotspur_E=9C9BB40743560EF0ECFE5A6EDE7D70CB086C44E2A5249BAADF133B779F675DBF751570FE161026E65FB10703F327F9A85913733E64D2FB2163255AC068118A2D7585B0466BC395158E5A256C752CCB46A6E2E82A28B6DE94A046E3EEE0E653497602092143E19AFC8C69CB7713344A2126480D3D5C538BBD9BEBCBDF172137C5752247936090E680E3D8E7EF47C970922F7D2CD2E5FFEBAD99566ACB9FC5523DB1509E72E0C4A31748709AA0BF95AE5CF624042F24CB462E95E819BF220F6B35BBC785BEC66FE3E2B57FE70B9B7460AFE81C96596BD23A9FCC5AFEC27C0FD72BD24FD61FC218A5B3BE542D3A0ADD3F240583B3C5FB30C111CE1CB5D1A1313CA29891716AADC851F117CF66C37D67A9BD0FC333794D357FD7B21173F253AA94F0D47CD537CE187DCFD917872F2C9572E7BD0E0C548E18E170B126B17DF4C67BEAE6CF2A75A05D29BB64D81C75D50B7AB7CC08953EB2FD811006F31AE722A85661E9F18E65; ASP.NET_SessionId=cjnmswmfcexaragfei0xnlxw; uniqueid=cjnmswmfcexaragfei0xnlxw; Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3D323673b0-5741-444f-b58f-f576c53cf21e%26Expires%3D1711632029%26Hash%3D8ba6d5aafa0c717f45b20adff912a6f30994870ac6ee6ac3f288efbd893cdebc; NSC_JOoilvjmbv3hpnkb35fzrxc5ykb2ocv=ffffffff0943ed3d45525d5f4f58455e445a4a423660; eps_sid=892af8bd04df944c78ba79d3581780e019e68525; _sctr=1%7C1711119600000; referrer=; session=1; NSC_JOydqodicsnriladjes2uzco3apr2dv=ffffffffc3a06e0145525d5f4f58455e445a4a423660; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
#   "_sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; selectedCulture=en-GB; _screload=; _ga=GA1.3.24637876.1709650705; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711630237.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711630237.0.0.0; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711630237.54.0.0; _gid=GA1.3.1638996738.1711623560; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; _sc_cspv=; _scid_r=; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+21%3A50%3A36+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; reese84=3:Ms+79B9LlNfAMtrCUtOzYQ==:eBO344qQPlMYiSFwHzbW5o3g4sTiizhgLjgWIxNwPX7hsUWJY+BG9yYsaHP0tq3u5cz99/YExaekilX2PXpFIMvNFr7quRpnhLrLGw7QGuoORspaIKbwQMdPsoOMmiwJLs/BXJwuLduTF7+/jEH6I/eLsS9lhEbRc0iJYVbcQm4WaBPM0KQz2JscowRV3XQxQ9RIA9MwD1Ul75JFWai6jxzr4BTZ70AF1MW5CMAMuKjHVwNjN0u8pth5hPZDd30TeWzS9qcuWieWzK0i+TDhnFP4gPHYjP4XEGUpI/UriT1ZRhnrChbMxSNTS9FiJjQ/GbNk8CvicgWBJXSEddw08TINpWtMvfEuEg4d4cIY4Qf3vTsdh9Ex3drIlSvIr/F4NOiWZNscmyhvnmm6Ln+pRDTrZEXFGweiFkBZ2oTRh92xNgdtfMQDcLVqrB2khL2C3Jyzoj1k6JBvqbBrR8+97/Ul0vMJ9JpXNReSJaeJs9MQQp+7scUswGzsSQIrtd0H:+ga/thxBazBUF4zy4kYb34nyVHpcXeKY0KbFXs/Lemw=; Queueit-Session-tottenhamhotspur=EventId%3Dtottenhamhotspur%26QueueId%3D323673b0-5741-444f-b58f-f576c53cf21e%26Expires%3D1711632029%26Hash%3D8ba6d5aafa0c717f45b20adff912a6f30994870ac6ee6ac3f288efbd893cdebc; www.eticketing.co.uk/tottenhamhotspur_E=4024C80AA63C2C0B4CC345C9BCA3183D3C1BCDF7282CDF402E3BD31FE41BE4D345383AA0A057F07ED5AED84B62F52DF062BF31B881FF03DB0FC76598A5265EAA026A8ABDBCB1BF85391AD9A8B52F84B8FB4B06C6F4FFAFE8B9E25E480A9965E8F1E73219EEE8D95B937681FB529513238E144602468D6205B17D7EA4A86F3CD40816E733F1A3647C7798A211C5DEFCD2A0D0271A2161C528D94C22FBE7D049E924BEF952E5BD73EDC8E19FC833CB99CB2366BE3F57D941D1F961EB86096B028AE3938C0DA1958EC4E45AE12CF72A8A7A42CACF658ED814FE718B3FBD6B97AC459BFB851DEED054F798FBD30B64CA76090FE23C8D2A322E8A829FBEA0A93EA9F7641E1D8B8FDCD06AE38A2A45E15EFD393E1F7B063FD8347CD5A32A76902D9543D610D07D97E69CC428F2B27054BF7FB038DB4F587D67D03DD3FAB8FA61C0AB4028CDD96480753FCE8F71AA69E44C9CBE886EF3E0E62CF20925A52B2327F6835652372A9D; www.eticketing.co.uk/tottenhamhotspur=9C6CEAC626190940CC38DA92CBA28440F02591ADD931B44BB4DD55BBC03D9B94EC116319A2D9199D8F864C730D4DE6FB189B266C9FC7ECCB62F76E7DCE974A273C4A3756B83263A2F5956EEC83F09B24B9D664D4; ASP.NET_SessionId=3mu0hoa0isfqpklquvgvcsnh; uniqueid=3mu0hoa0isfqpklquvgvcsnh; NSC_JOoilvjmbv3hpnkb35fzrxc5ykb2ocv=ffffffff0943ed3d45525d5f4f58455e445a4a423660; eps_sid=892af8bd04df944c78ba79d3581780e019e68525; _sctr=1%7C1711119600000; referrer=; session=1; NSC_JOydqodicsnriladjes2uzco3apr2dv=ffffffffc3a06e0145525d5f4f58455e445a4a423660; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
#   "_sc_cspv=https%3A%2F%2Ftr6.snapchat.com%2Fp; _screload=; _ga=GA1.3.24637876.1709650705; _ga_75QKF6HR92=GS1.1.1711625523.24.1.1711630237.0.0.0; _ga_Y0V04R4JYH=GS1.1.1711625523.27.1.1711630237.0.0.0; _ga_YH99Z57HZQ=GS1.1.1711625545.26.1.1711630237.54.0.0; _gid=GA1.3.1638996738.1711623560; _scid_r=0a06e373-af58-4bfb-a795-daaa6d972d10; _sc_cspv=; _scid_r=; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+21%3A50%3A36+GMT%2B0900+(%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=245068d6-c81f-473e-a3a2-5e8edaf7e500&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=KR%3B11&AwaitingReconsent=false&isAnonUser=1; reese84=3:Ms+79B9LlNfAMtrCUtOzYQ==:eBO344qQPlMYiSFwHzbW5o3g4sTiizhgLjgWIxNwPX7hsUWJY+BG9yYsaHP0tq3u5cz99/YExaekilX2PXpFIMvNFr7quRpnhLrLGw7QGuoORspaIKbwQMdPsoOMmiwJLs/BXJwuLduTF7+/jEH6I/eLsS9lhEbRc0iJYVbcQm4WaBPM0KQz2JscowRV3XQxQ9RIA9MwD1Ul75JFWai6jxzr4BTZ70AF1MW5CMAMuKjHVwNjN0u8pth5hPZDd30TeWzS9qcuWieWzK0i+TDhnFP4gPHYjP4XEGUpI/UriT1ZRhnrChbMxSNTS9FiJjQ/GbNk8CvicgWBJXSEddw08TINpWtMvfEuEg4d4cIY4Qf3vTsdh9Ex3drIlSvIr/F4NOiWZNscmyhvnmm6Ln+pRDTrZEXFGweiFkBZ2oTRh92xNgdtfMQDcLVqrB2khL2C3Jyzoj1k6JBvqbBrR8+97/Ul0vMJ9JpXNReSJaeJs9MQQp+7scUswGzsSQIrtd0H:+ga/thxBazBUF4zy4kYb34nyVHpcXeKY0KbFXs/Lemw=; _gat_UA-24386340-2=1; _gat_gtag_UA_137194665_26=1; _gat_gtag_UA_5723713_13=1; _gat_gtag_UA_7935519_2=1; _sctr=1%7C1711119600000; referrer=; session=1; _rdt_uuid=1709650814055.db0ef7bf-0cea-43ef-95f5-b13129623656; _scid=0a06e373-af58-4bfb-a795-daaa6d972d10; OptanonAlertBoxClosed=2024-03-05T14:59:52.086Z; _gcl_au=1.1.966782287.1706430073"
seatAvailable = sa.SeatAvailable(cookie_session)

result = ""
while result not in ('identify', 'captcha', 'error'):
  seatAvailable.request()
  if seatAvailable.getStatus() == 200:
    if seatAvailable.response.text.startswith("<!DOCTYPE html>"):
      result = 'captcha'
      Message.send_slack_notification(f"Required Capture Code  : {seatAvailable.captureUrl}")
      subprocess.Popen(['open', '-na', 'Safari', seatAvailable.captureUrl])
      #webbrowser.open_new_tab()
    elif seatAvailable.response.text != '[]':
      result = seatAvailable.getJsonReponse()
      Message.send_slack_notification("Available Seat!!!")
  else:
    result = seatAvailable.getJsonReponse()['response']
    if result == 'identify':
      Message.send_slack_notification(f"Required Login : {seatAvailable.ticketUrl}")
    elif result == 'captcha':
      Message.send_slack_notification(f"Required Capture Code  : {seatAvailable.captureUrl}")
      subprocess.Popen(['open', '-na', 'Safari', seatAvailable.captureUrl])
    else:
      result = 'error'
      Message.send_slack_notification(f"Occur Error : {seatAvailable.ticketUrl}")
  time.sleep(random.randint(55, 65))

print("exit")

