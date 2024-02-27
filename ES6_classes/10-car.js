const brandSymbol = Symbol('brand');
const motorSymbol = Symbol('motor');
const colorSymbol = Symbol('color');

class Car {
    constructor(brand, motor, color) {
        // Use symbols to store attributes
        this[brandSymbol] = brand;
        this[motorSymbol] = motor;
        this[colorSymbol] = color;
    }

    cloneCar() {
        // Create a new object of the same class with the same attribute values
        return new Car(this[brandSymbol], this[motorSymbol], this[colorSymbol]);
    }
