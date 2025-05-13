const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const startBtn = document.getElementById("startBtn");
const gameOverDiv = document.getElementById("gameOver");

let snake, food, dx, dy, gameInterval;

startBtn.addEventListener("click", startGame);
document.addEventListener("keydown", changeDirection);

function startGame() {
    // Inicialización
    snake = [{ x: 10, y: 10 }];
    food = randomFood();
    dx = 1;
    dy = 0;

    // UI
    startBtn.style.display = "none";
    gameOverDiv.style.display = "none";
    canvas.style.display = "inline";

    // Start loop
    if (gameInterval) clearInterval(gameInterval);
    gameInterval = setInterval(update, 100);
}

function randomFood() {
    return {
        x: Math.floor(Math.random() * (canvas.width / 20)),
        y: Math.floor(Math.random() * (canvas.height / 20))
    };
}

function changeDirection(event) {
    switch (event.key) {
        case "ArrowUp": if (dy === 0) { dx = 0; dy = -1; } break;
        case "ArrowDown": if (dy === 0) { dx = 0; dy = 1; } break;
        case "ArrowLeft": if (dx === 0) { dx = -1; dy = 0; } break;
        case "ArrowRight": if (dx === 0) { dx = 1; dy = 0; } break;
    }
}

function update() {
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };

    // Colisión con borde
    if (
        head.x < 0 || head.x >= canvas.width / 20 ||
        head.y < 0 || head.y >= canvas.height / 20
    ) {
        endGame();
        return;
    }

    // Colisión con cuerpo
    for (let part of snake) {
        if (part.x === head.x && part.y === head.y) {
            endGame();
            return;
        }
    }

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
        food = randomFood();
    } else {
        snake.pop();
    }

    draw();
}

function draw() {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "lime";
    for (let part of snake) {
        ctx.fillRect(part.x * 20, part.y * 20, 20, 20);
    }

    ctx.fillStyle = "red";
    ctx.fillRect(food.x * 20, food.y * 20, 20, 20);
}

function endGame() {
    clearInterval(gameInterval);
    gameOverDiv.style.display = "block";
}
