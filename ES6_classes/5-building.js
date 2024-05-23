export default class Building {
  constructor(sqft) {
    if (this.constructor === Building) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    } else {
      this._sqft = sqft;
    }
  }

  get sqft() {
    return this._sqft;
  }

  /* eslint-disable class-methods-use-this */
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
    /* eslint-disable class-methods-use-this */
  }
  /* eslint-disable class-methods-use-this */
}
