document.getElementById("calculadora").addEventListener("click", calculos);

function calculos(e){
        
         x=e.target.innerHTML;
        var result=document.getElementsByClassName('result');
        if(result[0].innerHTML!="0")
            result[0].innerHTML+=x;
        else
            result[0].innerHTML=x;
                                       
       if(e.target.className=="calculate"){
           var operacion=result[0].innerHTML.split("=");
          result[0].innerHTML+= eval(operacion[0]);
       }
       if(e.target.className=="reset"){
           result[0].innerHTML="0";
       }
}
