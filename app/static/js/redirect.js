let wait;

function timer(){
    $("#count").text(wait.toString());
    if(wait == 0){
        console.log("redirect");
        console.log($('a').attr('href'));
        //location.href = "https://www.kfip-games.link/";
    }else{
        wait -= 1;
    }
}

$(window).on('load', function(){
    wait = 5;
    setInterval('timer()', 1000);
});