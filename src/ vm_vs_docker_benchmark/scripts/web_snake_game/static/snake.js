const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
const box = 20;
const canvasSize = 20;
let snake = [{ x: 9 * box, y: 9 * box }];
let food = {
    x: Math.floor(Math.random() * canvasSize) * box,
    y: Math.floor(Math.random() * canvasSize) * box
};
let direction;
let score = 0;

document.addEventListener('keydown', event => {
    if (event.key === 'ArrowUp' && direction !== 'DOWN') direction = 'UP';
    else if (event.key === 'ArrowDown' && direction !== 'UP') direction = 'DOWN';
    else if (event.key === 'ArrowLeft' && direction !== 'RIGHT') direction = 'LEFT';
    else if (event.key === 'ArrowRight' && direction !== 'LEFT') direction = 'RIGHT';
});

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = i === 0 ? 'lime' : 'green';
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
    }

    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, box, box);

    let headX = snake[0].x;
    let headY = snake[0].y;

    if (direction === 'LEFT') headX -= box;
    if (direction === 'RIGHT') headX += box;
    if (direction === 'UP') headY -= box;
    if (direction === 'DOWN') headY += box;

    // Game over
    if (headX < 0 || headY < 0 || headX >= canvas.width || headY >= canvas.height || snake.some((s, i) => i !== 0 && s.x === headX && s.y === headY)) {
        alert("💀 Game Over!");
        document.location.reload();
        return;
    }

    if (headX === food.x && headY === food.y) {
        score++;
        food = {
            x: Math.floor(Math.random() * canvasSize) * box,
            y: Math.floor(Math.random() * canvasSize) * box
        };
    } else {
        snake.pop();
    }

    const newHead = { x: headX, y: headY };
    snake.unshift(newHead);
}

setInterval(draw, 100);
