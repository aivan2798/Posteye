from xpert_mod import Xpert
#from retina import Retina
class Cortex:
  def __init__(self,str_msg):
    self.comment_msg=str_msg
    self.xpert_obj=Xpert(str_msg)
    
  def parse_sentiments(self):
    return self.xpert_obj.get_sentiments()
    
  def parse_emotions(self):
  # emotions_list=[]
   emotion_group=[]
   emotions_list=self.xpert_obj.get_emotions()
   if len(emotions_list)>0:
    for emotions in emotions_list:
     emotion_group.append(emotions[0])
    # print(emotion_group)
   return emotion_group
  # print(emotions_list[0])
   # emotions_group_list=[]
   # for emotions_list_item in emotions_list:
   #   emotions_group_list.append(emotions_list_item[0])
   # retina_obj=Retina(emotions_group_list)
   #  return retina_obj.mix_emotions()
   #return emotions_group
   
  def parse_behaviors(self):
  # emotions_list=[]
   behavior_group=[]
   behaviors_list=self.xpert_obj.get_behaviors()
   if len(behaviors_list)>0:
    for behaviors in behaviors_list:
     behavior_group.append(behaviors[1])
     print(behavior_group)
   return behavior_group