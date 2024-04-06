<template>
  <main class="animate-opacity projects" id="projects">

    <!-- Tab Links -->
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
    
    <section class="project-content" :class="{hidden: selectedTab === 'softwareTab' ? false : true}">
      <section class="project-info">
        <div class="image-box"> <!-- to adjust image as a content model w/in flex-item -->
          <img src="~/assets/images/ritual.png" alt="Video Color Analyzer Preview">
        </div>
        <article>
          <h2>Video Color Analyzer</h2>
          <h4>April 18, 2023</h4>
          <p>
              Python script using OpenCV-Python, Pillow, and various preprocessing & processing packages to return the most frequent
              colors in a video file.
          </p>
          <nav class="project-links">
              <ul>
                  <li class="github-link">
                      <a href="https://github.com/jmcruz14/dominant_color_analyzer">GitHub</a>
                  </li>
              </ul>
          </nav>
        </article>
      </section>
        
      <section class="project-info">
          <div class="image-box">
            <img src="~/assets/images/top_250.jpeg" alt="Top 250 Letterboxd Preview">
          </div>
          <article>
            <h2>
                Analysis of the Top 250 Filipino Movies on Letterboxd
            </h2>
            <h4>
                March 29, 2023
            </h4>
            <p>
                An Exploratory Data Analysis of the 'Top 250 Filipino Movies' on social
                media website Letterboxd.
            </p>
            <nav class="project-links">
              <ul>
                <li class="github-link">
                  <a href="https://github.com/jmcruz14/top_250_filipino_eda">GitHub</a>
                </li>
              </ul>
            </nav>
          </article>
      </section>
  
      <section class="project-info">
        <div class="image-box">
          <img src="~/assets/images/phr4r_logo.png" alt="Reddit R4R Webscrape Preview">
        </div>
        <article>
          <h2>
            r/phr4r webscrape and analysis
          </h2>
          <h4>
            July 15, 2022
          </h4>
          <p>
            A study of the r/phr4r subreddit's demographics and other observable trends through data webscraped from June 15 to 22, 2022.
        Data webscraped using the pRAW package and analyzed with pandas and matplotlib.
          </p>
          <nav class="project-links">
            <ul>
              <li class="github-link">
                <a href="https://github.com/jmcruz14/r4r_webscraper_app" target="_blank" rel="noopener noreferrer">GitHub</a>
              </li>
              <li class="blog-link">
                <a href="https://medium.com/@carlczech/the-underlying-trends-of-phr4r-515314ceed43" target="_blank" rel="noopener noreferrer">Blog</a>
              </li>
            </ul>
          </nav>
        </article>
      </section>
      
      <section class="project-info">
        <div class="image-box">
          <img src="~/assets/images/geospatial_image.jpg" alt="Route Optimization Preview">
        </div>
        <article>
          <h2>
            Route Optimizer Program for Last-Mile Delivery
          </h2>
          <h4>
            June 2022
          </h4>
          <p>
            Geospatial Navigation program utilizing Google Geocoder and MapQuest APIs using Dash Plotly framework.
          </p>
        </article>
      </section>
    </section>

    <section class="analytics-content" :class="{hidden: selectedTab === 'dataTab' ? false : true}">
      <div style="border: 1px solid grey; border-radius: 5px; padding: 1.5em; display: flex; gap: 0.75em; background-color: rgb(237, 237, 237); align-items: center">
        <i class="las la-exclamation-triangle" style="font-size: 32px;"></i>
        <span style="font-weight: 300; font-size: 28px">Data-powered projects coming soon!</span>
      </div>
    </section>
      
  </main>
</template>

<script>
import { definePageMeta, useSeoMeta } from '#imports';
import { ref, onMounted } from 'vue';

export default {
  setup () {
    definePageMeta(
      { layout: 'generic' }
    )
    useSeoMeta(
      {
        title: 'Projects - Jay Cruz',
        description: 'List of projects worked on'
      }
    )

    const softwareTab = ref(null);
    const dataTab = ref(null);
    const selectedTab = ref('softwareTab');
    const selectTab = (e, refLoc) => {
      console.warn('ref-loc', refLoc)
      selectedTab.value = refLoc
    }

    return {
      softwareTab,
      dataTab,
      selectedTab,
      selectTab
    }
  },
}

</script>

<style scoped>
  /* Projects Page */
  main.projects {
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    align-items: center;
    gap: 5em;
    margin-block-start: 5em;
  }

  .hidden {
    display: none !important;
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

  /* Project Content */
  section.project-content {
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    align-items: center;
    gap: 5em;
  }

  /* Project Info Rules */
  section.project-info {
      width: 50%;
      display: flex;
      gap: 2em;
      box-sizing: border-box;
  }

  section.project-info h2, section.project-info h4 {
      font-family: 'Lato'
  }

  section.project-info h2 {
      font-weight: 500;
      margin-block-start: 0em;
      margin-block-end: 0em;
  }

  section.project-info h4 {
      font-weight: 400;
      color: #939393;
      margin-block-start: 0em;
  }

  section.project-info p {
      font-weight: 300;
      color: black;
  }

  /* Project Info Flex Item Widths */
  section.project-info img {
      width: 199px;
      height: 187px; 
  }

  div.image-box {
      justify-self: center;
  }

  section.project-info article {
      width: 80%;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
  }

  /* Project Info Nav Link Rules */
  section.project-info nav {
      padding-block-start: 1em;
  }

  section.project-info nav > ul {
      display: flex;
      flex-direction: row;
      padding: 0;
      margin: 0;
  }


  section.project-info nav > ul > li {
      list-style-type: none;
      width: 73px;
      height: 20px;
      text-align: center;
      line-height: 16px;
      margin-inline-end: 0.5em;
  }

  section.project-info nav > ul > li > a {
      text-decoration: none;
      color: white;
      font-size: 10px;
      font-weight: 300px;
  }

  section.project-info li.github-link {
      background-color: #BF78CB;
      border-radius: 50px;
  }

  section.project-info li.blog-link {
      background-color: #4C60CC;
      border-radius: 50px;
  }

  /* Mobile Page */
  @media screen and (max-width: 640px) {
    section.project-info {
      flex-direction: column;
      align-items: center;
      width: 80%;
    }

    nav.project-links {
      display: flex;
      justify-content: center;
    }
  }
</style>