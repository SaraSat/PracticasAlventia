<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">ListaCompra</router-link> | 
      <router-link to="/about">Relojes</router-link>
    </div>
    <router-view/>
<!--En la app, hay dos links,ver router/index.js, 
ahi se especifica las rutas de cada link, home y about en este caso, 
donde en cada uno se generan una serie de componentes distintos,
los ejercicios de la  lista de la compra y el del reloj central
En views se pueden ver -->
  </div>
</template>
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
