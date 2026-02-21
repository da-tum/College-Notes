class EventDashboard {
    constructor() {
        this.events = JSON.parse(localStorage.getItem('events')) || [];
        this.currentFilter = 'all';
        this.init();
    }

    init() {
        this.bindEvents();
        this.renderEvents();
        this.updateInsights();
    }

    bindEvents() {
        const form = document.getElementById('eventForm');
        form.addEventListener('submit', (e) => this.addEvent(e));

        // Filter buttons
        document.getElementById('filterAll').addEventListener('click', () => this.setFilter('all'));
        document.getElementById('filterUpcoming').addEventListener('click', () => this.setFilter('upcoming'));
        document.getElementById('filterToday').addEventListener('click', () => this.setFilter('today'));
        document.getElementById('filterHighPriority').addEventListener('click', () => this.setFilter('high'));

        // Smart notifications
        this.setupSmartNotifications();
    }

    addEvent(e) {
        e.preventDefault();

        const eventName = document.getElementById('eventName').value;
        const eventDate = document.getElementById('eventDate').value;
        const eventDescription = document.getElementById('eventDescription').value;
        const eventPriority = document.getElementById('eventPriority').value;

        const event = {
            id: Date.now(),
            name: eventName,
            date: new Date(eventDate),
            description: eventDescription,
            priority: eventPriority,
            completed: false
        };

        this.events.push(event);
        this.saveEvents();
        this.renderEvents();
        this.updateInsights();

        // Reset form
        e.target.reset();

        // Smart notification
        this.showNotification(`Event "${eventName}" added successfully!`);
    }

    deleteEvent(id) {
        this.events = this.events.filter(event => event.id !== id);
        this.saveEvents();
        this.renderEvents();
        this.updateInsights();
        this.showNotification('Event deleted successfully!');
    }

    toggleComplete(id) {
        const event = this.events.find(e => e.id === id);
        if (event) {
            event.completed = !event.completed;
            this.saveEvents();
            this.renderEvents();
            this.updateInsights();
        }
    }

    setFilter(filter) {
        this.currentFilter = filter;
        this.updateFilterButtons();
        this.renderEvents();
    }

    updateFilterButtons() {
        const buttons = document.querySelectorAll('.filters button');
        buttons.forEach(btn => btn.classList.remove('active'));

        const activeBtn = document.getElementById(`filter${this.currentFilter.charAt(0).toUpperCase() + this.currentFilter.slice(1)}`);
        if (activeBtn) activeBtn.classList.add('active');
    }

    renderEvents() {
        const container = document.getElementById('eventsContainer');
        container.innerHTML = '';

        const filteredEvents = this.getFilteredEvents();

        if (filteredEvents.length === 0) {
            container.innerHTML = '<p>No events found.</p>';
            return;
        }

        filteredEvents.forEach(event => {
            const eventElement = this.createEventElement(event);
            container.appendChild(eventElement);
        });
    }

    getFilteredEvents() {
        const now = new Date();
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

        switch (this.currentFilter) {
            case 'upcoming':
                return this.events.filter(event => event.date > now && !event.completed);
            case 'today':
                return this.events.filter(event => {
                    const eventDate = new Date(event.date.getFullYear(), event.date.getMonth(), event.date.getDate());
                    return eventDate.getTime() === today.getTime() && !event.completed;
                });
            case 'high':
                return this.events.filter(event => event.priority === 'high' && !event.completed);
            default:
                return this.events;
        }
    }

    createEventElement(event) {
        const div = document.createElement('div');
        div.className = `event-item ${event.priority}-priority ${this.isToday(event.date) ? 'today' : ''}`;

        const timeUntil = this.getTimeUntil(event.date);
        const isPast = event.date < new Date();

        div.innerHTML = `
            <div class="event-name">${event.name}</div>
            <div class="event-date">${event.date.toLocaleString()} ${timeUntil}</div>
            <div class="event-description">${event.description || 'No description'}</div>
            <div class="event-actions">
                <button class="edit-btn" onclick="dashboard.editEvent(${event.id})">Edit</button>
                <button class="delete-btn" onclick="dashboard.deleteEvent(${event.id})">Delete</button>
                <button onclick="dashboard.toggleComplete(${event.id})">
                    ${event.completed ? 'Mark Incomplete' : 'Mark Complete'}
                </button>
            </div>
        `;

        if (event.completed) {
            div.style.opacity = '0.6';
        }

        if (isPast && !event.completed) {
            div.style.borderLeftColor = '#6c757d';
        }

        return div;
    }

    isToday(date) {
        const today = new Date();
        return date.toDateString() === today.toDateString();
    }

    getTimeUntil(date) {
        const now = new Date();
        const diff = date - now;

        if (diff < 0) return '(Past)';

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));

        if (days > 0) return `(${days} days, ${hours} hours left)`;
        if (hours > 0) return `(${hours} hours left)`;
        return '(Soon)';
    }

    updateInsights() {
        const now = new Date();
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

        const totalEvents = this.events.length;
        const upcomingEvents = this.events.filter(event => event.date > now && !event.completed).length;
        const todayEvents = this.events.filter(event => {
            const eventDate = new Date(event.date.getFullYear(), event.date.getMonth(), event.date.getDate());
            return eventDate.getTime() === today.getTime() && !event.completed;
        }).length;
        const highPriorityEvents = this.events.filter(event => event.priority === 'high' && !event.completed).length;

        document.getElementById('totalEvents').textContent = totalEvents;
        document.getElementById('upcomingEvents').textContent = upcomingEvents;
        document.getElementById('todayEvents').textContent = todayEvents;
        document.getElementById('highPriorityEvents').textContent = highPriorityEvents;
    }

    setupSmartNotifications() {
        // Check for upcoming events every minute
        setInterval(() => {
            this.checkUpcomingEvents();
        }, 60000);

        // Initial check
        this.checkUpcomingEvents();
    }

    checkUpcomingEvents() {
        const now = new Date();
        const oneHourFromNow = new Date(now.getTime() + 60 * 60 * 1000);

        this.events.forEach(event => {
            if (event.date > now && event.date <= oneHourFromNow && !event.completed) {
                this.showNotification(`Reminder: "${event.name}" is coming up soon!`, 'reminder');
            }
        });
    }

    showNotification(message, type = 'success') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;

        // Style the notification
        Object.assign(notification.style, {
            position: 'fixed',
            top: '20px',
            right: '20px',
            background: type === 'reminder' ? '#ffc107' : '#28a745',
            color: 'white',
            padding: '15px 20px',
            borderRadius: '8px',
            boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
            zIndex: '1000',
            maxWidth: '300px',
            animation: 'slideIn 0.3s ease-out'
        });

        document.body.appendChild(notification);

        // Remove after 5 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease-in';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }, 5000);
    }

    saveEvents() {
        localStorage.setItem('events', JSON.stringify(this.events.map(event => ({
            ...event,
            date: event.date.toISOString()
        }))));
    }

    loadEvents() {
        const saved = localStorage.getItem('events');
        if (saved) {
            this.events = JSON.parse(saved).map(event => ({
                ...event,
                date: new Date(event.date)
            }));
        }
    }

    editEvent(id) {
        const event = this.events.find(e => e.id === id);
        if (!event) return;

        // Populate form with event data
        document.getElementById('eventName').value = event.name;
        document.getElementById('eventDate').value = event.date.toISOString().slice(0, 16);
        document.getElementById('eventDescription').value = event.description;
        document.getElementById('eventPriority').value = event.priority;

        // Change form submit to update
        const form = document.getElementById('eventForm');
        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.textContent = 'Update Event';

        form.onsubmit = (e) => {
            e.preventDefault();
            this.updateEvent(id);
        };
    }

    updateEvent(id) {
        const eventName = document.getElementById('eventName').value;
        const eventDate = document.getElementById('eventDate').value;
        const eventDescription = document.getElementById('eventDescription').value;
        const eventPriority = document.getElementById('eventPriority').value;

        const eventIndex = this.events.findIndex(e => e.id === id);
        if (eventIndex !== -1) {
            this.events[eventIndex] = {
                ...this.events[eventIndex],
                name: eventName,
                date: new Date(eventDate),
                description: eventDescription,
                priority: eventPriority
            };

            this.saveEvents();
            this.renderEvents();
            this.updateInsights();

            // Reset form
            document.getElementById('eventForm').reset();
            const submitBtn = document.getElementById('eventForm').querySelector('button[type="submit"]');
            submitBtn.textContent = 'Add Event';
            document.getElementById('eventForm').onsubmit = (e) => this.addEvent(e);

            this.showNotification(`Event "${eventName}" updated successfully!`);
        }
    }
}

// Add CSS animations for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Initialize the dashboard
const dashboard = new EventDashboard();
