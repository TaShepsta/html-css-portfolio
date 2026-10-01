<template>
  <main>
    <!-- Home Section -->
     <header id="home">
      <h1>Welcome to My Portfolio</h1>
      <p>This is a showcase of my work, skills, and experiences.</p>
      <a href="#about" class="btn" @click.prevent="scrollToAbout">About Me</a>
     </header>
  </main>

  <!-- About Section -->
   <div class="container">
    <section id="about">
      <h2 class="section-title">About Me</h2>
      <div class="about-wrapper">
        <div class="about-image">
          <img src="https://i.ibb.co/wNx4nVnT/IMG-1084.jpg" alt="Profile Image" border="o">
        </div>
        <div class="about-text">
          <p>Good day! I'm Lisekho Smith, a detail-oriented graduate with an Advance Diploma in Management transitioning to software development and data analytics. I'm excited to share my journey and accomplishments with you.</p>
        </div>
      </div>
    </section>
   </div>

   <footer>
    <p>&copy; 2026 My Portfolio - Lisekho Smith</p>
   </footer>
</template>

<script setup>
const scrollToAbout = () => {
  document.getElementById('about')?.scrollIntoView({behavior: 'smooth'})
};
</script>

