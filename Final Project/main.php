<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HariBantAI: PLM Attendance Tracking System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #fff5e6; /* Light yellow background */
        }
        h1 {
            color: #8B0000; /* Dark red for the title */
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background-color: #ffffff; /* White background for the table */
        }
        th, td {
            border: 1px solid #ffcccc; /* Light red border */
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #ffcccc; /* Light red header */
            color: #8B0000; /* Dark red text for header */
        }
        tr:nth-child(even) {
            background-color: #fff5e6; /* Light yellow for even rows */
        }
        tr:hover {
            background-color: #ffe6e6; /* Lighter red for hover effect */
        }
    </style>
</head>
<body>
    <h1>HariBantAI: PLM Attendance Tracking System</h1>
    <table>
        <thead>
            <tr>
                <th>Date</th>
                <th>Time</th>
                <th>Name</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $filename = 'db.txt';
            if (file_exists($filename)) {
                $lines = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
                foreach ($lines as $line) {
                    if (preg_match('/^(\d{4}-\d{2}-\d{2})(?: (\d{2}:\d{2}:\d{2}))? - (.+): (.+)$/', $line, $matches)) {
                        echo "<tr>";
                        echo "<td>{$matches[1]}</td>"; // Date
                        echo "<td>" . (isset($matches[2]) ? $matches[2] : "") . "</td>"; // Time (blank for absent)
                        echo "<td>{$matches[3]}</td>"; // Name
                        echo "<td>{$matches[4]}</td>"; // Status
                        echo "</tr>";
                    }
                }
            } else {
                echo "<tr><td colspan='4'>No attendance data available.</td></tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>     