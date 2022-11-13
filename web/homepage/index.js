const texts = [
    "Hello, world! I have been taking CS50 for a few weeks by now, and this is the best course I've ever been in.",
    "I really hate C's pointers. Not like i will use C again in the future, tho.",
    "I love Python.",
    "So this is what studying in a top university of the world feels like",
    "Best thing to do in quarantine...!",
    "Every single question is a 'really good question', I like that idea",
    "The production quality is way too good!",
    "To think us self-learners have access to this kind of materials from amazing teacher like David for free...",
    "What really matters in this course is not much where you end up relative to your classmates, but where you end up relative to yourself when you began."
]

const btn = document.querySelector("#changeText");
btn.addEventListener("click", function () {
    let text
    currText = document.querySelector("#home-quotes").innerHTML
    do {
        text = texts[Math.round(Math.random() * (texts.length - 1))]
    } while (text === currText)
    document.querySelector("#home-quotes").innerHTML = text
});
