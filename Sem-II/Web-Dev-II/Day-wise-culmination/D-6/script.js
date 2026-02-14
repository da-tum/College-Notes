let user = {
  name: "ABC",
  address: "Gurugram",
  mobileno: 123456790,
  favcolor: ["red", "green", "blue"],
  demo: function () {
    return "demo";
  },
};

console.log(
  "My name is " + user.name + ". My favourite color is " + user.favcolor[0],
);

// String Literals
console.log(
  `My name is ${user.name} My favourite color is ${user.favcolor[0]}`,
);

// Object Methods

console.log(Object.keys(user));

console.log(Object.values(user));

console.log(Object.entries(user));

// Mutable object
const car = { manufacturer: "Aston Martin", model: "Vulcan" };
car.color = "Purple";
console.log(car);

// Allows updating pre-existing properties while preventing addition of key value pairs
Object.seal(car);
car.price = "1Cr";
console.log(car);

// Makes object immutable, cannot add or update any key value pairs
Object.freeze(car);
car.model = "Valkriye";
console.log(car);

// Homework, verifying tic tac toe victory
function verifyWin(board) {
  let playerXBoard = 0;
  let playerOBoard = 0;
  for (let i in board) {
    for (let j in board[i]) {
      playerXBoard += board[i][j] == "x" ? 2 ** parseInt(3*i+j) : 0;
      playerOBoard += board[i][j] == "o" ? 2 ** parseInt(3*i+j) : 0;
    }
  }
  const winConditions = [7, 56, 448, 73, 146, 292, 273, 84];
}

function check() {
  const board = [
    ["x", "x", "x"],
    ["x", "o", "o"],
    ["o", "o", "x"],
  ];
  verifyWin(board);
}

check();
