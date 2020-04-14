<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
            <h4>Añadir producto</h4>
        <input type="text" ref="newItem">
        <button @click="add">Añadir</button>

  </div>
</template>
<script>
export default {
        data:function(){
          return{
            items:[]
          }
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
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
