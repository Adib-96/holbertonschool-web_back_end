// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
    it('should return the sum of two rounded numbers', function() {
        assert.strictEqual(calculateNumber(1.4, 4.5), 6);
        assert.strictEqual(calculateNumber(1.6, 4.2), 6);
        assert.strictEqual(calculateNumber(2.5, 2.5), 6);
    });

    it('should handle positive and negative numbers', function() {
        assert.strictEqual(calculateNumber(-1.4, 4.5), 4);
        assert.strictEqual(calculateNumber(-1.6, -4.2), -6);
        assert.strictEqual(calculateNumber(1.6, -4.5), -2);
    });

    it('should handle zero', function() {
        assert.strictEqual(calculateNumber(0, 0), 0);
        assert.strictEqual(calculateNumber(0.4, 0.4), 0);
        assert.strictEqual(calculateNumber(0.5, 0.5), 2);
    });

    it('should handle edge cases', function() {
        assert.strictEqual(calculateNumber(Number.MAX_VALUE, Number.MAX_VALUE), Infinity);
        assert.strictEqual(calculateNumber(Number.MIN_VALUE, Number.MIN_VALUE), 0);
    });
});
