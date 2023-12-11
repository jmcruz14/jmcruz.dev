// import { headerContent } from './js/header.js'

// const currentUrl = window.location.href;
// const main = document.querySelector('main')

// // Global header content
// const headerContent = document.createElement('header');
// headerContent.classList.add('title-bar');
// headerContent.innerHTML = `
//   <hgroup>
//     <h1>
//       Jay Cruz
//     </h1>
//     <h3>
//       Software Developer
//     </h3>
//   </hgroup>

//   <nav class="personal-links">
//     <ul>
//       <li>
//         <a title="LinkedIn" href="https://www.linkedin.com/in/juan-carlos-c-54530b16b/" target="_blank" rel="author noreferrer noopener">
//           <img src="images/linkedin-logo.png" alt="LinkedIn Link" class="icon-size">
//         </a>
//       </li>
//       <li>
//         <a title="GitHub" href="https://github.com/jmcruz14" target="_blank" rel="author noreferrer noopener">
//         <img src="images/github_icon.svg" alt="GitHub Link" class="icon-size">
//         </a>
//       </li>
//       <li>
//         <a title="Email" href="mailto:jccruz009@yahoo.com" target="_blank" rel="author noreferrer noopener">
//           <img src="images/email_icon.png" alt="Email Link" class="icon-size">
//         </a>
//       </li>
//     </ul>
//   </nav>
// `
// document.body.insertBefore(headerContent, main)

// const navLinksContent = document.createElement('nav');
// navLinksContent.classList.add('nav-links');
// navLinksContent.innerHTML = `
//   <ul>
//     <li>
//       <a href="index.html" rel="next author noreferrer noopener">About Me</a>
//     </li>
//     <li>
//       <a href="work.html" rel="next author noreferrer noopener">Work</a>
//     </li>
//     <li>
//       <a href="projects.html" rel="next author noreferrer noopener">Projects</a> 
//     </li>
//   </ul>
// `
// document.body.insertBefore(navLinksContent, main)

// // Global footer link
// const footerContent = document.createElement('footer');
// footerContent.innerHTML = `<p style="margin-block: 6px">
// Source code can be found
// <a href="https://github.com/jmcruz14/jmcruz14.github.io/" rel="noreferrer noopener">here.</a>
// </p>`
// footerContent.style.cssText = `
//   display: flex;
//   flex-direction: flex-row;
//   width: 100%;
//   box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 -2px 4px -2px rgb(0 0 0 / 0.1);
//   background-color: #E5E4E2;
// `
// document.body.insertBefore(footerContent, main.nextSibling); // this semantically doesn't make sense, but whatever. a hack is a hack.

// // Check if the current URL ends with "index.html"
// if (currentUrl.endsWith("index.html") || currentUrl.endsWith("/")) {
//   // If yes, set the text-decoration of the element with href "index.html" to "underline"
//   // since we currently have two html files in the root directory
//   // simple if-else statement is fine
//   document.querySelector("a[href='index.html']").style.textDecoration = "underline";
// } else if (currentUrl.endsWith("work.html")) {
//   document.querySelector("a[href='work.html']").style.textDecoration = "underline";
// } else if (currentUrl.endsWith("projects.html")) {
//   // If not, set the text-decoration of the element with ID "my-link" to "none"
//   document.querySelector("a[href='projects.html']").style.textDecoration = "underline";
// }