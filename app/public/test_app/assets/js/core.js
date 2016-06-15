function initialize(){
	var socket = io.connect();

	var w = window,
    d = document,
    e = d.documentElement,
    g = d.getElementsByTagName('body')[0],
    x = w.innerWidth || e.clientWidth || g.clientWidth,
    y = w.innerHeight|| e.clientHeight|| g.clientHeight;


	
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
	for(i=1;i<=10;i++){
		var string1 = 'channel_' ;
	    var str2 = i.toString();
	    var channelid = string1+str2;
		document.getElementById(channelid).innerHTML = channels.all[(i-1)];
		}
		document.getElementById('test_img').style.left = ((channels.all[0]/255)*x)-(document.getElementById('test_img').width/2) + "px";
		document.getElementById('test_img').style.top = ((channels.all[1]/255)*y)-(document.getElementById('test_img').height/2) + "px";
		rotation('test_img',(channels.all[2]/255)*360);
		
});


}

function rotation(id,deg){
    var div = document.getElementById(id),
       
    div.style.webkitTransform = 'rotate('+deg+'deg)'; 
    div.style.mozTransform    = 'rotate('+deg+'deg)'; 
    div.style.msTransform     = 'rotate('+deg+'deg)'; 
    div.style.oTransform      = 'rotate('+deg+'deg)'; 
    div.style.transform       = 'rotate('+deg+'deg)'; 
}



