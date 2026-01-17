// Simple rent data (average monthly rent in INR)
const rentData = [
  { locality: "dwarka", bhk: "1BHK", rent: 15000 },
  { locality: "dwarka", bhk: "2BHK", rent: 25000 },
  { locality: "dwarka", bhk: "3BHK", rent: 32000 },

  { locality: "rohini", bhk: "1BHK", rent: 14000 },
  { locality: "rohini", bhk: "2BHK", rent: 22000 },
  { locality: "rohini", bhk: "3BHK", rent: 30000 },

  { locality: "saket", bhk: "1BHK", rent: 18000 },
  { locality: "saket", bhk: "2BHK", rent: 28000 },
  { locality: "saket", bhk: "3BHK", rent: 38000 },

  { locality: "vasant kunj", bhk: "4BHK", rent: 75000 }
];

// Get DOM elements
const searchBtn = document.getElementById("searchBtn");
const resultDiv = document.getElementById("result");

// Flask API endpoint
const API_URL = "http://127.0.0.1:5000/api/rent";

/**
 * Handle search button click
 */
searchBtn.addEventListener("click", () => {
  // Read user inputs
  const localityInput = document.getElementById("localityInput");
  const bhkSelect = document.getElementById("bhkType");

  const locality = localityInput.value.trim().toLowerCase();
  const bhk = bhkSelect.value;

  // Input validation
  if (!locality || !bhk) {
    resultDiv.textContent = "Please enter locality and select BHK type.";
    return;
  }

  // Show loading message
  resultDiv.textContent = "Fetching rent price...";

  // Build API URL with query parameters
  const requestUrl =
    `${API_URL}?locality=${encodeURIComponent(locality)}&bhk=${encodeURIComponent(bhk)}`;

  // Call Flask API
  fetch(requestUrl)
    .then(response => {
      // Handle HTTP errors
      if (!response.ok) {
        return response.json().then(err => {
          throw new Error(err.message || "API error");
        });
      }
      return response.json();
    })
    .then(data => {
      // Handle API success response
      if (data.success) {
        resultDiv.textContent =
          `Estimated Rent: ₹${data.estimated_rent} per month`;
      } else {
        resultDiv.textContent = data.message || "No rent data found.";
      }
    })
    .catch(error => {
      // Handle network or server errors
      console.error("Error:", error);
      resultDiv.textContent =
        "Unable to fetch rent data. Please check if the server is running.";
    });
});
