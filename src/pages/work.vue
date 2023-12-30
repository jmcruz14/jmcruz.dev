<template>
  <main class="animate-opacity" id="work">

    <div class="timeline">
      <div class="container">
        <img src="~/assets/images/work-logos/large_mycure_logo.png">
        <section>
          <hgroup>
            <h2>MYCURE Inc.</h2>
            <h3>Junior Software Developer</h3>
            <h4>April 2023 - November 2023</h4>
          </hgroup>
          <!-- IDEA: Show the full list on hover -->
          <!-- <ul>
            <li>Used Vue.js to make improvements in the Billing, Inventory, Medical Records, and other modules of the Clinic Management System</li>
            <li>Contributed at least 20 feature implementations and bugfixes to the company’s main product and helped close a company side project’s first milestone</li>
          </ul> -->
        </section>
      </div>

      <!-- TODO: Insert timeline here wherein I graduated from Colloege -->

      <div class="container">
        <img src="~/assets/images/work-logos/up_nec_logo.png">
        <section>
          <hgroup>
            <h2>UP National Engineering Center</h2>
            <h3>Developer 2</h3>
            <h4>June 2022 - December 2022</h4>
          </hgroup>
          <!-- <ul>
            <li>Developed, designed, and tested web-based modules scripted in Python and SQL for the University's Budget Office</li>
            <li>Streamlined the administration management process for user ownership and control</li>
          </ul> -->
        </section>
      </div>
      <div class="container">
        <img src="~/assets/images/work-logos/ilc_diliman_square.png">
        <section>
          <hgroup>
            <h2>ILC Diliman</h2>
            <h3>Intern</h3>
            <h4>July 2021 - Sept 2021</h4>
          </hgroup>
          <!-- <ul>
            <li>Evaluated and provided suggestions on 5 prototype wire frame designs to be further developed for public use</li>
            <li>Provided voice-over for at least 20 training modules on how to use company-produced applications and systems for public use</li>
          </ul> -->
        </section>
      </div>
    </div>

    <a href="/jccruz_resume.pdf" download="RESUME - JUAN CARLOS CRUZ" class="download-link">
      <div style="background-color: rgba(163, 150, 153, 0.75); padding: 1.5em; display: flex; flex-direction: column; align-items: center;
        border: 1px solid #737373;" class="download-button">
        <span>
          Download Resume
        </span>
        <!-- <span style="font-size: 12px">Coming soon</span> -->
      </div>
    </a>

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
import { definePageMeta, useSeoMeta } from '#imports';

export default {
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
    gap: 5em;
    margin-block-start: 5em;
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
  
  .timeline {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 1200px;
    gap: 0.5rem;
    margin: 0;
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

  .left {
    left: 0;
  }

  .right {
    left: 50%;
  }

  .container > img {
    width: 20%;
    height: 20%;
  }

  .container > section > ul {
    padding-left: 20px;
  }

  div.timeline hgroup > h1, 
  div.timeline hgroup > h2, 
  div.timeline hgroup > h3, 
  div.timeline hgroup > h4,
  div.timeline hgroup > h5,
  div.timeline hgroup > h6 {
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