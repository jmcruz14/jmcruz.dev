// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  nitro: {
    preset: 'vercel',
    // Minimize output size
    minify: true,
    // Compact internal paths to avoid length issues
    inlineDynamicImports: true,
    // Use shorter file names
    output: {
      serverDir: './.output/server-short',
      publicDir: './.output/public-short'
    }
  },

  devtools: { enabled: false },
  ssr: true,
  spaLoadingTemplate: false,

  plugins: [
    '~/plugins/analytics.client.js',
  ],

  srcDir: 'src/',

  modules: [
    '@nuxt/image',
  ],

  alias: {
    "@/": "./src"
  },

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

  typescript: {
    builder: "vite",
    strict: true,
    shim: false,
    typeCheck: false,
  },

  vite: {
    // Optimize build for production
    build: {
      // Use shorter chunk names
      rollupOptions: {
        output: {
          manualChunks: undefined,
          entryFileNames: 'entry-[hash].js',
          chunkFileNames: 'chunk-[hash].js',
          assetFileNames: 'asset-[hash][extname]'
        }
      },
      // Minimize CSS output
      cssCodeSplit: false
    },
    // Flatten node_modules resolution
    resolve: {
      dedupe: ['vue']
    },
    // Reduce preprocessor output path length
    css: {
      preprocessorOptions: {
        scss: {
          // Any SCSS options if you're using it
        }
      }
    }
  },

  app: {
    head: {
      htmlAttrs: {
        lang: 'en',
      },
      link: [
        {
          rel: 'stylesheet',
          href: 'https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css',
          media: 'none',
          onload: "if(media!='all')media='all'",
        },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap',
          media: 'none',
          onload: "if(media!='all')media='all'",
        },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&family=Inter:wght@100;200;300;400;500;600;700&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700&family=Raleway&family=Roboto:wght@100&display=swap',
          media: 'none',
          onload: "if(media!='all')media='all'",
        },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Raleway:ital,wght@0,100..900;1,100..900&family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap',
          media: 'none',
          onload: "if(media!='all')media='all'",
        }
      ],
    },
  },

  compatibilityDate: '2025-04-22',
})