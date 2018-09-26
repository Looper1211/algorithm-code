import requests
from lxml import etree
import re
import time
from datetime import datetime, timedelta
import xlwt


class Record(object):
    time_9 = datetime.strptime("09:00:00", "%H:%M:%S")
    time_9_20 = datetime.strptime("09:20:00", "%H:%M:%S")
    time_10_30 = datetime.strptime("10:30:00", "%H:%M:%S")
    time_10_50 = datetime.strptime("10:50:00", "%H:%M:%S")
    time_13 = datetime.strptime("13:00:00", "%H:%M:%S")
    time_13_20 = datetime.strptime("13:20:00", "%H:%M:%S")
    time_18 = datetime.strptime("18:00:00", "%H:%M:%S")
    time_20 = datetime.strptime("20:00:00", "%H:%M:%S")
    time_22 = datetime.strptime("22:00:00", "%H:%M:%S")

    minutes_20 = timedelta(minutes=20)

    def __init__(self, index):
        self.recode_start = None
        self.recode_end = None
        self.ban = "PH"
        self.flag = 0  # 0正常，1补卡一次
        self.late = 0  # 不迟到，1 迟到
        self.index = index
        self.proposal = ""

    def read_recode(self, recode_time):
        recode_time = datetime.strptime(recode_time.split(" ")[-1], "%H:%M:%S")
        if self.recode_start == None:
            self.recode_start = recode_time
        elif self.recode_start > recode_time:
            self.recode_start = recode_time

        if self.recode_end == None:
            self.recode_end = recode_time
        elif self.recode_end < recode_time:
            self.recode_end = recode_time

    def slove(self):
        if self.recode_start == None:
            self.ban = "PH"
            return

        if self.recode_start <= self.time_9_20:
            if self.recode_start > self.time_9:
                self.late = 1

            if self.recode_end < self.time_18:
                self.ban = "晚017"
                self.flag = 1
                self.proposal = "20:00"
            elif self.time_18 <= self.recode_end < self.time_20:
                self.ban = "早002"
            elif self.recode_end >= self.time_20:
                self.ban = "晚017"

            return

        if self.time_9_20 < self.recode_start <= self.time_10_50:

            if self.recode_start > self.time_10_30:
                self.late = 1

            if self.recode_end < self.time_20:
                self.ban = "晚017"
                self.flag = 1
                self.proposal = "20:00"
            elif self.recode_end >= self.time_20:
                self.ban = "晚017"

            return

        if self.recode_start <= self.time_13_20:

            if self.recode_start > self.time_13:
                self.late = 1

            if self.recode_end < self.time_18:
                self.flag = 1
                self.ban = "早017"
                self.proposal = "22:00"
            elif self.time_18 <= self.recode_end < self.time_20:
                self.ban = "早002"
                self.flag = 1
            elif self.time_20 <= self.recode_end < self.time_22:
                self.ban = "晚017"
                self.flag = 1
                self.proposal = "20:00"
            elif self.recode_end >= self.time_22:
                self.ban = "早017"

            return

        if self.recode_start > self.time_13_20:
            if self.recode_end < self.time_18:
                self.ban = "PH"
                self.flag = 2
                self.proposal = "价值溢出"
            elif self.time_18 <= self.recode_end < self.time_20:
                self.ban = "早002"
                self.flag = 1
                self.proposal = "09:00"
            elif self.time_20 <= self.recode_end:
                self.ban = "晚017"
                self.flag = 1
                self.proposal = "10:30"

    def slove_end(self):
        if self.recode_start:
            if self.recode_start > self.time_13_20:
                self.recode_start = " " * 12
            if self.recode_end < self.time_18:
                self.recode_end = " " * 12

    def print_recode(self):

        if self.recode_start:
            print("{}\t{}\t{}\t{}\t\t{}\t{}".format(self.index + 1,
                                                    self.recode_start.strftime(
                                                        "%H:%M:%S") if isinstance(self.recode_start,
                                                                                  datetime) else self.recode_start,
                                                    self.recode_end.strftime(
                                                        "%H:%M:%S") if isinstance(self.recode_end,
                                                                                  datetime) else self.recode_end,
                                                    self.ban,
                                                    self.flag,
                                                    self.late))
        else:
            print("{}\t{}{}{}\t        {}\t{}".format(self.index + 1,
                                                      " " * 16,
                                                      " " * 16,
                                                      self.ban,
                                                      self.flag,
                                                      self.late))


