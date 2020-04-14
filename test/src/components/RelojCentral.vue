<template>
    <div>
        <Reloj  v-for='reloj in relojes' :key='reloj.nombre'
        v-bind:title='reloj.nombre'
        v-bind:ts='ts'
        v-bind:offset='reloj.offset'
        v-bind:style="{position: 'relative',top: reloj.Rtop + 'px', left: reloj.Rleft +'px'}"
    ></Reloj>
    </div>
    <!--En el reloj central se añade el componente reloj
    que tiene el v-for para ir añadiendolos, como dato inicializamos
    el ts en 0 y generamos un interval para los segundos--->
</template>

<script>
import Reloj from '@/components/Reloj.vue'

export default {
    name:'RelojCentral',
    components:{
        Reloj
    },
    props:{
        relojes:[]
    },
    data:function(){
        return{
            ts:0
        }
    },
    created: function(){
        setInterval(()=>{
            this.ts=(new Date()).getTime();
        },1000);
        this.ts=(new Date()).getTime();
    }


}
</script>