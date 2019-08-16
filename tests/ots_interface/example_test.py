from utils.assertion import isIn,wcf_isIn
import json
import time
import random
def now():
    return time.strftime("%Y-%m-%d %H:%M:%S")
def ymd():
    return time.strftime("%Y%m%d")
def rand100_999():
    return str(random.randint(100, 999))

def test_All(self,args):
    print(args, type(args))
    if self.obj.excel.getCaseID(args) != "":
        print("第" + str(args+1) + "行")
        if self.obj.excel.getPre_CaseID(args) != "":
            case = eval(self.obj.excel.getPre_CaseID(args))
            for i in case:
                run_predata(self,i)
        if self.obj.excel.getHeaders(args) != "":
            '''获取请求头，如果没有则用默认请求头'''
            header = eval(self.obj.excel.getHeaders(args))
        else:
            header = self.obj.excel.getDefaultHeaders()
        if self.obj.excel.getAuthorization(args) != "":
            '''添加授权到headers'''
            data = eval(self.obj.excel.getAuthorization(args))
            header = self.obj.get_authorizaiton(header, data[0], data[1])
        if self.obj.excel.getRequest_Type(args).lower() == "post":
            '''如果excel里面是post请求，则使用post请求'''
            print("header:", header)
            url = self.obj.excel.getUrl(row=args)
            #data = eval(json.dumps(self.obj.excel.get_request_data(row=args)))
            data = eval(json.dumps(str(eval(self.obj.excel.get_request_data(row=args).replace("null", '""')))))#将请求参数值为null变成空值
            print("请求地址", url, "请求地址结束")
            print("请求参数", data, "请求参数结束")
            r = self.obj.post_new(url=url,data=data.encode("utf-8"), header=header)
            description = self.obj.excel.getTitle(args)
            expect = self.obj.excel.getExcept(args)
            print("用例描述", description, "用例描述结束")
            print("期望", expect, "期望结束")
            print("返回报文",r.text,"返回报文结束")
            if self.obj.excel.getsql(args)!="":
                '''执行sql操作，可以是多条sql'''
                sqls = eval(self.obj.excel.getsql(args))
                for sql in sqls:
                    #print(sql)
                    result = self.obj.db.update(sql)
                    print("数据库返回：",result)
                    self.assertTrue(result)
                    if result:
                        print(sql+"执行成功")
                    else:
                        print(sql + "执行失败")
            if self.obj.excel.getExcept(args) != "":
                '''做断言'''
                isIn(self, r, args)
        if self.obj.excel.getRequest_Type(args).lower() == "webservice":
            '''如果excel里面是webservice请求，则使用webservice请求'''
            url = self.obj.excel.getUrl(row=args)
            # data = eval(json.dumps(self.obj.excel.get_request_data(row=args)))
            data = self.obj.excel.get_request_data(row=args)  # 将请求参数值为null变成空值
            print("请求地址", url, "请求地址结束")
            print("请求参数", data, "请求参数结束")
            description = self.obj.excel.getTitle(args)
            expect = self.obj.excel.getExcept(args)
            print("用例描述", description, "用例描述结束")
            print("期望", expect, "期望结束")
            r = self.obj.request_wcf(url=url, data=data)
            print("返回报文", r, "返回报文结束")
            if self.obj.excel.getsql(args) != "":
                '''执行sql操作，可以是多条sql'''
                sqls = eval(self.obj.excel.getsql(args))
                for sql in sqls:
                    # print(sql)
                    result = self.obj.db.update(sql)
                    print("数据库返回：", result)
                    self.assertTrue(result)
                    if result:
                        print(sql + "执行成功")
                    else:
                        print(sql + "执行失败")
            if self.obj.excel.getExcept(args) != "":
                '''做断言'''
                wcf_isIn(self, r, args)

        elif self.obj.excel.getRequest_Type(args).lower() == "get":
            '''如果excel里面是get请求，则使用get请求'''
            url = self.obj.excel.getUrl(row=args)
            print("请求地址", url, "请求地址结束")
            r = self.obj.get_new(args, header=header)
            description = self.obj.excel.getTitle(args)
            expect = self.obj.excel.getExcept(args)
            print("用例描述", description, "用例描述结束")
            print("期望", expect, "期望结束")
            print("返回报文", r.text, "返回报文结束")
            if self.obj.excel.getExcept(args) != "":
                '''做断言'''
                isIn(self, r, args)
            if self.obj.excel.getsql(args) != "":
                '''执行sql操作，可以是多条sql'''
                sqls = eval(self.obj.excel.getsql(args))
                for sql in sqls:
                    self.obj.db.update(sql)
    else:
        print("第" + str(args+1) + "行测试数据未填写")
def run_predata(self,args):
    print(args, type(args))
    if self.obj.excel_pre.getCaseID(args) != "":
        print("第" + str(args+1) + "行")
        if self.obj.excel_pre.getHeaders(args) != "":
            '''获取请求头，如果没有则用默认请求头'''
            header = eval(self.obj.excel_pre.getHeaders(args))
        else:
            header = self.obj.excel_pre.getDefaultHeaders()
        if self.obj.excel_pre.getAuthorization(args) != "":
            '''添加授权到headers'''
            data = eval(self.obj.excel_pre.getAuthorization(args))
            header = self.obj.get_authorizaiton(header, data[0], data[1])
        if self.obj.excel_pre.getRequest_Type(args).lower() == "post":
            '''如果excel里面是post请求，则使用post请求'''
            print("header:", header)
            url = self.obj.excel_pre.getUrl(row=args)
            data = eval(json.dumps(str(eval(self.obj.excel_pre.get_request_data(row=args).replace("null", '""')))))
            print("【请】【求】【参】【数】--：",data)
            r = self.obj.post_new(url=url,data=data.encode("utf-8"), header=header)
            print(r.text)
            if self.obj.excel_pre.getsql(args)!="":
                '''执行sql操作，可以是多条sql'''
                print("数据库语句", self.obj.excel_pre.getsql(args))
                sqls = eval(self.obj.excel_pre.getsql(args))
                print("数据库语句sqls", sqls)
                for sql in sqls:
                    print(sql)
                    self.obj.db.update(sql)
        elif self.obj.excel_pre.getRequest_Type(args).lower() == "get":
            pass
            '''如果excel里面是get请求，则使用get请求'''
            r = self.obj.get_new(args, header=header)
            if self.obj.excel_pre.getsql(args) != "":
                '''执行sql操作，可以是多条sql'''
                sqls = eval(self.obj.excel_pre.getsql(args))
                for sql in sqls:
                    self.obj.db.update(sql)
    else:
        print("第" + str(args+1) + "行测试数据未填写")
if __name__ == "__main__":
    print("test")