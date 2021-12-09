("use strict");
var expect = chai.expect;
function cyfry(napis) {
  var nums = napis.match(/\d/g);
  var suma = 0;
  if (nums === null) {
    return 0;
  }
  for (let i = 0; i < nums.length; i++) {
    suma += parseInt(nums[i]);
  }
  return suma;
}

function litery(napis) {
  var litery = napis.match(/[a-z]/gi);
  if (litery === null) {
    return 0;
  }
  return litery.length;
}

function suma(napis) {
  if (napis.match(/^\d+/g)) added += parseInt(napis.match(/^\d+/g));
  return added;
}

var added = 0;
do {
  input = window.prompt("Podaj napis");
  if (input != null)
    console.log(`
    \t ${cyfry(input)} \t ${litery(input)} \t ${suma(input)}
    `);
} while (input != null);

describe("Funkcja cyfry()", function () {
  it("Zwraca 3 dla 111", function () {
    expect(cyfry("111")).to.equal(3);
  });
  it("Zwraca 3 dla a$%^!dsW1@1_1aaa_", function () {
    expect(cyfry("a$%^!dsW1@1_1aaa_")).to.equal(3);
  });
  it("Zwraca 0 dla asdasd", function () {
    expect(cyfry("asdasd")).to.equal(0);
  });
});

describe("Funkcja litery()", function () {
  it("Zwraca 0 dla 111", function () {
    expect(litery("111")).to.equal(0);
  });
  it("Zwraca 7 dla a$%^!dsW1@1_1aaa_", function () {
    expect(litery("a$%^!dsW1@1_1aaa_")).to.equal(7);
  });
  it("Zwraca 6 dla asdasd", function () {
    expect(litery("asdasd")).to.equal(6);
  });
});

describe("Funkcja suma()", function () {
  before(function () {
    var added = 0;
  });
  beforeEach(function () {
    added = 0;
  });
  afterEach(function () {
    added = 0;
  });

  it("Zwraca 123 dla 123", function () {
    suma("123");
    expect(added).to.equal(123);
  });
  it("Zwraca 123 dla 123 a po nim a123", function () {
    suma("123");
    suma("a123");
    expect(added).to.equal(123);
  });
  it("Zwraca 246 dla 123 a po nim 123a", function () {
    suma("123");
    suma("123a");
    expect(added).to.equal(246);
  });
});
