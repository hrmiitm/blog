/* Apply before paint; a blocked storage API must not break the page. */
(() => {
  const root = document.documentElement;
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  let preference = null;
  try {
    preference = localStorage.getItem("theme");
  } catch {
    /* Use system preference. */
  }
  if (preference !== "light" && preference !== "dark") preference = null;
  function apply(theme) {
    root.dataset.theme = theme;
    const button = document.getElementById("theme-toggle");
    if (button) {
      button.hidden = false;
      button.setAttribute(
        "aria-label",
        `Switch to ${theme === "dark" ? "light" : "dark"} theme`,
      );
      button.title = button.getAttribute("aria-label");
    }
  }
  apply(preference || (system.matches ? "dark" : "light"));
  system.addEventListener("change", (event) => {
    if (!preference) apply(event.matches ? "dark" : "light");
  });
  document.addEventListener("DOMContentLoaded", () => {
    apply(root.dataset.theme);
    document.getElementById("theme-toggle")?.addEventListener("click", () => {
      preference = root.dataset.theme === "dark" ? "light" : "dark";
      try {
        localStorage.setItem("theme", preference);
      } catch {
        /* Session still works. */
      }
      apply(preference);
    });
  });
})();
