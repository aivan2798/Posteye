from cortex import Cortex
import const_params,utilfx
from retina import Retina
from fb_mod import fb_ctrl

class Vessels:
  def __init__(self,active_fb_token,post_id):
    self.fb_module=fb_ctrl(active_fb_token)
    #active_fb_object
    self.post_id=post_id
    comments_count_raw=self.fb_module.getCommentsCount(post_id)
    self.comments_count=int(comments_count_raw)
    self.sentiments_full_data={}
    self.emotions_full_data={}
    self.behaviors_full_data={}
  def parseAll(self):
    nxt_cursor=""
    sentiments_id_dic={}
    emotions_id_dic={}
    behaviors_id_dic={}
    
    emotions_count_dic={}
    behaviors_count_dic={}
    indexer=self.comments_count
    while indexer>0:
      comments_json=self.fb_module.getComments(self.post_id,nxt_cursor)
      nxt_cursor=comments_json["paging"]["cursors"]["after"]
      for comment in comments_json["data"]:
       # comment_msg=comment["message"]
      #  overall_sentiment=
        self.comment_vein_sentiments(comment,sentiments_id_dic)
       # overall_sentiment=
        self.comment_vein_emotions(comment,emotions_id_dic,emotions_count_dic)
        self.comment_vein_behaviors(comment,behaviors_id_dic,behaviors_count_dic)
      indexer=indexer-2
    self.sentiments_full_data=self.pack_sentiments(sentiments_id_dic)
    self.emotions_full_data=self.pack_emotions(emotions_id_dic,emotions_count_dic)
    self.behaviors_full_data=self.pack_behaviors(behaviors_id_dic,behaviors_count_dic)
        
  def comment_vein_sentiments(self,comment,csentiments_id_dic):
    data_veins=[]
    data_veins_dict=[]
    sentiments_full_data={}
    cortex_frag=Cortex(comment["message"])
    overall_sentiment=cortex_frag.parse_sentiments()
    if csentiments_id_dic.get(overall_sentiment)==None:
         csentiments_id_dic[overall_sentiment]=[]
    csentiments_id_dic[overall_sentiment].append(comment["id"])
  #  return overall_sentiment
    
  def pack_sentiments(self,psentiments_id_dic):
     # data_veins.append(overall_sentiment)
    #  data_veins_dict.append(sentiments_dic)
    sentiments_full_data={}
    sentiments_dic={}
    sentiments_dic["type"]=const_params.SENTIMENTS
    sentiments_dic["labels"]=utilfx.gen_sentiment_labels(len(psentiments_id_dic.keys()))
  #  sentiments_dic["data"]=data_veins
    sentiments_dic["data"]=list(psentiments_id_dic.keys())
    sentiments_dic["data_len"]=len(list(psentiments_id_dic.keys()))
    
    sentiments_full_data["client_data"]=sentiments_dic
    sentiments_full_data["server_data"]=psentiments_id_dic
    return sentiments_full_data
    
  def comment_vein_emotions(self,comment,cemotions_id_dic,cemotions_count_dic):
    emotions_count=[]
    emotions_dic={}
    
    cortex_frag=Cortex(comment["message"])
    emotions=cortex_frag.parse_emotions()
    for emotion in emotions:
     if cemotions_id_dic.get(emotion)==None:
          cemotions_id_dic[emotion]=[]
          cemotions_count_dic[emotion]=0
     cemotions_id_dic[emotion].append(comment["id"])
     cemotions_count_dic[emotion]=int(cemotions_count_dic[emotion]+1)
   # print(emotions_count)
   
  def pack_emotions(self,cemotions_id_dic,cemotions_count_dic):
    emotions_full_data={}
    emotions_dic={}
    retina_obj=Retina(cemotions_count_dic)
    
    emotions_groups=retina_obj.mix_emotions()
    emotions_dic["type"]=const_params.EMOTIONS
  #  emotions_dic["labels"]=list(emotions_count_dic.keys())
    emotions_dic["labels"]=list(emotions_groups.keys())
   # emotions_dic["data"]=list(emotions_count_dic.values())
    emotions_dic["data"]=list(emotions_groups.values())
    emotions_dic["data_len"]=len(cemotions_count_dic)
    
    emotions_full_data["client_data"]=emotions_dic
    emotions_full_data["server_data"]=cemotions_id_dic
    return emotions_full_data
    
  def comment_vein_behaviors(self,comment,cbehaviors_id_dic,cbehaviors_count_dic):
    comment_msg=comment["message"]
    cortex_frag=Cortex(comment_msg)
    behaviors=cortex_frag.parse_behaviors()
    for behavior in behaviors:
        print(behavior)
        if cbehaviors_id_dic.get(behavior)==None:
          cbehaviors_id_dic[behavior]=[]
          cbehaviors_count_dic[behavior]=0
        cbehaviors_id_dic[behavior].append(comment["id"])
        cbehaviors_count_dic[behavior]=int(cbehaviors_count_dic[behavior]+1)
  #  print(cbehaviors_count_dic)
    
    
  def pack_behaviors(self,pbehaviors_id_dic,pbehaviors_count_dic):
    behaviors_full_data={}
    behaviors_dic={}
    retina_obj=Retina(pbehaviors_count_dic)
    behaviors_groups=retina_obj.mix_behaviors()
    behaviors_dic["type"]=const_params.BEHAVIORS
    behaviors_dic["labels"]=list(behaviors_groups.keys())
    behaviors_dic["data"]=list(behaviors_groups.values())
    behaviors_dic["data_len"]=len(behaviors_groups)
    
    behaviors_full_data["client_data"]=behaviors_dic
    behaviors_full_data["server_data"]=retina_obj.behaviors_fix(pbehaviors_id_dic)
    return behaviors_full_data
    
  def getSentiments(self):
    return self.sentiments_full_data
  def getEmotions(self):
    return self.emotions_full_data
  def getBehaviors(self):
    return self.behaviors_full_data