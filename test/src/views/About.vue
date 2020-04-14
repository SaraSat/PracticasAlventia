<template>
  <div class="about">
    <RelojCentral v-bind:relojes='relojes'></RelojCentral>
  </div>
</template>
<!--La aplicación tiene un reloj central que contiene los 
datos de cada uno de ellos -->

<script>
import RelojCentral from '@/components/RelojCentral.vue'

export default {
  name:'About',
  components:{
    RelojCentral,
  },
    data: function(){
    return {
      relojes:[
        {
          nombre:'Madrid',
          offset:0,
          Rleft:10
        },

        {
          nombre:'Lisboa',
          offset:-1,
          Rleft:10,
          Rtop:100
        },
        {
          nombre:'Nueva York',
          offset:-6,
          Rleft:150,
          Rtop:47.5
        },
        {
          nombre:'Nuena Delhi',
          offset:4.5,
          Rleft:300,
          Rtop:-5
        }
      ]
      }
  }

}
</script>
