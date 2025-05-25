// This file contains JavaScript for client-side functionality. 

document.addEventListener('DOMContentLoaded', function() {
    // --- INICIO LÓGICA DE FILTROS ---
    const filterForm = document.getElementById('filter-form'); // Asume que tu formulario de filtros tiene este ID

    const applyFilters = () => {
        // Obtener valores de todos los campos de filtro
        const cityInput = document.getElementById('city-input')?.value.toLowerCase() || ''; // ?. para evitar error si no existe
        const minAmountInput = document.getElementById('min-amount')?.value || '';
        const maxAmountInput = document.getElementById('max-amount')?.value || '';
        const tipoPropiedadInput = document.getElementById('tipo-propiedad')?.value.toLowerCase() || ''; // Asume que tienes un select con este ID

        const landItems = document.querySelectorAll('.land-item');

        landItems.forEach(item => {
            let matchesCity = true;
            let matchesMinAmount = true;
            let matchesMaxAmount = true;
            let matchesTipoPropiedad = true;

            // Filtrar por ciudad
            if (cityInput) {
                const itemCity = item.dataset.city?.toLowerCase() || '';
                matchesCity = itemCity.includes(cityInput);
            }

            // Filtrar por monto mínimo (asume que los items tienen data-price)
            if (minAmountInput) {
                const itemPrice = parseFloat(item.dataset.price);
                matchesMinAmount = !isNaN(itemPrice) && itemPrice >= parseFloat(minAmountInput);
            }

            // Filtrar por monto máximo
            if (maxAmountInput) {
                const itemPrice = parseFloat(item.dataset.price);
                matchesMaxAmount = !isNaN(itemPrice) && itemPrice <= parseFloat(maxAmountInput);
            }

            // Filtrar por tipo de propiedad (asume que los items tienen data-type)
            if (tipoPropiedadInput) {
                const itemType = item.dataset.type?.toLowerCase() || '';
                matchesTipoPropiedad = itemType === tipoPropiedadInput;
            }
            
            // Mostrar el item si cumple todos los criterios
            if (matchesCity && matchesMinAmount && matchesMaxAmount && matchesTipoPropiedad) {
                item.style.display = 'block'; // O tu estilo de display por defecto, ej: 'flex'
            } else {
                item.style.display = 'none';
            }
        });
    };


    // Event listener para el envío del formulario de filtros
    if (filterForm) {
        filterForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevenir el envío tradicional del formulario
            applyFilters();
        });
    }
    // --- FIN LÓGICA DE FILTROS ---

    // --- INICIO LÓGICA DE OTROS FORMULARIOS (EJ: ADD LAND) ---
    const handleFormSubmission = (event) => {
        event.preventDefault();
        // Add form submission logic here
        console.log('Formulario "add-land-form" enviado');
    };

    const addLandForm = document.getElementById('add-land-form');
    if (addLandForm) {
        addLandForm.addEventListener('submit', handleFormSubmission);
    }
    // --- FIN LÓGICA DE OTROS FORMULARIOS ---

    // --- INICIO LÓGICA DE LIGHTBOX ---
    const lightbox = document.getElementById('myImageLightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const closeBtn = document.querySelector('.lightbox-close');
    const galleryImages = document.querySelectorAll('.image-gallery img');

    galleryImages.forEach(img => {
        img.style.cursor = 'pointer'; // Indica que la imagen es clickeable
        img.addEventListener('click', function() {
            if (lightbox && lightboxImg) {
                lightbox.style.display = 'flex'; // Mostrar el lightbox
                lightboxImg.src = this.src;
                lightboxImg.alt = this.alt || 'Imagen agrandada'; // Usar el alt de la imagen original
            }
        });
    });

    if (closeBtn && lightbox) {
        closeBtn.addEventListener('click', function() {
            lightbox.style.display = 'none';
        });
    }

    if (lightbox) {
        lightbox.addEventListener('click', function(event) {
            if (event.target === lightbox) { // Si el clic es en el fondo del lightbox
                lightbox.style.display = 'none';
            }
        });
    }
    // --- FIN LÓGICA DE LIGHTBOX ---
});

// --- INICIO FUNCIONES DE MODAL (GLOBALES) ---
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
    }
}

function switchModal(currentModalId, targetModalId) {
    closeModal(currentModalId);
    openModal(targetModalId);
}

// Cierra los modales si se hace clic fuera de ellos
window.onclick = function(event) {
    const loginModal = document.getElementById('loginModal');
    const registerModal = document.getElementById('registerModal');
    // Puedes añadir más IDs de modales aquí si es necesario
    // const otroModal = document.getElementById('otroModalId');

    if (loginModal && event.target === loginModal) {
        loginModal.style.display = 'none';
    }
    if (registerModal && event.target === registerModal) {
        registerModal.style.display = 'none';
    }
    // if (otroModal && event.target === otroModal) {
    //     otroModal.style.display = 'none';
    // }
};
