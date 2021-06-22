from flask import Flask, render_template, request, jsonify, session, json, redirect, url_for

import utilfx,lens,const_params, curl_mod
#print("starting flask")
flask_obj=Flask(__name__)
flask_obj.secret_key="shinobioftheleaf"
@flask_obj.route("/",methods=["GET","POST"])
def hi():
 #access_token=request.args.get("ac")
# access_token=request.url
 if session.get("loged_in")==True:
   msg="hello world"
  #fb_code=request.get_json()
 #fb_resp=fb_code.access_token
 #session["user_token"]=fb_resp
 return render_template("index.html",token="WELCOME TO POSTEYE")
  

@flask_obj.route("/parse",methods=["POST"])
def parse():
 jsono=request.get_json()
 reply_data=str()
 cmd=jsono["cmd"]
# token=jsono["token"]
 #("token: "+str(token))
 if cmd==const_params.ANALYZE_POST:
   post_id=utilfx.gen_post_id(jsono["name"])
   print(post_id)
   page_id=post_id.split("_")
   if jsono["type"]=="user_post":
    session["fb_token"]=session["user_token"]
   else:
    page_token_json=curl_mod.send_request("https://graph.facebook.com/"+page_id[0],"fields=access_token&access_token="+str(session["user_token"]),False)
    print(page_token_json)
    page_token_obj=json.loads(page_token_json)
    session["fb_token"]=page_token_obj["access_token"]
 
   reply_data=lens.analyze_post(session["fb_token"],post_id)
   return reply_data
 elif cmd==const_params.FILTER_COMMENTS:
   reply_data=lens.filter_comments(jsono["name"])
   return reply_data
 elif cmd==const_params.CMD_LOGOUT:
   loged={}
   for sessions in list(session.keys()):
     session[sessions]=None
   loged["status"]=False
   reply_data=json.dumps(loged)
   return reply_data
 #return analysis_json
# return comments_json
# return reply_data

@flask_obj.route("/test",methods=["POST"])
def test():
  post_data=request.data
  return post_data

@flask_obj.route("/fbcheck",methods=["POST"])
def fbcheck():
  fb_login=request.get_json()
  
  if fb_login["status"]=="unknown" and (session.get("loged_in")==None or session.get("loged_in")==False):
    fb_check={}
   # if request.args.get("code")==None:
    fb_check["STATUS"]=const_params.CMD_REDIR
    fb_check["url"]="https://www.facebook.com/v11.0/dialog/oauth?client_id=314957010159410&redirect_uri="+const_params.fb_redirect_url+"/fbctrl&state=7yearsold&scope="+const_params.permissions
    print(json.dumps(fb_check))
    return json.dumps(fb_check)
  elif fb_login["status"]=="unauthorized":
    return "auth failed"
  elif session.get("loged_in")==True:
    if session.get("user_token")!=None:
     fb_check={}
  #  
     fb_check["STATUS"]=const_params.CMD_TICK
     return json.dumps(fb_check)
    else:
      fb_check={}
   # if request.args.get("code")==None:
      fb_check["STATUS"]=const_params.CMD_REDIR
      fb_check["url"]="https://www.facebook.com/v11.0/dialog/oauth?client_id=314957010159410&redirect_uri="+const_params.fb_redirect_url+"/fbctrl&state=7yearsold&scope="+const_params.permissions
      print(json.dumps(fb_check))
      return json.dumps(fb_check)
  else:
    fb_check={}
    session["user_token"]=fb_login["token"]
  #  print(fb_resp["token"])
    fb_check["STATUS"]=const_params.CMD_TICK
    return json.dumps(fb_check) 
    
@flask_obj.route("/fbctrl",methods=["POST","GET"])
def hand():
  fb_resp=None;
  if request.method=="GET":
    fb_code=request.args.get("code")
    if fb_code!=None:
      token_data=curl_mod.send_request("https://graph.facebook.com/v11.0/oauth/access_token","client_id=314957010159410&redirect_uri="+str(const_params.fb_redirect_url)+"/fbctrl&client_secret=cf8d4c9561d57caae00a2f28eddff431&code="+str(fb_code),False)
      
      token_data_json=json.loads(token_data)
      session["user_token"]=token_data_json["access_token"]
      session["loged_in"]=True
      print("token: "+session["user_token"])
   #   fb_resp="code obtained"
   #   return fb_resp
      return redirect(url_for("hi"))
  elif request.method=="POST":
   fb_code=request.get_json()
   fb_resp=json.dumps(fb_code)
   fb_resp=""
   return fb_resp 
  #if __name__ == '__main__':
# flask_obj.run()