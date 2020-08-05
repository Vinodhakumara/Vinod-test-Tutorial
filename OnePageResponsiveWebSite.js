function mouseover(threelists){

    console.log("hi im mouse over");

    console.log(threelists.getAttribute('id'));
    var side1 = threelists.getAttribute('id');
    var side =document.getElementById(side1);
    var sideSubMenu = document.createElement('li');
    sideSubMenu.setAttribute('id','list1')
    var txt = document.createTextNode('View Project');
    
    sideSubMenu.appendChild(txt);
    side.appendChild(sideSubMenu)
    
    var sideSubMenu = document.createElement('li');
    sideSubMenu.setAttribute('id','list2')
    var txt = document.createTextNode('Update Project');
    sideSubMenu.appendChild(txt);
    side.appendChild(sideSubMenu)
    
    var sideSubMenu = document.createElement('li');
    sideSubMenu.setAttribute('id','list3')
    var txt = document.createTextNode('Delete Project');
    sideSubMenu.appendChild(txt);
    side.appendChild(sideSubMenu)
    
}

function mouseout(threelists){
    let side1 = threelists.getAttribute('id');
    let side =document.getElementById(side1);
    
    side.removeChild(list1);
    side.removeChild(list2);
    side.removeChild(list3);
    console.log("hi im mouse out");
}

function zoomMyProject(){
    
    let elemen1 = document.getElementById('section0')
    let burger = document.querySelector(".burger");
    let bar = getComputedStyle(burger);
    check=bar.display;
    if(check==="none"){
        elemen1.style.width="100vw";
        elemen1.style.paddingBottom = "50px";
        elemen1.style.height="auto";
        elemen1.style.paddingLeft="30vw";
        elemen1.style.transition="all 0s ease-in-out";
        var h2 = document.getElementById('h2')
        h2.style.marginLeft = "-30vw";
        let btnSize=document.getElementsByClassName('list');
        for (let index = 0; index < btnSize.length; index++) {
            btnSize[index].style.width = "30vw";
            btnSize[index].style.marginTop = "20px";
        }
        
        document.getElementById('section1').style.width="50vw";
        document.getElementById('section1').style.height="auto";
        document.getElementById('section2').style.width="100vw";
        document.getElementById('section2').style.height="auto";
        document.getElementById('section2-divId').style.paddingTop="50px";
    }
    
}

// function zoomMyProjectOut(){
    
//     let elemen1 = document.getElementById('section0')
//     let burger = document.querySelector(".burger");
//     let bar = getComputedStyle(burger);
//     check=bar.display;
//     if(check==="none"){
//         elemen1.style.width="25vw";
//         elemen1.style.paddingBottom = "50px";
//         elemen1.style.height="95vh";
//         elemen1.style.paddingLeft="0vw";
//         elemen1.style.transition="all 3s ease-in-out";
//         var h2 = document.getElementById('h2')
//         h2.style.marginLeft = "0vw";
//         let btnSize=document.getElementsByClassName('list');
//         for (let index = 0; index < btnSize.length; index++) {
//             btnSize[index].style.width = "15vw";
//             btnSize[index].style.marginTop = "0px";
//         }
        
//         document.getElementById('section1').style.width="25vw";
//         document.getElementById('section1').style.height="95vh";
//         document.getElementById('section1').style.transition="all 3s ease-in-out";
//         document.getElementById('section2').style.width="48.9vw";
//         document.getElementById('section2').style.height="95vh";
//         document.getElementById('section2').style.transition="all 0s ease-in-out";
//         document.getElementById('section2-divId').style.paddingTop="40vh";
//     }
    
// }
