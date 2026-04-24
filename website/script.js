function parseJobs(input) {
    const lines = input.trim().split("\n");
    const jobs = [];

    for (let line of lines) {
        const [name, duration] = line.split(",");
        if (name && duration) {
            jobs.push({
                name: name.trim(),
                duration: parseInt(duration.trim())
            });
        }
    }
    return jobs;
}

// Simple Minimax-like evaluation (frontend simulation)
function evaluateSchedule(order) {
    let time = 0;

    for (let job of order) {
        time += job.duration;

        // simulate worst-case delay
        const delay = [0, 2, 5][Math.floor(Math.random() * 3)];
        time += delay;
    }

    return time;
}

function permute(arr) {
    if (arr.length <= 1) return [arr];

    const result = [];

    for (let i = 0; i < arr.length; i++) {
        const rest = permute(arr.slice(0, i).concat(arr.slice(i + 1)));
        for (let r of rest) {
            result.push([arr[i]].concat(r));
        }
    }

    return result;
}

function runScheduler() {
    const input = document.getElementById("jobsInput").value;
    const jobs = parseJobs(input);

    if (jobs.length === 0) {
        alert("Enter valid jobs!");
        return;
    }

    const permutations = permute(jobs);

    let bestOrder = null;
    let bestCost = Infinity;

    for (let order of permutations) {
        const cost = evaluateSchedule(order);

        if (cost < bestCost) {
            bestCost = cost;
            bestOrder = order;
        }
    }

    const resultText = `
Best Order: ${bestOrder.map(j => j.name).join(" → ")}
Worst Case Time: ${bestCost}
    `;

    document.getElementById("result").innerText = resultText;
}
