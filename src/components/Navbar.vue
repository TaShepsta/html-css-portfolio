<template>
  <nav>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/projects">Projects</router-link></li>
      <li><router-link to="/contact">Contact</router-link></li>
      <li><router-link to="/education">Learning Journey</router-link></li>
      <li><router-link to="/gallery">Gallery</router-link></li>
      <li><router-link to="/reflection">Reflection</router-link></li>
    </ul>
  </nav>
</template>

<style scoped>
nav {
  background-color: #333;
  color: #fff;
  padding: 15px;
  text-align: center;
  position: sticky;
  top: 0;
  z-index: 100;
  animation: slideDown 0.6s ease;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 24px;
  margin: 0;
  padding: 0;
}

nav ul li a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

nav ul li a:hover {
  color: #93C5FD;
}
</style>