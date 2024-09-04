<template>
  <div 
    class="container"
  >
    <img v-if="work_logo_image" :src="`/work-logos/${work_logo_image}.png`">
    <i v-else class="las la-briefcase" style="
      font-size: 90px;
    "></i>
    <section>
      <hgroup>
        <h2>{{ company }}</h2>
        <h3>{{ title }}</h3>
        <h4>{{ startDate }} - {{ endDate }}</h4>
      </hgroup>
    </section>
    
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  props: {
    work_logo_image: {
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
  },
  setup (props, { emit }) {
    return {
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

.container {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1em;
  width: 45%;
  padding: 20px;

  background-color: #C7C7C7;
  border: 1px solid #737373;
  border-radius: 9999px;
}

.container > section {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.container > img {
    width: 20%;
    height: 20%;
  }

.container > section > ul {
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