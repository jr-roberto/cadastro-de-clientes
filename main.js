const main = document.getElementById('main');
var num = [0,1,2,3,4,5,6,7,8,9]

var sorteio = ()=>{

    main.innerHTML = Math.floor(Math.random() * num.length);

    setTimeout(sorteio,5000)
}

setTimeout(sorteio, 100);
