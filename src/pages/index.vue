<template>
  <NuxtPage />
</template>

<script lang="ts">
import { definePageMeta, useSeoMeta } from '#imports';

export default {
  setup () {
    definePageMeta({ layout: 'generic' })
    useSeoMeta({ 
      title: 'Jay Cruz Portfolio',
      description: 'Developer Portfolio Website for Jay Cruz',
    })
    navigateTo('/work')
  }
}
</script>
