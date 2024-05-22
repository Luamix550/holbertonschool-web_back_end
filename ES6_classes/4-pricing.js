import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  set amount(value) {
    if (typeof value === 'number') {
      this._amount = value;
    } else {
      throw TypeError('Amount must be a number');
    }
  }

  get amount() {
    return this._amount;
  }

  set currency(value) {
    if (value instanceof Currency) {
      this._currency = value;
    } else {
      throw TypeError('Currency must be an instance of Currency');
    }
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }
}
