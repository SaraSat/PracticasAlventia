<template>
    <div>
        <h1>Lista de la compra</h1>
                    <h4>Añadir producto</h4>
        <input type="text" ref="newItem">
        <button @click="add">Añadir</button>
        <p>-------------------------------</p>

    </div>
</template>

<!--En la cabecera aparece el botón para añadir los items,
tiene como propiedad el array de items y un método para añadirlos-->

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
    
