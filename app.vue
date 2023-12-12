<script setup>
import { SpeedInsights } from '@vercel/speed-insights'
</script>

<template>
  <div>
    <SpeedInsights/>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
