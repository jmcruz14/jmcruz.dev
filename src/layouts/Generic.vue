<template>
  <SpeedInsights/>
  <div>
    <PersonalHeader />
    <NavLinks />
      <slot />
  </div>
</template>

<script>
import { SpeedInsights } from '@vercel/speed-insights/vue';
import PersonalHeader from '~/components/PersonalHeader.vue'
import NavLinks from '~/components/NavLinks.vue'

export default {
  components: {
    SpeedInsights,
    PersonalHeader,
    NavLinks,
  },
  setup () {
    return {

    }
  }
}
</script>