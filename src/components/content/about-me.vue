<template>
  <body class="about-me">
    
    <main class="animate-opacity">
      <section class="personal-image">
        <img src="~/assets/images/jay_prf_square.png" alt="Jay Cruz Photo">
      </section>
    
      <article class="write-up">
        <h3>
          About Me
        </h3>
        <p>
          Hi! I'm Jay, a graduate of Industrial Engineering with a passion for 
          creating and cultivating meaningful experiences in tech. I'm heavily drawn to fields such data science and design,
          and I am often fascinated with the intersection of data, technology, human behavior, and problem-solving.
        </p>
        <p>
          Outside of work, you can find me watching <a href="https://letterboxd.com/tuesjays/" target=_blank>movies</a>, reading
          <a href="https://www.goodreads.com/user/show/136888605-jay" target=_blank>books</a>, or biking around the city. 
          I also co-manage and write for <a href="https://www.sinegang.ph/" target=_blank>SINEGANG.ph</a>, a film collective aimed at providing a written platform for young aspiring cinephiles. 
        </p>
        <p class="entry-date">
          December 3, 2023
        </p>

        <blockquote style="margin-top: 80px;">
          <q>The best moments usually occur when a person's body or mind is stretched to its limits in a voluntary effort to
            accomplish something difficult and worthwhile.</q>
          <p>- Mihaly Csikszentmihalyi, Flow</p>
        </blockquote>
      </article>
    </main>

    <!-- <footer>
      <p>
        GitHub Source Code for this website can be found 
        <a href="https://github.com/jmcruz14/jmcruz14.github.io/" rel="noreferrer noopener">here.</a>
      </p>
    </footer> -->

  </body>
</template>

<style>
  /* local CSS rules */
  body.about-me main {
      display: flex;
      justify-content: space-around;
      align-items: center;
      margin-inline: 5em;
      margin-block-start: 10em;
      gap: 2em;
  }
  article.write-up > p {
    font-weight: 300;
  }
  article.write-up a {
    display: inline-block;
    transform-origin: center;
    transition: transform 0.2 ease-in-out;
    font-weight: 500;
    text-decoration: none;
  }
  article.write-up a:hover {
    transform: scale(1.025)
  }
  article.write-up a:visited {
    color: black;
  }
</style>