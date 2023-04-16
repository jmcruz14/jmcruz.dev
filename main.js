const currentUrl = window.location.href;

// Check if the current URL ends with "index.html"
if (currentUrl.endsWith("index.html")) {
    // If yes, set the text-decoration of the element with href "index.html" to "underline"
    // since we currently have two html files in the root directory
    // simple if-else statement is fine
    document.querySelector("a[href='index.html']").style.textDecoration = "underline";
  } else {
    // If not, set the text-decoration of the element with ID "my-link" to "none"
    document.querySelector("a[href='works.html']").style.textDecoration = "underline";
  }
  