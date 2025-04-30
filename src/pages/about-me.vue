<template>
  <main class="animate-opacity" id="about-me">
    <article class="write-up developer-text">
      <h3>
        About Me
      </h3>
      <p>
        Hi! I'm Jay, a considerably curious developer with an interest for data, design, and collaboration. My favorite
        type of career growth is to try and put myself in situations where I enjoy the things that I learn! (This is how I
        tend to get involved in my own share of personal projects, collaborate with my friends at the UP Data Science Society, 
        or engage in something that is social impact oriented.)
      </p>

      <p>
        I've previously worked at a HealthTech startup, and I currently do mentorship work for <a href="https://www.eskwelabs.com/" target=_blank>Eskwelabs</a>
        while serving as an open-source contributor to the <a href="https://cinemata.org/" target=_blank>Cinemata</a> video platform.
      </p>
      
      <blockquote>
        <q>The best moments usually occur when a person's body or mind is stretched to its limits in a voluntary effort to
          accomplish something difficult and worthwhile.</q>
        <p>- Mihaly Csikszentmihalyi, Flow</p>
      </blockquote>

      <p>
        Outside of work, you can find me watching <a href="https://letterboxd.com/tuesjays/" target=_blank>movies</a>, reading
        <a href="https://www.goodreads.com/user/show/136888605-jay" target=_blank>books</a>, or biking around the city.
        I also co-manage and write for <a href="https://www.sinegang.ph/" target=_blank>SINEGANG.ph</a>, a film collective aimed at providing a written platform for young aspiring cinephiles.
      </p>
      <p class="entry-date">
        April 30, 2025
      </p>

    </article>
  </main>

  <!-- <footer>
    <p>
      GitHub Source Code for this website can be found
      <a href="https://github.com/jmcruz14/jmcruz14.github.io/" rel="noreferrer noopener">here.</a>
    </p>
  </footer> -->
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
        title: 'About Me - Jay Cruz',
        description: 'About me section of my personal developer page.'
      }
    )
  }
}

</script>

<style scoped>
  /* local CSS rules */
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-inline: auto;
    margin-block-start: 2.5em;
    gap: 2em;

    max-width: 750px;
  }

  article.write-up {
    display: flex;
    flex-direction: column;
    gap: 0.5em;
  }

  article.write-up > p {
    font-weight: 300;
    font-size: 20px;
  }
  article.write-up a {
    display: inline-block;
    transform-origin: center;
    transition: transform 0.2 ease-in-out;
    font-weight: 500;
    color: black;
    text-decoration: none;
  }
  article.write-up a:hover {
    transform: scale(1.025)
  }
  article.write-up a:visited {
    color: black;
  }

  @media screen and (max-width: 640px) {
    main#about-me {
      flex-direction: column;
      align-items: center;
      margin-inline-start: 3em;
      margin-inline-end: 3em;
      margin-block-start: 1em;
      gap: 0.25em;
    }
    /* section.personal-image {
      align-items: center;
    }

    section.personal-image > img,
    section.personal-image > NuxtImg {
        text-align: center;
        width: 18em;
    } */

    article.write-up {
      font-size: 16px;
      flex-basis: 55%;
    }
  }

  @media screen and (min-width: 640px) and (max-width: 768px) {
    main#about-me {
        flex-direction: column;
        align-items: center;
        margin-inline-start: 3em;
        margin-inline-end: 3em;
        margin-block-start: 5em;
        gap: 0.25em;
    }

    section.personal-image {
        align-items: center;
    }

    section.personal-image > img,
    section.personal-image > NuxtImg {
        text-align: center;
        width: 18em;
    }

    article.write-up {
        flex-basis: 55%;
    }
  }
  @media screen and (min-width: 768px) and (max-width: 1024px) {

    main.about-me {
        margin-inline-start: 5em;
        margin-inline-end: 5em;
        margin-block-start: 7em;
        gap: 0.5em;
    }

    section.personal-image > img,
    section.personal-image > NuxtImg {
        width: 20em;
    }

    article.write-up {
        flex-basis: 60%;
    }

  }
</style>
