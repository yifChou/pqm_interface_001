# from base.method import *
# re = Method()
# # response = re.request_wcf(url="",data="")
# from suds.client import Client
# client = Client("http://120.76.198.181:9701/APIServicesDelegate/MEX")
# client.set_options(location = "net.tcp://10.168.95.140:9702/APIServicesDelegate/mex")
# print(client)
# #client.service.FindCustomerInvoice(customerCode=100010,SystemSource="YT")

# import requests
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# url = "http://10.168.95.149:8055/"
# data = "UserName=admin&Password=123456"
# r = requests.post(headers=headers,url=url,data=data,allow_redirects=False)
# print(r.text,r.cookies["User_Id"],r.headers)
data_json = '{"jsonstr":"{\"Waybill_Code\":\"YT2020072114530001\",\"Currency_Code\":\"YD\",\"Customer_Code\":\"AUTO-CUSTO\",\"Product_Code\":\"PK0029\",\"Server_Code\":\",\"Server_Type\":\"PS\",\"ServerPlace_Code\":\",\"System_Code\":\"YT\",\"Og_id_ChargeFirst\":\"YT-SZ\",\"Og_id_ChargeSecond\":\"\",\"Arrival_Date\":\"2020-07-21T14:53:10\",\"Country\":\"AR\",\"Postcode\":\"518000\",\"City\":\"005001\",\"Province\":\"005\",\"Charge_Weight\":45.0,\"Unit_Code\":\"KG\",\"Unit_Length\":\"CM\",\"Unit_Area\":null,\"Unit_Bulk\":null,\"Unit_Volume\":null,\"ExtraService\":\"ss\",\"ExtraService_Coefficient\":\"0.8\",\"Pieces\":5,\"Category_Code\":\"5\",\"Declared_Value\":0.8,\"Currency\":null,\"Tariff\":\"0.6\",\"Airline\":\"中国南方\",\"Departure_Airport\":\"宝安机场\",\"Destination_Airport\":\"伦敦机场\",\"Customs_Clearance_Port\":\"QHKA\",\"Start_Place\":\"MD\",\"end_Place\":\"MX\",\"Remark\":null,\"Ticket\":5,\"HS_Code\":5,\"Box_Number\":5,\"First_Long\":0.0,\"Two_Long\":0.0,\"Three_Long\":0.0,\"BusinessTime\":\"2020-03-11T00:00:00\",\"airline_two_code\":\"BR\",\"detailEntities\":null,\"Goods_Code\":null,\"IsFinalCharge\":false,\"ChargType\":null,\"HCustomsNumber\":0.0,\"MCustomsNumber\":0.0,\"LCustomsNumber\":0.0,\"HCargoValueNumber\":0.0,\"MCargoValueNumber\":0.0,\"LCargoValueNumber\":0.0,\"Charge_Volume\":5.0,\"Truck_Number\":1,\"Tray_Number\":1,\"TimeUnti\":\"Day\",\"TimeVaule\":5,\"TrackingNumber\":\"33P\"}","billno":"YT2020072114530001"}'
print(eval(data_json))
