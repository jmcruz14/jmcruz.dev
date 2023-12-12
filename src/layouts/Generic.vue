<template>
  <SpeedInsights/>
  <div>
    <PersonalHeader />
    <slot />
  </div>
</template>

<script>
import { SpeedInsights } from '@vercel/speed-insights/vue';
import PersonalHeader from '~/components/PersonalHeader.vue'

export default {
  components: {
    SpeedInsights,
    PersonalHeader,
  },
  setup () {
    return {

    }
  }
}
</script>