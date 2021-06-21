class Post_str
{
cmd;
name;
token;
}
class Filter
{
 filter_type;
 filter_data;
 action_type;
 action_data;
}
class Fb_man
{
 status;
 token;
}
var SENTIMENTS=19980;
var EMOTIONS=20140;
var BEHAVIORS=20170;
var SENTIMENT_FILTER=199801;
var EMOTIONS_FILTER=201401;
var BEHAVIORS_FILTER=201701;
//var redirector="https://127.0.0.1:5000/";
var redirector="https://posteye.herokuapp.com";
var ANALYZE_POST=24645;
var FILTER_COMMENTS=24646;

var CMD_REDIR=19000;
var CMD_TICK=19010;
var CMD_LOGOUT=19020;

var loged=true;

/*
var pp=new Post_str;
pp.name="hello";

console.log(JSON.stringify(pp));
*/