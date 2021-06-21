function charts(chart_id,chart_label,data_labels,chart_data)
{
 var chartid=document.getElementById(chart_id);
 //var chartid=document.getElementById("chart_paper");
 //alert("drawing");
 //var values={50,100,150,200};
 
 var chart_obj=new Chart(chartid,{
   type:'line',
   data:
   {
  labels:data_labels,
   datasets:[{
     label:chart_label,
     data:chart_data,
     parsing:true,
     backgroundColor:"red",
     borderColor:"grey",
     fill: true
     }]
 },
   options:
   {
    responsive: true,
 //   maintainAspectRatio: false,
    scales:
    {
      y:{
       beginAtZero:true
      }
    }
  /*    layout:
      {
       padding:{
         left:20
       }
      }*/
    }
 });
}

function data()
{
 JSON.encode();
}
//data:[{y:5,x:'2'},{x:'5',y:10},{x:'10',y:3}],

//data:[55,55,67,56],


function tcharts()
{
 var chartid=document.getElementById("chart_paper");
 //alert("drawing");
 //var values={50,100,150,200};
 
 var chart_obj=new Chart(chartid,{
   type:'line',
   data:
   {
  labels:["","","",""],
   datasets:[{
     label:"testing",
     data:[55,67,88,90],
     parsing:true,
     backgroundColor:"red",
     borderColor:"green",
     fill: true
     }]
 },
   options:
   {
    scales:
    {
      y:{
       beginAtZero:true
      }
    }
   }
 });
}

function data()
{
 JSON.encode();
}
//data:[{y:5,x:'2'},{x:'5',y:10},{x:'10',y:3}],

//data:[55,55,67,56],