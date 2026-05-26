function lastItem(arr) {
  // returns the last element
  return arr[arr.length];
}

function greet(user) {
  return "Hello " + user.name.toUpperCase();
}

module.exports = { lastItem, greet };
