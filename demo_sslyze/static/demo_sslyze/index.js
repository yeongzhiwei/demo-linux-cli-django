"use strict";

document.addEventListener('DOMContentLoaded', () => {
    let taskId = document.getElementById('output').dataset.taskId;
    if (taskId !== "") {
        console.log(`Fetching result for task id: ${taskId}`);
        fetch_result(taskId);
    } else {
        console.log('No task');
    }
})

function fetch_result(taskId) {
    fetch(`/sslyze/results/${taskId}`).then(
        data => data.json()
    ).then(
        json_data => {
            let outputElement = document.getElementById('output')
            if (json_data.status === "Success") {
                outputElement.textContent = json_data.output;
            } else if (json_data.status === "Failure") {
                outputElement.textContent = "Failed to run sslyze. Please try again later.";
            } else if (json_data.status === "Pending") {
                outputElement.textContent = "Running... please wait. This page will refresh every 10 sec.";
                setTimeout(() => fetch_result(taskId), 10000);
            }
        }
    )
}