setTimeout(function(){
    //do what you need here
    console.log("wait to finish")
    let elem = document.getElementsByClassName("material-icons");
    if(elem.length>1) document.getElementsByClassName("guide-name")[0].innerHTML = "FoundTheFuckingToy!";
    
    let elemlist = document.querySelectorAll('.other_itemlist'); 
    elemlist.forEach(function(node) {
      let elem1 = node.getElementsByClassName("addcart");
      if(elem1.length > 0) document.getElementsByClassName("guide-name")[0].innerHTML = "FoundTheFuckingToy!";
    });
}, 2000);
