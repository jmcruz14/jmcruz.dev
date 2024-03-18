<template>
  <header class="title-bar">
    <hgroup>
      <h1>
        Jay Cruz
      </h1>
      <!-- NOTE: add some hover effect here to shower "Aspiring Data Scientist/Engineer" -->
      <h3 class="title-designation">
        Software Developer
      </h3>
    </hgroup>
  
    <nav class="personal-links">
      <ul>
        <li>
          <NuxtLink title="LinkedIn" to="https://www.linkedin.com/in/juan-carlos-c-54530b16b/" target="_blank" rel="author noreferrer noopener">
            <img src="~/assets/images/linkedin-logo.png" alt="LinkedIn Link" class="icon-size">
          </NuxtLink>
        </li>
        <li>
          <NuxtLink title="GitHub" to="https://github.com/jmcruz14" target="_blank" rel="author noreferrer noopener">
          <img src="~/assets/images/github_icon.svg" alt="GitHub Link" class="icon-size">
          </NuxtLink>
        </li>
        <li>
          <NuxtLink title="Email" to="mailto:jccruz009@yahoo.com" target="_blank" rel="author noreferrer noopener">
            <img src="~/assets/images/email_icon.png" alt="Email Link" class="icon-size">
          </NuxtLink>
        </li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
.title-designation {
  transition: color 0.3s ease-in-out;
}

.title-designation:hover {
  cursor: crosshair;
}

h3:hover::after {
  content: "Aspiring Data Scientist/Engineer";
  color: rgb(95, 146, 95); /* Change color of the added text */
  transition: color 0.3s ease-in-out;
}
</style>