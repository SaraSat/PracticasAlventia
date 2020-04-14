
<!-- <template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>


<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script> -->
<template>
  <div class="home">
    <Cabecera v-bind:items='items'></Cabecera>
            <Lista v-for='item in items' :key='item.id' v-bind:id='item.id'
            v-bind:texto='item.texto' v-bind:comprado='item.comprado'
            :class="{comprado:item.comprado}" v-model='item.comprado'></Lista>
  </div>
</template>




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