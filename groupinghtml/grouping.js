$(document).ready(function () {
    let originalList, groupedList;

    $("#upload-file").change(function () {
        const fileInput = document.getElementById('upload-file');
        const file = fileInput.files[0];
        if (file) {
            // Read the uploaded Excel file
            const reader = new FileReader();
            reader.onload = function (e) {
                // Assuming the data is in CSV format for simplicity
                originalList = parseCsv(e.target.result);

                // Display the uploaded list
                displayList(originalList, "#original-list");
            };
            reader.readAsText(file);
        }
    });

    $("#group-button").click(function () {
        // Implement the logic to group students here
        // Update the groupedList accordingly
        const teamSize = $("#team-size").val();
        groupedList = groupStudents(originalList, teamSize);

        // Display the grouped list
        displayList(groupedList, "#grouped-teams");
    });

    $("#download-button").click(function () {
        // Implement the logic to download the grouped teams as Excel
        // You may use AJAX to send a request to the server to generate and provide the download link
        // Update the download link accordingly
    });

    function parseCsv(csvData) {
        // Assuming a simple CSV parsing logic for demonstration
        const rows = csvData.split('\n');
        const headers = rows[0].split(',');
        const data = [];
        for (let i = 1; i < rows.length; i++) {
            const row = rows[i].split(',');
            const rowData = {};
            for (let j = 0; j < headers.length; j++) {
                rowData[headers[j]] = row[j];
            }
            data.push(rowData);
        }
        return data;
    }

    function groupStudents(studentList, teamSize) {
        // Implement the logic to group students based on teamSize
        // Return the grouped list
        const groupedList = [];

        // Placeholder logic: Group students in teams of teamSize
        for (let i = 0; i < studentList.length; i += teamSize) {
            const team = studentList.slice(i, i + teamSize);
            groupedList.push(team);
        }

        return groupedList;
    }

    function displayList(data, elementId) {
        const table = $('<table>').addClass('list-table');
        const headers = Object.keys(data[0]);
        const headerRow = $('<tr>');
        headers.forEach(header => {
            headerRow.append($('<th>').text(header));
        });
        table.append(headerRow);

        data.forEach(row => {
            const rowElement = $('<tr>');
            headers.forEach(header => {
                rowElement.append($('<td>').text(row[header]));
            });
            table.append(rowElement);
        });

        $(elementId).empty().append(table);
    }
});
