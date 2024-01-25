export default class HolbertonCourse {
  constructor (name, length, students) {
<<<<<<< HEAD
    if (typeof name !== 'string') throw TypeError('name must be a string');
    if (typeof length !== 'number') throw TypeError('length must be a number');
    if (students.constructor !== Array && students.every((el) => typeof el === 'string')) {
      throw TypeError('students must be an array of strings');
=======
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
>>>>>>> c23c9783d8a644678389ae4d17f855850e144bba
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name () {
    return this._name;
  }

<<<<<<< HEAD
  set name (newName) {
    if (typeof newName !== 'string') throw TypeError('name must be a string');
    this._name = newName;
=======
  set name (value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
>>>>>>> c23c9783d8a644678389ae4d17f855850e144bba
  }

  get length () {
    return this._length;
  }

<<<<<<< HEAD
  set length (newLength) {
    if (typeof newLength !== 'number') throw TypeError('length must be a number');
    this._length = newLength;
=======
  set length (value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    } else {
      this._length = value;
    }
>>>>>>> c23c9783d8a644678389ae4d17f855850e144bba
  }

  get students () {
    return this._students;
  }

<<<<<<< HEAD
  set students (newStudents) {
    if (newStudents.constructor !== Array && newStudents.every((el) => typeof el === 'string')) {
      throw TypeError('students must be an array of strings');
=======
  set students (value) {
    if (!Array.isArray(value) || !value.every((student) => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
>>>>>>> c23c9783d8a644678389ae4d17f855850e144bba
    }
    this._students = newStudents;
  }
}
