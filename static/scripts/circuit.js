
function circuits(signal_in)
{
 //signal_type=SENTIMENTS;
 signal_type=signal_in.type;
 signal_data=signal_in.data;
 signal_labels=signal_in.labels;
  switch(signal_type)
  {
    case SENTIMENTS:
    charts("sentiments_chart","sentiments",signal_labels,signal_data);
    //  alert("sentiments");
     break;
    case EMOTIONS:
      charts("emotions_chart","emotions",signal_labels,signal_data);
      
      break;
    case BEHAVIORS:
      charts("behaviors_chart","behaviors",signal_labels,signal_data);
    //  alert("BEHAVIOR");
      break;
  //  default:
   //  charts("no data",[0,0,0,0])
 //  alert("no data");
    }
}