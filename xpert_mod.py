import os, json
from expertai.nlapi.cloud.client import ExpertAiClient

class Xpert:
  q_str="";
  def __init__(self,str):
    os.environ["EAI_USERNAME"]=#input expert.ai username
    os.environ["EAI_PASSWORD"]=#input expert.ai password
    self.xpert_client=ExpertAiClient()
    self.q_str=str
 
  def get_sentiments(self):
    print(self.q_str)
    xpert_analysis_data=self.xpert_client.specific_resource_analysis(body={'document':{'text':self.q_str}},params={'language':'en','resource':'sentiment'})
    return xpert_analysis_data.sentiment.overall
    
  def get_emotions(self):
    xpert_cats=[]
    xpert_emotions={}
    xpert_emo_data=self.xpert_client.classification(body={'document':{'text':self.q_str}},params={'language':'en','taxonomy':'emotional-traits'})
    for xpert_category in xpert_emo_data.categories:
      xpert_cats.append((xpert_category.hierarchy))
    print(xpert_cats)
    return xpert_cats

  def get_behaviors(self):
    xpert_behavior=[]
    xpert_behavior_data=self.xpert_client.classification(body={'document':{'text':self.q_str}},params={'language':'en','taxonomy':'behavioral-traits'})
    for xpert_behavior_category in xpert_behavior_data.categories:
     xpert_behavior.append(xpert_behavior_category.hierarchy)
    print(xpert_behavior)
    return xpert_behavior
