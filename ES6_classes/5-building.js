export default class Building {
  constructor(sqft) {
    if (this.constructor === Building) {
      throw new Error('You cannot instantiate an abstract class!');
    }
    if (this.evacuationWarningMessage === undefined) {
      throw new Error('The class extending Building must override the method evacuationWarningMessage');
    }

    if (typeof sqft === 'number') {
      this._sqft = sqft;
    } else {
      throw new Error('Square footage must be a number.');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (typeof value === 'number') {
      this._sqft = value;
    } else {
      throw new TypeError('Square footage must be a number.');
    }
  }

  /* eslint-disable class-methods-use-this */
  evacuationWarningMessage() {
    throw new Error("Method 'evacuationWarningMessage()' must be implemented");
  }
  /* eslint-enable class-methods-use-this */
}
