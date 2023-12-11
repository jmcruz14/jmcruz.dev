// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  srcDir: 'src/',
  css: ['@/assets/css/main.css'],
  image: {
    dir: 'assets/images',
    screens: {
      xs: 320,
      sm: 640,
      md: 768,
      lg: 1024,
      xl: 1280,
      xxl: 1536,
      '2xl': 1536,
      '3xl': 1920,
    },
  },
  app: {
    head: {
      htmlAttrs: {
        lang: 'en',
      },
      link: [
        // {
        //   rel: 'stylesheet',
        //   href: 'https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css',
        //   media: 'none',
        //   onload: "if(media!='all')media='all'",
        // },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap',
          media: 'none',
          onload: "if(media!='all')media='all'",
        },
      ],
    },
  },
})
