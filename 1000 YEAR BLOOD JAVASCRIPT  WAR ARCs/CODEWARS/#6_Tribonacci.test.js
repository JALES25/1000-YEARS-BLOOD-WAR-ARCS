const tribonacci = require('tribonacci');

describe('tribonacci function', () => {
  it('returns an empty array when n is 0', () => {
    expect(tribonacci([1, 2, 3], 0)).toEqual([]);
  });

  it('returns the first n elements of the signature array when n is less than or equal to the signature length', () => {
    expect(tribonacci([1, 2, 3], 1)).toEqual([1]);
    expect(tribonacci([1, 2, 3], 3)).toEqual([1, 2, 3]);
  });

  it('returns the tribonacci sequence for n > signature.length', () => {
    expect(tribonacci([1, 2, 3], 5)).toEqual([1, 2, 3, 6, 11]);
    expect(tribonacci([1, 1, 1, 3], 10)).toEqual([1, 1, 1, 3, 5, 9, 17, 31, 57, 105]);
  });

  it('handles edge cases correctly', () => {
    expect(tribonacci([1, 2, 3], 0)).toEqual([]);
    expect(tribonacci([1, 1, 1], 1)).toEqual([1]);
  });

  it('returns the first n elements of the signature array when n is less than the signature length', () => {
    expect(tribonacci([1, 2, 3], 2)).toEqual([1, 2]);
    expect(tribonacci([1, 1, 1, 3], 3)).toEqual([1, 1, 1]);
  });
});
