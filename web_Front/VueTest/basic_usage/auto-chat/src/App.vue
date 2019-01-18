<template>
  <div id="app"> <!--这个是容器, 各个组件都会在这里得到承载-->
    <router-view/> <!--这是展示区-->
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  html {
    height: 100%;
    width: 100%;
    margin: 0px;
    padding: 0px;
  }

  body {
    height: 100%;
    width: 100%;
    margin: 0px;
    padding: 0px;
  }

  p {
    margin: 0px;
  }

  #app {
    height: 100%;
    width: 100%;
  }

  ul {
    margin: 0px;
    padding: 0px 0px 46px 0px;
  }

  li {
    padding: 6px 12px;
    list-style: none;
  }
 
</style>
