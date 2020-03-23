document.getElementById("calculadora").addEventListener("click", calculos);

function calculos(e){
    if(e.target.className="button"){
        var x=e.target.innerHTML;
        var result=document.getElementsByClassName('result');
        if(result[0].innerHTML!="0")
            result[0].innerHTML+=x;
        else
            result[0].innerHTML=x;
                                       
       if(x=="="){
           var operacion=result[0].innerHTML.split("=");
          result[0].innerHTML+= resultado(operacion[0]);
       }
       if(x=="R"){
           result[0].innerHTML="0";
       }
        

    }
}
    function resultado(op){
        for(let i=0; i<op.length;i++){
            if(op.charAt(i)=='+' ||op.charAt(i)=='-'||op.charAt(i)=='*'){
                var operador=op.charAt(i);
                op=op.split(operador);
                switch(operador){
                    case "+":
                        return parseInt(op[0])+parseInt(op[1]);
                    case "-":
                        return parseInt(op[0])-parseInt(op[1]);
                     case "*":
                        return parseInt(op[0])*parseInt(op[1]);

                }
            }
        }
    }
