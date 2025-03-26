<template>
  <router-view/>
</template>

<style>
:root {
  --primary-color: #42b983;
  --secondary-color: #35495e;
  --light-gray: #f5f5f5;
  --medium-gray: #e0e0e0;
  --dark-gray: #2c3e50;
  --error-color: #ff4444;
  --success-color: #00c851;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--dark-gray);
  line-height: 1.6;
  min-height: 100vh;
  background-color: #f9f9f9;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
