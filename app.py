from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom, BaseSize, ImagemapArea,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction, URIImagemapAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageSendMessage, ImageMessage, VideoMessage, AudioMessage, FileMessage, ImagemapSendMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)



app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('CK3ILqwfM4ALLtx45iOadDvCTU6AAPPaS/5+5DxX4OVfm5IkBmSWnAxU5Iyu3W52FPrefVEjn31rtfOh6p7P8z+gc9V342PmD0/DVAe0v4f6SQcX+0tHKbspctEIKMPBnOs/jBEkqU3Fg5VQAVoC3AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('158e54cf7e883373fe92f45ec90f1423')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text =  event.message.text
    # message = TextSendMessage(text=event.message.text)
    if text.find("自我介紹") != -1:
        self(event.reply_token)
    elif text.find("工作經驗") != -1:
        work(event.reply_token)
    elif text.find("專業技術") != -1:
        skill(event.reply_token)
    elif text.find("學術研究") != -1:
        academic(event.reply_token)
    elif text.find("競賽經歷") != -1:
        competition(event.reply_token)
    elif text.find("數據分析競賽") != -1:
        AIOT(event.reply_token)
    elif text.find("競賽成果") != -1:
        AIOTproject(event.reply_token)
    elif text.find("大學專題介紹") != -1:
        project(event.reply_token)
    elif text.find("專題成果") != -1:
        projectResult(event.reply_token)
    elif text.find("遊戲設計競賽") != -1:
        game(event.reply_token)
    elif text.find("遊戲成果") != -1:
        gameResult(event.reply_token)
    elif text.find("電子商務競賽") != -1:
        market(event.reply_token)
    elif text.find("競賽結果") != -1:
        marketResult(event.reply_token)
    elif text.find("求學歷程") != -1:
        education(event.reply_token)
    elif text.find("個人特質") != -1:
        personality(event.reply_token)
    

        
        pass
    else:
        default(event.reply_token)



# customize function
def self(reply_token):
    buttons_template = ButtonsTemplate(
        title='自我介紹', text='請選擇下方按鍵來了解更多：',
        thumbnail_image_url = 'https://imgur.com/wZAEy4Z.jpg', 
        actions=[
            MessageTemplateAction(label='「關於德馨」', text='關於德馨'),
            MessageTemplateAction(label='「求學歷程」', text='求學歷程'),
			MessageTemplateAction(label='「個人特質」', text='個人特質'),
        ])
    template_message = TemplateSendMessage(
        alt_text='自我介紹', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)

def education(reply_token):
   
    message1 = TextMessage(text="- 大學：國立高雄大學資訊管理系\n"+"- 研究所：台灣科技大學資管所(碩一)"+"--------------------------------------------------------------\n"+"在這兩個階段我都有幸碰到非常盡責的指導教授，"+"由於他們的幫助，讓我在每段期間都有良好的學習與成長!"+"受益良多!!!"+"\uDBC0\uDC8D"+"\uDBC0\uDC8D")
    
    line_bot_api.reply_message(reply_token,message1)

def personality(reply_token):
   
    message1 = TextMessage(text="- 做事積極負責、有效率；\n"+"- 有領導能力(曾帶領過系桌球隊)；\n"+"- 使命必達(幾乎沒有怨言)\n"+"以上是許多人對我的看法")
    
    line_bot_api.reply_message(reply_token,message1)


def work(reply_token):
   
    message1 = ImageSendMessage(
		original_content_url='https://imgur.com/unEjMBg.jpg',
        preview_image_url='https://imgur.com/unEjMBg.jpg')

    message2 = TextMessage(text="以上經歷是曾經在校支援的一些工作\n"+"(包含計畫撰寫、課程助教、輔導教師等)")
    message3= TextMessage(text="但我還沒有參與過任何企業實習計畫\n"+"希望能在碩一到畢業前獲取實習經驗!而LINE正是我夢想的企業之一"+"\uDBC0\uDC8D \n"+"期望有機會能夠加入你們的團隊，為你們盡心盡力!")

    line_bot_api.reply_message(
        reply_token,
        [message1,message2,message3])

def skill(reply_token):
    
    message1 = ImageSendMessage(
		original_content_url='https://imgur.com/kpKimU4.jpg',
        preview_image_url='https://imgur.com/kpKimU4.jpg')

    message2 = TextMessage(text="在程式語言的部分我接觸過前端設計(JavaScript、HTML、CSS)等做網頁設計與應用程式開發，也利用過C#、JAVA等做後端程式應用\n"+"而在研究所後由於課程與競賽需求我自學Python語言做資料分析與視覺處理\n"+"我主要運用的開發工具有Visual Studio、Jupyter、Unity、Eclipse等")
    message3= TextMessage(text="由於我的興趣是畫畫，因此有在自學電繪，主要使用的電繪軟體為Painting及Photoshop，大學時為了訂立目標，我曾經上架過LINE貼圖(不過當時繪畫能力還不夠成熟，就不獻醜了"+"\uDBC0\uDC8E !) \n"+"另外我的文書處理能力(包括Word撰寫與PPT製作能力...等)都很不錯喔!")

    line_bot_api.reply_message(
        reply_token,
        [message1,message2,message3])

def academic(reply_token):
   
    message1 = ImageSendMessage(
    original_content_url='https://imgur.com/HgClCtN.jpg',
    preview_image_url='https://imgur.com/HgClCtN.jpg')

    message2 = TextMessage(text="我在大學期間和專題組員與指導教授共同撰寫了兩篇研討會論文，主要是以智慧城市發展為主題，研究所碩一時則協助教授做論文發表，內容則為軟體協同開發相關。\n"+"我目前所屬研究室是軟體工程專業，指導教授為黃世禎教授，未來論文撰寫之主題偏向轉體專案開發與遊戲化之導入為主"+"\uDBC0\uDC90")
    message3 = TextMessage(text="以下附上研討會論文證明"+"\uDBC0\uDC41")
    message4 = ImageSendMessage(
    original_content_url='https://imgur.com/nlVVhyg.jpg',
    preview_image_url='https://imgur.com/nlVVhyg.jpg')
    message5 = ImageSendMessage(
    original_content_url='https://imgur.com/IMXQDSD.jpg',
    preview_image_url='https://imgur.com/IMXQDSD.jpg')

    line_bot_api.reply_message(
        reply_token,
        [message1,message2,message3,message4,message5])     
"""def TA(reply_token):
    image_url1 = createUri('/static/pics/TA.jpg')
    
    line_bot_api.reply_message(reply_token, template_message)"""

def competition(reply_token):
    Carousel_template = CarouselTemplate(
		columns=[
			CarouselColumn(
				title='北醫 x 麻省理工\n'+'AIOT智慧醫療聯合黑客松', text='特別獎 Most WOW Position ',
                thumbnail_image_url = 'https://imgur.com/jvEvwI1.jpg', 
                actions=[
					MessageTemplateAction(label='「數據分析競賽」', text='數據分析競賽'),
                    MessageTemplateAction(label='「競賽成果」', text='競賽成果'),
				]
			),
			CarouselColumn(
				title='國立高雄大學資訊管理學系107級畢業專題競賽', text='第一名',
                thumbnail_image_url = 'https://imgur.com/2xlZR0r.jpg', 
                actions=[
					MessageTemplateAction(label='「大學專題介紹」', text='大學專題介紹'),
                    MessageTemplateAction(label='「專題成果」', text='專題成果'),
				]
			),
			CarouselColumn(
				title='第三屆波克盃遊戲設計大賽', text='佳作',
                thumbnail_image_url = 'https://imgur.com/6466ec1.jpg', 
                actions=[
					MessageTemplateAction(label='「遊戲設計競賽」', text='遊戲設計競賽'),
                    MessageTemplateAction(label='「遊戲成果」', text='遊戲成果'),
				]
			),
			CarouselColumn(
				title='2016 EC-IC Yahoo!奇摩全國大專院校電子商務創意競賽 ', text='整體營運獎 特優',
                thumbnail_image_url = 'https://imgur.com/LGVMOgL.jpg', 
                actions=[
					MessageTemplateAction(label='「電子商務競賽」', text='電子商務競賽'),
                    MessageTemplateAction(label='「競賽結果」', text='競賽結果'),
				]
			),
		]
	)
    template_message = TemplateSendMessage(
        alt_text='競賽經歷', template=Carousel_template)
    
    line_bot_api.reply_message(reply_token, template_message)



def AIOT(reply_token):
    message1 = TextMessage(text="這個比賽是由台北醫學大學與麻省理工共同合辦的智慧醫療黑克松競賽，主要期望參賽者在為期3天的期間運用其給予之醫療相關open data，發想製作出對醫學界有幫助的事物或研究\n"+"--------------------------------------------------------------\n"+"本小組組成成員共有五位，分別有2位醫學界與3位資訊領域學生\n"+"我們有幸在最後拿到 Most WOW Position的特別獎殊榮!!")
    message2 = ImageSendMessage(
    original_content_url='https://imgur.com/KaWDXdw.jpg',
    preview_image_url='https://imgur.com/KaWDXdw.jpg')

    line_bot_api.reply_message(reply_token, [message1,message2])

def AIOTproject(reply_token):
    message1 = TextMessage(text="競賽成果:\n"+"我們將比賽提供的開放資料中之ICU病房資料做SQL資料萃取與數據分析技術，研究加護病房病患初始 Lactate 值正常之死亡率現象\n"+"下圖為我們的實作模型，歡迎參考!")
    message2 = ImageSendMessage(
    original_content_url='https://imgur.com/tOMkxrW.jpg',
    preview_image_url='https://imgur.com/tOMkxrW.jpg')
    message3 = ImageSendMessage(
    original_content_url='https://imgur.com/BgXnYcA.jpg',
    preview_image_url='https://imgur.com/BgXnYcA.jpg')
    
    line_bot_api.reply_message(reply_token, [message1,message2,message3])



def project(reply_token):
    message1 = TextSendMessage(text="我們製作一個協助市民與政府交流的第三方平台，作為智慧政府之開端。\n"+"--------------------------------------------------------------\n"+"主要方法是爬取高雄市政新聞文章Open Data給予市民進行討論回覆，並利用Jieba中文斷詞函式庫針對留言進行情緒分析與關鍵字分析，以了解該施政民意傾向為何(正向/負向)，\n"+"前台行動APP部份我們結合遊戲化元素，吸引使用者長期使用，而後台我們則以視覺化(如文字雲、雷達圖等)呈現相關數據給予需求人事使用。")
    message2 = TextSendMessage(text="關鍵字：輿情分析、關鍵詞分析、大數據視覺化呈現、軟體遊戲化\n "+"[下圖分別為專題前、後端架構圖]")
    message3 = ImageSendMessage(
    original_content_url='https://imgur.com/sQVlFb9.jpg',
    preview_image_url='https://imgur.com/sQVlFb9.jpg')
    message4 = ImageSendMessage(
    original_content_url='https://imgur.com/08IjOKJ.jpg',
    preview_image_url='https://imgur.com/08IjOKJ.jpg')
    
    line_bot_api.reply_message(reply_token, [message1, message2,message3, message4])

def projectResult(reply_token):
    message1 = TextSendMessage(text="以下為系統介面，歡迎參考\n"+"[第一張為後台資料分析介面]\n"+"[第二張為前台遊戲化資料蒐集介面]")
    message2 = ImageSendMessage(
    original_content_url='https://imgur.com/tNllhHF.jpg',
    preview_image_url='https://imgur.com/tNllhHF.jpg')
    message3 = ImageSendMessage(
    original_content_url='https://imgur.com/OTguGRy.jpg',
    preview_image_url='https://imgur.com/OTguGRy.jpg')

    
    line_bot_api.reply_message(reply_token, [message1, message2, message3])

def game(reply_token):
    message1 = TextSendMessage(text="此競賽為期一學期，最終參賽組別需在比賽當天開發出一套完全自行設計與開發的遊戲。\n"+"而本組以賣場購物車挑選商品為發想，透過手機畫面模擬真實購物畫面，做出極具生活化的休閒遊戲。\n"+"----------------------------------------------------------\n"+"本遊戲以Unity開發，並用2D繪圖呈現3D視覺效果，由於遊戲故事與角色設定鮮明獲得評審青睞。")
    message2 = TextSendMessage(text="遊戲名稱：阿母，砸摳")
    message3 = ImageSendMessage(
    original_content_url='https://imgur.com/zR0KNL4.jpg',
    preview_image_url='https://imgur.com/zR0KNL4.jpg')
    
    line_bot_api.reply_message(reply_token, [message1, message2, message3])

def gameResult(reply_token):
    message1 = TextSendMessage(text="遊戲介面都是我獨立完成的喔~"+"\uDBC0\uDC97\n"+"(下面附上遊戲介面圖)")
    message2 = ImageSendMessage(
    original_content_url='https://imgur.com/0QeSPty.jpg',
    preview_image_url='https://imgur.com/0QeSPty.jpg')
    message3 = ImageSendMessage(
    original_content_url='https://imgur.com/foKJNfZ.jpg',
    preview_image_url='https://imgur.com/foKJNfZ.jpg')
    
    line_bot_api.reply_message(reply_token, [message1, message2, message3])

def market(reply_token):
    message1 = TextSendMessage(text="此競賽為期兩個月，為YAHOO主辦的電子商務競賽，其主辦方期望參賽組員在YAHOO電商平台運用各種行銷方式販賣自選商品\n"+"本組組員利用各大社群平台行銷高雄在地名產地瓜酥")
    message2 = TextSendMessage(text="電商名稱：錦憨吉的夯吉人生")
    message3 = ImageSendMessage(
    original_content_url='https://imgur.com/lmyvoyU.jpg',
    preview_image_url='https://imgur.com/lmyvoyU.jpg')
    
    line_bot_api.reply_message(reply_token, [message1, message2, message3])

def marketResult(reply_token):
    message1 = TextSendMessage(text="本組在為期兩個月的比賽期間突破以往參賽組別成績：\n"+"1)粉專讚數突破1000\n"+"2)一路坐穩本次競賽周營業額第一寶位\n"+"3)競賽最終累計營業額突破20萬(最高營業額隊伍)")
    message2 = ImageSendMessage(
    original_content_url='https://imgur.com/oFrDjei.jpg',
    preview_image_url='https://imgur.com/oFrDjei.jpg')
    message3 = TextSendMessage(text="我們最後有被中國時報受訪呢!"+"\uDBC0\uDC97")
    message4 = ImageSendMessage(
    original_content_url='https://imgur.com/Lp1aw5X.jpg',
    preview_image_url='https://imgur.com/Lp1aw5X.jpg')
    
    line_bot_api.reply_message(reply_token, [message1, message2, message3, message4])

def default(reply_token):
    message1 = TextMessage(text="如果你想知道更多關於德馨的秘密可以輸入關鍵字或點選圖文選單喔!!"+
                                "\uDBC0\uDC8D")
    sticker1 = StickerSendMessage(
        package_id='11538',
        sticker_id='51626496')
    
    line_bot_api.reply_message(
        reply_token,
        [message1,
        sticker1])

def createUri(pathName):
    return 'https://'+appName+'.herokuapp.com'+pathName
    


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

