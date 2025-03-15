<template>
  <div
    class="box-card-main"
    @click.prevent="isModalOpen = true"
  >

     <NuxtImg :src="imgSrc" />
     <h2 style="padding-top: 10px">{{ title }}</h2>
     <h4>{{ projectYear }}</h4>

     <div class="links">
        <i v-if="githubLink" class="lab la-github"></i>
        <i v-if="blogLink" class="las la-newspaper"></i>
      <!-- show github, blog links, sample website -->
     </div>

  </div>

  <!-- Modal Component -->
  <div v-if="isModalOpen" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h2>{{ title }}</h2>
        <div class="close-button" @click="isModalOpen = false">
          <i class="las la-times"></i>
        </div>
      </div>
      
      <div class="modal-body">
        <NuxtImg :src="imgSrc" class="modal-image" />
        
        <div class="modal-details">
          <h3>Project Details</h3>
          <p>Year: {{ projectYear }}</p>
          <p v-if="description">{{ description }}</p>
          <p v-else>This is a detailed view of the {{ title }} project created in {{ projectYear }}. 
            Additional information about this project would be displayed here.</p>
            
          <div class="modal-links">
            <NuxtLink v-if="githubLink" 
              :href="githubLink" 
              target="_blank" 
              class="link-button"
            >
                <i class="lab la-github"></i> GitHub
            </NuxtLink>
            <NuxtLink 
              v-if="blogLink" 
              :href="blogLink" 
              target="_blank"
              class="link-button">
              <i class="las la-newspaper"></i> Blog
            </NuxtLink>
            
            <a v-if="demoLink" :href="demoLink" target="_blank" class="link-button">
              <i class="las la-external-link-alt"></i> Live Demo
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  props: {
    imgSrc: {
      type: String,
      default: null
    },
    title: {
      type: String,
      default: "Default Title"
    },
    projectYear: {
      type: Number,
      default: 2025
    },
    description: {
      type: String
    },
    githubLink: {
      type: String,
      default: null
    },
    blogLink: {
      type: String,
      default: null
    },
    demoLink: {
      type: String,
      default: null
    }
  },
  setup () {
    const isModalOpen = ref(false);

    return {
      isModalOpen
    }
  }
}

</script>

<style scoped>
  .box-card-main {
    padding: 1em;
    margin: 0;

    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .box-card-main:hover {
    border: 1px grey solid;
    box-shadow: 5px 10px 18px #888888;
    cursor: pointer;
    transition: border 0.3s ease, box-shadow 0.3s ease;
  }
  
  .links {
    display: flex;
    align-items: center;
    gap: 2em;
    margin-top: 10px;

    font-size: 2em;
  }

  h1, h2, h3, h4, h5, h6 {
    padding: 0;
    margin: 0;

    text-wrap: wrap;
  }

  h2 {
    font-family: "Lato";
    font-weight: 400;
    word-wrap: break-word;
    overflow-wrap: break-word;
    max-width: 33vw;

  }

  h4 {
   font-family: "Lato";
   font-weight: 500;
   color: #939393;
  }

  img {
    /* margin: 0.25em; */
    width: 199px;
    height: 187px;
  }

  /* Modal styles */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
    animation: fadeIn 0.3s ease;
  }

  .modal-content {
    background-color: white;
    border-radius: 8px;
    width: 80%;
    max-width: 800px;
    max-height: 90vh;
    overflow-y: auto;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    animation: slideIn 0.3s ease;
  }

  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    border-bottom: 1px solid #eee;
  }

  .modal-details {
    flex: 1;
  }

  .close-button {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    height: 32px;
    width: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.2s;
  }

  .close-button:hover {
    background-color: #f0f0f0;
  }

  .link-button {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: #f0f0f0;
    border-radius: 4px;
    text-decoration: none;
    color: #333;
    transition: background-color 0.2s;
  }

  .link-button:hover {
    background-color: #e0e0e0;
  }

  .modal-body {
    padding: 1.5rem;
    display: flex;
    flex-direction: row;
    gap: 1.5rem;
  }
</style>