export default function appendToEachArrayValue(array, appendString) {
  for (const [index, idx] of array.entries()) {
    const clonedArray = array;
    clonedArray[index] = appendString + idx;
  }

  return array;
}
