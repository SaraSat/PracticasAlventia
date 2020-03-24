document.getElementById("calculadora").addEventListener("click", calculos);

function calculos(e){
        
        var x=e.target.innerHTML; // x=7 x=* x=2 x='='-->clase calculate
        var result=document.getElementsByClassName('result'); //donde escribe la operacion
        if(result[0].innerHTML!="0")
            result[0].innerHTML+=x; // 7*2
        else
            result[0].innerHTML=x; //se escribe el 7 
                                       
       if(e.target.className=="calculate"){ //if(x=="=");
           var operacion=result[0].innerHTML.split("="); // "7*2="=>operacion[0]=7*2 operacion[1]="";
          result[0].innerHTML+= eval(operacion[0]); // a lo que hay escrito 7*2= se le añade el resultado de operacion[0]=7*2;
          //el resultado= 7*2=14
       }
       if(e.target.className=="reset"){ //if(x=="R")
           result[0].innerHTML="0";
       }
}
