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
    
    <h2 style="margin: 0 0 0.5em 0; padding: 0">Timeline</h2>
    <div class="timeline">

      <timelineContainer
        work-logo-url="https://upload.wikimedia.org/wikipedia/commons/a/aa/EngageMedia_Logo.jpg"
        company="EngageMedia"
        title="Django Developer"
        start-date="March 2025"
        work-type="work"
        :has-info="true"
      >
        <template #hover-info>
          <div style="padding: 1em">
            <p>Currently handling milestone developments for EngageMedia's video platform, Cinemata.</p>
          </div>
        </template>
      </timelineContainer>

      <timelineContainer
        work-logo-url="https://m-cdn.flipboard.social/accounts/avatars/111/537/184/025/760/825/original/a44d96f68b267301.png"
        company="Omdena AI"
        title="Volunteer"
        start-date="July 2024"
        end-date="March 2025"
        work-type="volunteer"
        :has-info="true"
      >
        <template #hover-info>
          <div style="padding: 1em">
            <h4 style="margin: 0">
              Projects Done
            </h4>
            <ol>
              <li>
                <span>Housing Affordability Analysis in the Greater Parisian Region</span>
              </li>
              <li>
                <span>Predicting Air Pollution Levels in Mexico</span>
              </li>
            </ol>
          </div>
        </template>
      </timelineContainer>

      <timelineContainer
        work-logo-image="large_mycure_logo"
        company="MYCURE Inc."
        title="Junior Software Developer"
        start-date="April 2023"
        end-date="November 2023"
        :has-info="true"
      >
        <template v-slot:hover-info>
          <ul>
            <li>Worked on improvements to various modules of the company Clinic Management System</li>
            <li>Engaged in additional work related to training and onboarding of users, and integration of analytics</li>
          </ul>
        </template>
      </timelineContainer>
        <!-- IDEA: Show the full list on hover -->
        <!-- <ul>
          <li>Used Vue.js to make improvements in the Billing, Inventory, Medical Records, and other modules of the Clinic Management System</li>
          <li>Contributed at least 20 feature implementations and bugfixes to the company’s main product and helped close a company side project’s first milestone</li>
        </ul> -->

      <!-- TODO: Insert timeline here wherein I graduated from Colloege -->

      <timelineContainer 
        work-logo-image="up_nec_logo"
        company="UP National Engineering Center"
        title="Python Developer"
        start-date="June 2022"
        end-date="December 2022"
        :has-info="true"
      >
        <template v-slot:hover-info>
          <ul>
            <li>Developed, designed, and tested web-based modules scripted in Python and SQL for the University's Budget Office</li>
            <li>Streamlined the administration management process for user ownership and control</li>
          </ul>
        </template>
      </timelineContainer>

      <timelineContainer 
        work-logo-image="ilc_diliman_square"
        company="Interactive Learning Center Diliman"
        title="Intern"
        start-date="July 2021"
        end-date="September 2021"
      />
    </div>
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

  li {
    margin-bottom: 10px
  }

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
    display: grid;
    grid-template-columns: auto auto;

    /* flex-direction: column;
    align-items: center; */
    max-width: 70%;
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