// Assuming you have a global variable with the list of countries
const countries = [
    "Iceland", "Luxembourg", "United States", "Switzerland", "Belgium", 
    "Denmark", "Austria", "Netherlands", "Australia", "Canada", "Germany", 
    "United Kingdom", "Norway", "France", "Ireland", "Finland", "New Zealand", 
    "Sweden", "South Korea", "Slovenia", "Italy", "Israel", "Lithuania", 
    "Spain", "Japan", "Poland", "Estonia", "Latvia", "Czech Republic", 
    "Chile", "Costa Rica", "Portugal", "Hungary", "Slovakia", "Greece", "Mexico"
];

// Populate the dropdown
const countrySelect = document.getElementById('country-select');
countries.forEach((country) => {
    const option = document.createElement('option');
    option.value = country;
    option.text = country;
    countrySelect.appendChild(option);
});

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
    countryInfo.innerHTML = `<h2>${selectedCountry}</h2>
        <p>Year 2000: ${data.wages[0]}</p>
        <p>Year 2010: ${data.wages[1]}</p>
        <p>Year 2020: ${data.wages[2]}</p>
        <p>Year 2022: ${data.wages[3]}</p>`;

    const ctx = document.getElementById('wage-chart').getContext('2d');
    if (window.myChart) {
        window.myChart.destroy();
    }
    window.myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [2000, 2010, 2020, 2022], // This should be an array of years
            datasets: [{
                label: `${selectedCountry} Wages Growth`,
                data: data.wages, // This should be an array of wage values
                fill: false,
                borderColor: 'red', // Change the line color to red
                backgroundColor: 'rgba(255, 99, 132, 0.2)', // Optional: change the fill color
                borderWidth: 3, // Make the line thicker
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false // Set to true if you want the scale to start at zero
                }
            },
            plugins: {
                legend: {
                    labels: {
                        // This more specific font property overrides the global property
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    }
                }
            }
        }
    });
}