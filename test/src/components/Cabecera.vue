<template>
    <div>
        <h1>Lista de la compra</h1>
                    <h4>Añadir producto</h4>
        <input type="text" ref="newItem">
        <button @click="add">Añadir</button>

    </div>
</template>

<script>
export default {
    name:'Cabecera',
    props:{
        items:[]
    },
    methods:{
        add: function(){
            this.items.push({
                id:this.items.length +1, texto:this.$refs.newItem.value,comprado:false
            });
            this.$refs.newItem.value="";
        }
    }

}
</script>
    
