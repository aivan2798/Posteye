from urllib.parse import urlparse,parse_qs
import facebook,validators


def gen_post_id(url):
 parsed_url=urlparse(url)
 parsedurl_json=parse_qs(parsed_url.query)
 fb_me_id=(parsedurl_json['id'][0])
 id_mid="_"
 fb_story_id=parsedurl_json['story_fbid'][0]
 fb_post_id=fb_me_id+id_mid+fb_story_id
 return fb_post_id


def_access_coin="EAAEec6S1xzIBAAsyB46h06HxYrZB5ZB6stc9mAKKbZCjjR6Q6N3ZCiQ5L6SWE3H34Qsz1YZClO3vRDFsFiMODTNpaLw5r2SXt7XxX6a0FcfeBwcb3auQb8AMzIzXKcTgwSlzFiv7fPMib2SK5BcyCM84G5Ni5EcDK5WPsDpcIH6X9WaABuRYH"

def_version="3.1"
print("\tTESTING FB GRAPH\n")
fb_obj=facebook.GraphAPI(access_token=def_access_coin, version=def_version)

post_id=input("please input node id: ")
#print(post_id)
active_node=""
if validators.url(post_id)==True:
  active_node=gen_post_id(post_id)
  print("id from url: "+active_node)
else:
  active_node=post_id
  print("non url id: "+active_node)


qfields=input("please input required field: ")

#node_data=fb_obj.get_object(id=active_node,fields=qfields)
node_data=fb_obj.get_connections(id=active_node, connection_name=qfields)

print("GRAPH DATA\n")
print(node_data)