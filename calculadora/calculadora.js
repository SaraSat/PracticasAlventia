document.getElementById("calculadora").addEventListener("click", calculos);

function calculos(e){
    if(e.target.className="button"){
        var x=e.target.innerHTML;
        var result=document.getElementsByClassName('result');
        if(result[0].innerHTML!="0")
            result[0].innerHTML+=x;
        else
            result[0].innerHTML=x;
    }
}