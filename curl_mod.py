import pycurl, json
from io import BytesIO

def send_request(endp,params,meth_switch):
  json_data=params
  #if(json_switch==True):
  #  json_data=json.dumps({'name':'ivn'})
  #else:
  #  json_data=params
    
  data_can=BytesIO()
  curl_obj=pycurl.Curl()
  
#  custom_head=["Content-Type: application/json"]
  if(meth_switch==True):
    custom_head=["Content-Type: application/json"]
    curl_obj.setopt(curl_obj.HTTPHEADER,custom_head)
    curl_obj.setopt(curl_obj.URL,endp)
    curl_obj.setopt(curl_obj.POSTFIELDS, json_data)
  else:
    curl_obj.setopt(curl_obj.URL,endp+"?"+params)
  #curl_obj.setopt(curl_obj.USERAGENT, "curl/7.72.0");
  curl_obj.setopt(curl_obj.WRITEDATA,data_can)
  curl_obj.perform()
  curl_obj.close()
  
  body=data_can.getvalue()
  return body.decode("utf8")
  
#print(send_request("http://127.0.0.1:5000/parse","name=ivan",True))