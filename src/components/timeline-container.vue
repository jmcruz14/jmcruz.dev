<template>
  <div 
    class="container"
    :style="{'background-color': workTypeColor(workType)}"
  >
    <img 
      v-if="workLogoImage" 
      :src="`/work-logos/${workLogoImage}.png`"
    >
    <img
      v-else-if="workLogoUrl"
      :src="workLogoUrl"
    >
    <i 
      v-else 
      class="las la-briefcase" 
      style="font-size: 90px;"
    />
    <section>
      <hgroup>
        <h2>{{ company }}</h2>
        <h3>{{ title }}</h3>
        <h4>{{ startDate }} - {{ endDate }}</h4>
      </hgroup>
    </section>
    
    <!-- extra info -->
     <!-- TODO: re-enable later -->
    <!-- <div style="width: 100%" v-if="hasInfo">
      <div style="font-size:24px;width:100%; display:flex; justify-content: space-around;">
        <i class="las la-angle-double-down"></i>
        <span>More info</span>
      </div>
      <slot name="hover-info" />
    </div> -->
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  props: {
    workLogoImage: {
      type: String,
      default: ''
    },
    workLogoUrl: {
      type: String,
      default: ''
    },
    company: {
      type: String,
      default: 'Company Name'
    },
    title: {
      type: String,
      default: 'Generic Title'
    },
    startDate: {
      type: String,
      default: 'No Date'
    },
    endDate: {
      type: String,
      default: ''
    },
    workType: {
      type: String,
      default: 'paid'
    },
    hasInfo: {
      type: Boolean,
      default: false
    }
  },
  setup (props, { emit }) {
    const hoverOpen = ref(false);
    const toggleDivOpen = () => {
      hoverOpen.value = true;
    }
    const toggleDivClose = () => {
      hoverOpen.value = false;
    }

    const workTypeColor = (workType) => {
      // if (workType === 'volunteer') return 'white'
      return '#F9F8F8'
    }

    return {
      toggleDivOpen,
      toggleDivClose,

      workTypeColor,
      hoverOpen,
    }
  }
}

</script>

<style scoped>
hgroup > h1, 
hgroup > h2, 
hgroup > h3, 
hgroup > h4,
hgroup > h5,
hgroup > h6 {
  margin-block: 0px
}

h2 {
  font-size: 20px;
  font-weight: 600
}

h3 {
  font-weight: 500;
}

h4 {
  font-weight: 400
}

.hover-info {
  position: absolute;
  background-color: white;
  width: 300px;
  right: -20.5em;
  padding-right: 0.75em;
  box-shadow: 8px 9px 0px 0px rgba(0, 0, 0, 0.3);
}

.container {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1em;
  /* width: 45%; */
  padding: 20px;
  height: 90px;

  background-color: #C7C7C7;
  border: 1px solid #737373;
  border-radius: 10px;
}

/* .container:hover {
  background-color: rgba(150, 150, 150, 0.813) !important;
  cursor: pointer;
} */

.container section {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.container img {
    width: 20%;
  }

.container section > ul {
  padding-left: 20px;
}

@media screen and (max-width: 640px) {
  /* Full-width containers */
  .container {
      width: 75%;
      padding: 20px;
    }

  /* Make sure that all arrows are pointing leftwards */
    .container::before {
      left: 60px;
      border: medium solid white;
      border-width: 10px 10px 10px 0;
      border-color: transparent white transparent transparent;
    }
}


</style>