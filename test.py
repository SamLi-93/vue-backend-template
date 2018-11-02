# -*- coding:utf-8 -*-
from flask import Flask
from flask_cors import CORS
import json
from flask import jsonify

app = Flask(__name__)
CORS(app)


@app.route("/user/login", methods=['GET', 'POST'])
def test():
    res_data = {
        "code": 0,
        "data": {
            "token": '123456'
        }
    }
    return jsonify(res_data)


@app.route("/user/info", methods=['GET'])
def test1():
    res_data = {
        "code": 0,
        "data": {
            "roles": ['1', '2']
        }
    }
    return jsonify(res_data)


@app.route("/user/menu", methods=['GET'])
def menu():
    res_data = {
        "code": 0,
        "message": "获取权限成功",
        "data": {
            "menuList": [
                {
                    "parent": "investor",
                    "children": [
                        {"name": "investor"}
                    ]
                },
                {
                    "parent": "financing",
                    "children": [
                        {"name": "order"},
                        {"name": "appeal"}
                    ]
                }
            ]
        }
    }
    return jsonify(res_data)


@app.route("/table/list", methods=['GET'])
def test2():
    res_data = {
        "code": 0,
        "data": {
            "total": 2,
            "labelKeys": [
                {"key1": '表头1', "key2": '表头2', "key3": '表头3', "key4": '表头4', "key5": '表头5', }
            ],
            "items": [
                {
                    "id": "640000204138129",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "6138129",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "1",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "3",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "61384129",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "5",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "6",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "8",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "9",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "91",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "92",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },
                {
                    "id": "93",
                    "title": "Ktylcwifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                },

                {
                    "id": "640000201804138129",
                    "title": "Ktylcwe dfcsf lkbifltquk dmudoumlk myrebmnlso tikbvtr gjwechg mthhcvv wsdl gjfhwlcvgr qqld skjt kic hutjlztpf uxpke okzmuxj rvg lhges.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "1988-09-23 19:53:15",
                    "pageviews": 3119
                }, {
                    "id": "610000198507239687",
                    "title": "Xush qrnekkkme ziswic lnet vtegjixu xabvyd gpx lfqzjudvq bpzxzjflbn oldtxp uriqhjmbb vstcpu wbieuox ywt jog gfkingru.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "2015-08-23 07:59:47",
                    "pageviews": 3946
                }, {
                    "id": "22000019920502202X",
                    "title": "Tcyiw inqruh fgdpe rdpkyr nboer yqyrrhb rpcsot sybz jpbmkfmntx vtzscq cnu.",
                    "status": "deleted",
                    "author": "name",
                    "display_time": "1984-09-22 06:02:28",
                    "pageviews": 4963
                }, {
                    "id": "540000199009126643",
                    "title": "Jschtegg tjq jfpd xqbgmhhe cauorj vcgfs yyfjtiebhj ujuoxzkkc rmsynohxc zhvlao lvonmiae quvpcu dtwcmgxvs wdfkjmn.",
                    "status": "draft",
                    "author": "name",
                    "display_time": "2000-11-20 02:51:00",
                    "pageviews": 2059
                }, {
                    "id": "710000198404205656",
                    "title": "Nyrski qqbdpqbrkt mkbxbzai kuley bujv hvf obofidvh iirjjpssu iqyw zfzz nuwgj gbmkbcnlk.",
                    "status": "deleted",
                    "author": "name",
                    "display_time": "2006-04-27 09:33:43",
                    "pageviews": 3118
                }]
        }
    }
    return jsonify(res_data)
