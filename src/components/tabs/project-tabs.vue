<template>
  <div class="content">
    <div class="tabs">
      <button class="tablinks" ref="softwareTab" :class="{active: selectedTab === 'softwareTab' ? true : false}" @click="selectTab($event, 'softwareTab')">
        <i class="las la-hammer"></i>
        <span>Software</span>
      </button>
      <button class="tablinks" ref="dataTab" :class="{active: selectedTab === 'dataTab' ? true : false}" @click="selectTab($event, 'dataTab')">
        <i class="las la-chart-bar" />
        <span>Data</span>
      </button>
    </div>
  
    <!-- <div class="tab-description">
      <p>{{ tabDesc }}</p>
      <hr>
    </div> -->
  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  props: {
    selectedTab: {
      type: String,
      default: 'softwareTab',
    }
  },
  emits: ['change-tab'],
  setup (props, { emit }) {
    const currentTab = computed({
      get: () => props?.selectedTab,
      set: (val) => emit('change-tab', val)
    });
    // const tabDesc = ref(`I think developing software through programming is just as important as analyzing, building, and preserving data systems. Here is a collection of work that I'm proud of.`)

    const selectTab = (event, tabName) => {
      currentTab.value = tabName;

      // switch (tabName) {
      //   case 'softwareTab':
      //     tabDesc.value = "I think developing software through programming is just as important as analyzing, building, and preserving data systems. Here is a collection of work that I'm proud of."
      //     break
      //   case 'dataTab':
      //     tabDesc.value = `
      //       I believe we live in 
      //       a data-driven society and understanding data is highly important in this world.
      //       Here are some studies and explorations I've undertaken since I've started doing this.
      //     `
      //     break
      //   default:
      //     tabDesc.value = 'N/A'
      // }
    }
    return {
      currentTab,
      // tabDesc,
      selectTab
    }
  }
}
</script>

<style scoped>
  /* Content */
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.25em;
  }

  /* Tabs */
  .tabs {
    display: flex;
    gap: 2.5em;
  }

  .tabs button {
    display: flex;
    align-items: center;
    gap: 0.25em;
    background-color: inherit;
    font-family: var(--font-family);
    font-weight: 400;
    font-size: 18px;

    border: 0.5px solid grey;
    border-radius: 9999px;
    cursor: pointer;
    padding: 9px 12px;
    transition: 0.3s;
  }

  /* Change background color of buttons on hover */
  .tabs button:hover {
    background-color: #ddd;
  }

  /* Create an active/current tablink class */
  .tabs button.active {
    background-color: #000000;
    color: rgb(237, 237, 237)
  }

  /* Description */
  .content .tab-description {
    width: 50%;
    font-weight: 300;
    letter-spacing: 0.025em;
    line-height: 1.5em;
  }
</style>