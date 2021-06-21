from flask import session,json

def sentiments_filter(filter_data):
  low_value=filter_data[0]
  high_value=filter_data[1]
  sentiments_in_len=len(filter_data)
  filtrate_data={}
  filtrate_ids=[]
  print("sentiments_data: "+str(session["sentiments"]["server_data"]))
  
  for keyv in list(session["sentiments"]["server_data"].keys()):
    for value in range(int(low_value),int(high_value)):
      if str(value) in str(keyv):
        for filtrate_id in session["sentiments"]["server_data"][str(keyv)]:
          filtrate_ids.append(filtrate_id)
  
  
 # for value in range(int(low_value),int(high_value)):
  # if session["sentiments"]["server_data"].get(str(value))!=None:
  #  for filtrate_id in session["sentiments"]["server_data"][str(value)]:
  #    filtrate_ids.append(filtrate_id)
  return list(set(filtrate_ids))
 # return sentiments_ids
def emotions_filter(filter_data):
  emotion_in="Group "+str(filter_data)
  filtrate_data={}
  filtrate_ids=session["emotions"]["server_data"][str(emotion_in)]
  
  #filtrate_data["filtrate"]=filtrate_ids
 # return json.dumps(filtrate_ids)
  return filtrate_ids
  
def behaviors_filter(filter_data):
  behavior_in=str(filter_data)
  filtrate_data={}
  filtrate_ids=session["behaviors"]["server_data"][str(behavior_in)]
  #filtrate_data["filtrate"]=filtrate_ids
  #return json.dumps(filtrate_ids)
  return filtrate_ids