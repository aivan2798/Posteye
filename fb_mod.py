import facebook

class fb_ctrl:
 access_coin=""
 def __init__(self,accesstoken):
   access_coin=accesstoken
   self.fb_obj=facebook.GraphAPI(access_token=access_coin,version="3.1")
   
 def getCommentsCount(self,comment_id):
   comments=self.fb_obj.get_connections(id=comment_id, connection_name="comments?summary=total_count&limit=2")
   return comments["summary"]["total_count"]
   
 def getComments(self,node_id,nxt_node):
   comments=[]
 # comments_dic={}
  #comments_list=[]
 # comments=self.fb_obj.get_connections(id=node_id, connection_name="comments?summary=total_count&limit=10")
 # nxt_node=comments["paging"]["cursors"]["after"]
 # bck_node=comments["paging"]["cursors"]["before"]
  
  #comments_no=comments["summary"]["total_count"]
 # comments_list["data"].append(comments["data"])
#  comments=None
   if nxt_node!="":
    comments=self.fb_obj.get_connections(id=node_id, connection_name="comments?limit=10&after="+str(nxt_node))
 #   comments_list.append(comments)
   else:
     comments=self.fb_obj.get_connections(id=node_id, connection_name="comments?limit=10")
  #  comments_list.append(comments)
    
  #print("number of comments"+str(comments_no))
   return comments

 def getPost(self,node_id):
  post_node=self.fb_obj.get_object(id=node_id,fields="message")
  return post_node
  
 def postCommentReply(self,comment_id,reply_data):
   self.fb_obj.put_object(parent_object=comment_id,connection_name="comments",message=reply_data)
   
 def postLike(self,comment_id):
   self.fb_obj.put_like(object_id=comment_id)
   
#print("incoming")
