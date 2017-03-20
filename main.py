from personal_python_collections.cmd_utility import *
from personal_python_collections.networking import *
from personal_python_collections.regexp_string import *
from personal_python_collections.file_manager import *
from personal_python_collections.BeautifulSoup_utility import *


# personal_python_collections.BeautifulSoup_utility的使用
def beautifulSoup_utility_demo():

    web_string = """
                    <div class="download_content">
                    <div class="download_pic">
                        <a href="http://www.gamersky.com/Soft/201406/375305.shtml" target="_blank"><img style="width:110px" alt="《植物大战僵尸：花园战争》XBOX360简体中文GOD版下载" src="http://img1.gamersky.com/image2014/06/20140624g_1/gamersky_01small_02_20146241850859.jpg" /></a>
                    </div>
                    <div class="content_right">
                        <div class="download_title"><a href="http://www.gamersky.com/Soft/201406/375305.shtml" title="《植物大战僵尸：花园战争》XBOX360简体中文GOD版下载" target="_blank">《植物大战僵尸：花园战争》XBOX360简体中文G</a></div>
                        <div class="download_short">
                            <ul>
                                <li><span class="short_title">上市时间：</span><span class="short_content">2014-06-25</span><span class="short_title">游戏大小：</span><span class="short_content">2.31 GB</span></li>
                                <li><span class="short_title">游戏类型：</span><span class="short_content"><a href="/Soft/tv/xbox360/2-0-3-0-0-0-0-00.html">第三人称射击</a></span><span class="short_title">游戏语言：</span><span class="short_content"><a href="/Soft/tv/xbox360/0-0-3-0-0-0-0-00.html">简体中文</a></span></li>
                                <li class="noneboder"><span class="short_title">游戏下载：</span><span class="short_content"><a href="http://www.gamersky.com/Soft/201406/375305.shtml" target="_blank">点击进入</a></span></li>
                            </ul>
                        </div>
                    </div>
                </div>
    """
    soup_manager = BeautifulSoupManager(web_string)

    for item in soup_manager.find_all('div', 'class = download_content'):

        # 开始查找所有的子节点
        for data in item.descendants:

            # 确保是Tag对象
            if BeautifulSoupElement(data).is_Tag:

                # 找到了div class="download_title"的Tag
                if BeautifulSoupElement(data).is_match('div', 'class = download_title'):
                    print("网页名字：%s" % data.string)

                # 找到了div class="download_pic"的Tag
                if BeautifulSoupElement(data).is_match('div', 'class = download_pic'):
                    print("下载地址：%s" % data.a['href'])
                    print("图片地址：%s" % data.a.img['src'])

                # 找到span class="short_title"的Tag
                if BeautifulSoupElement(data).is_match('span', 'class = short_title'):
                    print("%s%s" % (data.string, data.next_sibling.string))


# personal_python_collections.file_manager的使用
def file_manager_demo():

    for item in FileObjectManager(FileObject(File.path())).scan_with_depth(1).all_file_objects():

        file = FileObject.item(item)
        file.show_info()


# personal_python_collections.regexp_string的使用
def regexp_demo():
    # 查询的例子
    def search():
        print(RegExpString('windows 98').search_with_pattern(r'\d+').search_result)

    # 替换的例子
    def replace():
        print(RegExpString('windows 98').replace_with_pattern(r'\d+', 'XP').replace_result)

    # 遍历
    def item_list():
        for item in RegExpString('48 29 29 10').find_all(r'\d+').item_list:
            print(item)

    search()
    replace()
    item_list()


# personal_python_collections.networking的使用
def networking_demo():
    # get请求
    def get():
        web_text = Networking("http://www.cnblogs.com/").get().response.text
        print(web_text)

    # post请求
    def post():
        web_text = Networking("http://www.cnblogs.com/").post().response.text
        print(web_text)

    # 下载
    def download():
        def download_report(block_num, block_size, size):
            per = 100.0 * block_num * block_size / size
            print("%2.2f%%" % per)

        url = "http://hiphotos.baidu.com/mgzcalice/pic/item/ed96859676e2607dd0135ee4.jpg"
        dst = '/Users/YouXianMing/Desktop/ed96859676e2607dd0135ee4.jpg'

        network = Networking(url, dst, download_report).download()
        print(network.message)
        print(network.file_path)

    get()
    post()
    download()


# personal_python_collections.cmd_utility import的使用
def cmd_demo():

    def normal():

        print(Process("""cd / && ls | grep 'U'""").run().output)

    def special():

        print(Process('ping www.cnblogs.com').run(timeout=3).output)

    normal()
    special()


# 查询pip安装的python工具以及其版本
def pip_freeze_list(width=20):

    for item in Process("pip3 freeze").run().output.split('\n'):

        if len(item) and len(RegExpString(item).search_with_pattern(r'.+0[.]0[.]0$').search_result) == 0:

            tmp_list = item.split('==')
            name = tmp_list[0]
            ver = tmp_list[1]
            print('%s %s' % (name.ljust(width), ver))


# 查询pip安装的python工具以及其详细信息
def pip_freeze_detail_list(width=20):

    for item in Process("pip3 freeze").run().output.split('\n'):

        if len(item) and len(RegExpString(item).search_with_pattern(r'.+0[.]0[.]0$').search_result) == 0:

            tmp_list = item.split('==')
            name = tmp_list[0]
            print(Process("pip3 show %s" % name).run().output)

beautifulSoup_utility_demo()
# file_manager_demo()
# regexp_demo()
# networking_demo()
# cmd_demo()
# pip_freeze_list()
# pip_freeze_detail_list()

