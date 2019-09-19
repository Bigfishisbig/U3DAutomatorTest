# coding=utf-8
__author__ = 'Administrator'

import json
import time
import http as cofHttp
import restful as CoRestful

class SendNew99U(object):
    """
    新99u推送消息接口封装
    QA机器人：
    uri:281474976720219
    password:4abb8356-d8bd-44eb-b8cc-ee6c2a281ad8
    """
    def __init__(self):
        """
        初始化
        """
        self.host = "im-agent.web.sdp.101.com"
        # self.port = None
        self.http_obj = cofHttp.Http(self.host)
        self.header = {
            "Content-Type": "application/json"
        }
        self.rest_o = CoRestful.Restful()

    def get_agent_mac_token(self):
        """
        获取推送号（只能是公众号）的授权信息
        body参数：
        uri: uid
        password: 密码
        返回值：
        {
            "mac_algorithm": "hmac-sha-256",
            "nonce": "1438677808798:2OLebj6B",
            "mac": "aIlsdFuRcV0jji+u+uwAw3hsNFSS2YJ95LnjYS0h9OY=",
            "access_token": "agent_281474976720145"
        }
        """
        # 1.发送请求
        url = "/v0.2/api/agents/users/tokens"
        body = {
            "uri": "281474976720219",
            "password": "4abb8356-d8bd-44eb-b8cc-ee6c2a281ad8"
        }
        param = json.dumps(body)
        self.http_obj.set_header(self.header)
        res = self.http_obj.post(url, param)
        code = 200
        msg = "获取代理用户授权失败"
        data = self.rest_o.parse_response(res, code, msg)

        # 2.拼装数据
        access_token = data['access_token']
        nonce = data['nonce']
        mac = data['mac']
        authorization = 'MAC id="%s",nonce="%s",mac="%s"' % (access_token, nonce, mac)
        #print "authorization: ", authorization
        return authorization

    def send_to_receivers(self, info, receiver_list, ishtml = False, html_type = "box/xml"):
        """
        发送内容到各知照人的99u
        content：内容
        list：需要通知的人的名单，list类型
        """
        # 1.获取代理授权信息
        content_type = "text/plain"
        authorization = self.get_agent_mac_token()
        self.header["Authorization"] = authorization
        time.sleep(5)
        # 2.发送消息
        url = "/v0.2/api/agents/messages"
        if ishtml:
            content_type = html_type
        content = "Content-Type:" + content_type + "\r\n\r\n%s" % info
        body = {
            "filter": [
                {
                    "name": "uri",
                    "args": {
                        "uri_list": receiver_list
                    }
                }
            ],
            "body": {
                "content": content,
                "flag": 0
            }
        }
        param = json.dumps(body)
        self.http_obj.set_header(self.header)
        print param
        print url

        code = 200
        msg = "send message to anyone failed!"
        res = self.http_obj.post(url, param)
        self.rest_o.parse_response(res, code, msg)

    def send_to_groups(self, info, group_list, ishtml = False, html_type = "box/xml"):
        """
        发送内容到99u群
        content：内容
        group_id：群id列表，list类型
        """
        # 1.获取代理授权信息
        content_type = "text/plain"
        authorization = self.get_agent_mac_token()
        self.header["Authorization"] = authorization

        # 2.发送消息
        url = "/v0.2/api/agents/messages"
        if ishtml:
            content_type = html_type
        content = "Content-Type:" + content_type + "\r\n\r\n%s" % info
        body = {
            "filter": [
                {
                    "name": "gid",
                    "args": {
                        "gid": group_list
                    }
                }
            ],
            "body": {
                "content": content,
                "flag": 0
            }
        }
        param = json.dumps(body)
        self.http_obj.set_header(self.header)

        code = 200
        msg = "发送消息给群组失败"
        res = self.http_obj.post(url, param)
        self.rest_o.parse_response(res, code, msg)

if __name__ == "__main__":
    # 旧99u方式：
    # content = "lsx testing~!!"
    # group_list = [526397]
    # send_o = Send99U()
    # send_o.send_to_receivers(content, group_list)

    # 新99u方式：
    # 推送给个人

    content = ""
    """
    content = "<box data-summary='百团大战'>"
    content += "<div class=\"row\">"
    content += "<div class=\"col-6\">"
    content += "<span style=\"font-size: 1em; font-weight: bold; color:#FF0000;\">【百团大战】战时提醒：</span>"
    content += "</div>"
    content += "</div>"
    
    content += "<div class=\"row\">"
    content += "<div class=\"col-6\">"
    content += "<span style=\"font-size: 2em; color:#FF0000;\">时间：2016年5月21日—2016年6月20日23:59</span>"
    content += "<span style=\"font-size: 2em; color:#FF0000;\">\n1、务必日事日清！补签不算！</span>"
    content += "<span style=\"font-size: 2em; color:#FF0000;\">\n2、团队的异常单不能超过5单！所以请杜绝出现异常</span>"
    content += "<span style=\"font-size: 2em; color:#FF0000;\">\n(漏打指纹、事后填单)！</span>"
    content += "<span style=\"font-size: 2em; color:#FF0000;\">\n3、单据及时完成率100%，请务必及时处理单据！</span>"
    content += "</div>"    
    content += "</div>"
    
    content += "<div class=\"row\">"
    content += "<div class=\"col-6\">"
    content += "<span style=\"font-size: 1em; font-weight: bold; color:#FF0000;\">童鞋们！！！为了银子！$_$ 请时刻保持警惕！！</span>"
    content += "<span style=\"color:#D3D3D3;\">\n———————————————————————</span>"
    content += "</div>"    
    content += "</div>"   
    
    content += "<div class=\"row\">"
    content += "<div class=\"col-4\">"
    content += "</div>"   
    content += "<div class=\"col-2\">"
    content += "<button class=\"link-default\" style=\"text-align:right\" data-href=\"http://777.nd.com.cn/news/news.aspx?id=20022\">查看详情</button>" 
    content += "</div>" 
    content += "</div>" 
    
    content += "</box>"
    """
    group_list = [108917678]
    receiver_list = [235257]
    send_o = SendNew99U()
    send_o.send_to_receivers(content, receiver_list, ishtml=True)
    # send_o.send_to_groups(content, group_list, ishtml=True)

    # 推送给群
    # content = "能收到吗？"
    # group_list = [2180138, 2146295]
    # send_o = SendNew99U()
    # send_o.send_to_groups(content, group_list)

