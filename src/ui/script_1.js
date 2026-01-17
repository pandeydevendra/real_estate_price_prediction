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


const searchBtn = document.getElementById("searchBtn");
const resultDiv = document.getElementById("result");

searchBtn.addEventListener("click", () => {
  const locality = document.getElementById("localityInput").value.toLowerCase();
  const bhk = document.getElementById("bhkType").value;

  if (!locality || !bhk) {
    resultDiv.textContent = "Please enter locality and BHK type.";
    return;
  }

  const match = rentData.find(
    item => item.locality === locality && item.bhk === bhk
  );

  if (match) {
    resultDiv.textContent = `Estimated Rent: ₹${match.rent} per month`;
  } else {
    resultDiv.textContent = "No rent data found for this search.";
  }
});

