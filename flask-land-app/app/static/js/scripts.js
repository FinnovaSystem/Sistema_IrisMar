// This file contains JavaScript for client-side functionality. 

document.addEventListener('DOMContentLoaded', function() {
    // Example function to filter land by city
    const filterLandByCity = () => {
        const cityInput = document.getElementById('city-input').value;
        const landItems = document.querySelectorAll('.land-item');

        landItems.forEach(item => {
            if (item.dataset.city === cityInput || cityInput === '') {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    };

    // Event listener for the city filter input
    const cityInput = document.getElementById('city-input');
    if (cityInput) {
        cityInput.addEventListener('input', filterLandByCity);
    }

    // Example function to handle form submission
    const handleFormSubmission = (event) => {
        event.preventDefault();
        // Add form submission logic here
    };

    // Event listener for the add land form
    const addLandForm = document.getElementById('add-land-form');
    if (addLandForm) {
        addLandForm.addEventListener('submit', handleFormSubmission);
    }
});

function openModal() {
    document.getElementById('loginModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('loginModal').style.display = 'none';
}

// Cierra el modal si se hace clic fuera de él
window.onclick = function(event) {
    const modal = document.getElementById('loginModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};


function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

function switchModal(currentModalId, targetModalId) {
    closeModal(currentModalId);
    openModal(targetModalId);
}

// Cierra el modal si se hace clic fuera de él
window.onclick = function(event) {
    const loginModal = document.getElementById('loginModal');
    const registerModal = document.getElementById('registerModal');
    if (event.target === loginModal) {
        loginModal.style.display = 'none';
    } else if (event.target === registerModal) {
        registerModal.style.display = 'none';
    }
};