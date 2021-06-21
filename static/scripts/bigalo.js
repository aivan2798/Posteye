
function magi()
{
 if(loged==true)
 {
 var poststr=new Post_str();
 var tok=false;
 var post_link=document.getElementById("post-link-input").value;
 poststr.cmd=ANALYZE_POST;
 poststr.name=post_link;
 //poststr.token=tok;
 //poststr.token=login();
 var post_json=JSON.stringify(poststr);
 document.getElementById("div-progress").innerHTML="<table><tc><td><b color='white'>GENERATING ANALYTICS <b></td><td><div id='load_div' style='color:red'></div></td></tc></table>";
// document.getElementById("prog-anime").style.display="";
//arar res_string=res_string=
 poster2(post_json,postman,tok);
}
else
{
 alert("please login first");
}
}

function postman(res_string)
{
 var res_json=JSON.parse(res_string);
 
 var res_json_arr=res_json.data;
 //document.getElementById(" div-progress").innerHTML=res_string;
// alert(res_string);
 for(x=0;x<res_json.analysis_size;x++)
 {
 
 circuits(res_json_arr[x]);
 }
// circuits(res_json_arr[0]);
 
document.getElementById("div-progress").innerHTML="Analysis finished";
//document.getElementById("prog-anime").style.display="none";
  
 //alert(post_link);
 //progress_cal Drc();
}

function filter()
{
  var ctrl_div=document.getElementById("filter_div");
  ctrl_div.style.display="";
 // alert("making filter");
}

function kanfilters()
{
  var ctrl_div=document.getElementById("filter_div");
  ctrl_div.style.display="none";
  //alert("hiding filter");
}

function login()
{
 var access_token="";
 var fbman=new Fb_man();
 window.fbAsyncInit = function(){
 FB.init({appId:'314957010159410',xfbml:true,status:true,cookie:true,version:'v2.7'});//*284*90#
 
 FB.getLoginStatus(function(response)
 {
 //  alert("Facebook login "+response.status);
   fbman.status=response.status;
   switch(response.status)
   {
    case "connected":
    fbman.token=response.authResponse.accessToken;
    var fb_ans=JSON.parse(fbpush(JSON.stringify(fbman)));
    switch(fb_ans.STATUS)
       {
        case CMD_REDIR:
         window.open(fb_ans.url,"_self");
        break;
        case CMD_TICK:
         document.getElementById("main_div").style.display="";
         document.getElementById("fb_div").style.display="none";
        break;
       }
    break;
    case "unknown":
      fbman.status="unknown";
       var fb_ans=JSON.parse(fbpush(JSON.stringify(fbman)));
     //  alert(fb_ans.STATUS);
       switch(fb_ans.STATUS)
       {
        case CMD_REDIR:
          window.open(fb_ans.url,"_self");
        break;
        case CMD_TICK:
          document.getElementById("main_div").style.display="";
         document.getElementById("fb_div").style.display="none";
        break;
       }
    break;
   }
  
 });
 };
}