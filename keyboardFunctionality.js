let textContainer = document.querySelector(".textContainer");
let enterKey = document.querySelector(".enter");
let spaceKey = document.querySelector(".space");
let deleteKey = document.querySelector(".delete");
let capsLockKey = document.querySelector(".CapsLock")
let allKeys = document.querySelectorAll(".key");
let isCaps = false;


enterKey.addEventListener("click", function(){
    let content = textContainer.innerText;
    let newContent = content + "\n";
    textContainer.innerText = newContent; 
});

spaceKey.addEventListener("click", function(){
    let content = textContainer.innerText;
    let newContent = content + " ";
    textContainer.innerText = newContent;
});

deleteKey.addEventListener("click", function(){
    let content = textContainer.innerText;
    let newContent = content.slice(0, content.length-1);
    textContainer.innerText = newContent;
});
capsLockKey.addEventListener("click", function(){
    if(isCaps){
        CapsLock.classList.remove("active");
        
    }else{
        CapsLock.classList.add("active");
        for(let key of allKeys){
            if(key.classList.length > 1){
                //do nothing 
            }else{
                key.innerText = key.innerText.toUpperCase();
            }
        }
    }
    isCaps = !isCaps;
})

for(let key of allKeys){
    if(key.classList.length > 1){
        //do nothing
    }else{
        key.addEventListener("click", function(){
            textContainer.innerText += key.innerText;
        })
    }
}