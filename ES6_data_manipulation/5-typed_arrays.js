export default function createInt8TypedArray(length, position, value) {
  const arrayBuff = new ArrayBuffer(length);
  const view = new DataView(arrayBuff);
  view.setUint8(position, value);
  return view;
}
