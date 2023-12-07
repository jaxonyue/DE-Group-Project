// Add event listener for the button
document.getElementById('get-wages-btn').addEventListener('click', function() {
    const countrySelectElement = document.getElementById('country-select');
    const selectedCountry = countrySelectElement.options[countrySelectElement.selectedIndex].value;
    fetch(`/api/wages?country=${encodeURIComponent(selectedCountry)}`)
        .then(response => response.json())
        .then(data => {
            updateChart(data, selectedCountry);
        })
        .catch(error => {
            console.error('Error fetching wage data:', error);
        });
});

// Function to update the chart and display country name with wages
function updateChart(data, selectedCountry) {
    const countryInfo = document.getElementById('country-info');
    countryInfo.innerHTML = `<h2>${selectedCountry}</h2>` +
        data.years.map((year, index) => `<p>Year ${year}: $${data.wages[index].toLocaleString()}</p>`).join('');

    const ctx = document.getElementById('wage-chart').getContext('2d');
    if (window.myChart) {
        window.myChart.destroy();
    }
    window.myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.years, // This uses the years array from the data
            datasets: [{
                label: `${selectedCountry} Wages Growth`,
                data: data.wages, // This uses the wages array from the data
                fill: false,
                borderColor: 'rgb(75, 192, 192)', // A more colorful line color
                backgroundColor: 'rgba(75, 192, 192, 0.2)', // A matching fill color
                borderWidth: 3,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false,
                    ticks: {
                        // Include a dollar sign in the ticks and comma as thousands separators
                        callback: function(value, index, values) {
                            return '$' + value.toLocaleString();
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    }
                }
            },
            animation: {
                // New property to animate the chart when it loads
                onProgress: function(animation) {
                    if (animation.currentStep / animation.numSteps === 1) {
                        // Animate elements here if needed when the animation is complete
                    }
                }
            }
        }
    });
}