class QiankaSpider(object):
    def __init__(self, username, password):
        self.login_url = "http://211.103.142.26:6301/iclock/accounts/login/"
        self.home_url = "http://211.103.142.26:6301/iclock/staff/"
        self.qianka_url = "http://211.103.142.26:6301/iclock/staff/transaction/?p={}&t=staff_transaction.html&UserID__id__exact={}&fromTime={}&toTime={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36"
        }
        self.session = requests.Session()
        self.uid = None
        now = time.localtime()
        mon_time = datetime.strptime(
            '%d-%02d-01' % (now.tm_year, now.tm_mon), "%Y-%m-%d")
        self.month = mon_time.month
        self.start_time = mon_time.strftime("%Y-%m-%d")
        self.end_time = datetime.now().strftime("%Y-%m-%d")
        self.password = password
        self.username = username
        self.real_name = ""

    def login(self):
        data = {
            "username": self.username,
            "password": self.password
        }
        self.session.post(self.login_url, headers=self.headers, data=data)

    def parse_url(self, url):
        response = self.session.get(url, headers=self.headers)
        return response.content.decode()

    def get_uid(self):
        html_str = self.parse_url(self.home_url)
        try:
            ret = re.findall(r"uid=\"(\d+)\";", html_str)
            self.uid = ret[0]
            self.real_name = re.findall(
                r"<strong>员工 (.*?)</strong>", html_str)[0]
            return self.uid
        except:
            return None

    def get_record(self):
        reord_list = []
        page_index = 1
        total_page = 1
        while page_index <= total_page:
            html_str = self.parse_url(
                url=self.qianka_url.format(page_index, self.uid, self.start_time, self.end_time))
            total_count = int(re.findall(
                r"totalRecCnt_emp=(\d+);", html_str)[0])
            total_page = total_count // 40 if total_count % 40 == 0 else total_count // 40 + 1

            el = etree.HTML(html_str)
            tr_list = el.xpath("//table[@id='tbl']//tr")
            for tr in tr_list[1:-1]:
                ret = tr.xpath("./td[2]/text()")[0]

                reord_list.append(ret)
            page_index += 1
        return reord_list

    def recode(self, ret_list):
        record_list = []
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(days[self.month]):
            record_list.append(Record(i))

        for ret in ret_list:
            day = int(ret.split(" ")[0].split("-")[-1]) - 1
            record_list[day].read_recode(ret)

        for record in record_list:
            record.slove()
            record.slove_end()

        end_day = int(self.end_time.split("-")[-1]) - 1

        # for i in range(end_day):
        #     record_list[i].print_recode()

        return record_list

    def write_excle(self, record_list):
        book = xlwt.Workbook()
        sheet_ban = book.add_sheet('班次')
        for i in range(len(record_list)):
            sheet_ban.write(0, i, record_list[i].index+1)
            sheet_ban.write(1, i, record_list[i].ban)

        sheet_detail = book.add_sheet("考勤详情")

        sheet_detail.write(0, 0, "日期")
        sheet_detail.write(0, 1, "上班打卡")
        sheet_detail.write(0, 2, "下班打卡")
        sheet_detail.write(0, 3, "建议排班")
        sheet_detail.write(0, 4, "补卡")
        sheet_detail.write(0, 5, "迟到")
        sheet_detail.write(0, 6, "补卡时间")

        for i in range(len(record_list)):
            sheet_detail.write(
                i+1, 0, "{}月{}日".format(self.month, record_list[i].index+1))

            recode_start = record_list[i].recode_start
            if recode_start and isinstance(recode_start, datetime):
                sheet_detail.write(i+1, 1, recode_start.strftime("%H:%M:%S"))

            record_end = record_list[i].recode_end
            if record_end and isinstance(record_end, datetime):
                sheet_detail.write(i+1, 2, record_end.strftime("%H:%M:%S"))

            sheet_detail.write(i+1, 3, record_list[i].ban)
            sheet_detail.write(
                i+1, 4, "补卡" if record_list[i].flag == 1 else "")
            sheet_detail.write(
                i+1, 5, "迟到" if record_list[i].late == 1 else "")
            sheet_detail.write(
                i+1, 6, record_list[i].proposal)

        book.save('排版_{}月_{}.xls'.format(self.month, self.real_name))

    def run(self):
        self.login()
        ret = self.get_uid()
        if ret:
            ret_list = self.get_record()
            record_list = self.recode(ret_list)
            self.write_excle(record_list)
            print("{} {}月 排班完成".format(self.real_name,self.month))
        else:
            print("用户名或密码错误")


if __name__ == '__main__':
    qianka = QiankaSpider("87030", "87030")
    qianka.run()
