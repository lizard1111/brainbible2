// Variables to keep track of the current sorting state
var currentSortColumn = null;
var currentSortOrder = "ascending"; // or "descending"

// Define the colors for the sequential gradient heatmap
var heatmapColors = d3.interpolateYlGnBu;

// Function to create the table
function createTable(data) {
    // Clear existing table
    d3.select("#brainRegionsTable").html("");

    // Create table headers
    var headers = Object.keys(data[0]);
    var thead = d3.select("#brainRegionsTable").append("thead");
    thead.append("tr")
        .selectAll("th")
        .data(headers)
        .enter()
        .append("th")
        .text(d => d)
        .on("click", function(header, i) {
            // Toggle between ascending and descending order
            if (currentSortColumn === header && currentSortOrder === "ascending") {
                currentSortOrder = "descending";
            } else {
                currentSortOrder = "ascending";
            }
            currentSortColumn = header;

            // Sort the data based on the clicked column and current sort order
            data.sort((a, b) => currentSortOrder === "ascending"
                ? d3.ascending(a[header], b[header])
                : d3.descending(a[header], b[header]));

            // Recreate the table with the sorted data
            createTable(data);
        });

    // Create table body
    var tbody = d3.select("#brainRegionsTable").append("tbody");
    tbody.selectAll("tr")
        .data(data)
        .enter()
        .append("tr")
        .selectAll("td")
        .data((d, i) => headers.map((header, j) => ({ value: d[header], index: j, row: d })))
        .enter()
        .append("td")
        .attr("style", d => {
            var style = "";
            if (d.index === 0 || d.index === 1 || d.index === 2) { // Name, Acronym, and RGB columns
                style += `font-weight: bold; background-color: #${d.row.RGB}; color: ${getContrastColor(d.row.RGB)};`;
            } else if (d.index >= 3 && d.index <= 5) { // Count, Volume, and Density columns
                style += `background-color: ${heatmapColors(d.value / getMaxCount(data))};`;
            }
            return style;
        })
        .text(d => {
            if (d.index >= 3 && d.index <= 5) { // Apply number formatting to Count, Volume, and Density columns
                return formatNumber(d.value, 3); // Format with up to 3 decimal places
            }
            return d.value; // Don't apply formatting to RGB and parent structure columns
        });
}

// Function to format numbers with thousands separators and limited decimal places
function formatNumber(number, maxDecimals) {
    return Number(number).toLocaleString(undefined, {
         minimumFractionDigits: 0,
        maximumFractionDigits: maxDecimals
    });
}

// Function to calculate contrast color (black or white) based on RGB value
function getContrastColor(hexColor) {
    var r = parseInt(hexColor.slice(0, 2), 16);
    var g = parseInt(hexColor.slice(2, 4), 16);
    var b = parseInt(hexColor.slice(4, 6), 16);
    var brightness = (r * 299 + g * 587 + b * 114) / 1000;
    return brightness > 128 ? "black" : "white";
}

// Function to get the maximum count value
function getMaxCount(data) {
    var maxCount = 0;
    data.forEach(d => {
        for (var i = 3; i <= 6; i++) { // Count columns are from index 3 to 6
            maxCount = Math.max(maxCount, +d[Object.keys(d)[i]]);
        }
    });
    return maxCount;
}

// Load CSV file and create table
d3.csv("merged_json.csv").then(data => {
    createTable(data);
});
