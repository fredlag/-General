const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");           /* shows the menu */
    navMenu.classList.toggle("active");             /* closes the menu */
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {                /* removes after a selected item have been clicked */
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");

}));