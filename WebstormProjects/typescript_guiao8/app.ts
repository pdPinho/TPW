class Animal {
    name: string;
    animals: number;
    static count = 0;
    constructor(n: string){
        this.name = n;
        this.animals = ++Animal.count;
    }

    nAnimals() : number {
        return this.animals;
    }
    habitat() {}
    show() {}
}

class Reptile extends Animal{}

class Mammal extends Animal{
    mammals: number;
    static count = 0;
    constructor(name: string){
        super(name);
        this.mammals = ++Mammal.count;
    }
    nMammals() : number{
        return this.mammals;
    }
    show() {}
    talk() {
        return this.name + " is talking: ";
    }
}

class Canine extends Mammal{
    canines: number;
    breed: string;
    static count = 0;
    constructor(name: string){
        super(name);
        this.canines = ++Canine.count;
    }
    nCanines() : number {
        return this.canines;
    }
    race(breed: string) {
        this.breed = breed;
    }
}
class Dog extends Canine{
    dogs: number;
    static count = 0;
    constructor(name: string, breed: string){
        super(name);
        this.dogs = ++Dog.count;
        this.race(breed);
    }
    nDogs() : number{
        return this.dogs;
    }
    bark() : string {
        return 'Woof! Woof!';
    }
    talk(){
        return super.talk() + this.bark();
    }
}
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

let animal = new Animal('d');

let dogs = [new Dog('Doggy', 'Golden Retriever'), new Dog('NewDoggo', 'American Bulldog')];

console.log();