const { exec } = require('child_process');
const path = require('path');

// Path to the Python script (with spaces in the path)
const scriptPath = '/home/priyanshu/ECDM/MainParts/TracksList.py';

// Command to execute the Python script
const command = `python "${scriptPath}"`;

// Execute the command
exec(command, (error, stdout, stderr) => {
    if (error) {
        console.error(`Error executing Python script: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`Python script produced an error: ${stderr}`);
        return;
    }
    console.log(`Python script output: ${stdout}`);
});
