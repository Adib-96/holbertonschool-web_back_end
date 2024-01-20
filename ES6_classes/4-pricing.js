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
    const { _name } = this._currency;
    if (_name[_name.length - 1] === 's') {
      this._currency._name = Array.from(this._currency._name).slice(0, _name.length - 1).join('').toLowerCase();
    }
    return this._currency._name;
  }

  set currency(value) {
    this._currency = value;
  }

  displayFullPrice() {
    const { code, name } = new Currency(this._currency._name, this._currency._code);
    return `${this.amount} ${code} (${name})`;
  }

  static convertPrice(amount, converionRate) {
    return amount * converionRate;
  }
}
