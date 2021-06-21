from urllib.parse import urlparse, parse_qs
from fb_mod import fb_ctrl
#urll="https://m.facebook.com/story.php?story_fbid=2319430228126003&id=1028442447224794&fs=5&focus_composer=0"


def gen_post_id(url):
 parsed_url=urlparse(url)
 id_mid="_"
 parsedurl_json=parse_qs(parsed_url.query)
 if parsedurl_json.get('id')!=None:
  fb_me_id=(parsedurl_json['id'][0])
  fb_story_id=parsedurl_json['story_fbid'][0]
  fb_post_id=fb_me_id+id_mid+fb_story_id
  return fb_post_id
 else :
   urls=url.split('/')
   return urls[3]+id_mid+urls[5]

#print(gen_post_id(urll))


def gen_sentiment_labels(arr_len):
  arr_labels=[]
  for x in range(arr_len):
    arr_labels.append("")
  return arr_labels
  
def fb_reply(action_type,token,post_id,data_in):
  fb_obj=fb_ctrl(token)
  print(action_type)
  if action_type=="Reply":
   fb_obj.postCommentReply(post_id,data_in)
  elif action_type=="Like":
    fb_obj.postLike(post_id)
  elif action_type=="Private Message":
    msg="hello"
  return "replied"