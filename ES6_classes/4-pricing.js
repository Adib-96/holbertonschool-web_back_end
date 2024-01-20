import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = value;
  }

  displayFullPrice() {
    const { code, name } = new Currency(this._currency._code, this._currency._name);
    return `${this.amount} ${code} (${name})`;
  }

  static convertPrice(amount, converionRate) {
    return amount * converionRate;
  }
}
