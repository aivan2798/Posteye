
class Retina:
  def __init__(self,xpert_post_obj):
    self.xpert_post=xpert_post_obj
    print(xpert_post_obj)
  def mix_emotions(self):
    knwn_emotions=["Group Rage","Group Apprehension","Highly Socialble","Group Dejection","Group Surprise","Group Fondness"]
    emotions_count={"Group Rage":0,"Group Apprehension":0,"Group Distress":0,"Group Dejection":0,"Group Surprise":0,"Group Fondness":0,"Group Resentment":0,"Group Delight":0}
   # emotions_in=self.xpert_post
    #["Group Rage","Group Rage","Group Rage","Group Surprise"]
    x=0
    for emotions in list(self.xpert_post.keys()):
       emotions_count[emotions]=self.xpert_post[emotions]
      #print(emotions_count[emotions])
   # print(emotions_in)
    return emotions_count
    
  def mix_behaviors(self):
    knwn_behaviors=["Socially low","Fair Socialble","Highly Socialble","Low Activity","Highly Active","Low Openess"]
    behaviors_count_template={"Socially low":0,"Fairly Socialble":0,"Highly Socialble":0,"Low Activity":0,"Fairly Active":0,"Highly Active":0,"Low Openess":0,"Fairly Open":0,"Highly Open":0,"Low Conscious":0,"Highly Conscious":0,"Low Ethics":0,"High Ethics":0,"Low Capability":0,"Fair Capability":0,"High Capability":0,"Low Moderation":0,"Fair Moderation":0,"High Moderation":0}
    behaviors_count={"Sociality low":0,"Sociality fair":0,"Sociality high":0,"Action low":0,"Action fair":0,"Action high":0,"Openness low":0,"Openness fair":0,"Openness high":0,"Consciousness low":0,"Consciousness high":0,"Ethics low":0,"Ethics high":0,"Capability low":0,"Capability fair":0,"Capability high":0,"Moderation low":0,"Moderation fair":0,"Moderation high":0}
    behaviors_in=self.xpert_post
    #["Group Rage","Group Rage","Group Rage","Group Surprise"]
  #  x=0
#behavior_values=behaviors_count.values
    for behaviors in list(behaviors_in.keys()):
       behaviors_count[behaviors]=behaviors_in[behaviors]
    x=0
    behavior_values=list(behaviors_count.values())
    for behaviors_labels in list(behaviors_count_template.keys()):
      behaviors_count_template[behaviors_labels]=behavior_values[x]
      x=x+1
      #print(behaviors_count[behaviors])
   # print(behaviors_in)
    return behaviors_count_template
  def behaviors_fix(self,behaviors_in):
   behaviors_ids_template={"Socially low":[],"Fairly Socialble":[],"Highly Socialble":[],"Low Activity":[],"Fairly Active":[],"Highly Active":[],"Low Openess":[],"Fairly Open":[],"Highly Open":[],"Low Conscious":[],"Highly Conscious":[],"Low Ethics":[],"High Ethics":[],"Low Capability":[],"Fair Capability":[],"High Capability":[],"Low Moderation":[],"Fair Moderation":[],"High Moderation":[]}
   behaviors_map={"Socially low":"Sociality low","Fairly Socialble":"Sociality fair","Highly Socialble":"Sociality high","Low Activity":"Action low","Fairly Active":"Action fair","Highly Active":"Action high","Low Openness":"Openness low","Fairly Open":"Openness fair","Highly Open":"Openness high","Low Conscious":"Consciousness low","Highly Conscious":"Consciousness high","Low Ethics":"Ethics low","High Ethics":"Ethics high","Low Capability":"Capability low","Fair Capability":"Capability fair","High Capability":"Capability high","Low Moderation":"Moderation low","Fair Moderation":"Moderation fair","High Moderation":"Moderation high"}
   behaviors_ids={}
#   behaviors_count={"Sociality low":0,"Sociality fair":0,"Sociality high":0,"Action low":0,"Action fair":0,"Action high":0,"Openness low":0,"Openness fair":0,"Openness high":0,"Consciousness low":0,"Consciousness high":0,"Ethics low":0,"Ethics high":0,"Capability low":0,"Capability fair":0,"Capability high":0,"Moderation low":0,"Moderation fair":0,"Moderation high":0}
   
   print(behaviors_in)
   behavior_labelss=list(behaviors_ids_template.keys())
   for behavior in list(behaviors_in.keys()):
    for key, value in behaviors_map.items():
     if(value == behavior):
        # behaviors_ids_template[key]=behaviors_in[behavior]
        behaviors_ids[key]=behaviors_in[behavior]
   return behaviors_ids
    
 #   x=[]
  #  behavior_values=list(behaviors_count.values())
  #  for behaviors_labels in list(behaviors_count_template.keys()):
 #     behaviors_count_template[behaviors_labels]=behavior_values[x]
#      x=x+1