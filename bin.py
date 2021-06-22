 analysis_dic={}
 analysis_data=[]
 client_data={}
 server_data=[]
 session_data={}
 fb_ctrl_obj=fb_ctrl(session["fb_token"])
 post_id=utilfx.gen_post_id(jsono['name'])
 comments_json=fb_ctrl_obj.getComments(post_id)
 #comments_json=json.loads(comment_list)
 #return comment_list["data"]
 vessel=Vessels(comments_json)
 session["sentiments"]=vessel.comment_vein_sentiments()
# session_data["sentiments"]=vessel.comment_vein_sentiments()
 analysis_data.append(session["sentiments"]["client_data"])
 
 
 session["emotions"]=(vessel.comment_vein_emotions())
# session_data["emotions"]=(vessel.comment_vein_emotions())
 analysis_data.append(session["emotions"]["client_data"])
# analysis_data.append(session_data["emotions"]["client_data"]
# analysis_data.append(vessel.comment_vein_emotions())
 
 session["behaviors"]=(vessel.comment_vein_behaviors())
# session_data["behaviors"]=(vessel.comment_vein_behaviors())
 analysis_data.append(session["behaviors"]["client_data"])
 #analysis_data.append(vessel.comment_vein_behaviors())
 
 analysis_dic["data"]=analysis_data
 analysis_dic["analysis_size"]=len(analysis_data)
 analysis_json=json.dumps(analysis_dic)
 
   <div id="fb_login_div" style="border:1px solid blue;position:fixed;top:35%;width:80vw;background-color:white;margin-left:2%;height:30vh">
   <b>WELCOME TO POSTEYE</b>
  </div>
 

