<template> 
    <div class="reloj-vue">
        <h1>{{title}}</h1>

    <div>
        <span>
            {{hh}}:{{mm}}:{{ss}}
        </span>
        </div>
    </div>
    <!--en esta plantilla se imprime el nombre del reloj, 
    y la hora en función del valor del offset-->
</template>
<script>
export default {
    name:'Reloj',
    props:{
        offset:{type:Number,default:0},
        title:{type:String,default:'-'},
        ts:{type:Number,default:0},
    },
    computed:{
        hh(){
            let d =this.getDate();
            return d.getHours();
        },
        mm(){
            let d =this.getDate();
            return d.getMinutes();
        },
        ss(){
            let d =this.getDate();
            return d.getSeconds();
        },
    },
    methods:{
        getDate(){
            return new Date(this.ts+ this.offset *3600*1000)
        }
    },
}
</script>
<style>
    template{
        display: none;
    }
    .reloj-vue{
        width: 100px;
        border:1px solid black;
        font-family: sans-serif;
    }
    .reloj-vue h1{
        font-size: 80%;
    }
</style>
