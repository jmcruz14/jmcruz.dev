<template>
  <NavLinks />
</template>

<script>
import NavLinks from '@/components/NavLinks';
import { definePageMeta, useSeoMeta } from '#imports';
import { useRoute, useRouter } from 'vue-router';

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
  },
  setup () {
    definePageMeta({ layout: 'generic' })
    useSeoMeta({ 
      title: 'Jay Cruz Portfolio',
      description: 'Developer Portfolio Website for Jay Cruz',
    })

    const route = useRoute();
    const router = useRouter();

    return {}
  }
}
</script>
