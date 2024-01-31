export default function cleanSet(set, startString) {
  if (startString.length === 0) {
    return '';
  }
  const myarray = Array.from(set);
  return myarray.filter((item) => item.startsWith(startString))
    .map((item) => item.replace(startString, '')).join('-');
}
