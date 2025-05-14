/***** CONFIGURABLE DESDE EL MENÚ *****/
let grid = 20;          // tamaño de celda en píxeles
let cells = 20;         // lado del tablero (n × n)
let foodTarget = 5;     // nº de comidas simultáneas (0=aleatorio)
let interval = 100;     // ms entre frames

/***** VARIABLES DE JUEGO *****/
const canvas = document.getElementById("gameCanvas");
const ctx     = canvas.getContext("2d");
let snake, dir, foods, timer, running = false, score = 0, best = 0;

/***** ELEMENTOS UI *****/
const hud         = document.getElementById("hud");
const mainMenu    = document.getElementById("mainMenu");
const playBtn     = document.getElementById("playBtn");
const settingsBtn = document.getElementById("settingsBtn");
const settingsBox = document.getElementById("settingsPanel");
const pauseBtn    = document.getElementById("pauseBtn");
const gameOverTxt = document.getElementById("gameOver");
const statScore   = document.getElementById("statScore");
const statBest    = document.getElementById("statBest");
const appleCounter= document.getElementById("appleCounter");
const speedLabel  = document.getElementById("speedLabel");

/***** AJUSTES ******/
const mapSizeSel  = document.getElementById("mapSize");
const foodSel     = document.getElementById("foodCount");
const speedRange  = document.getElementById("speedRange");
const speedDisp   = document.getElementById("speedDisplay");

speedRange.oninput = () =>{
  const v = +speedRange.value;
  speedDisp.textContent = v<75 ? "Rápido" : v>150 ? "Lento" : "Normal";
};

/***** MENÚ *****/
settingsBtn.onclick = ()=> settingsBox.style.display = settingsBox.style.display? "none":"flex";

playBtn.onclick = () =>{
  // aplicar ajustes del usuario
  cells       = +mapSizeSel.value;
  foodTarget  = +foodSel.value || (Math.floor(Math.random()*5)+1);
  interval    = +speedRange.value;

  startGame();
};

pauseBtn.onclick = ()=> running ? stopGame() : resumeGame();

/***** TECLAS *****/
document.addEventListener("keydown", e=>{
  if(!running) return;

  const key = e.key.toLowerCase();
  if(["arrowleft","a"].includes(key) && dir!=="R") dir="L";
  else if(["arrowup","w"].includes(key) && dir!=="D") dir="U";
  else if(["arrowright","d"].includes(key)&& dir!=="L") dir="R";
  else if(["arrowdown","s"].includes(key) && dir!=="U") dir="D";
});

/***** GAME LOOP *****/
function startGame(){
  // tamaño real del canvas
  canvas.width  = canvas.height = cells*grid;

  // reiniciar estado
  snake   = [{x:Math.floor(cells/2), y:Math.floor(cells/2)}];
  dir     = "R";
  foods   = [];
  score   = 0;
  appleCounter.textContent = "🍎 0";
  speedLabel.textContent   = speedDisp.textContent;
  spawnFoods(foodTarget);

  // UI
  mainMenu.style.display="none";
  canvas.style.display  ="block";
  hud.style.display     ="block";
  pauseBtn.style.display="block";
  gameOverTxt.style.display="none";

  running = true;
  timer   = setInterval(update, interval);
}

function stopGame(){
  running=false;
  clearInterval(timer);
  pauseBtn.textContent="Reanudar";
}
function resumeGame(){
  running=true;
  timer=setInterval(update,interval);
  pauseBtn.textContent="Pausa";
}

function endGame(){
  running=false;
  clearInterval(timer);
  best = Math.max(best, score);
  statScore.textContent = score;
  statBest.textContent  = best;
  gameOverTxt.style.display="block";
  pauseBtn.style.display="none";
  mainMenu.style.display="block";
}

function spawnFoods(n){
  while(foods.length<n){
    const f={x:rand(cells),y:rand(cells)};
    if(!occupied(f)) foods.push(f);
  }
}

function rand(max){return Math.floor(Math.random()*max);}
function occupied(pos){
  return snake.some(s=>s.x===pos.x&&s.y===pos.y)||
         foods .some(f=>f.x===pos.x&&f.y===pos.y);
}

function update(){
  // mover cabeza
  const head={...snake[0]};
  if(dir==="L") head.x--; if(dir==="R") head.x++;
  if(dir==="U") head.y--; if(dir==="D") head.y++;

  // colisión pared/cuerpo
  if(head.x<0||head.x>=cells||head.y<0||head.y>=cells||
     snake.some(s=>s.x===head.x&&s.y===head.y)){
    endGame(); return;
  }

  snake.unshift(head);

  // comer?
  const foodIdx=foods.findIndex(f=>f.x===head.x&&f.y===head.y);
  if(foodIdx>-1){
    foods.splice(foodIdx,1);
    score++; appleCounter.textContent="🍎 "+score;
    spawnFoods(foodTarget);
  }else{
    snake.pop();
  }

  draw();
}

function draw(){
  // tablero
  ctx.fillStyle="#263238";
  ctx.fillRect(0,0,canvas.width,canvas.height);

  // celdas (cuadrícula suave)
  ctx.fillStyle="#2e3d44";
  for(let i=0;i<cells;i++){
    for(let j=0;j<cells;j++){
      if((i+j)%2) ctx.fillRect(i*grid,j*grid,grid,grid);
    }
  }

  // comidas
  ctx.fillStyle="#ff5252";
  foods.forEach(f=>ctx.fillRect(f.x*grid,f.y*grid,grid,grid));

  // serpiente
  snake.forEach((s,i)=>{
    ctx.fillStyle=i? "#66bb6a":"#00e676";
    ctx.fillRect(s.x*grid,s.y*grid,grid,grid);
  });
}
