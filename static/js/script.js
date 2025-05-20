document.addEventListener('DOMContentLoaded', function() {
    // Form submission
    const form = document.getElementById('prediction-form');
    const loadingSpinner = document.getElementById('loading');
    const predictionResult = document.getElementById('prediction-result');
    const priceValue = document.getElementById('price-value');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading spinner
        loadingSpinner.classList.remove('hidden');
        predictionResult.classList.add('hidden');
        
        // Get form data
        const formData = new FormData(form);
        
        // Send prediction request
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading spinner
            loadingSpinner.classList.add('hidden');
            predictionResult.classList.remove('hidden');
            
            if (data.success) {
                // Display prediction
                priceValue.textContent = data.prediction;
                
                // Animate the result
                animateValue();
            } else {
                // Display error
                priceValue.textContent = 'Error';
                alert('Prediction error: ' + data.message);
            }
        })
        .catch(error => {
            // Hide loading spinner
            loadingSpinner.classList.add('hidden');
            predictionResult.classList.remove('hidden');
            
            // Display error
            priceValue.textContent = 'Error';
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });
    
    // Animation for the price value
    function animateValue() {
        priceValue.style.transform = 'scale(1.1)';
        setTimeout(() => {
            priceValue.style.transform = 'scale(1)';
        }, 300);
    }
});