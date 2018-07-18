import  urllib.request
import  urllib.parse
import  json


url = "http://www.guqiankun.com/tools/music/"
headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
music = input("请输入音乐名：")
# 平台字典
pt_dict = {
    "netease": "网易",
    "qq": "QQ",
    "kugou": "酷狗",
    "kuwo" : "酷我",
    "xiami": "虾米",
    "baidu": "百度",
    "1ting": "一听",
    "migu": "咪咕",
    "lizhi": "荔枝",
    "qingting": "蜻蜓",
    "ximalaya": "喜马拉雅",
    "kg": "全民K歌",
    "5singyc": "5sing原创",
    "5singfc": "5sing翻唱"
}
for i in pt_dict.values():
    # 遍历字典的value并输出，end=" "表示输出不换行
    print(i,end=" ")

#判断输入是否正确
while True:
    try:
        pt_value = input("请选择平台：")
# 根据value值反推key值，这里可以有更好的做法。我是输入过了懒得改了。
        pt_key = list(pt_dict.keys())[list(pt_dict.values()).index(pt_value)]
    except ValueError:
        print("请输入列表里的平台!")
    else:
        break


#初始页
page = 1
while True:
    formdata = {
    "filter": "name",
    "input": music,
    "page": page,
    "type": pt_key
 }
    print(url)
    data = urllib.parse.urlencode(formdata).encode(encoding="utf-8")
    request = urllib.request.Request(url, data = data, headers =headers )
    response = urllib.request.urlopen(request).read().decode("utf-8")
    data_list = json.loads(response)['data']

# 初始化序号，url列表和音乐名列表
    XH = 0
    music_url = []
    music_name = []
    print("**************************************************\n")
    for items in data_list:
        title = items['title']
        author = items['author']
        each_url = items['url']
        music_url.append(each_url)
        music_name.append(title + "-" + author)
        XH += 1
        #里面的(X-len(**))是为了让排版更整齐，但是不知道为什么有的没用。。
        print(str(XH)+ " "*(6-len(str(XH)))+title.strip() + "-"*(30-len(title)) + author.strip())
    X = input("\n是否选择下一页?(按Y下一页)")
    if X == "Y":
        page += 1
        #重新初始化
        XH = 0
        music_url = []
        music_name = []
    else:
        break


while True:
    try:
        uesr_XH = int(input('请输入希望下载的音乐的序号：'))
        filename = music_name[uesr_XH-1] + ".mp3"
        print(filename+"正在下载！")
        music_request = urllib.request.Request(url = music_url[uesr_XH-1], headers = headers)
        music_response = urllib.request.urlopen(music_request).read()
        with open(filename, 'wb') as f:
            f.write(music_response)
            print("下载完成！")
    except Exception as e:
        print("发生异常！请重新输入序号！")
    else:
        print("谢谢使用！")
        break





