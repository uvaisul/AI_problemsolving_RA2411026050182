function parseMatrix(input) {
    return input.trim().split("\n").map(row =>
        row.split(",").map(Number)
    );
}

function nearestNeighbor(matrix) {
    let n = matrix.length;
    let visited = Array(n).fill(false);
    let route = [0];
    let total = 0;

    visited[0] = true;
    let current = 0;

    for (let i = 0; i < n - 1; i++) {
        let min = Infinity, next = -1;

        for (let j = 0; j < n; j++) {
            if (!visited[j] && matrix[current][j] < min) {
                min = matrix[current][j];
                next = j;
            }
        }

        route.push(next);
        visited[next] = true;
        total += min;
        current = next;
    }

    total += matrix[current][0];
    route.push(0);

    return { route, total };
}

function runTSP() {
    const input = document.getElementById("tspInput").value;
    const matrix = parseMatrix(input);

    const result = nearestNeighbor(matrix);

    document.getElementById("tspResult").innerText =
        `Route: ${result.route.join(" → ")} | Distance: ${result.total}`;
}
