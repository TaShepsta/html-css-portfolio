<template>
  <div class="container">
     <section id="contact">
       <h2>Contact Me</h2>
       <p class="contact-intro">Feel free to reach out to me on my Github profile and LinkedIn.</p>
       <!-- social links -->
      <div class="social-links">
       <p>
        <strong>Github:</strong> <a href="https://github.com/TaShepsta" target="_blank">TaShepsta</a></p>
       <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/lisekho-smith-407840226" target="_blank">Lisekho Smith</a></p>
      </div>
   <!-- Leave me a message form -->
    <h3>Leave me a message</h3>
    <form action="https://formspree.io/f/xzdwnjjr" method="POST">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>
      <label for="email">Email:</label>
      <input type="email" id="email" name="_replyto" required>
      <label for="message">Message:</label>
      <textarea id="message" name="message" rows="5" required></textarea>
      <button type="submit">Send</button>
    </form>
    </section>
  </div>
   <footer>
    <p>&copy; 2026 My Portfolio - Lisekho Smith</p>
   </footer>
</template>