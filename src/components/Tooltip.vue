<template>
  <div class="wrapper" @mouseenter="onMouseEnter" @mouseleave="onMouseLeave">
    <slot :open="open">
    </slot>

    <div v-if="open" ref="container" class="container">
      <Transition appear>
        <div class="developer-text content">
          <slot name="text">
            <span :style="{ 'font-size': fontSize }">
              {{ text }}
            </span>
          </slot>
        </div>
      </Transition>
    </div>
  </div>

</template>

<script>
import { ref, computed, toRef } from 'vue'

export default {
  props: {
    text: {
      type: String,
      default: null
    },
    fontSize: {
      type: String,
      default: '16px'
    },
    openDelay: {
      type: Number,
      default: 100
    },
    closeDelay: {
      type: Number,
      default: 100
    }
  },
  setup (props, { emit }) {
    const open = ref(false);
    const onMouseEnter = () => {
      if (open?.value) {
        return
      }
      open.value = true
    }

    const onMouseLeave = () => {
      if (!open.value) { 
        return
      }
      open.value = false
    }

    return {
      open,
      onMouseEnter,
      onMouseLeave
    }
  }
}
</script>

<style scoped>
.wrapper {
  position: relative;
}

.container {
  position: absolute;
  width: 100%;
  margin: auto;
}

.content { 
  background: black;
  color: white;
  text-align: center;
}

</style>