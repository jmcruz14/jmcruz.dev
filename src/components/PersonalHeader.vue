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
          <Tooltip text="LinkedIn" fontSize="14px">
            <NuxtLink to="https://www.linkedin.com/in/juan-carlos-c-54530b16b/" target="_blank" rel="author noreferrer noopener" class="download-link">
              <i class="lab la-linkedin"></i>
            </NuxtLink>
          </Tooltip>
        </li>
        <li>
          <Tooltip text="Medium" fontSize="14px">
            <NuxtLink to="https://medium.com/@jcmcruz14" target="_blank" rel="author noreferrer noopener" class="download-link">
              <i class="lab la-medium"></i>
            </NuxtLink>
          </Tooltip>
        </li>
        <li>
          <Tooltip text="GitHub" fontSize="14px">
            <NuxtLink to="https://github.com/jmcruz14" target="_blank" rel="author noreferrer noopener" class="download-link">
              <i class="lab la-github"></i>
            </NuxtLink>
          </Tooltip>
        </li>
        <li>
          <Tooltip text="Email" fontSize="14px">
            <NuxtLink to="mailto:jccruz009@yahoo.com" target="_blank" rel="author noreferrer noopener" class="download-link">
              <i class="las la-envelope"></i>
            </NuxtLink>
          </Tooltip>
        </li>
        <li>
          <Tooltip text="Resume" fontSize="14px">
            <NuxtLink to="/jccruz_resume.pdf" download="RESUME - JUAN CARLOS CRUZ" class="download-link">
              <i class="las la-file-alt"></i>
            </NuxtLink>
          </Tooltip>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script lang="ts">
import Tooltip from './Tooltip.vue'

export default {
  components: {
    Tooltip
  },
  setup () {

  }
}
</script>

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

a {
  margin-inline: 0.5em;
}

h3:hover::after {
  content: "Data Scientist/Engineer";
  color: rgb(95, 146, 95); /* Change color of the added text */
  transition: color 0.3s ease-in-out;
}
</style>