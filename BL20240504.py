# -*- coding = utf-8 -*-
# @Time: 2024/5/4 10:30
# @Author: JaDM
# @File: BL20240504.py
# @Software: PyCharm
# @Url: https://www.bilibili.com/video/BV12E411A7ZQ/?p=17&spm_id_from=pageDriver&vd_source=a2baf25ae75bc2f30de0f8ce15b304f3

from bs4 import BeautifulSoup
import re
import urllib
import xlwt
import sqlite3

# 1.爬取网页
# 2.解析数据
# 3.保存数据

def doubantop250():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # 3.保存数据

    savepath = '.\\豆瓣电影Top250.xls'
    dbpath = '.\\project_douban.db'
    saveData(datalist,savepath)
    saveData2DB(datalist,dbpath)

    # webspider(baseurl)

findlink = re.compile(r'<a class="" href="(.*?)">')
findImgSrc = re.compile(r'<img alt=.*class="" src="(.*?)"', re.S)
findTittle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 1.获取数据
def getData(baseurl):
    datalist = []
    for i in range(10):
        url = baseurl + str(i * 25)
        html = webspider(url)
        # 2.解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # div class="item"
            # print(item)
            oneMoiveData = []
            item = str(item)

            link = re.findall(findlink, item)[0]
            # print(link)
            oneMoiveData.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            # print(imgSrc)
            oneMoiveData.append(imgSrc)

            tittles = re.findall(findTittle, item)
            # print(tittles)
            if len(tittles) == 2:
                ctittle = tittles[0]
                oneMoiveData.append(ctittle)
                otittle = tittles[1].replace("/", '')
                # print(otittle)
                oneMoiveData.append(otittle)
            else:
                oneMoiveData.append(tittles[0])
                oneMoiveData.append(' ')

            rating = re.findall(findRating, item)[0]
            # print(rating)
            oneMoiveData.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            # print(judgeNum)
            oneMoiveData.append(judgeNum)

            inq = re.findall(findInq, item)
            # print(inq)
            if len(inq) != 0:
                # inq = inq.replace('。','')
                oneMoiveData.append(inq[0])
            else:
                oneMoiveData.append(' ')

            bd = re.findall(findBd, item)[0]
            # print(bd)
            bd = re.sub('<br(\s+)?/>(\s+)?', '', bd)  # bd = bd.replace('<br/>',' ')
            # print(bd)
            bd = re.sub(' / ', ' ', bd)
            # print(bd)
            bd = bd.strip()
            # print(bd)
            oneMoiveData.append(bd)

            datalist.append(oneMoiveData)
    # print(datalist)
    return datalist


# 1.1 爬取网页
def webspider(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    webrequest = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(webrequest)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as error:
        if hasattr(error, "reason"):
            print("error occurred:", error.reason)
        if hasattr(error, "code"):
            print("error code:", error.code)
    finally:
        return html


# 3.保存数据
def saveData(datalist, savapath):
    # pass
    # 用.xls保存
    excelbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
    excelsheet = excelbook.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    column = ("电影详情链接", "电影海报链接", "影片中文译名", "影片其他译名", "电影评分", "评价人数", "概况", "相关信息")
    for i in range(8):
        excelsheet.write(0, i, column[i])
    for i in range(250):
        print(f'no.{i+1} written successfully')
        data = datalist[i]
        for j in range(8):
            excelsheet.write(i+1,j,data[j])
    excelbook.save(savapath)


def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index in (4,5):
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into doubanMovieTop250(
            info_link
            ,pic_link
            ,cname
            ,oname
            ,rating
            ,rated
            ,introduction
            ,info
            )
            values(
            %s
            );
        '''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table if not exists doubanMovieTop250(
            id integer primary key autoincrement
            ,info_link text
            ,pic_link text
            ,cname varchar
            ,oname varchar
            ,rating numeric
            ,rated numeric
            ,introduction text
            ,info text
        );
    '''
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    doubantop250()
    print('Done')

# 将数据存入数据库
# conn = sqlite3.connect("test_sqlite.db")
# print("open database successfully")
# cur = conn.cursor()
# sql = '''
#
# '''
# cur.execute(sql)
# conn.commit()
# cur.close()
# conn.close()

# Excel写入九九乘法表

# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('s1')
# # worksheet.write(0, 3, 100)
# for i in range(1,10):
#     for j in range(1,i+1):
#         worksheet.write(i - 1, j - 1, f'{i} * {j} = {i * j}')
#         # print(i - 1, j - 1, f'{i} * {j} = {i * j}')
# workbook.save('九九乘法表.xls')
