
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
            <lista v-for='item in items' :key='item.id' v-bind:id='item.id'
            v-bind:texto='item.texto' v-bind:comprado='item.comprado'
            :class="{comprado:item.comprado}" v-model='item.comprado'>

        </lista>    
  </div>
</template>




<script>
// @ is an alias to /src
import lista from '@/components/lista.vue'

export default {
  name: 'Home',
  components: {
    listaCentral,lista
  },  

      
}
</script> 