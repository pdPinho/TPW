var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Animal = /** @class */ (function () {
    function Animal(n) {
        this.name = n;
        this.animals = ++Animal.count;
    }
    Animal.prototype.nAnimals = function () {
        return this.animals;
    };
    Animal.prototype.habitat = function () { };
    Animal.prototype.show = function () { };
    Animal.count = 0;
    return Animal;
}());
var Reptile = /** @class */ (function (_super) {
    __extends(Reptile, _super);
    function Reptile() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Reptile;
}(Animal));
var Mammal = /** @class */ (function (_super) {
    __extends(Mammal, _super);
    function Mammal(name) {
        var _this = _super.call(this, name) || this;
        _this.mammals = ++Mammal.count;
        return _this;
    }
    Mammal.prototype.nMammals = function () {
        return this.mammals;
    };
    Mammal.prototype.show = function () { };
    Mammal.prototype.talk = function () {
        return this.name + " is talking: ";
    };
    Mammal.count = 0;
    return Mammal;
}(Animal));
var Canine = /** @class */ (function (_super) {
    __extends(Canine, _super);
    function Canine(name) {
        var _this = _super.call(this, name) || this;
        _this.canines = ++Canine.count;
        return _this;
    }
    Canine.prototype.nCanines = function () {
        return this.canines;
    };
    Canine.prototype.race = function (breed) {
        this.breed = breed;
    };
    Canine.count = 0;
    return Canine;
}(Mammal));
var Dog = /** @class */ (function (_super) {
    __extends(Dog, _super);
    function Dog(name, breed) {
        var _this = _super.call(this, name) || this;
        _this.dogs = ++Dog.count;
        _this.race(breed);
        return _this;
    }
    Dog.prototype.nDogs = function () {
        return this.dogs;
    };
    Dog.prototype.bark = function () {
        return 'Woof! Woof!';
    };
    Dog.prototype.talk = function () {
        return _super.prototype.talk.call(this) + this.bark();
    };
    Dog.count = 0;
    return Dog;
}(Canine));
/*
class Feline extends Mammal {
    nFelines() {}
    family() {}
}


class Cat extends Feline{
    constructor(name: string){
        super(name);
    }
    nCats() {}
    meow() {}
    name() : string{
        return this.name;
    }

    talk() {
        return super.talk() + 'Meow, meow!';
    }
}
*/
var animal = new Animal('d');
var dog = new Dog('Doggy', 'Golden Retriever');
var dog2 = new Dog('NewDoggo', 'American Bulldog');
console.log(dog.nAnimals(), dog.nCanines());
