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

<script lang="ts">
import type { PropType } from 'vue'
import { ref, computed, toRef, defineComponent } from 'vue';

interface Props {
  text: string | null
  fontSize: string
  openDelay: number
  closeDelay: number
}

export default {
  props: {
    text: {
      type: String as PropType<string | null>,
      default: null
    },
    fontSize: {
      type: String as PropType<string>,
      default: '16px'
    },
    openDelay: {
      type: Number as PropType<number>,
      default: 100
    },
    closeDelay: {
      type: Number as PropType<number>,
      default: 100
    }
  },
  setup (props: Props, { emit }) {
    const open = ref<boolean>(false);
    const onMouseEnter = (): void => {
      if (open?.value) {
        return
      }
      open.value = true
    }

    const onMouseLeave = (): void => {
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