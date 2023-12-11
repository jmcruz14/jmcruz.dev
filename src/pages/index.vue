<template>
  <span>Test</span>
  <span>What?</span>
</template>

<script>
import { definePageMeta, useSeoMeta } from '#imports';

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
  setup () {
    definePageMeta({ layout: 'generic' })
    useSeoMeta({ 
      title: 'Jay Cruz Portfolio',
      description: 'Developer Portfolio Website for Jay Cruz',
    })

    return {}
  }
}
</script>
