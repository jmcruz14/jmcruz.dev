<template>
  <main class="animate-opacity" id="work">

    <div class="skills">
      <h2>Skills</h2>
      <div class="skills-showcase">
        <section class="skill-box">
          <img src="~/assets/images/skills/html.png">
          HTML
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/css.png">
          CSS
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/js.png">
          JS
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/postgresql.png">
          PostgreSQL
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/python.png">
          Python
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/vue-logo.png">
          Vue 3
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/git.png">
          Git
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/React-icon.svg.png">
          React
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/postman-icon.svg">
          Postman
        </section>
        <section class="skill-box">
          <img src="~/assets/images/skills/docker_logo.webp">
          Docker
        </section>
      </div>
    </div>
    
    <div class="timeline">
      <h2 style="margin: 0 0 0.5em 0; padding: 0">Timeline</h2>
      <timelineContainer
        work_logo_image=""
        company="MYCURE Inc."
        title="Junior Software Developer"
        startDate="April 2023"
        endDate="November 2023"
      />
        <!-- IDEA: Show the full list on hover -->
        <!-- <ul>
          <li>Used Vue.js to make improvements in the Billing, Inventory, Medical Records, and other modules of the Clinic Management System</li>
          <li>Contributed at least 20 feature implementations and bugfixes to the company’s main product and helped close a company side project’s first milestone</li>
        </ul> -->

      <!-- TODO: Insert timeline here wherein I graduated from Colloege -->

      <timelineContainer 
        work_logo_image="up_nec_logo"
        company="UP National Engineering Center"
        title="Python Developer"
        startDate="June 2022"
        endDate="December 2022"
      />

      <timelineContainer 
        work_logo_image="ilc_diliman_square"
        company="Interactive Learning Center Diliman"
        title="Intern"
        startDate="July 2021"
        endDate="September 2021"
      />


      <!-- <div class="container">
        <img src="~/assets/images/work-logos/up_nec_logo.png">
        <section>
          <hgroup>
            <h2>UP National Engineering Center</h2>
            <h3>Developer 2</h3>
            <h4>June 2022 - December 2022</h4>
          </hgroup> -->
          <!-- <ul>
            <li>Developed, designed, and tested web-based modules scripted in Python and SQL for the University's Budget Office</li>
            <li>Streamlined the administration management process for user ownership and control</li>
          </ul> -->
        <!-- </section>
      </div> -->

      <!-- <div class="container">
        <img src="~/assets/images/work-logos/ilc_diliman_square.png">
        <section>
          <hgroup>
            <h2>Interactive Learning Center Diliman</h2>
            <h3>Intern</h3>
            <h4>July 2021 - Sept 2021</h4>
          </hgroup> -->
          <!-- <ul>
            <li>Evaluated and provided suggestions on 5 prototype wire frame designs to be further developed for public use</li>
            <li>Provided voice-over for at least 20 training modules on how to use company-produced applications and systems for public use</li>
          </ul> -->
        <!-- </section>
      </div> -->
    </div>

    <!-- <article style="background-color: rgba(163, 150, 153, 0.75); padding: 1.5em">
      <span>
        More information coming soon!
      </span>
    </article> -->

    <!-- <section class="project-info">
      <div class="image-box"> 
        to adjust image as a content model w/in flex-item
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
    </section> -->
  </main>
</template>

<script>
import timelineContainer from '~/components/timeline-container.vue';
import { definePageMeta, useSeoMeta } from '#imports';

export default {
  components: {
    timelineContainer
  },
  setup () {
    definePageMeta(
      { layout: 'generic' }
    )
    useSeoMeta(
      {
        title: 'Work - Jay Cruz',
        description: 'Work and Company History'
      }
    )
  }
}

</script>

<style scoped>
  main {
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    align-items: center;
    gap: 2.5em;
    margin-block-start: 2.5em;
  }

  /* .timeline {
    position: relative;
    max-width: 1024px;
    margin: 0;
  } */

  /* .timeline::after{
    content: '';
    position: absolute;
    width: 6px;
    background-color: rgba(163, 150, 153, 0.75);
    top: 0;
    bottom: 0;
    left: 50%;
  } */
  /* margin-left: -3px; */

  .skills {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 800px;
  }

  .skills .skills-showcase {
    display: grid;
    grid-template-columns: auto auto auto auto auto auto;
    gap: 25px 50px;
  }

  .skill-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5em;
    padding: 1em;
  }

  .skill-box > img {
    height: 100px;
  }
  
  .timeline {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 1200px;
    gap: 0.5rem;
    margin: 0;
  }

  .left {
    left: 0;
  }

  .right {
    left: 50%;
  }

  a.download-link {
    text-decoration: none;
  }

  .download-button {
    background-color: rgb(213, 213, 213) !important;
    /* color: rgb(158, 158, 158); */
    color: black;
    text-decoration: none !important;
    border: 1px solid black;
    /* color: white; */
  }

  .download-button:hover {
    color: white;
    background-color: #2a2a2a !important;
    cursor: pointer;
  }

  @media screen and (max-width: 640px) {

    .skills .skills-showcase {
      grid-template-columns: auto auto;
    }

    .timeline {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
    }

  /* Place the timelime to the left */
    /* .timeline::after {
      left: 31px;
    } */

  /* Make sure all circles are at the same spot */
    .left::after, .right::after {
      left: 15px;
    }

  /* Make all right containers behave like the left ones */
    .right {
      left: 0%;
    }
  }

</style>