function genfilter()
 {
   var filter_type;
  if(post_type=="page_post")
  {
  // alert(post_type);
   var type_box=document.getElementById("data").value;
   var filter_data=document.getElementById("filter_data");
   var action_type=document.getElementById("action_type");
   var action_data=document.getElementById("action_msg");
  var filter_bp=new Filter();
  var server_data=new Post_str()
  switch(type_box)
  {
   case "sentiments filter":
    filter_type="sentiments";
    filter_bp.filter_type=SENTIMENT_FILTER;
    filter_bp.filter_data=[document.getElementById("low").value,document.getElementById("high").value];
    filter_bp.action_type=action_type.value;
    filter_bp.action_data=action_data.value;
   break;
   case "Emotions filter":
   filter_type="Emotions";
   filter_bp.filter_type=EMOTIONS_FILTER;
    filter_bp.filter_data=filter_data.value;
    filter_bp.action_type=action_type.value;
    filter_bp.action_data=action_data.value;
   break;
   case "Behavior filter":
   filter_type="Behavior";
   filter_bp.filter_type=BEHAVIORS_FILTER;
    filter_bp.filter_data=filter_data.value;
    filter_bp.action_type=action_type.value;
    filter_bp.action_data=action_data.value;
   break;
   }
   server_data.cmd=FILTER_COMMENTS;
   server_data.name=filter_bp;
   var stats;
   var server_json=JSON.stringify(server_data);
   var client_json=poster2(server_json,function(responsed){logs(filter_type+" filter response applied");},stats);
   show_progress("GENERATING REPLY");
  }
  else
  {
 //   alert(post_type);
   logs("sorry, filters are limited to page posts");
  }
  }
  
  function pusher(idstr)
  {
  //  alert("sentiments: "+idstr.cust);
  var filter_ctrl=document.getElementById("filter_ctrls");
   switch(idstr.value)
   {
    case "sentiments filter":
 //   alert("parsing sentimentts");
    filter_ctrl.innerHTML="<input id='low' placeholder='low' style='width:25%'/> <input id='high' placeholder='high' onfocus='action(this)' style='width:25%'/>";
    break;
    
    case "Emotions filter":
     var emotion_filter="<input id='filter_data' list='emotion_group' placeholder='choose filter' onfocus='nuller(this)' onchange='action(this)' style='width:85%'><datalist id='emotion_group'><option value='Rage'/><option  value='Apprehension'/><option  value='Distress'/><option  value='Dejection'/><option  value='Surprise'/><option  value='Fondness'/><option  value='Resentment'/><option  value='Delight'/></datalist></input>";
  
     filter_ctrl.innerHTML=emotion_filter;
    break;
    
    case "Behavior filter":
    //   alert("parsing behavior");
    var behavior_filter=  "<input id='filter_data' list='behavior_group' placeholder='choose filter' onfocus='nuller(this)' onchange='action(this)' style='width:80%'><datalist id='behavior_group'><option value='Socially low'/><option value='Fairly Socialble'/><option value='Highly Socialble'/><option value='Low Activity'/><option value='Fairly Active'/><option value='Highly Active'/><option value='Low Openness'/><option value='Fairly Open'/><option value='Highly Open'/><option value='Low Conscious'/><option value='Highly Conscious'/><option value='Low Ethics'/><option value='High Ethics'/><option value='Low Capability'/><option value='Fair Capability'/><option value='High Capability'/><option value='Low Moderation'/><option value='Fair Moderation'/><option value='High Moderation'/></datalist></input>";
    filter_ctrl.innerHTML=behavior_filter;
    
    break;
    }
  }
  
  function action(filter_obj)
  {
   var action_box=document.getElementById("action_div"); 
   action_box.style.display="";
  //  alert("action pending");
  }
  
  function action_in(action_obj)
  {
   var action_holder=document.getElementById("action_holder"); 
 //  action_box.style.display="";
 //   alert("action pending");
  switch(action_obj.value)
  {
   case "Reply":
   action_holder.innerHTML="<textarea id='action_msg' placeholder='please_write_message' style='width:90%'></textarea>";
   break;
   case "Like":
   action_holder.innerHTML="<input id='action_msg' list='reaction_group' placeholder='choose reaction' onfocus='nuller(this)' onchange='action_in(this)' style='display:none' value='Like'></input>";
   break;
   case "Private Message":
   action_holder.innerHTML="<textarea id='action_msg' placeholder='please_write_message' style='width:90%'></textarea>";
   break;
  }
  }