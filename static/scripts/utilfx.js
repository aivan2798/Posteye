function progress_calc()
{
 var prog_div=document.getElementById("div-progress");
 var digit=0;
 for(x=0;x<10;x++)
 {
  prog_div.innerHTML=digit;
  //setTimeout(()=>{digit=digit+5;},1000);
  prog_div.innerHTML=digit;
///  continue;
 }
 
}

function show_progess(msg)
{
 document.getElementById("div-progress").innerHTML="<table><tc><td><b text='white'>"+msg+" <b></td><td><div id='load_div' style='color:red'></div></td></tc></table>";
}


function poster2(post_data,callback,stats)
{
 var postman=new XMLHttpRequest();
 var response_txt;
 postman.onreadystatechange=function()
 {
  response_txt=postman.responseText;
  stats=true;
  callback(response_txt);
 }
 
 postman.open("POST","parse",true);
 postman.setRequestHeader("Content-Type","application/json")
 postman.send(post_data);
 
// return postman.responseText;
}
function poster(post_data)
{
 var postman=new XMLHttpRequest();
 var response_txt;
 postman.onreadystatechange=function()
 {
  response_txt=postman.responseText;
//  stats=true;
//  callback(response_txt);
 }
 
 postman.open("POST","parse",false);
 postman.setRequestHeader("Content-Type","application/json")
 postman.send(post_data);
 
 return postman.responseText;
}

function fbpush(post_data)
{
 var postman=new XMLHttpRequest();
 var response_txt;
 postman.onreadystatechange=function()
 {
  response_txt=postman.responseText;
 }
 
 postman.open("POST","fbcheck",false);
 postman.setRequestHeader("Content-Type","application/json")
 postman.send(post_data);
 
 return postman.responseText;
}


function gen_sentiment_labels(signal_arr)
{
 signal_labels=[];
  for(x=0;x<signal_arr.length;x++)
  {
   signal_labels[x]="";
  }
  
  return signal_labels;
}
function marq()
{
  
}

function logout(buttonobj)
{
 
 if(loged==true)
 {
 buttonobj.innerHTML="LOGIN";
 var postobj=new Post_str();
 var stats=false;
 loged=false;
 postobj.cmd=CMD_LOGOUT;
 
 poster2(JSON.stringify(postobj),logout_call,stats);
 }
 else{
 buttonobj.innerHTML="LOGOUT";
 
 window.open(redirector,"_self");
 loged=true;
   
 }
// alert("loged out");
  
}

function logout_call(response)
{
 response_json=JSON.parse(response);
 loged=response_json.status;
 FB.logout(logs("you have successfully loged out"));
}

function logs(msg)
{
  var prog_div=document.getElementById("div-progress");
  prog_div.innerHTML=msg;
}

function nuller(target)
{
 target.value="";
}