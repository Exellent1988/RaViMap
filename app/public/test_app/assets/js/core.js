function initialize(){
	var socket = io.connect();



	
	document.getElementById('checkbox').addEventListener("click", function($){
		var slidervalue = document.getElementById('slider_1').value;
	if (this.checked){
	socket.emit('lampe',{'value': slidervalue});
	}
	else{
	socket.emit('lampe',{'value':0});
	}
	console.log(this.checked);
	console.log(slidervalue);
	});



socket.on('channels',function(channels){
	for(i=1;i<=2;i++){
		var string1 = 'channel_' ;
	    var str2 = i.toString();
	    var channelid = string1+str2;
		document.getElementById(channelid).innerHTML = channels.all[(i-1)];
		}
});

}


