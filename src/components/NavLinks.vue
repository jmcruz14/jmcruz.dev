<template>
  <nav class="nav-links">
    <ul>
      <li>
        <!-- @click.stop="() => {
          $router.navigateTo({ path: '/', hash: '#about-me'})
          activeLink = 'about-me'
        }" -->
        <NuxtLink
          :to="{ hash: '#about-me' }"
          rel="next author noreferrer noopener"
          class="cursor-hover"
          :style="{ 'text-decoration: underline': activeLink === 'about-me' }"
        >
          About Me
        </NuxtLink>
      </li>
      <li>
        <!-- @click.stop="() => {
          $router.push({ path: '/', hash: '#work'})
          activeLink = 'work'
        }" -->
        <NuxtLink
          :to="{ hash: '#work' }"
          rel="next author noreferrer noopener"
          class="cursor-hover"
          :style="{ 'text-decoration: underline': activeLink === 'work' }"
        >Work</NuxtLink>
      </li>
      <li>
        <!-- @click.stop="() => {
          $router.push({ path: '/', hash: '#projects'})
          activeLink = 'projects'
        }"  -->
        <NuxtLink
          :to="{ hash: '#projects' }"
          rel="next author noreferrer noopener" 
          class="cursor-hover"
          :style="{ 'text-decoration: underline': activeLink === 'projects' }"
        >
            Projects
        </NuxtLink> 
      </li>
    </ul>
  </nav>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router';

export default {
  setup () {

    const route = useRoute();
    const router = useRouter();
    const activeLink = ref(null);

    onBeforeRouteUpdate((to, from) => {
      console.warn('navigation-to', to);
      console.warn('navigation-from', from);
    })
    
    // Check if the current URL ends with "index.html"
    // if (currentUrl.endsWith("index.html") || currentUrl.endsWith("/")) {
    //   // If yes, set the text-decoration of the element with href "index.html" to "underline"
    //   // since we currently have two html files in the root directory
    //   // simple if-else statement is fine
    //   document.querySelector("a[href='index.html']").style.textDecoration = "underline";
    // } else if (currentUrl.endsWith("work.html")) {
    //   document.querySelector("a[href='work.html']").style.textDecoration = "underline";
    // } else if (currentUrl.endsWith("projects.html")) {
    //   // If not, set the text-decoration of the element with ID "my-link" to "none"
    //   document.querySelector("a[href='projects.html']").style.textDecoration = "underline";
    // }

    return {
      activeLink,
    }
  }
}
</script>