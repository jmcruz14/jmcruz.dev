<template>
  <main class="animate-opacity projects" id="projects">

    <!-- Tab Links -->
    <Tabs :selected-tab="selectedTab" @change-tab="(e) => selectedTab = e"/>
    
    <section
      class="project-grid animate-opacity"
      :class="{hidden: selectedTab === 'softwareTab' ? false : true}"
    >
      <BoxCard 
        imgSrc="/ritual.png"
        title="Video Color Analyzer"
        :projectYear=2023
        description="Python script using OpenCV-Python, Pillow, and various preprocessing & processing packages to return the most frequent
              colors in a video file."
        githubLink="https://github.com/jmcruz14/dominant_color_analyzer"
      />
      <BoxCard 
        imgSrc="/geospatial_image.jpg"
        title="Route Optimizer Program"
        :projectYear=2022
        description="Geospatial Navigation program utilizing Google Geocoder and MapQuest APIs using Dash Plotly framework."
      />

    </section>
      

    <section 
      class="project-grid animate-opacity" 
      :class="{hidden: selectedTab === 'dataTab' ? false : true}"
    >
      <BoxCard 
        imgSrc="/dashboard_prev.png"
        title="Letterboxd List Dashboard"
        :projectYear=2024
        description="A project built using the NuxtJS, FastAPI, and MongoDB stack with the goal of
            featuring a Letterboxd list according to its observed statistical data.

            The project utilizes a personal Top 250 list as a starting point for this project."
        githubLink="https://github.com/jmcruz14/top-250-website"
        blogLink="https://medium.com/@jcmcruz14/documenting-projects-ep-1-the-letterboxd-list-dashboard-603075a4f869"
      />

      <BoxCard 
        imgSrc="/top_250.jpeg"
        title="Letterboxd List Analysis"
        :projectYear=2023
        description="An Exploratory Data Analysis of the 'Top 250 Filipino Movies' on social
            media website Letterboxd."
        githubLink="https://github.com/jmcruz14/top_250_filipino_eda"
      />

      <BoxCard 
        imgSrc="/phr4r_logo.png"
        title="r4r webscrape-analysis"
        :projectYear=2022
        description="A study of the r/phr4r subreddit's demographics and other observable trends through data webscraped from June 15 to 22, 2022.
            Data webscraped using the pRAW package and analyzed with pandas and matplotlib."
        githubLink="https://github.com/jmcruz14/top_250_filipino_eda"
        blogLink="https://medium.com/@carlczech/the-underlying-trends-of-phr4r-515314ceed43"
      />
    </section>

    <section class="see-more">
      <NuxtLink
        href="https://github.com/jmcruz14?tab=repositories"
        target="_blank"
      >
        <button type="button">
          <img src="~/assets/images/github_icon.svg" />
          <span>See more at GitHub</span>
        </button>
      </NuxtLink>
    </section>
    
  </main>
</template>

<script>
import { ref, onMounted } from 'vue';

import BoxCard from '@/components/BoxCard';
import Tabs from '@/components/tabs/project-tabs'

export default {
  components: {
    BoxCard,
    Tabs
  },
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

    return {
      softwareTab,
      dataTab,
      selectedTab,
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
    margin-block-start: 2.5em;
  }

  .hidden {
    display: none !important;
  }

  /* Project Content Test */
  section.project-grid {
    display: grid;
    grid-template-columns: auto auto auto;
    gap: 6em;
  }

  /* Project Content */
  section.project-content,
  section.analytics-content {
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    align-items: center;
    gap: 5em;
  }

/* Project Info Rules */
section.project-info {
  width: 70%;
  display: flex;
  gap: 2em;
  box-sizing: border-box;
}

section.project-info h2,
section.project-info h4 {
  font-family: "Lato";
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
  justify-content: center;
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
  background-color: #bf78cb;
  border-radius: 50px;
}

section.project-info li.blog-link {
  background-color: #4c60cc;
  border-radius: 50px;
}

section.see-more button {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 3em;

  padding: 1em 0.25em 1em 0.25em;
  width: 28em;
  font-family: inherit;
  font-weight: 300;

  transition: all 0.3s ease;

  /* background: linear-gradient(to bottom, #e5e4e2, rgb(255, 255, 255)) */
  background: rgb(237, 237, 237)
    rgb(0, 0, 0);
  border-radius: 8px;
  border: 0.5px grey solid;
}

section.see-more a {
  text-decoration: none;
}

section.see-more button > span {
  font-size: 18px;
}

section.see-more button:hover {
  cursor: pointer;
  background: #686464;
  opacity: 0.75;
}

section.see-more button:hover > span {
  color: #d5d5d5;
}

/* filter is a new CSS rule that lets you manipulate svg/png images */
section.see-more button:hover > img {
  filter: invert(100%) sepia(2%) saturate(171%) hue-rotate(226deg)
    brightness(105%) contrast(67%);
}

section.see-more button > img {
  width: 3em;
}

/* NOTE: this css declaration is lifted from the Next.js template
use accordingly

:root {
  --foreground-rgb: 0, 0, 0;
  --background-start-rgb: 214, 219, 220;
  --background-end-rgb: 255, 255, 255;
}

@media (prefers-color-scheme: dark) {
  :root {
    --foreground-rgb: 255, 255, 255;
    --background-start-rgb: 0, 0, 0;
    --background-end-rgb: 0, 0, 0;
  }
}

body {
  color: rgb(var(--foreground-rgb));
  background: linear-gradient(
      to bottom,
      transparent,
      rgb(var(--background-end-rgb))
    )
    rgb(var(--background-start-rgb));
} */

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

  section.see-more > button > img {
    display: none;
  }
}
</style>
