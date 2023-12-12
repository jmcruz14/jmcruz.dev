<template>
  <NavLinks />


  <component :is="selectedComponent" />
</template>

<script>
import { onMounted, watch, ref, markRaw } from 'vue';
import NavLinks from '@/components/NavLinks';
import { definePageMeta, useSeoMeta } from '#imports';
import { useRoute, useRouter } from 'vue-router';

import AboutMe from '@/components/content/about-me';
import Projects from '@/components/content/projects';
import Work from '@/components/content/work';

// export default (opts) => {
//   definePageMeta({
//     layout: opts.layout || 'default',
//   });

//   useSeoMeta({
//     title: opts.title || 'Home page title',
//     description: opts.description || 'Home page description',
//     image: opts.image || 'https://via.placeholder.com/1200x630',
//   });
// };


export default {
  components: {
    NavLinks,
    AboutMe,
    Work,
    Projects,
  },
  setup () {
    const route = useRoute();
    const router = useRouter();
    const selectedComponent = ref(null);
    definePageMeta({ layout: 'generic' })
    useSeoMeta({ 
      title: 'Jay Cruz Portfolio',
      description: 'Developer Portfolio Website for Jay Cruz',
    })

    watch(() => route.hash, (newRouteHash) => {
      // console.warn('new-route-hash', newRouteHash);
      if (!newRouteHash || newRouteHash === '#about-me') {
        selectedComponent.value = markRaw(AboutMe);
      }
      if (newRouteHash === '#work') {
        selectedComponent.value = markRaw(Work)
      }
      if (newRouteHash === '#projects') {
        selectedComponent.value = markRaw(Projects)
      }
    }, { immediate: true, deep: true });

    return {
      selectedComponent
    }
  }
}
</script>
