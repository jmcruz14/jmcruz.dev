<template>
  <div>
    <PersonalHeader />
    <slot />
  </div>
</template>

<script>
import PersonalHeader from '~/components/PersonalHeader.vue'

export default {
  components: {
    PersonalHeader,
  },
  setup () {
    return {

    }
  }
}
</script>