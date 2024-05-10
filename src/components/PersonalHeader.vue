<template>
  <header class="title-bar">
    <hgroup>
      <h1 class="developer-text">
        Jay Cruz
      </h1>
      <h3 class="title-designation developer-text">
        Software Developer
      </h3>
    </hgroup>
  
    <nav class="personal-links">
      <ul>
        <li>
          <NuxtLink title="LinkedIn" to="https://www.linkedin.com/in/juan-carlos-c-54530b16b/" target="_blank" rel="author noreferrer noopener" class="download-link">
            <i class="lab la-linkedin"></i>
          </NuxtLink>
        </li>
        <li>
          <NuxtLink title="GitHub" to="https://github.com/jmcruz14" target="_blank" rel="author noreferrer noopener" class="download-link">
            <i class="lab la-github"></i>
          </NuxtLink>
        </li>
        <li>
          <NuxtLink title="Email" to="mailto:jccruz009@yahoo.com" target="_blank" rel="author noreferrer noopener" class="download-link">
            <i class="las la-envelope"></i>
          </NuxtLink>
        </li>
        <li>
          <NuxtLink title="Resume" to="/jccruz_resume.pdf" download="RESUME - JUAN CARLOS CRUZ" class="download-link">
            <i class="las la-file-alt"></i>
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

.download-link {
  font-size: 38px;
  color: black;
}

h3:hover::after {
  content: "Data Scientist/Engineer";
  color: rgb(95, 146, 95); /* Change color of the added text */
  transition: color 0.3s ease-in-out;
}
</style>