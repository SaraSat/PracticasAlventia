
<template>
  <div class="home">
    <Cabecera v-bind:items='items'></Cabecera>
            <Lista v-for='item in items' :key='item.id' v-bind:id='item.id'
            v-bind:texto='item.texto' v-bind:comprado='item.comprado'
            :class="{comprado:item.comprado}" v-model='item.comprado'></Lista>
  </div>
</template>

<!--Plantilla que contiene dos componentes, una cabecera y 
la lista de la compra que contiene a su vez el v-for para
añadir todos los elementos que se vayan añadiendo
Se importan ambos componentes, a su vez, se añade los estilos,
y se especifica que la aplicación devuelve como datos los items-->


<script>
// @ is an alias to /src
import Lista from '@/components/Lista.vue'
import Cabecera from '@/components/Cabecera.vue'

export default {
  name: 'Home',
  components: {
    Lista,Cabecera
  },  
  data: function(){
    return {
      items:[]
      }
  }

      
}
</script> 

    <style>
        .comprado{
            text-decoration: line-through;

        }
    </style>