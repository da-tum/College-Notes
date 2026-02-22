// DOM Element Selectors
const eventForm = document.getElementById("eventForm");
const eventTitle = document.getElementById("eventTitle");
const eventDate = document.getElementById("eventDate");
const eventCategory = document.getElementById("eventCategory");
const eventDescription = document.getElementById("eventDescription");

const clearAllBtn = document.getElementById("clearAllBtn");
const addSampleBtn = document.getElementById("addSampleBtn");
const eventContainer = document.getElementById("eventContainer");
const demoContent = document.getElementById("demoContent");

let sampleEvents = [
    { title: "Web dev", date: "2026-12-04", category: "Workshop", description: "Learn Vanilla JS." },
    { title: "Web dev2", date: "2026-12-05", category: "Conference", description: "Advanced JS Session." }
];

// Function to Create Event Card (Learning Obj: Dynamically create elements)
function createEventCard(eventData) {
    const card = document.createElement("div");
    card.className = "event-card";
    
    // Using innerHTML to build the card structure
    card.innerHTML = `
        <button class="delete-btn">X</button>
        <h3>${eventData.title}</h3>
        <div>${eventData.date}</div>
        <span class="category-tag"><strong>${eventData.category}</strong></span>
        <p>${eventData.description}</p>
    `;
    return card;
}

// Function to Add Event to UI
function addEvent(eventData) {
    const emptyState = document.querySelector(".empty-state");
    if (emptyState) emptyState.remove(); // Removes "No events" message
    
    eventContainer.appendChild(createEventCard(eventData));
}

// Form Submission (Learning Obj: Handle user interactions)
eventForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevents page reload
    
    const eventData = {
        title: eventTitle.value,
        date: eventDate.value,
        category: eventCategory.value,
        description: eventDescription.value
    };

    addEvent(eventData);
    eventForm.reset();
});

// Event Delegation (Learning Obj: Event bubbling/delegation)
eventContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
        e.target.parentElement.remove(); // Removes the entire card
        
        // Restore empty state if no cards left
        if (eventContainer.children.length === 0) {
            eventContainer.innerHTML = '<div class="empty-state">No events yet. Add your first event!</div>';
        }
    }
});

// Controls
addSampleBtn.addEventListener("click", () => {
    sampleEvents.forEach(data => addEvent(data));
});

clearAllBtn.addEventListener("click", () => {
    eventContainer.innerHTML = '<div class="empty-state">No events yet. Add your first event!</div>';
});

// DOM Manipulation Demo (Learning Obj: Compare innerText vs innerHTML)
window.addEventListener("keydown", (e) => {
    const rawHTML = `<strong>Pressed:</strong> ${e.key}`;
    
    // Setting content using innerHTML (renders tags)
    demoContent.innerHTML = rawHTML;
    
    // Logging differences to console for Lab verification
    console.log("innerText:", demoContent.innerText);    // Returns: "Pressed: a"
    console.log("textContent:", demoContent.textContent); // Returns: "Pressed: a" (raw content)
    console.log("innerHTML:", demoContent.innerHTML);     // Returns: "<strong>Pressed:</strong> a"
});