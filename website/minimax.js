function parseJobs(input) {
    return input.trim().split("\n").map(line => {
        let [name, duration] = line.split(",");
        return { name: name.trim(), duration: parseInt(duration) };
    });
}

function permute(arr) {
    if (arr.length <= 1) return [arr];

    let result = [];
    for (let i = 0; i < arr.length; i++) {
        let rest = permute(arr.slice(0, i).concat(arr.slice(i + 1)));
        for (let r of rest) {
            result.push([arr[i]].concat(r));
        }
    }
    return result;
}

function evaluate(order) {
    let time = 0;

    for (let job of order) {
        time += job.duration;

        // simulate worst-case delay
        let delay = [0, 2, 5][Math.floor(Math.random() * 3)];
        time += delay;
    }

    return time;
}

function runMinimax() {
    const input = document.getElementById("jobInput").value;
    const jobs = parseJobs(input);

    let perms = permute(jobs);

    let best = null;
    let bestCost = Infinity;

    for (let p of perms) {
        let cost = evaluate(p);
        if (cost < bestCost) {
            bestCost = cost;
            best = p;
        }
    }

    document.getElementById("jobResult").innerText =
        `Best Order: ${best.map(j => j.name).join(" → ")} | Time: ${bestCost}`;
}
