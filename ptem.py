import pycurl, json
from io import BytesIO
  
print("starting curl\n")

json_data=json.dumps({'name':'ivan'})
data_can=BytesIO()
data_cann=""
curl_obj=pycurl.Curl()
  
custom_head=["Content-Type: application/json"]
curl_obj.setopt(curl_obj.URL,"http://127.0.0.1:5000/parse")
curl_obj.setopt(curl_obj.POSTFIELDS, json_data)
  
curl_obj.setopt(curl_obj.HTTPHEADER,custom_head)
  #curl_obj.setopt(curl_obj.USERAGENT, "curl/7.72.0");
curl_obj.setopt(curl_obj.WRITEDATA,data_can)
curl_obj.perform()
curl_obj.close()
  
body=data_can.getvalue()

print(body.decode("utf8"))