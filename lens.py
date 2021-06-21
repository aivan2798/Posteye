from fb_mod import fb_ctrl
from heart import Vessels
from flask import session

import json,utilfx,const_params,filters
def analyze_post(token,post_id):
 analysis_dic={}
 nxt_cursor=""
 analysis_data=[]
 client_data={}
 server_data=[]
 session_data={}
 fb_ctrl_obj=fb_ctrl(token)
# post_id=utilfx.gen_post_id(active_url)
 
 #comments_json=json.loads(comment_list)
 #return comment_list["data"]
 vessel=Vessels(token,post_id)
 vessel.parseAll()
 session["sentiments"]=vessel.getSentiments()
# session_data["sentiments"]=vessel.comment_vein_sentiments()
 analysis_data.append(session["sentiments"]["client_data"])
 session["emotions"]=(vessel.getEmotions())
# session_data["emotions"]=(vessel.comment_vein_emotions())
 analysis_data.append(session["emotions"]["client_data"])
# analysis_data.append(session_data["emotions"]["client_data"]
# analysis_data.append(vessel.comment_vein_emotions())
 
 session["behaviors"]=(vessel.getBehaviors())
# session_data["behaviors"]=(vessel.comment_vein_behaviors())
 analysis_data.append(session["behaviors"]["client_data"])
 #analysis_data.append(vessel.comment_vein_behaviors())
 analysis_dic["data"]=analysis_data
 analysis_dic["analysis_size"]=len(analysis_data)
 analysis_json=json.dumps(analysis_dic)
 return analysis_json
 

def filter_comments(filter_obj):
  active_token=session["fb_token"]
  filter_type=filter_obj["filter_type"]
  filter_data=filter_obj["filter_data"]
  action_type=filter_obj["action_type"]
  action_data=filter_obj["action_data"]
  residue=""
  if filter_type==const_params.SENTIMENT_FILTER:
    filtrate=filters.sentiments_filter(filter_data)
  #  print("sentiments: "+str(filter_data))
    print("filtered: "+str(filtrate))
    for filtered_ids in filtrate:
     residue=utilfx.fb_reply(action_type,active_token,filtered_ids,action_data)
  elif filter_type==const_params.EMOTIONS_FILTER:
    filtrate=filters.emotions_filter(filter_data)
    for filtered_ids in filtrate:
     residue=utilfx.fb_reply(action_type,active_token,filtered_ids,action_data)
  elif filter_type==const_params.BEHAVIORS_FILTER:
    filtrate=filters.behaviors_filter(filter_data)
    for filtered_ids in filtrate:
     residue=utilfx.fb_reply(action_type,active_token,filtered_ids,action_data)
     print("data: "+action_data+" ids: "+filtered_ids)
  return residue