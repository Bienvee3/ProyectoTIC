const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let snake = [{ x: 10, y: 10 }];
let food = { x: 15, y: 15 };
let dx = 1, dy = 0;

document.addEventListener("keydown", changeDirection);

function changeDirection(event) {
    switch (event.key) {
        case "ArrowUp": if (dy === 0) { dx = 0; dy = -1; } break;
        case "ArrowDown": if (dy === 0) { dx = 0; dy = 1; } break;
        case "ArrowLeft": if (dx === 0) { dx = -1; dy = 0; } break;
        case "ArrowRight": if (dx === 0) { dx = 1; dy = 0; } break;
    }
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

function update() {
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };
    snake.unshift(head);

    // Comer comida
    if (head.x === food.x && head.y === food.y) {
        food = {
            x: Math.floor(Math.random() * (canvas.width / 20)),
            y: Math.floor(Math.random() * (canvas.height / 20))
        };
    } else {
        snake.pop();
    }

    draw();
}

setInterval(update, 100);
